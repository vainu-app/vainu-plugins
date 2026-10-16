# Event types reference

Canonical list for vainu-mcp: `vainu.data.mcp.event_types_data` → `EVENT_TYPES_DATA` (`EventTypeRow`: id, label, category, databases).  Filtering uses **numeric id**.

## Quick reference table

| ID      | Label                                              | Category   | Databases |
|---------|----------------------------------------------------|------------|-----------|
| 6967635 | EU funding                                         | finance    | FI        |
| 43544   | Internationalization                               | major      | FI, SE, DK, NL, US, NO |
| 2999389 | Registered web-address / domain                    | marketing  | FI, SE, NO, NL, DK |
| 8000040 | Achieved 1MEUR Turnover                            | finance    | FI, SE, NO, DK |
| 8000076 | Stock Trade                                        | normal     | US, GB, NO |
| 8000080 | Change of Company Form                             | basic_data | FI        |
| 6931739 | Change in Credit Rating                            | other      | FI        |
| 43551   | Awards                                             | other      | US, GB, NL, NO, SE, DK, FI |
| 8000034 | Key Person Departure                               | staff      | FI, SE, NO, DK, NL, FR |
| 8000039 | Change in Board of Directors                       | staff      | FI, SE, NO, DK, FR, FI_realestate |
| 8000052 | Granted Public Transport License                   | public     | FI        |
| 8000063 | New CMS Platform                                   | technology | (all)     |
| 8000064 | New ATS Tool                                       | technology | (all)     |
| 8000072 | Change of Company Name                             | basic_data | (all)     |
| 77883   | Mergers & Acquisitions                             | major      | US, GB, NL, NO, SE, DK, FI, FR |
| 8000060 | New Auxiliary Name                                 | basic_data | FI, SE, NL, DK, NO |
| 43545   | Won Contracts                                      | normal     | US, GB, NL, NO, SE, DK, FI, FR |
| 8000016 | Public Decision on Financing                       | finance    | NO        |
| 8000018 | Growth in Sales or Market Share                    | finance    | NO, DK, NL, SE, FI |
| 8000053 | Granted Cargo Transport License                   | public     | FI        |
| 8000058 | New Vehicle                                        | other      | FI, SE, NO |
| 8000073 | New Reservation Technology                         | technology | (all)     |
| 8000077 | IPO                                                | major      | FI, NL, SE, NO |
| 8000083 | New CRM Technology                                 | technology | (all)     |
| 4507192 | Partnerships                                       | normal     | US, GB, NL, NO, SE, DK, FI, FR |
| 8000065 | New Server Technology                              | technology | (all)     |
| 2932622 | New Product / Service                              | normal     | US, GB, NL, NO, SE, DK, FI, FR |
| 8000010 | Bankruptcy                                         | finance    | NL, SE, NO, DK, FI |
| 8000013 | Patents                                            | public     | US, FI, SE, NO, DK |
| 8000022 | Change in Strategy                                 | major      | NL, NO, FI, SE, DK |
| 8000029 | Legal Dispute                                      | negative   | SE, DK, NO, FR, FI |
| 8000074 | New Payment Technology                             | technology | (all)     |
| 43535   | Open Positions                                     | staff      | US, GB, NL, NO, SE, DK, FI, FR |
| 8000020 | Investment - Machines and equipment                | major      | FI, SE, DK, NO, NL |
| 8000050 | New Company Established                            | major      | FI, SE, NO, NL, DK |
| 8000019 | Investment - New Place of Business                | major      | FI, SE, NO, DK, NL, US, GB, FR |
| 8000021 | Investment – Software                              | major      | FI, NL    |
| 8000024 | Earnings Release                                   | finance    | US, GB, NL, NO, SE, DK, FI, FR |
| 8000025 | Decline in Sales or Market Share                  | finance    | NL, NO, SE, FI, DK |
| 8000037 | New Financial Statement                            | finance    | FI, SE, NO |
| 8000066 | New Analytics Tool                                 | technology | (all)     |
| 8000068 | New Trademark                                      | public     | (all)     |
| 8000061 | New e-commerce technology                          | technology | (all)     |
| 8000081 | Granted Energy Certificate                         | other      | FI, FI_realestate |
| 8000049 | Late Registration of Financial Statement          | finance    | FI, SE, NO |
| 8000062 | New Chat and Support Tool                          | technology | (all)     |
| 8000075 | New Advertising Technology                        | technology | (all)     |
| 2943080 | Protest list                                       | finance    | FI, FI_realestate |
| 8000071 | Apartment sales notice                             | other      | FI, FI_realestate |
| 8000084 | New Social Media Channel                           | technology | (all)     |
| 6067468 | Change in Legislation                              | public     | FI        |
| 3325073 | Relocation                                         | normal     | FI, SE, DK, NL, NO |
| 8000054 | Granted social services or health services license| public     | FI        |
| 6893088 | Key Person Appointment                             | staff      | FI, SE, NO, NL, DK, US, GB, FR |
| 6944439 | Minutes                                            | public     | FI, SE, NO, DK, FI_realestate |
| 4467311 | New Technology                                     | technology | (all)     |
| 7200000 | Permit                                             | public     | FI, FI_realestate |
| 8000056 | Granted Alcohol License                            | public     | FI        |
| 8000059 | New Marketing Automation Tool                      | technology | (all)     |
| 8000069 | Change of Status                                   | basic_data | (all)     |
| 8000085 | Construction Project                               | major      | NL, FI, DK, SE, NO |
| 8000086 | Temporary exceptions in business                   | other      | FI        |
| 2940230 | Government & Public Contract Notices               | public     | FI, SE, NL, NO, DK, FI_realestate |
| 43543   | Funding                                            | major      | US, GB, NL, NO, SE, DK, FI, FR |
| 8000015 | Events                                             | marketing  | FI, NO, NL, FR, SE, DK |
| 77884   | Changes in Personnel                               | staff      | GB, NL, NO, SE, DK, FI, US, FR |
| 4507212 | Financial (Equity) Arrangements                    | finance    | FI, SE, NO, DK |
| 43536   | Layoffs                                            | finance    | NL, NO, SE, DK, FI, US, GB |
| 8000002 | Real Estate Transactions                           | normal     | US, GB, NL, NO, SE, DK, FI, FI_realestate |
| 8000038 | Change of CEO                                      | staff      | FI, SE, NO, DK, NL, US, GB |
| 8000051 | Granted Taxi License                              | public     | FI        |
| 8000090 | Environmental Impact Assessment                    | other      | FI, SE, NO, DK |

