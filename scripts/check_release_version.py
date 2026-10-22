"""Fails when any plugin manifest disagrees with the others or with the release tag."""

import argparse
import json
import sys
from pathlib import Path

_PLUGINS_DIR = Path(__file__).resolve().parent.parent / 'plugins'


class _ReleaseVersionError(Exception):
    pass


def get_base_version_from_tag(*, tag: str) -> str:
    """Returns `1.2.3` for `v1.2.3` and for a pre-release such as `v1.2.3-rc.1`."""
    return tag.removeprefix('v').split('-', 1)[0]


def _read_version_from_manifest(*, manifest_path: Path) -> str:
    if not manifest_path.is_file():
        raise _ReleaseVersionError(f'Missing manifest `{manifest_path}`!')
    version = json.loads(manifest_path.read_text()).get('version')
    if not isinstance(version, str) or not version:
        raise _ReleaseVersionError(f'Missing `version` in `{manifest_path}`!')
    return version


def read_plugin_versions_by_path(*, plugins_dir: Path) -> dict[Path, tuple[str, str]]:
    """Returns (Agent Plugins version, Claude version) for every plugin folder."""
    plugin_dirs = sorted(path for path in plugins_dir.iterdir() if path.is_dir())
    if not plugin_dirs:
        raise _ReleaseVersionError(f'No plugin folders in `{plugins_dir}`!')
    return {
        plugin_dir: (
            _read_version_from_manifest(manifest_path=plugin_dir / 'plugin.json'),
            _read_version_from_manifest(manifest_path=plugin_dir / '.claude-plugin' / 'plugin.json'),
        )
        for plugin_dir in plugin_dirs
    }


def _check_all_plugins_share_one_version(*, plugins_dir: Path) -> str:
    """Returns the version every manifest of every plugin carries; raises on any disagreement."""
    versions_by_path = read_plugin_versions_by_path(plugins_dir=plugins_dir)
    for plugin_dir, (agent_plugins_version, claude_version) in versions_by_path.items():
        if agent_plugins_version != claude_version:
            raise _ReleaseVersionError(
                f'`{plugin_dir}`: plugin.json says `{agent_plugins_version}` but .claude-plugin/plugin.json says `{claude_version}`!'
            )
    plugin_dir_by_version = {agent_plugins_version: plugin_dir for plugin_dir, (agent_plugins_version, _) in versions_by_path.items()}
    if len(plugin_dir_by_version) > 1:
        listing = ', '.join(f'`{plugin_dir.name}`=`{version}`' for version, plugin_dir in sorted(plugin_dir_by_version.items()))
        raise _ReleaseVersionError(f'All plugins must share one version, found {listing}!')
    return next(iter(plugin_dir_by_version))


def _check_shared_version_matches_tag(*, plugins_dir: Path, tag: str) -> None:
    shared_version = _check_all_plugins_share_one_version(plugins_dir=plugins_dir)
    base_version = get_base_version_from_tag(tag=tag)
    if shared_version != base_version:
        raise _ReleaseVersionError(f'Manifests say `{shared_version}` but tag `{tag}` means `{base_version}`!')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', help='Release tag, e.g. v1.0.0 or v1.0.0-rc.1; omit to check manifests against each other only')
    parser.add_argument('--plugins-dir', type=Path, default=_PLUGINS_DIR)
    args = parser.parse_args()
    try:
        if args.tag is None:
            shared_version = _check_all_plugins_share_one_version(plugins_dir=args.plugins_dir)
            print(f'check_release_version: every plugin is at {shared_version}')
        else:
            _check_shared_version_matches_tag(plugins_dir=args.plugins_dir, tag=args.tag)
            print(f'check_release_version: every plugin matches {args.tag}')
    except _ReleaseVersionError as err:
        print(f'check_release_version: {err}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
