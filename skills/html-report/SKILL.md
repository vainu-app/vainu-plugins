---
name: html-report
description: Generates a polished, self-contained HTML report styled to match the Vainu app. Invoke this skill automatically whenever Vainu MCP tools have been used (or are about to be used) and the user's request is about producing a report, document, export, analysis, or summary of company/contact/market data. Do NOT wait for the user to ask for HTML explicitly — if the intent is a shareable document or report, use this skill.
allowed-tools: Agent Read Write Bash(mkdir *) Bash(node *) Bash(ls *) ToolSearch
metadata:
  user-invocable: "false"
---

# html-report skill

Generates a self-contained `.html` file from Vainu MCP data. Apply this skill
automatically whenever the context involves Vainu data and the output should be
a shareable document or report — do not wait to be asked.

**Arguments passed by caller:** `$ARGUMENTS`

---

## Build the HTML file

Produce a complete, self-contained HTML file. All CSS is embedded in `<style>`.
No JavaScript, no external assets except the Google Fonts import below.

### Full CSS to embed

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');

/* ─── Reset ─────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
img, svg { display: block; }

/* ─── Design tokens ─────────────────────────────────────────── */
:root {
  /* Brand palette */
  --onyx:            #0A0A0A;
  --body:            #3F3F3F;
  --subtle:          #898989;
  --middle:          #BFBFBF;
  --border:          #E1E1E1;
  --cloud:           #F5F5F5;
  --cloud-muted:     #F1F1F1;
  --app-bg:          #FAFAFA;
  --light-paper:     #FCFCFC;
  --white:           #FFFFFF;

  /* Primary green scale */
  --green:           #00E880;
  --green-100:       #D9FCDF;
  --green-200:       #9BFAB7;
  --green-500:       #00CC70;
  --green-700:       #008549;
  --green-900:       #004727;
  --green-brand:     #349780;

  /* Sky blue */
  --sky:             #2F80ED;
  --sky-100:         #EBF3FD;

  /* Tertiary blue */
  --blue:            #4F80FF;
  --blue-100:        #E5EDFF;
  --blue-700:        #1C54E5;

  /* Secondary purple */
  --purple:          #700078;
  --purple-100:      #F9E8FF;

  /* Status */
  --success:         #079992;
  --success-100:     #EDF8F6;
  --warning:         #FA983A;
  --warning-100:     #FEF2E6;
  --error:           #E84D9E;
  --error-100:       #FCE8F3;
  --critical:        #E82235;

  /* Down to earth (warm tones) */
  --warm-100:        #F5EDDF;
  --warm-200:        #E5D5BC;

  /* Elevation shadows (matches MUI Paper overrides exactly) */
  --shadow-1:  0px 2px 4px rgba(138,138,138,0.05), 0px 2px 4px rgba(10,10,10,0.05);
  --shadow-2:  0px 4px 24px rgba(10,10,10,0.05);
  --shadow-3:  0px 4px 12px rgba(10,10,10,0.15);
  --shadow-4:  0px 16px 16px -8px rgba(10,10,10,0.1);
  --shadow-5:  0px 16px 36px -8px rgba(10,10,10,0.15), 0px 1px 1px rgba(10,10,10,0.1);
  --shadow-menu: 2px 2px 12px -4px rgba(0,0,0,0.18);

  /* Typography */
  --font:       'Roboto', sans-serif;
  --font-brand: 'Roboto', sans-serif; /* Aeroport unavailable in standalone HTML */

  /* Layout */
  --max-width:  1360px;
  --radius:     8px;
  --radius-sm:  4px;
  --radius-xs:  3px;
}

/* ─── Base ───────────────────────────────────────────────────── */
html { font-size: 14px; }

body {
  font-family: var(--font);
  font-size: 14px;
  font-weight: 400;
  line-height: 1.4;
  color: var(--body);
  background: var(--app-bg);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ─── Layout ─────────────────────────────────────────────────── */
.page {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 48px 40px 80px;
}

.cols-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.cols-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.cols-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.cols-auto { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; }

@media (max-width: 768px) {
  .page { padding: 24px 16px 48px; }
  .cols-2, .cols-3, .cols-4, .cols-auto { grid-template-columns: 1fr; }
}

/* ─── Report header ──────────────────────────────────────────── */
.report-header {
  padding-bottom: 32px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 40px;
}

.report-wordmark {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 24px;
  text-decoration: none;
}
.report-wordmark svg { width: 28px; height: 28px; flex-shrink: 0; }
.report-wordmark-text {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--onyx);
}