---

## Deeper descriptions

Concise descriptions for each event: **what it means** and **what it can be used for**. Use these to match user intent to the right event IDs. Based on signals/news data and canonical event semantics.

### Finance

- **6967635 – EU funding**  
  - *What it means:* Company has received or been granted EU-level funding (e.g. programmes, grants). Raised when such funding is reported or registered (FI).  
  - *Use cases:* Lead scoring for EU-backed companies, funding-campaign targeting, public-sector and innovation-focused lists.

- **8000040 – Achieved 1MEUR Turnover**  
  - *What it means:* Company’s turnover has reached or exceeded 1 million EUR (or local equivalent). Milestone indicating growth into a larger size class.  
  - *Use cases:* Growth-stage targeting, account prioritization, upsell for companies crossing the 1M threshold.

- **8000080** – (see basic_data)

- **6931739 – Change in Credit Rating**  
  - *What it means:* A credit bureau or rating agency has changed the company’s credit rating (upgrade or downgrade). FI only.  
  - *Use cases:* Risk monitoring, credit and collections, financing and partnership decisions.

- **8000016 – Public Decision on Financing**  
  - *What it means:* A public body has made a formal decision on financing (e.g. grants, loans, guarantees). NO only.  
  - *Use cases:* Tracking publicly funded projects and beneficiaries, B2G and funding-intelligence lists.

