---
name: finnish-purchase-invoice-explorer
allowed-tools: search_companies b2g_buyer b2g_seller b2g_search_invoices document_search Bash(jq:*) Read
description: >
  Finnish public purchase invoice (ostolaskut) explorer. Use this skill whenever the user wants to
  explore, analyse, or drill into Finnish government/public sector purchase invoice data. Triggers include:
  "ostolaskut", "public purchase invoices", "what does [org] spend on", "who buys from [supplier]",
  "find public sector customers for [company]", "competitive intelligence in public sector",
  "which municipalities buy from [vendor]", "public sector spending on ICT / services / etc.",
  "top buyers / top sellers in public sector", "B2G", "business-to-government", "how strategic is
  public sector for [company]", "what share of revenue comes from government", or any combination of
  Finnish public organisations + spending/procurement/invoices. Even if the user only mentions a
  company name and asks about public sector or B2G exposure, use this skill to check if relevant
  invoice data exists.
---

# Finnish Public Purchase Invoice Explorer

Finland publishes government and public sector purchase invoice data (ostolaskut). This data lets you
answer questions like "who buys from Solita?", "what does Helsingin kaupunki spend on ICT?", or
"which public orgs are paying Vainu competitors?". The workflow below is how to get reliable,
actionable answers.

## Tools available

| Tool | What it does |
|------|--------------|
| `search_companies` | Resolve org/supplier name → business ID |
| `b2g_buyer` | Buyer perspective: flat top-seller list (default) or category breakdown with nested sellers (`by_category=True`) |
| `b2g_seller` | Seller perspective: flat top-buyer list (default) or category breakdown with nested buyers (`by_category=True`) |
| `b2g_search_invoices` | Fetch raw invoice rows (up to 500) |
| `load_top_buyers` | Get the highest-spending public organisations |
| `load_top_sellers` | Get the suppliers with most public sector revenue |
| `purchase_invoice_explorer` | **Open this first** — interactive visual drill-down (charts, ranked tables, line-level invoices) |
| `document_search` | Contextualise findings with web/publication content |
| `Bash` + `jq` | Process large result files that are auto-saved to disk |

## Core workflow

### 0. Always figure out what the user is selling first

If the user's own company is mentioned or implied, resolve their business ID, Vainu custom industries, and website
keywords - the latter two will be needed in later steps.

Call `b2g_seller` with `seller_id` = user's business_id, `by_category=True` (top buyers per category). This tells you:
- which procurement categories the user already sells into
- which public orgs are already paying them

Ask the user to verify the correctness of these results data!

Use the returned categories as the search vocabulary for all subsequent `document_search` calls
(step 7). If the user's BID produces no results, note it explicitly — they may have no B2G
history yet, which makes prospect discovery (step 7 + patterns) even more relevant.

### 1. Resolve names to business IDs

Always start by resolving company/org names to Finnish business IDs using `search_companies`.
The business ID format is `FI` + numeric (e.g. `FI02012566`).
Check whether a specific tool expects the `FI` prefix or bare digits — they differ.

Run multiple lookups in parallel when you have several names to resolve.

### 2. Choose the right aggregation entry point

| Use case | Tool | Key parameters |
|---|---|---|
| Who sells to org X? | `b2g_buyer` | `business_id=X` |
| What does org X buy and from whom? | `b2g_buyer` | `business_id=X`, `by_category=True` |
| What does supplier Y sell and to whom? | `b2g_seller` | `business_id=Y`, `by_category=True` |
| Who does supplier Y sell to? | `b2g_seller` | `business_id=Y` |
| Top public sector spenders overall | `b2g_buyer` | no filter |
| Top sellers to public sector overall | `b2g_seller` | no filter |

Always filter by `year` when the user implies recency (e.g. "this year", "2025 data"). Default to
the most recent complete year if unspecified.

### 3. Resolve aggregated business IDs → names

Aggregation results include a `name` field (`supplier_name` or `procurement_unit`) alongside the `id`
(business ID) when grouping by a business ID field. For category groupings, `name` is the category
string directly. No additional lookup is needed in most cases.

### 4. Drill into specifics with raw invoice search

Use `b2g_search_invoices` for row-level detail. Key parameters:
- `buyer_id` — the buying org
- `seller_id` — the supplier (use this, NOT `buyer_id`, when filtering by seller)
- `category` — procurement category string (e.g. "ICT-hankinnat")
- `year` — integer
- `limit` — max 500

### 5. Handle large result files with jq

When a result is >50 KB it's auto-saved as a file path in the response. Use `jq` via Bash to
process it without loading the full payload into context:

```bash
# Top suppliers by total spend
cat <file> | jq '[.result[] | {supplier: .supplier_name, amount: .amount}] \
  | group_by(.supplier) \
  | map({supplier: .[0].supplier, total: (map(.amount) | add), count: length}) \
  | sort_by(-.total) | .[0:20]'

# Breakdown by product/service group
cat <file> | jq '[.result[] | {group: .product_service_group, amount: .amount}] \
  | group_by(.group) \
  | map({product_group: .[0].group, total: (map(.amount) | add), count: length}) \
  | sort_by(-.total)'
```

