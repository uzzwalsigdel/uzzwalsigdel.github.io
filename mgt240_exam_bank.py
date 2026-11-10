from notes_base import (
    Paragraph, Spacer, PageBreak, add_unit, add_topic, add_subtopic,
    add_body, add_example, add_tip, make_table, P, P_hdr
)

def build_mgt240_exam_bank(story):
    story.append(PageBreak())
    add_unit(story, "SECTION 6: MGT 240 — HIGH-YIELD EXAM QUESTION BANK & CASE-STUDY MASTER PLAYBOOK")

    add_topic(story, "6.1 Complete Rapid-Fire Group A (2-Mark) Definitions & Answers (Top 25 Exam Questions)")
    t_qa = make_table([
        [P_hdr("Q#"), P_hdr("Exam Brief Question (2 Marks)"), P_hdr("Concise Full-Marks Answer Key")],
        [P("1"), P("What is Strategic Management?"), P("The continuous process of environmental scanning, strategy formulation, implementation, and evaluation/control that enables an organization to achieve long-term objectives and competitive advantage.")],
        [P("2"), P("What is an Organization's Vision?"), P("A forward-looking declaration of what the organization aspires to become in the long-term future (5–20+ years), comprising Core Ideology and Envisioned Future (BHAG).")],
        [P("3"), P("What is a Mission Statement?"), P("An enduring statement of an organization's current purpose and scope ('Who we are, what we do, and whom we serve') that distinguishes it from similar firms.")],
        [P("4"), P("Define Strategic Intent."), P("Coined by Hamel & Prahalad, it is an ambitious long-term obsession with winning market leadership that stretches the organization beyond its current resources.")],
        [P("5"), P("Write four features of Strategic Decisions."), P("(1) Long-term future orientation, (2) Top-management involvement, (3) Substantial resource commitment, and (4) Matches internal capabilities with external environment.")],
        [P("6"), P("What is PESTEL Analysis?"), P("A macro-environmental scanning framework analyzing Political, Economic, Socio-Cultural, Technological, Environmental (Ecological), and Legal forces.")],
        [P("7"), P("What is ETOP?"), P("Environmental Threat and Opportunity Profile—a structured summary matrix of external analysis categorizing macro/industry trends as Opportunities (+) or Threats (-).")],
        [P("8"), P("What is SAP?"), P("Strategic Advantage Profile—a structured internal analysis table evaluating functional areas (Marketing, Finance, Operations, HR, R&D) as Strengths (+) or Weaknesses (-).")],
        [P("9"), P("Define Scenario Planning."), P("A strategic forecasting technique that builds 3–4 plausible alternative future narratives (optimistic, pessimistic, base) to test strategies and build contingency plans.")],
        [P("10"), P("Define Hyper-Competition."), P("Coined by Richard D'Aveni, it is an environment of intense, rapid competitive moves where rivals quickly erode any advantage, making all competitive advantages temporary.")],
        [P("11"), P("What is a Strategic Group?"), P("A cluster of rival firms within the same industry following similar strategies along key dimensions like price, quality, and geographic scope (e.g., 5-star vs. budget hotels).")],
        [P("12"), P("Threshold vs. Strategic Resources?"), P("Threshold resources are minimum baseline assets needed merely to survive at parity; Strategic resources are rare, valuable, inimitable (VRIO) assets creating competitive advantage.")],
        [P("13"), P("What is Core Competence?"), P("A unique bundle of internal skills and technologies (Prahalad & Hamel) that provides access to multiple markets, delivers high buyer value, and is hard for rivals to imitate.")],
        [P("14"), P("What is Benchmarking?"), P("The process of measuring a firm's products, services, and processes against the toughest 'best-in-class' industry or global leaders to close performance gaps.")],
        [P("15"), P("Write Ansoff's 4 Growth Directions."), P("(1) Market Penetration, (2) Market Development, (3) Product Development, and (4) Diversification (Related & Unrelated).")],
        [P("16"), P("Related vs. Unrelated Diversification?"), P("Related diversification enters new businesses sharing common technology/markets (synergy); Unrelated (conglomerate) diversification enters completely unconnected industries.")],
        [P("17"), P("What is Retrenchment Strategy?"), P("A defensive corporate strategy adopted during financial decline to reduce operational scope and restore viability via Turnaround, Divestment, or Liquidation.")],
        [P("18"), P("What does 'Stuck in the Middle' mean?"), P("Porter's term for a firm that fails to achieve either low-cost leadership or clear differentiation, resulting in a confused positioning and below-average profitability.")],
        [P("19"), P("What is Hofer's Matrix?"), P("A 15-cell (5x3) portfolio matrix plotting SBUs across 5 stages of Product-Market Evolution (Development, Growth, Shakeout, Maturity, Decline) and 3 Competitive Positions.")],
        [P("20"), P("What are the SFA Choice Criteria?"), P("Johnson & Scholes's three criteria for evaluating and selecting a strategy: (1) Suitability, (2) Feasibility, and (3) Acceptability (Return, Risk, Stakeholder reactions).")],
        [P("21"), P("What is a Matrix Structure?"), P("A dual-authority organizational structure combining vertical functional departments with horizontal project/product teams, where employees report to two bosses.")],
        [P("22"), P("What is Strategic Leadership?"), P("The ability to anticipate, envision, maintain flexibility, and empower others to create strategic change and execute strategy effectively across the organization.")],
        [P("23"), P("What is a Strategic Audit?"), P("A comprehensive, systematic, and objective diagnostic review of all aspects of an organization's strategic management process using a standardized checklist.")],
        [P("24"), P("List the 4 Types of Strategic Control."), P("(1) Premise Control, (2) Strategic Surveillance, (3) Special Alert Control, and (4) Implementation Control.")],
        [P("25"), P("Four ways to reduce production cost?"), P("(1) Economies of scale & experience curve, (2) Process automation/lean manufacturing, (3) Just-in-Time (JIT) inventory & bulk procurement, (4) Value engineering.")],
    ], col_widths=[25, 150, 325])
    story.append(t_qa)
    story.append(Spacer(1, 6))

    add_topic(story, "6.2 Master Guide to Group B & C Analytical Questions & Group D Case Studies")
    add_body(story, """<b>1. Model Analytical Answer Structure: How to Write 5-Mark and 10-Mark Answers in MGT 240:</b>
• <b>Introduction (3–4 lines):</b> Start with a crisp definition of the concept and name the scholar/author (e.g., <i>Michael Porter, Igor Ansoff, Jay Barney, Prahalad & Hamel, Chandler, Collins & Porras, Charles Hofer</i>).
• <b>Visual Diagram / Matrix / Table:</b> Always sketch a clean box diagram or comparison table (even when not explicitly asked!). Diagrams immediately distinguish an A+ paper from an average paper.
• <b>Numbered Analytical Points with Bold Headings:</b> Write 5–6 points for a 5-mark question and 7–8 points for a 10-mark question, giving a brief Nepalese or global corporate example under each point.
• <b>Brief Conclusion (2 lines):</b> Summarize how the tool/concept contributes to sustainable competitive advantage.

<b>2. Step-by-Step Playbook for Solving Group D Comprehensive Case Studies (20 Marks):</b>
In TU BBA 8th Semester exams, the 20-mark Case Study in MGT 240 typically presents a real or realistic company facing competitive, structural, and operational challenges (such as <i>XTP Nepal / Xtep Footwear</i> or <i>Apple Inc. / MobileMe</i>). Use the following 4-part template:

• <b>Template 1 — When Asked for Industry / External Environment Analysis:</b>
  - Apply <b>Porter's Five Forces Model</b> systematically:
    1. <i>Intensity of Rivalry:</i> Name the specific competitors mentioned in the case (e.g., Adidas, Anta, Li-Ning, Rainbow) and their outlet counts/tactics.
    2. <i>Threat of Substitutes / Counterfeits:</i> Highlight local unbranded copies or alternative products mentioned in the case.
    3. <i>Bargaining Power of Suppliers / Brand Principal:</i> Highlight strict targets, reporting mandates, or supply constraints from the parent brand/supplier.
    4. <i>Bargaining Power of Buyers:</i> Discuss customer price sensitivity, demand for wide assortment/warranty, and low switching costs.
    5. <i>Threat of New Entrants & Macro Trends (PESTEL):</i> Mention youth demographics, sports culture, or import/regulatory hurdles.

• <b>Template 2 — When Asked to Formulate Corporate, Business (Generic), or Functional Strategies:</b>
  - <b>Business-Level Generic Strategy:</b> Recommend <b>Broad Differentiation</b>, <b>Best-Cost Provider (Hybrid Position 3 on Strategic Clock)</b>, or <b>Focused Differentiation</b>. Explain how to differentiate (e.g., offering full product assortment of shoes + apparel, brand authenticity warranty, celebrity endorsements, and prime youth locations).
  - <b>Corporate-Level Strategy:</b> Recommend <b>Market Penetration</b>, <b>Market Development</b> (expanding to new cities/provinces), or <b>Related Diversification</b> (expanding from hardware into digital ecosystem services).
  - <b>Pricing & Operations Strategy:</b> Identify whether the firm uses <b>Value-Based / Skimming Pricing</b> ("Value Leader, not Price Leader" like Apple) or <b>Just-in-Time (JIT) Supply Chain Optimization</b> (like Tim Cook at Apple).

• <b>Template 3 — When Asked to Recommend an Organizational Structure:</b>
  - Diagnose the structural flaw in the case (e.g., founders overloaded with both wholesale and retail, language/reporting bottleneck with foreign HQ, or functional silos).
  - Recommend a specific structure—such as a <b>Divisional / SBU Structure</b> (separating Wholesale from Branded Retail) or a <b>Functional Structure with a Dedicated International Liaison & Strategic Planning Unit</b>—and sketch a small organization chart showing the CEO, Divisional Heads, and Functional Managers.

• <b>Template 4 — When Asked for Strategic Control & Strategic Information Systems (SIS):</b>
  - Recommend an integrated <b>Retail ERP & Strategic Information System</b> with four modules:
    1. <i>Centralized Point-of-Sale (POS) & Real-Time Barcode Inventory System</i> (tracks fast/slow-moving SKUs across all outlets and prevents stockouts).
    2. <i>Automated Financial & Management Information System (MIS Dashboard)</i> (generates quarterly business plans and variance reports for HQ).
    3. <i>Customer Relationship Management (CRM) & Warranty Tracking System</i> (builds customer loyalty).
    4. <i>Supply Chain & Procurement Portal (SCM)</i> (links outlet demand forecasts directly to factory ordering).""")

    add_topic(story, "6.3 Complete Worked Solutions to Top Group B, C & D Exam Questions (With Figures & Examples)")

    add_subtopic(story, "Model Q1: Sample Strategic Advantage Profile (SAP) & Environmental Threat and Opportunity Profile (ETOP) for a Nepalese Commercial Bank (e.g., Nabil Bank / Global IME Bank)")
    t_bank_sap = make_table([
        [P_hdr("Internal Capability Area (SAP)"), P_hdr("Rating (+ / - / 0)"), P_hdr("Detailed Strategic Justification & Competitive Impact")],
        [P("1. Capital Base & Financial Strength", True), P("<b>+ (Major Strength)</b>"), P("Post-merger paid-up capital exceeding Rs 27–35 Billion gives the highest single-obligor lending capacity for large hydropower and infrastructure syndications.")],
        [P("2. Branch & Digital Distribution Network", True), P("<b>+ (Strength)</b>"), P("300+ nationwide branches, 400+ ATMs, and market-leading mobile banking app (nBank / Global Smart Plus) with over 1.5 million active digital users.")],
        [P("3. Brand Equity & Customer Trust", True), P("<b>+ (Strength)</b>"), P("Four decades of corporate heritage, strong corporate governance, and top credit ratings attract low-cost CASA (Current & Savings Account) deposits.")],
        [P("4. Asset Quality & Non-Performing Loans (NPL)", True), P("<b>- (Weakness)</b>"), P("Economic slowdown in construction, SME, and real estate sectors has pushed industry NPLs toward 3.5%–4.5%, requiring higher loan-loss provisioning.")],
        [P("5. Post-Merger Cultural & IT Integration", True), P("<b>- (Weakness)</b>"), P("Harmonizing staff grades, organizational cultures, and legacy branches after multiple bank mergers creates temporary operational friction.")],
        [P("6. Cybersecurity & Cloud Infrastructure", True), P("<b>0 (Neutral)</b>"), P("ISO-certified data centers, but rising global phishing/ransomware threats require continuous investment in AI fraud detection.")],
    ], col_widths=[125, 85, 290])
    story.append(t_bank_sap)
    story.append(Spacer(1, 6))

    add_subtopic(story, "Model Q2: SWOT / TOWS Matrix Formulation for a Nepalese Manufacturing / FMCG Firm (e.g., CG Foods — Wai Wai)")
    t_swot = make_table([
        [P_hdr("Internal / External"), P_hdr("INTERNAL STRENGTHS (S)\n• S1: Iconic brand & nationwide distribution\n• S2: Automated multi-province factories\n• S3: Strong cash flows & R&D"), P_hdr("INTERNAL WEAKNESSES (W)\n• W1: High dependence on imported wheat/oil\n• W2: Perceived as processed fast food\n• W3: Rising labor & logistics costs")],
        [P("<b>EXTERNAL OPPORTUNITIES (O)</b>\n• O1: Growing South Asian & global diaspora demand\n• O2: Rising youth demand for healthy/quick snacks\n• O3: E-commerce & modern retail expansion", True),
         P("<b>SO Strategies (Maxi-Maxi — Aggressive Growth):</b>\n• Use S1 & S2 to expand export plants in Europe, Middle East & Africa (O1 — Market Development).\n• Leverage S3 to launch baked, multigrain, and high-protein noodles (O2 — Product Development)."),
         P("<b>WO Strategies (Mini-Maxi — Developmental):</b>\n• Partner with domestic Nepalese agricultural cooperatives for contract wheat/spice farming (overcoming W1 via local supply chain).\n• Rebrand with fortified vitamin/mineral lines (overcoming W2 via O2).")],
        [P("<b>EXTERNAL THREATS (T)</b>\n• T1: Intense rivalry from Current, Rumpum, 2PM & Maggi\n• T2: Volatile global commodity & FX rates\n• T3: Stricter food-safety & plastic rules", True),
         P("<b>ST Strategies (Maxi-Mini — Defensive Leverage):</b>\n• Use nationwide distribution superiority (S1) and multi-plant scale (S2) to match competitors' spicy noodle promotions (T1).\n• Use financial strength (S3) to hedge commodity imports (T2)."),
         P("<b>WT Strategies (Mini-Mini — Turnaround / Cost Control):</b>\n• Automate packaging lines and optimize fleet routing to offset rising labor/fuel costs (W3) and defend margins against price wars (T1).")],
    ], col_widths=[130, 185, 185])
    story.append(t_swot)
    story.append(Spacer(1, 6))

    add_subtopic(story, "Model Q3: McKinsey 7S Framework for Strategy Implementation (With Hard vs. Soft S Classification)")
    add_body(story, """Developed by Tom Peters and Robert Waterman at McKinsey & Company, the <b>McKinsey 7S Framework</b> states that effective strategy implementation requires the harmonious alignment of seven interdependent internal organizational elements, grouped into <b>3 "Hard S's"</b> (tangible, easy for management to formally change) and <b>4 "Soft S's"</b> (intangible, culture- and people-driven, harder to change but critical for success):
• <b>The 3 "Hard S" Elements (Formal & Structural):</b>
  1. <b>Strategy:</b> The coherent action plan formulated to build and sustain competitive advantage over rivals.
  2. <b>Structure:</b> The organizational chart, hierarchy, division of labor, and reporting lines (Functional, Divisional, SBU, Matrix).
  3. <b>Systems:</b> The formal daily procedures, ERP/information systems, capital budgeting routines, performance appraisal, and reward systems that keep the organization running.
• <b>The 4 "Soft S" Elements (Cultural & Human):</b>
  4. <b>Shared Values (Superordinate Goals — At the Center of the 7S Model):</b> The core beliefs, ethical norms, and corporate culture that bind all six other S's together.
  5. <b>Style (Leadership Style):</b> How top executives behave, allocate their time, communicate, and lead (participative, transformational, or autocratic).
  6. <b>Staff:</b> The organization's human resources—demographics, recruitment, socialization, morale, and career progression.
  7. <b>Skills:</b> The distinctive capabilities and core competencies possessed by the organization's personnel as a whole.""")

    add_subtopic(story, "Model Q4: Balanced Scorecard (BSC — Kaplan & Norton) in Strategic Evaluation and Control")
    t_bsc = make_table([
        [P_hdr("Balanced Scorecard Perspective"), P_hdr("Core Strategic Question"), P_hdr("Key Performance Indicators (KPIs) & Targets"), P_hdr("Strategic Purpose")],
        [P("1. Financial Perspective", True), P("<i>'To succeed financially, how should we appear to our shareholders?'</i>"), P("Return on Equity (ROE), Return on Assets (ROA), Economic Value Added (EVA), Revenue Growth %, Operating Margin."), P("Measures lag outcomes of past strategic actions.")],
        [P("2. Customer Perspective", True), P("<i>'To achieve our vision, how should we appear to our customers?'</i>"), P("Customer Satisfaction Index, Net Promoter Score (NPS), Customer Retention Rate, Market Share %, On-Time Delivery."), P("Measures value proposition delivery in target segments.")],
        [P("3. Internal Business Process Perspective", True), P("<i>'To satisfy shareholders and customers, what business processes must we excel at?'</i>"), P("Manufacturing Cycle Time, Defect Rate (Six Sigma), Inventory Turnover, Cost per Unit, New Product Launch Speed."), P("Focuses on critical value-chain operations & innovation.")],
        [P("4. Learning & Growth Perspective", True), P("<i>'To achieve our vision, how will we sustain our ability to change and improve?'</i>"), P("Employee Training Hours per Year, Employee Turnover Rate, Revenue from New Products, IT/Digital System Readiness."), P("Leading indicator of future long-term capability renewal.")],
    ], col_widths=[105, 130, 145, 120])
    story.append(t_bsc)
    story.append(Spacer(1, 6))

    add_subtopic(story, "Model Q5: Blue Ocean Strategy vs. Red Ocean Strategy (Chan Kim & Renee Mauborgne)")
    t_blue = make_table([
        [P_hdr("Dimension"), P_hdr("Red Ocean Strategy (Conventional Competition)"), P_hdr("Blue Ocean Strategy (Value Innovation)")],
        [P("1. Market Space", True), P("Compete in <b>existing market space</b> with known boundaries."), P("Create <b>uncontested new market space</b>."),
        ],
        [P("2. Attitude Toward Competition", True), P("Focus on <b>beating the competition</b> head-to-head."), P("Make the <b>competition irrelevant</b>.")],
        [P("3. Demand Approach", True), P("Exploit and fight over existing customer demand."), P("Create and capture <b>new demand</b> (convert non-customers).")],
        [P("4. Value-Cost Trade-Off", True), P("Accept the value-cost trade-off (choose EITHER Differentiation OR Low Cost)."), P("Break the value-cost trade-off—pursue <b>Differentiation AND Low Cost simultaneously (Value Innovation)</b> via the ERRC Grid (Eliminate, Reduce, Raise, Create).")],
        [P("5. Real-World Example", True), P("Traditional circus competing with animal acts & star performers; legacy airlines."), P("<i>Cirque du Soleil</i> (eliminated expensive animal acts, added theatrical storyline for adults); Nintendo Wii; Pathao/Tootle creating app ride-sharing in Nepal.")],
    ], col_widths=[105, 195, 200])
    story.append(t_blue)
    story.append(Spacer(1, 6))

    add_subtopic(story, "Model Q6: Why Strategies Fail During Implementation & How to Prevent Implementation Failure")
    add_body(story, """Studies by Fortune and Harvard Business Review show that up to 70%–90% of formulated strategies fail during execution.
<b>Major Causes of Strategy Implementation Failure:</b>
• <b>1. Poor Communication & Lack of Shared Understanding:</b> Less than 5% of frontline employees understand the corporate strategy when top management keeps plans locked in the boardroom.
• <b>2. Structural Mismatch:</b> Trying to execute a new diversification or innovation strategy through a rigid, outdated functional hierarchy.
• <b>3. Failure to Link Budgets and Incentives to Strategy:</b> Annual capital budgets and employee bonus schemes remain tied to old operational routines rather than new strategic KPIs.
• <b>4. Cultural Resistance & Organizational Politics:</b> Deep-seated habits, fear of the unknown, and departmental turf wars sabotage change.
• <b>5. Lack of Top-Management Follow-Through:</b> Senior executives treat strategy formulation as the finish line and delegate implementation entirely to lower levels without leadership support.

<b>Remedies to Ensure Successful Implementation:</b>
• Translate the strategy into a clear <b>Balanced Scorecard & Action Plan</b> with department-level milestones; align <b>Structure, Culture, Budgets, and Rewards</b> with the strategy; and conduct regular <b>Implementation Control reviews</b>.""")