- **8000018 – Growth in Sales or Market Share**  
  - *What it means:* Company has reported or been attributed growth in sales or market share (revenue growth, market-share gains).  
  - *Use cases:* Growth and expansion targeting, competitive intelligence, upsell and partnership signals.

- **8000010 – Bankruptcy**  
  - *What it means:* Company has entered bankruptcy or similar insolvency proceedings.  
  - *Use cases:* Risk and exposure management, restructuring and insolvency services, list cleanup.

- **8000024 – Earnings Release**  
  - *What it means:* Company has published earnings or annual/quarterly results (revenue, profit, guidance). Often linked to press releases and regulatory filings.  
  - *Use cases:* Investor and sales timing, financial health checks, event-based outreach around results.

- **8000025 – Decline in Sales or Market Share**  
  - *What it means:* Company has reported or been attributed a decline in sales or market share.  
  - *Use cases:* Restructuring and cost-saving sales, risk monitoring, turnaround and advisory targeting.

- **8000037 – New Financial Statement**  
  - *What it means:* A new financial statement (annual report, accounts) has been filed or published. FI, SE, NO.  
  - *Use cases:* Fresh financial data for scoring and analytics, compliance and audit-related lists, timing for finance-based campaigns.

- **8000049 – Late Registration of Financial Statement**  
  - *What it means:* Company filed its financial statement after the statutory deadline.  
  - *Use cases:* Compliance and risk flags, governance and advisory targeting.

- **2943080 – Protest list**  
  - *What it means:* Company has been added to a protest list (e.g. tax or payment protest list). FI, FI_realestate.  
  - *Use cases:* Credit and payment risk, compliance and B2B risk screening.

- **4507212 – Financial (Equity) Arrangements**  
  - *What it means:* Equity-related events such as share buybacks, capital increases, or other formal financial/equity arrangements.  
  - *Use cases:* Investor relations, M&A and corporate development, financing and ownership monitoring.

- **43536 – Layoffs**  
  - *What it means:* Company has announced or implemented layoffs or significant workforce reductions.  
  - *Use cases:* HR and outplacement services, cost-saving and restructuring sales, risk and stability assessment.

### Staff

- **8000034 – Key Person Departure**  
  - *What it means:* A key person (e.g. executive, founder, key manager) has left the company. Often co-occurs with Change of CEO or Changes in Personnel.  
  - *Use cases:* Executive change outreach, succession and recruitment, account and relationship updates.

- **8000039 – Change in Board of Directors**  
  - *What it means:* One or more board members have been appointed, resigned, or changed role (e.g. new chair, new board member).  
  - *Use cases:* Governance and advisory targeting, investor and stakeholder mapping, board-level sales.

- **43535 – Open Positions**  
  - *What it means:* Company has published or is actively recruiting for open positions (job postings, hiring).  
  - *Use cases:* Recruitment and staffing sales, growth and expansion signals, employer-branding campaigns.

- **6893088 – Key Person Appointment**  
  - *What it means:* A key person has been appointed (e.g. new CEO, president, VP, director). Often overlaps with Change of CEO and Changes in Personnel.  
  - *Use cases:* New-decision-maker outreach, executive onboarding campaigns, relationship mapping.

- **77884 – Changes in Personnel**  
  - *What it means:* Broader personnel changes: hires, departures, or role changes (not limited to CEO/board). Aggregates multiple staff events.  
  - *Use cases:* HR and recruitment targeting, account planning, organizational change intelligence.

- **8000038 – Change of CEO**  
  - *What it means:* The company’s CEO (or equivalent top executive) has changed. Commonly seen in press and regulatory announcements.  
  - *Use cases:* New-leadership outreach, sales timing, executive briefing and relationship building.

### Major

- **43544 – Internationalization**  
  - *What it means:* Company has taken a step into new countries or markets (e.g. subsidiary, office, market entry).  
  - *Use cases:* Export and expansion services, international partnership and sales targeting.