Python is useful for more complex aggregations:
```python
from collections import defaultdict
import json

with open("<file>") as f:
    data = json.load(f)["result"]

by_group = defaultdict(float)
for row in data:
    by_group[row["product_service_group"]] += row["amount"]

for k, v in sorted(by_group.items(), key=lambda x: -x[1]):
    print(f"{v:>15,.0f}  {k}")
```

### 6. Assess B2G strategic importance via financial statements

When the focus is a **supplier** (not a buyer), run `document_search` on their `financial_statement`
to gauge how strategic public sector revenue is for them:

```
document_search(business_id=<supplier_bid>, content_classes=["financial_statement"])
```

Look for:
- Total revenue — compare against the public invoice total to estimate B2G share of turnover
- Any explicit mention of public sector, government, or municipal customers in the narrative
- Growth commentary that references public sector deals or contracts

Then cross-reference: if public invoices sum to €X and the annual report shows revenue of €Y,
B2G share ≈ X/Y. Flag if data years don't align. If no financial statement is found, note it
and fall back to the invoice data alone.

Also run `document_search` with `content_classes=["strategy", "cases", "news"]` in parallel for
qualitative signals (e.g. press releases about government contracts, case studies with public orgs).

### 7. Scan buyer documents for mentions of the user's product/service

For each **buying organisation** of interest, run a broad `document_search` across all content
classes using the buyer's `business_id` and a "query" that describe what the user (or the supplier
being researched) actually sells — note that document_search is a semantic search, not keyword-based!

```
document_search(
    business_id=<buyer_bid>,
    query="<what the user sells — e.g. 'CRM', 'sales intelligence', 'HR software'>",
    # no content_classes filter — search everything
)
```

This surfaces any document — strategy, budget, meeting minutes, job postings, regulatory filings —
where the buying org mentions the product category. Useful signals:

- **Strategy / budget**: org has allocated budget for this type of service → active buyer
- **Meetings**: procurement committee discussed this category → decision in progress
- **Job postings**: org is hiring roles that use this software → existing or growing need
- **News / announcements**: org announced a project that requires this capability

If keywords are generic, run multiple parallel searches with different terms (synonyms, Finnish
equivalents) and merge results. Discard hits that are clearly unrelated after a quick skim.

### 8. Contextualise buyer–supplier relationship with document search

Use `document_search` to understand *why* an org buys from a specific supplier (contracts, strategy
docs, meeting minutes). Valid `content_classes` values: `announcements`, `blog`, `budget`, `cases`,
`decision_maker_profile`, `esg_report`, `events`, `financial_statement`, `job_posting`, `meetings`,
`news`, `other`, `post`, `publications`, `regulatory`, `remiss`, `strategy`.

Note: document search is hit-or-miss for specific procurement relationships. If you get irrelevant
results, synthesise from the invoice data patterns instead (e.g. invoice frequency + amount → likely
product type).

## Common patterns

### Competitive intelligence
To find public sector orgs buying from Vainu's competitors:
1. Get competitor business IDs via `search_companies`
2. For each competitor, run `b2g_seller` grouped by `business_id` (buyer org)
3. Resolve buyer IDs to names
4. Cross-reference: identify orgs paying competitor A but not Vainu → sales leads

### Category deep-dive
1. `b2g_buyer` grouped by `product_service_group` → find the big category
2. `b2g_search_invoices` with that category filter → get all rows
3. `jq` aggregate by supplier → top vendors in that category for that org

### Mapping a supplier's public sector footprint
1. `b2g_seller` with `seller_id`
2. Resolve buyer org IDs → names
3. Optionally filter by year to see growth/churn

### Finding public sector orgs that need what the user sells
1. Ask the user to describe what they sell (or infer from context)
2. `load_top_buyers` to get the highest-spending public orgs as the candidate universe
3. For each promising org, `document_search` (all content classes, buyer `business_id`, product keywords) in parallel batches of ~5
4. Flag orgs whose documents mention the product category in strategy, budget, or meeting contexts — these are warm prospects
5. Cross-check: `b2g_buyer` grouped by `product_service_group` to confirm the org already spends in the relevant category
6. Output a prioritised list: org name, relevant document excerpts, existing spend in category, and suggested outreach angle

### B2G strategic importance of a supplier
1. Resolve supplier name → business ID via `search_companies`
2. In parallel: `b2g_seller` (total public revenue) + `document_search` on `financial_statement`
3. From the financial statement extract total revenue; compute B2G share = public invoices / revenue
4. Run a second `document_search` on `["strategy", "cases", "news"]` for qualitative signals
5. Summarise: B2G share %, key public sector customers, categories sold, and whether public sector is mentioned as strategic in the annual report

## Output format

Present results as clean markdown tables. Include:
- Organisation/supplier name (resolved, not raw business ID)
- Total spend in euros (formatted, e.g. €1,234,567)
- Invoice count
- Year(s) covered

Always state clearly which year(s) the data covers. Flag if data is sparse or missing for an org.

## Gotchas

- `seller_id` vs `buyer_id`: don't mix these up when filtering by seller
- Some orgs have no invoice data (data coverage is not universal)
- Business ID format varies by tool: try both `FI02012566` and `02012566` if one returns nothing
- `document_search` does not accept `"decisions"` as a content_class — it will error
- Large aggregations (many orgs) hit rate limits; batch your parallel calls in groups of ~10