.report-eyebrow {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--subtle);
  margin-bottom: 8px;
}
.report-title {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--onyx);
  line-height: 1.2;
  margin-bottom: 8px;
}
.report-description {
  font-size: 16px;
  font-weight: 400;
  color: var(--subtle);
  line-height: 1.5;
  max-width: 640px;
}
.report-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}
.report-meta-item {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 12px;
  color: var(--subtle);
}
.report-meta-item strong {
  font-weight: 500;
  color: var(--body);
}

/* ─── Sections ───────────────────────────────────────────────── */
.section { margin-bottom: 40px; }

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}
.section-title {
  font-size: 18px;
  font-weight: 500;
  color: var(--onyx);
  white-space: nowrap;
}
.section-rule {
  flex: 1;
  height: 1px;
  background: var(--border);
}
.section-count {
  font-size: 12px;
  color: var(--subtle);
  font-weight: 500;
  white-space: nowrap;
}

/* ─── Stat row ───────────────────────────────────────────────── */
/*
  IMPORTANT: never rely on auto-fill. Always set an explicit column count via
  inline style: style="grid-template-columns: repeat(N, 1fr)"
  where N = exact number of stat-cell children. See layout rules below.
*/
.stat-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* safe fallback — always override inline */
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  margin-bottom: 40px;
}
.stat-cell {
  background: var(--white);
  padding: 20px 24px;
}
.stat-label {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--subtle);
  margin-bottom: 10px;
}
.stat-value {
  font-family: var(--font-brand);
  font-size: 32px;
  font-weight: 500;
  color: var(--onyx);
  line-height: 1.1;
  display: flex;
  align-items: baseline;
  gap: 4px;
}
.stat-unit {
  font-size: 14px;
  font-weight: 400;
  color: var(--subtle);
}
.stat-delta {
  margin-top: 6px;
  font-size: 12px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 3px;
}
.stat-delta.up   { color: var(--success); }
.stat-delta.down { color: var(--error); }
.stat-delta.flat { color: var(--subtle); }

/* ─── Cards ──────────────────────────────────────────────────── */
.card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-1);
  overflow: hidden;
}
.card-body { padding: 24px; }
.card-header {
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.card-title {
  font-size: 14px;
  font-weight: 500;
  color: var(--onyx);
}
.card-subtitle {
  font-size: 12px;
  color: var(--subtle);
  margin-top: 2px;
}

/* Entity card (company / contact) */
.entity-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-1);
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.entity-card-top {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.entity-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-sm);
  background: var(--cloud);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  color: var(--subtle);
  flex-shrink: 0;
  overflow: hidden;
}
.entity-name {
  font-size: 14px;
  font-weight: 500;
  color: var(--onyx);
  line-height: 1.3;
}
.entity-meta {
  font-size: 12px;
  color: var(--subtle);
  margin-top: 2px;
}
.entity-fields {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.entity-field {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 8px;
  font-size: 12px;
}
.entity-field-label { color: var(--subtle); flex-shrink: 0; }
.entity-field-value { color: var(--body); text-align: right; font-weight: 500; }

/* ─── Tables ─────────────────────────────────────────────────── */
/* Exact match to MuiTable + MuiTableCell overrides */
.table-wrap {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-1);
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}
thead {
  background: var(--cloud);
  border-bottom: 1px solid var(--border);
}
th {
  padding: 8px 8px 8px 16px;
  text-align: left;
  font-size: 12px;
  font-weight: 500;
  color: var(--subtle);
  line-height: 1.4;
  white-space: nowrap;
}
td {
  padding: 8px 8px 8px 16px;
  font-size: 12px;
  color: var(--body);
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
}
tbody tr:last-child td { border-bottom: none; }
tbody tr:hover td { background: var(--app-bg); }