- **77883 – Mergers & Acquisitions**  
  - *What it means:* M&A activity: acquisitions, mergers, divestments, EU/competition approvals, strategic stakes. Sourced from news and regulatory filings.  
  - *Use cases:* M&A and corporate development targeting, integration and advisory services, competitive and market mapping.

- **8000077 – IPO**  
  - *What it means:* Company has gone public (initial public offering) or related IPO news. FI, NL, SE, NO.  
  - *Use cases:* Investor relations and equity sales, post-IPO advisory and services.

- **8000022 – Change in Strategy**  
  - *What it means:* Company has announced or reported a significant strategic shift (pivot, new focus, restructuring of strategy).  
  - *Use cases:* Consulting and advisory targeting, change-management and strategy sales.

- **8000020 – Investment - Machines and equipment**  
  - *What it means:* Significant investment in machinery, equipment, or production capacity has been reported.  
  - *Use cases:* Industrial and equipment sales, capacity expansion and CAPEX targeting.

- **8000050 – New Company Established**  
  - *What it means:* A new company (legal entity) has been registered or established.  
  - *Use cases:* New-business targeting, incorporation and startup services, early-stage sales.

- **8000019 – Investment - New Place of Business**  
  - *What it means:* Company has opened or announced a new location, office, or place of business.  
  - *Use cases:* Real estate and facility services, local B2B targeting, expansion campaigns.

- **8000021 – Investment – Software**  
  - *What it means:* Significant investment in software (licenses, systems, digitalization) has been reported. FI, NL.  
  - *Use cases:* Software and IT sales, digitalization and transformation targeting.

- **8000085 – Construction Project**  
  - *What it means:* Company is involved in or has started a construction project (new build, major renovation, infrastructure). Often appears with public tenders and contract notices.  
  - *Use cases:* Construction and building-materials sales, subcontractor and project targeting, public-project tracking.

- **43543 – Funding**  
  - *What it means:* Company has received funding (venture, growth, debt, grants, etc.). Covers pre-seed to late-stage and strategic investments.  
  - *Use cases:* Post-funding sales, investor and startup lists, growth and expansion targeting.

### Technology

- **8000063 – New CMS Platform**  
  - *What it means:* Company’s website or digital presence shows adoption of a new content management system (e.g. WordPress, Drupal, new CMS).  
  - *Use cases:* CMS and web-platform sales, digital presence and content tool targeting.

- **8000064 – New ATS Tool**  
  - *What it means:* Company has adopted a new applicant tracking system (recruitment software).  
  - *Use cases:* HR tech and ATS sales, recruitment software targeting.

- **8000073 – New Reservation Technology**  
  - *What it means:* Company has adopted new booking or reservation technology (e.g. for appointments, tables, travel).  
  - *Use cases:* Booking and reservation software sales, hospitality and service-industry targeting.

- **8000083 – New CRM Technology**  
  - *What it means:* Company has adopted a new CRM or sales/contact management platform.  
  - *Use cases:* CRM and sales-tech targeting, post-implementation services and add-ons.

- **8000065 – New Server Technology**  
  - *What it means:* New server, hosting, or infrastructure technology has been detected (e.g. cloud, CDN, server software).  
  - *Use cases:* Infrastructure and cloud sales, DevOps and IT ops targeting.

- **8000074 – New Payment Technology**  
  - *What it means:* Company has adopted new payment or checkout technology (e.g. payment provider, gateway).  
  - *Use cases:* Payment and fintech sales, e-commerce and retail targeting.

- **8000066 – New Analytics Tool**  
  - *What it means:* Company has adopted new analytics, BI, or data tools (e.g. web analytics, dashboards).  
  - *Use cases:* Analytics and BI sales, data-driven marketing and product targeting.

- **8000061 – New e-commerce technology**  
  - *What it means:* New e-commerce platform or online sales technology has been detected.  
  - *Use cases:* E-commerce platform and plugin sales, online retail and D2C targeting.

- **8000062 – New Chat and Support Tool**  
  - *What it means:* Company has adopted new chat, messaging, or customer-support technology.  
  - *Use cases:* Support and chat software sales, customer-service and CX targeting.

- **8000075 – New Advertising Technology**  
  - *What it means:* New advertising or ad-tech solution has been adopted (e.g. ad server, programmatic, tracking).  
  - *Use cases:* Ad tech and mar tech sales, marketing and media targeting.

- **8000084 – New Social Media Channel**  
  - *What it means:* Company has started using a new social media channel or presence (e.g. new platform account).  
  - *Use cases:* Social and community marketing sales, influencer and social campaign targeting.

- **4467311 – New Technology**  
  - *What it means:* Generic detection of new technology adoption (software, platform, or tool) when no specific technology event type fits.  
  - *Use cases:* Broad tech-stack and digitalization targeting, technology trend analysis.

- **8000059 – New Marketing Automation Tool**  
  - *What it means:* Company has adopted new marketing automation or email/campaign automation technology.  
  - *Use cases:* Marketing automation and email platform sales, demand-generation targeting.

### Public

- **8000052 – Granted Public Transport License**  
  - *What it means:* Authority has granted the company a license to operate public transport (e.g. bus, tram). FI.  
  - *Use cases:* Transport and mobility B2B, public-sector and regulated-industry lists.

- **8000053 – Granted Cargo Transport License**  
  - *What it means:* Authority has granted a license for cargo/freight transport. FI.  
  - *Use cases:* Logistics and freight sales, transport and supply-chain targeting.

- **8000013 – Patents**  
  - *What it means:* Company has been granted or applied for a patent (or patent activity has been recorded).  
  - *Use cases:* IP and innovation targeting, R&D and licensing, competitive intelligence.

- **8000068 – New Trademark**  
  - *What it means:* Company has registered or applied for a new trademark.  
  - *Use cases:* Brand and IP monitoring, licensing and partnership targeting.

- **6067468 – Change in Legislation**  
  - *What it means:* Legislative or regulatory change that may affect companies (e.g. sector-specific law). FI.  
  - *Use cases:* Compliance and legal services, regulatory change alerts and thought leadership.

- **8000054 – Granted social services or health services license**  
  - *What it means:* Company has been granted a license to provide social or health services. FI.  
  - *Use cases:* Healthcare and social care B2B, regulated care and welfare targeting.

- **6944439 – Minutes**  
  - *What it means:* Meeting minutes or similar official records have been published (e.g. board, municipal).  
  - *Use cases:* Governance and transparency research, public-sector and compliance monitoring.

- **7200000 – Permit**  
  - *What it means:* A permit of general or sector-specific type has been granted to the company. FI, FI_realestate.  
  - *Use cases:* Permits and compliance tracking, real estate and construction related lists.

- **8000056 – Granted Alcohol License**  
  - *What it means:* Company has been granted a license to sell or serve alcohol. FI.  
  - *Use cases:* Hospitality and retail alcohol sales, venue and restaurant targeting.

- **2940230 – Government & Public Contract Notices**  
  - *What it means:* Public procurement or government contract notices (tenders, contract awards, E3 notices). Often linked to construction, services, and supplies.  
  - *Use cases:* B2G and public tenders, subcontractor and bidder targeting, contract and project intelligence.

- **8000051 – Granted Taxi License**  
  - *What it means:* Authority has granted a taxi or similar passenger transport license. FI.  
  - *Use cases:* Transport and mobility sales, regulated transport operator lists.

### Marketing

- **2999389 – Registered web-address / domain**  
  - *What it means:* Company has registered a new domain or web address (or change was recorded).  
  - *Use cases:* Web and domain services, rebrand and launch detection, digital presence targeting.

- **8000015 – Events**  
  - *What it means:* Company is organizing or participating in a notable event (conference, trade show, webinar, etc.).  
  - *Use cases:* Event sponsorship and participation sales, audience and engagement targeting.