/* Column variants */
.col-name   { font-weight: 500; color: var(--onyx); }
.col-num    { text-align: right; font-variant-numeric: tabular-nums; }
.col-link a { color: var(--sky); text-decoration: none; font-weight: 500; }
.col-link a:hover { text-decoration: underline; }
.col-muted  { color: var(--subtle); }
.col-trunc  { max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

/* Row number */
td.col-rank { color: var(--middle); font-size: 11px; width: 32px; }

/* ─── Badges / chips ─────────────────────────────────────────── */
/* Exact match to MuiChip: font-size 13px, font-weight 500, background cloud */
.chip {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: 100px;
  font-size: 13px;
  font-weight: 500;
  background: var(--cloud);
  color: var(--body);
  white-space: nowrap;
}
.chip-border {
  border: 1px solid var(--border);
  background: var(--white);
  font-size: 14px;
  font-weight: 400;
}

/* Status badges — pill shape, 11px, matched to alert colors */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  border-radius: 100px;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.02em;
  white-space: nowrap;
}
.badge-green   { background: var(--green-100);  color: var(--green-900); }
.badge-teal    { background: var(--success-100); color: var(--success); }
.badge-blue    { background: var(--blue-100);    color: var(--blue-700); }
.badge-sky     { background: var(--sky-100);     color: #1A5FAD; }
.badge-orange  { background: var(--warning-100); color: #9A5C00; }
.badge-red     { background: var(--error-100);   color: #8C0044; }
.badge-purple  { background: var(--purple-100);  color: var(--purple); }
.badge-grey    { background: var(--cloud);        color: var(--subtle); }
.badge-warm    { background: var(--warm-100);     color: #6B5033; }

/* ─── Alerts ─────────────────────────────────────────────────── */
/* Exact MuiAlert: padding 4px 8px, borderRadius 3px, icon 14px */
.alert {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 8px;
  border-radius: var(--radius-xs);
  font-size: 10px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.alert-icon { font-size: 14px; line-height: 1; }
.alert-success { background: var(--success-100); color: var(--success); }
.alert-warning { background: var(--warning-100); color: var(--warning); }
.alert-error   { background: var(--error-100);   color: var(--error); }
.alert-info    { background: var(--blue-100);     color: var(--blue); }

/* ─── Key-value pairs ────────────────────────────────────────── */
.kv-list { display: flex; flex-direction: column; }
.kv-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
  font-size: 14px;
}
.kv-row:first-child { padding-top: 0; }
.kv-row:last-child  { border-bottom: none; padding-bottom: 0; }
.kv-key   { color: var(--subtle); font-weight: 500; flex-shrink: 0; }
.kv-value { color: var(--onyx); text-align: right; word-break: break-word; max-width: 65%; }

/* ─── Tag list ───────────────────────────────────────────────── */
.tag-list { display: flex; flex-wrap: wrap; gap: 6px; }
.tag {
  padding: 3px 10px;
  background: var(--cloud);
  border: 1px solid var(--border);
  border-radius: 100px;
  font-size: 12px;
  color: var(--body);
}

/* ─── Progress bar ───────────────────────────────────────────── */
.progress-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
}
.progress-label { color: var(--body); flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.progress-track {
  flex: 2;
  height: 6px;
  background: var(--cloud);
  border-radius: 100px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: var(--green);
  border-radius: 100px;
  min-width: 2px;
}
.progress-value { color: var(--subtle); text-align: right; min-width: 36px; font-variant-numeric: tabular-nums; }

/* ─── Signal / event feed ────────────────────────────────────── */
.signal-list { display: flex; flex-direction: column; gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }
.signal-item {
  background: var(--white);
  padding: 12px 16px;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.signal-item:hover { background: var(--app-bg); }
.signal-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-top: 5px;
  flex-shrink: 0;
}
.signal-dot-green  { background: var(--green); }
.signal-dot-sky    { background: var(--sky); }
.signal-dot-orange { background: var(--warning); }
.signal-dot-red    { background: var(--error); }
.signal-dot-grey   { background: var(--middle); }
.signal-body { flex: 1; min-width: 0; }
.signal-title { font-size: 13px; font-weight: 500; color: var(--onyx); }
.signal-text  { font-size: 12px; color: var(--subtle); margin-top: 2px; line-height: 1.4; }
.signal-date  { font-size: 11px; color: var(--middle); flex-shrink: 0; }

/* ─── Trend arrow helpers ────────────────────────────────────── */
.trend-up   { color: var(--success); }
.trend-down { color: var(--error); }
.trend-flat { color: var(--subtle); }

/* ─── Divider ────────────────────────────────────────────────── */
.divider { height: 1px; background: var(--border); margin: 32px 0; }

/* ─── Two-pane profile layout ────────────────────────────────── */
.profile-layout { display: grid; grid-template-columns: 2fr 1fr; gap: 24px; align-items: start; }
@media (max-width: 992px) { .profile-layout { grid-template-columns: 1fr; } }

/* ─── Report footer ──────────────────────────────────────────── */
.report-footer {
  margin-top: 64px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 12px;
  color: var(--middle);
}
.report-footer a { color: var(--sky); text-decoration: none; }

/* ─── Print ──────────────────────────────────────────────────── */
@media print {
  body  { background: white; }
  .page { padding: 0; }
  .card, .table-wrap, .signal-list { box-shadow: none; }
  .report-footer { margin-top: 32px; }
}
```

### Vainu logo mark SVG

Use in `.report-wordmark`:
```html
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill="#0A0A0A" d="M18.3837 4.02611C18.424 4.04334 18.4606 4.0686 18.4914 4.10044L20.6407 6.32048C20.7547 6.43776 20.8451 6.5771 20.9068 6.73052C20.9684 6.88393 21.0001 7.04839 21 7.21447V12.3693C21 12.5352 20.9683 12.6995 20.9067 12.8528C20.845 13.0061 20.7547 13.1453 20.6407 13.2624L18.4899 15.4817C18.432 15.5409 18.3553 15.576 18.2743 15.5809C18.3559 15.5764 18.4332 15.5412 18.4915 15.4816L13.9846 20.1292C13.755 20.366 13.4436 20.499 13.119 20.4991H10.9078C10.5831 20.499 10.2718 20.366 10.0421 20.1292L8.30452 18.3364C8.24258 18.272 8.20782 18.1849 8.20782 18.0941C8.20782 18.0034 8.24258 17.9163 8.30452 17.8518L10.0108 16.0945C10.1246 15.9771 10.2596 15.8838 10.4083 15.8202C10.557 15.7566 10.7163 15.7239 10.8773 15.7239H16.5597C16.6983 15.7231 16.8336 15.6802 16.9487 15.6005C17.0638 15.5208 17.1535 15.4078 17.2066 15.2757C17.2598 15.1437 17.274 14.9983 17.2475 14.858C17.2233 14.73 17.1662 14.6114 17.0826 14.5143L15.8686 13.2616C15.7548 13.1442 15.6646 13.0049 15.6031 12.8515C15.5416 12.6981 15.51 12.5337 15.5101 12.3676V7.21367C15.5099 7.04777 15.5415 6.88346 15.603 6.73018C15.6645 6.57691 15.7548 6.43767 15.8686 6.32048L18.0218 4.10044C18.0526 4.0686 18.0892 4.04334 18.1295 4.02611C18.1698 4.00887 18.213 4 18.2566 4C18.3002 4 18.3434 4.00887 18.3837 4.02611Z"/>
  <path fill="#0A0A0A" d="M5.74731 4.00147C5.83527 4.00147 5.91967 4.03733 5.98212 4.10124L8.13222 6.32128C8.24619 6.43856 8.3366 6.5779 8.39825 6.73131C8.4599 6.88473 8.49159 7.04919 8.49148 7.21527V12.3701C8.49153 12.536 8.45981 12.7003 8.39816 12.8536C8.33651 13.0069 8.24614 13.1461 8.13222 13.2632L5.97977 15.4825C5.91722 15.5462 5.83286 15.5819 5.74496 15.5819C5.65706 15.5819 5.5727 15.5462 5.51015 15.4825L3.35848 13.2624C3.12909 13.0251 3.00019 12.7036 3 12.3684V7.21447C3.00005 6.87949 3.12899 6.55823 3.35848 6.32128L5.51249 4.10124C5.57495 4.03733 5.65934 4.00147 5.74731 4.00147Z"/>
</svg>
```

---

## Step 4 — HTML structure rules

Produce a **complete, self-contained `.html` file** — nothing external except the
Google Fonts `@import` already inside the `<style>` block.

### Document skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[descriptive title]</title>
  <style>/* full CSS block above */</style>
</head>
<body>
<main class="page">

  <!-- Report header -->
  <header class="report-header">
    <div class="report-wordmark">
      <!-- SVG logo mark -->
      <span class="report-wordmark-text">Vainu</span>
    </div>
    <div class="report-eyebrow">[report type, e.g. "Market Analysis"]</div>
    <h1 class="report-title">[report title]</h1>
    <p class="report-description">[one-sentence scope description]</p>
    <div class="report-meta">
      <span class="report-meta-item">Generated <strong>[DD MMM YYYY]</strong></span>
      <span class="report-meta-item">Entities <strong>[count]</strong></span>
      <!-- add relevant meta like market, filters applied, etc. -->
    </div>
  </header>

  <!-- Stat row (top-level numbers, if applicable) -->
  <div class="stat-row">
    <div class="stat-cell">
      <div class="stat-label">Total companies</div>
      <div class="stat-value">1,234</div>
    </div>
    <!-- more stat-cells -->
  </div>

  <!-- Sections -->
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">Companies</h2>
      <div class="section-rule"></div>
      <span class="section-count">48 results</span>
    </div>
    <!-- section content: table-wrap / card grid / kv-list / signal-list -->
  </section>

</main>

<footer class="report-footer">
  <span>Generated <strong>[date]</strong> · Powered by <a href="https://vainu.io">Vainu</a></span>
  <span>[subject or filter summary]</span>
</footer>
</body>
</html>
```

### Layout selection guide

| Data shape | Use |
|---|---|
| List of entities (>5 rows, many columns) | `table-wrap > table` |
| Small set of entities (≤6) to highlight | `cols-auto` grid of `entity-card` |
| Single entity detail | `profile-layout` with `kv-list` + sidebar `card` |
| Aggregate numbers | `stat-row` at the top |
| Distribution / ranking | `progress-row` per item in a `card` |
| News / signals / events | `signal-list` |
| Mixed key facts | `card` with `kv-list` inside |

### Grid layout rules

#### stat-row — mandatory explicit column count

`auto-fill` cannot know how many tiles you will place, so it produces orphaned tiles whenever the count doesn't divide cleanly into the browser's chosen column width. **Always** set the column count explicitly via inline style:

```html
<div class="stat-row" style="grid-template-columns: repeat(N, 1fr);">
```

Where `N` = the exact number of `stat-cell` children. Follow this decision table:

| KPI count | Do this |
|---|---|
| 4 | `repeat(4, 1fr)` — single row |
| 5 | `repeat(5, 1fr)` — single row |
| 6 | `repeat(6, 1fr)` — single row |
| 7 | Split: one `stat-row` with 4, one with 3 — or drop/merge to reach 6 |
| 8 | `repeat(4, 1fr)` — two clean rows of 4 |
| 9 | Split: 5 + 4, or 3 + 3 + 3 using separate stat-rows |
| 10 | `repeat(5, 1fr)` — two rows of 5 |
| 12 | `repeat(4, 1fr)` — three rows of 4, or `repeat(6, 1fr)` two rows of 6 |

**Never** use more than 6 columns — cells become too narrow to read on 1360px pages. If you have >6 KPIs that must show, use two stacked `stat-row` blocks.

**Before writing the HTML:** count your KPIs, pick N from the table, set the inline style. This is not optional.

#### cols-* card grids — avoid orphaned tiles

Before using a multi-column grid, divide the item count by the column count and check for a bad remainder:

- `cols-4` (4 columns): avoid counts like 5 (4+1), 9 (8+1), 13 — use `cols-3` or `cols-2` instead, or adjust column count so the last row is full or at least half-full.
- `cols-3` (3 columns): avoid counts like 4 (3+1), 7, 10 — switch to `cols-2` or `cols-4` if the remainder is just 1.
- `cols-2` (2 columns): fine for any even count; for an odd count, consider a table or making the last card full-width with `grid-column: 1 / -1`.
- `cols-auto` uses `minmax(240px, 1fr)` — the browser decides column count based on viewport. Safe for 5+ items; for small counts (2–4) prefer an explicit `cols-2` or `cols-3` to avoid a single wrapped tile on wide screens.

**Rule of thumb:** the last row must contain at least half the columns. If it doesn't, reduce the column count or reorganise the content.

### Content rules

- Numbers: `toLocaleString()` formatting — `1,234,567`, `€42.5M`, `94%`
- Dates: `DD MMM YYYY` — `23 Apr 2026`
- Percentages: include `%` suffix and right-align in tables (`col-num`)
- Null / unknown values: use `—` (em dash), `.col-muted` class
- Long strings in table cells: add `col-trunc` to `td` and a `title="full value"` attribute
- Industry / size / status: pick the closest badge color semantically (green = active/positive, orange = caution/mid, blue = informational, grey = unknown)
- Delta / growth: use `.trend-up` / `.trend-down` span with `↑` / `↓` prefix
- Signals: assign dot color by signal type (green = hiring/growth, sky = news, orange = leadership change, red = risk)

---

## Step 5 — Save and confirm

1. Resolve the output path (from `$ARGUMENTS` or `~/Desktop/<slug>.html`)
2. Create parent directory if needed
3. Write the file with `Write`
4. Reply: file path, one-sentence summary of content, entity/row count