### Basic data

- **8000080 – Change of Company Form**  
  - *What it means:* Legal form of the company has changed (e.g. from partnership to limited company). FI.  
  - *Use cases:* Corporate and legal services, governance and restructuring lists.

- **8000072 – Change of Company Name**  
  - *What it means:* Official company name has changed in the business register.  
  - *Use cases:* Data quality and deduplication, rebrand and merger follow-up.

- **8000060 – New Auxiliary Name**  
  - *What it means:* A new trade name, DBA, or auxiliary name has been registered.  
  - *Use cases:* Brand and branch tracking, multi-brand and franchise mapping.

- **8000069 – Change of Status**  
  - *What it means:* Company’s official status has changed (e.g. active, dormant, dissolved, under liquidation).  
  - *Use cases:* List hygiene, risk and compliance, lifecycle-based targeting.

### Normal

- **8000076 – Stock Trade**  
  - *What it means:* Notable stock or share trading activity (e.g. listed company). US, GB, NO.  
  - *Use cases:* Investor and equity-related targeting, market and trading intelligence.

- **43545 – Won Contracts**  
  - *What it means:* Company has won a contract (public tender, framework, or major B2B deal). Often appears with Government & Public Contract Notices and Construction.  
  - *Use cases:* Post-win sales (subcontractors, suppliers), contract and project intelligence, competitive tracking.

- **4507192 – Partnerships**  
  - *What it means:* Company has announced or entered a partnership, collaboration, or strategic alliance.  
  - *Use cases:* Partnership and channel sales, ecosystem and alliance targeting.

- **2932622 – New Product / Service**  
  - *What it means:* Company has launched a new product or service (or significant product expansion).  
  - *Use cases:* Product launch timing, complementary product and channel sales, competitive and market tracking.

- **3325073 – Relocation**  
  - *What it means:* Company has moved or announced a move to a new address or location.  
  - *Use cases:* Relocation and facility services, local and regional targeting, data quality updates.

- **8000002 – Real Estate Transactions**  
  - *What it means:* Company has been involved in a real estate transaction (purchase, sale, lease of property).  
  - *Use cases:* Real estate and property services, facility and location-based targeting.

### Other

- **43551 – Awards**  
  - *What it means:* Company has received an award, recognition, or ranking (industry, innovation, employer, etc.).  
  - *Use cases:* PR and employer branding, award-based lists and congratulatory campaigns.

- **8000058 – New Vehicle**  
  - *What it means:* Company has registered or acquired a new vehicle (e.g. fleet). FI, SE, NO.  
  - *Use cases:* Fleet and vehicle sales, transport and logistics targeting.

- **8000081 – Granted Energy Certificate**  
  - *What it means:* Building or property has received an energy certificate (e.g. efficiency rating). FI, FI_realestate.  
  - *Use cases:* Energy and retrofit sales, green building and sustainability targeting.

- **8000071 – Apartment sales notice**  
  - *What it means:* Notice of apartment or housing unit sale (e.g. real estate listing or registration). FI, FI_realestate.  
  - *Use cases:* Real estate and housing market intelligence, property and developer targeting.

- **8000086 – Temporary exceptions in business**  
  - *What it means:* A temporary exception or derogation affecting the company’s business has been recorded (e.g. regulatory). FI.  
  - *Use cases:* Compliance and exception monitoring, regulated-sector targeting.

- **8000090 – Environmental Impact Assessment**  
  - *What it means:* Company or project is involved in an EIA process or EIA has been published. FI, SE, NO, DK.  
  - *Use cases:* Environmental and sustainability services, construction and project-related targeting.

### Negative

- **8000029 – Legal Dispute**  
  - *What it means:* Company is involved in a legal dispute (litigation, arbitration, or similar).  
  - *Use cases:* Legal and risk monitoring, litigation and dispute-related services, risk-based list exclusion.
