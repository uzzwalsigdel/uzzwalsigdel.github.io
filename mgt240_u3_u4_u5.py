from notes_base import (
    Paragraph, Spacer, PageBreak, add_unit, add_topic, add_subtopic,
    add_body, add_example, add_tip, make_table, P, P_hdr
)
from mgt240_figures import (
    fig_ansoff_and_clock, fig_bcg_ge_hofer, fig_org_structures
)

def build_mgt240_u3_u4_u5(story):
    # ==================== UNIT 3 ====================
    add_unit(story, "UNIT 3: STRATEGY FORMULATION & STRATEGIC CHOICE (12 Lecture Hours)")

    add_topic(story, "3.1 Concept & Importance of Strategy Formulation")
    add_body(story, """<b>• Concept:</b> Strategy formulation (often called strategic planning) is the analytical and creative phase of strategic management in which top managers synthesize the results of external (ETOP) and internal (SAP) environmental analysis to generate, evaluate, and select the best long-term Corporate, Business (SBU), and Functional strategies to achieve the organization's mission and objectives.
<b>• Importance of Strategy Formulation:</b>
• <b>1. Translates Analysis into Actionable Direction:</b> Bridges the gap between where the firm is today and where its Vision wants it to be.
• <b>2. Evaluates Multiple Strategic Options Objectively:</b> Prevents knee-jerk decisions by systematically comparing Stability, Growth, and Retrenchment alternatives.
• <b>3. Balances Corporate Portfolio Risk & Cash Flow:</b> Uses portfolio matrices (BCG, GE, Hofer) to ensure cash-generating mature units fund high-growth future winners.
• <b>4. Aligns Corporate, Business, and Functional Levels:</b> Ensures every department's tactics reinforce the business unit's competitive advantage.""")

    add_topic(story, "3.2 Strategic Alternatives at the Corporate Level (Grand Strategies — Glueck's Classification)")
    add_subtopic(story, "A. Stability Strategy (Maintaining the Current Scope and Pace)")
    add_body(story, """A firm pursues a <b>Stability Strategy</b> when it is satisfied with its current performance, operates in a stable/mature environment with low threats, and continues serving the same customer groups with the same products and technologies:
• <b>1. No-Change Strategy:</b> Continuing present operations and policies without any significant modification because the external environment is predictable and the firm's niche is secure.
• <b>2. Pause / Proceed-with-Caution Strategy:</b> A temporary "breathing spell" or consolidation phase adopted after a period of rapid, exhausting expansion (e.g., after a major merger or capacity doubling) to allow organizational systems and management to digest growth before making the next big move.
• <b>3. Profit (Harvesting) Strategy:</b> When a firm faces a temporary economic slump, it artificially maintains short-term net profits by deferring R&D, advertising, maintenance, and capital replacements. (Dangerous if prolonged!).""")

    add_subtopic(story, "B. Growth / Expansion Strategy (Directions for Strategy Development)")
    story.append(fig_ansoff_and_clock())
    add_body(story, """<b>1. Concentration / Intensive Growth Strategies (Igor Ansoff's Product-Market Matrix):</b>
• <b>(i) Market Penetration (Existing Products in Existing Markets):</b> Increasing sales and market share of current products in current markets by (a) encouraging existing customers to buy more frequently or in larger quantities, (b) attracting competitors' customers via aggressive promotion/price cuts, or (c) converting non-users into users. <i>Example: Ncell or NTC offering data-pack bonuses to boost mobile data usage among existing subscribers.</i>
• <b>(ii) Market Development (Existing Products in New Markets):</b> Selling current products into new geographical areas (new provinces, rural districts, or foreign export markets) or new demographic/institutional buyer segments. <i>Example: Goldstar Shoes or Wai Wai Noodles expanding exports into India, Bhutan, and the Middle East.</i>
• <b>(iii) Product Development (New/Modified Products in Existing Markets):</b> Developing new products, new features, or next-generation models for existing customers through R&D and product engineering. <i>Example: Dairy Development Corporation (DDC) or Sujal Dairy launching probiotic yogurt, flavored milk, and cheese cubes for its existing urban customer base.</i>

<b>2. Integration Strategies (Vertical & Horizontal Integration):</b>
• <b>(i) Backward Vertical Integration:</b> Gaining ownership or control over a firm's suppliers (moving upstream toward raw materials) to ensure reliable supply, quality control, and capture supplier margins. <i>Example: A Nepalese cement manufacturer acquiring its own limestone quarry and clinker plant, or a poultry feed company setting up its own maize/soybean contract farms.</i>
• <b>(ii) Forward Vertical Integration:</b> Gaining ownership or control over distributors or retailers (moving downstream toward final consumers) to control pricing, brand image, and customer experience. <i>Example: Apple opening Apple Retail Stores, or Bhatbhateni / footwear brands opening company-owned flagship showrooms.</i>
• <b>(iii) Horizontal Integration:</b> Acquiring or merging with one or more direct competitors operating at the same stage of the industry value chain to increase market share, achieve economies of scale, and eliminate rivalry. <i>Example: Global IME Bank merging with Bank of Kathmandu, or Nabil Bank acquiring Nepal Bangladesh Bank.</i>

<b>3. Diversification Strategies (Entering New Products AND New Markets):</b>
• <b>(i) Related (Concentric) Diversification:</b> Expanding into a new business that shares meaningful strategic fit and value-chain linkages (common technology, R&D, distribution channels, or brand name) with the existing business—generating <b>synergy (2 + 2 = 5)</b>. <i>Example: Apple expanding from Mac computers into iPod, iPhone, iPad, and Apple Watch; or Pathao expanding from bike ride-sharing into car taxis, food delivery (Pathao Food), and parcel delivery.</i>
• <b>(ii) Unrelated (Conglomerate) Diversification:</b> Expanding into an entirely new industry that has no technological, product, or market commonality with the firm's current business, primarily to spread financial risk across cyclical industries or exploit undervalued acquisition targets. <i>Example: IME Group or Chaudhary Group operating across banking, hydro-power, cement, hospitality, telecom, and FMCG.</i>""")

    add_subtopic(story, "C. Retrenchment (Defensive) & Combination Strategies")
    add_body(story, """<b>1. Retrenchment / Defensive Strategies (Adopted when performance is declining or survival is threatened):</b>
• <b>(i) Turnaround Strategy ("Surgical Restructuring"):</b> Reversing a failing firm's losses through four actions: (a) <i>Cost reduction</i> (slashing overhead, freezing hiring, reducing waste), (b) <i>Asset reduction</i> (selling idle land/vehicles), (c) <i>Revenue generation</i> (pushing high-margin products, collecting receivables), and (d) <i>Leadership replacement</i>.
• <b>(ii) Divestment (Divestiture / Spin-Off) Strategy:</b> Selling off, closing, or spinning off a major division or SBU that is chronically unprofitable, requires too much capital, or no longer fits the firm's core strategy (e.g., selling a "Dog" or failed "Question Mark" SBU to raise cash for core businesses).
• <b>(iii) Liquidation Strategy:</b> The strategy of last resort—admitting defeat, shutting down the entire company, and selling off all tangible assets piecemeal to pay creditors (because the firm is worth more dead than alive).

<b>2. Combination Strategy:</b> Simultaneously applying different grand strategies across different SBUs (e.g., divesting a loss-making textile unit while aggressively expanding a profitable hydropower unit).""")

    add_topic(story, "3.3 Strategic Alternatives at the Business (SBU) Level: Porter's Generic Strategies & Bowman's Strategic Clock")
    t_u3_porter = make_table([
        [P_hdr("Generic Strategy"), P_hdr("Competitive Scope & Basis of Advantage"), P_hdr("How It Is Achieved (Value Chain Actions)"), P_hdr("Major Risks / Pitfalls")],
        [P("1. Overall Cost Leadership", True), P("<b>Broad Market + Lowest Cost:</b> Producing standardized goods/services at a lower unit cost than all rivals."), P("Economies of scale, learning curve, tight cost/overhead control, process automation, bulk procurement, no-frills design."), P("Technological change may make low-cost plant obsolete; rivals may imitate; price cuts may erode quality.")],
        [P("2. Broad Differentiation", True), P("<b>Broad Market + Unique Value:</b> Offering unique attributes valued by buyers so the firm charges a <b>premium price</b>."), P("Superior R&D/innovation, iconic design (Apple), brand image (Nike/Adidas), durability, or rapid customer service."), P("Price premium becomes too high so buyers switch to cheap imitations; uniqueness is copied by rivals.")],
        [P("3. Focus (Cost Focus or Diff. Focus)", True), P("<b>Narrow Market Niche:</b> Serving a specific buyer group, product segment, or geographic region better than broad rivals."), P("Tailoring every value-chain activity exclusively to the specialized needs of the niche (e.g., Ferrari, luxury mountain resorts)."), P("Niche demand may shrink; broad-market competitors may invade the niche.")],
    ], col_widths=[95, 130, 145, 130])
    story.append(t_u3_porter)
    story.append(Spacer(1, 5))

    add_body(story, """<b>• Cliff Bowman's Strategic Clock (8 Market-Facing Generic Strategies):</b>
Expands Porter's model by plotting 8 positions around a clock face based on <b>Price (X-axis)</b> and <b>Perceived Added Value (Y-axis)</b>:
• <b>Position 1 (Low Price / Low Added Value — "No-Frills"):</b> Segment-specific bargain offer (e.g., budget airlines like Ryanair/IndiGo; local unbranded goods).
• <b>Position 2 (Low Price):</b> Offering standard perceived value at a lower price than competitors (Cost Leadership).
• <b>Position 3 (Hybrid / Best-Cost Provider):</b> Simultaneously offering higher perceived value at a moderate/low price (e.g., Toyota, Xiaomi, Xtep sportswear in Nepal).
• <b>Position 4 (Differentiation):</b> Offering high perceived value (quality, branding, features) either with or without a moderate price premium (e.g., Samsung, Adidas).
• <b>Position 5 (Focused Differentiation):</b> Offering very high perceived luxury/prestige value at a high premium price to a select segment (e.g., Rolex, Apple iPhone Pro Max).
• <b>Positions 6, 7 & 8 (Failure / Non-Viable Strategies):</b> Charging high/standard prices while delivering low perceived value—leads to rapid loss of market share unless protected by an artificial monopoly.""")

    add_topic(story, "3.4 Functional-Level Strategies (Marketing, Finance, Operations, HRM & R&D — 2/5-Mark Favourite)")
    t_u3_func = make_table([
        [P_hdr("Functional Area"), P_hdr("Key Strategic Decisions & Sub-Strategies"), P_hdr("Practical Examples")],
        [P("1. Marketing Strategy", True), P("Target market segmentation & positioning (STP); Product mix & branding; Pricing (skimming vs. penetration vs. value-based); Distribution channel selection; Integrated promotion & CRM."), P("Positioning Xtep with brand warranty; using celebrity cricket ambassadors; expanding digital e-commerce channels.")],
        [P("2. Financial Strategy", True), P("Capital raising & optimal capital structure (debt vs. equity); Capital budgeting (NPV/IRR project selection); Working capital & liquidity management; Dividend payout vs. retention policy; Financial risk hedging."), P("Maintaining low leverage during high interest rates; using internal retained earnings for expansion.")],
        [P("3. Operations / Production Strategy", True), P("Plant capacity, location & layout; Process technology & automation; Just-in-Time (JIT) inventory & supply chain management; Total Quality Management (TQM / Six Sigma); Make-or-Buy (outsourcing)."), P("Tim Cook implementing JIT inventory and outsourced Foxconn manufacturing at Apple to slash inventory holding days.")],
        [P("4. Human Resource (HRM) Strategy", True), P("Manpower planning, recruitment & selection; Training, upskilling & leadership development; Performance appraisal & KPI-linked compensation; Employee retention, health insurance & work-life quality."), P("Providing Group Health Insurance and performance bonuses to retain scarce IT engineers in a tech consultancy.")],
        [P("5. R&D / Technology Strategy", True), P("Technological leadership (first-mover pioneer) vs. technological followership (fast imitator); Basic vs. applied product/process R&D; In-house R&D vs. licensing/open innovation."), P("Pharmaceutical firm investing in patented drug discovery vs. generic drug manufacturer focusing on low-cost process R&D.")],
    ], col_widths=[95, 225, 180])
    story.append(t_u3_func)
    story.append(Spacer(1, 5))

    add_topic(story, "3.5 Methods of Strategy Development & Portfolio Analysis Matrices (BCG, GE 9-Cell & Hofer's 15-Cell)")
    story.append(fig_bcg_ge_hofer())
    add_body(story, """<b>1. Three Methods of Strategy Development:</b>
• <b>(i) Internal Development (Organic Growth):</b> Building new products, plants, and markets using the firm's own internal resources and R&D. <i>Pros:</i> Preserves corporate culture, avoids overpaying acquisition premiums, spreads investment over time. <i>Cons:</i> Slow speed of market entry.
• <b>(ii) Mergers and Acquisitions (M&A):</b> Combining two equals (Merger) or purchasing controlling ownership of another firm (Acquisition). <i>Pros:</i> Instant market entry, eliminates a rival, acquires established brands/patents. <i>Cons:</i> High takeover premium, culture clash, integration failure.
• <b>(iii) Joint Ventures & Strategic Alliances (Cooperative Strategies):</b> Two or more independent firms pooling resources via a joint venture company, licensing, franchising, or supply-chain partnership. <i>Pros:</i> Shares financial risk, combines complementary capabilities, overcomes foreign regulatory barriers.

<b>2. In-Depth Comparison of BCG Matrix, GE Business Screen & Hofer's Matrix (10-Mark Exam Favourite):</b>
• <b>(A) BCG Growth-Share Matrix (Boston Consulting Group — Bruce Henderson):</b>
  A <b>2x2 (4-cell)</b> matrix plotting SBUs on <b>Market Growth Rate</b> (vertical axis: High/Low, indicates cash usage) and <b>Relative Market Share</b> (horizontal axis: High/Low, indicates cash generation via experience curve):
  1. <b>Stars (High Growth, High Share):</b> Market leaders in fast-growing industries; generate large cash but also require heavy investment to maintain leadership -> <i>Strategy: Invest to Hold/Build.</i>
  2. <b>Cash Cows (Low Growth, High Share):</b> Dominant leaders in mature industries; generate huge surplus cash flow far exceeding their reinvestment needs -> <i>Strategy: Milk/Harvest cash to fund Stars and selected Question Marks.</i>
  3. <b>Question Marks / Problem Children (High Growth, Low Share):</b> Cash-hungry units with small share in fast-growing markets -> <i>Strategy: Invest heavily to turn into a Star, or divest before they drain cash.</i>
  4. <b>Dogs (Low Growth, Low Share):</b> Weak market share in stagnant industries; tie up capital and earn low returns -> <i>Strategy: Divest, harvest, or liquidate.</i>

• <b>(B) GE Nine-Cell Business Screen (McKinsey & General Electric Matrix):</b>
  A <b>3x3 (9-cell)</b> multi-factor matrix plotting SBUs on <b>Industry Attractiveness</b> (High, Medium, Low — weighted composite of market size, growth, profitability, Porter's 5 forces, PESTEL) and <b>Business Unit Competitive Strength</b> (Strong, Average, Weak — weighted composite of market share, brand, quality, cost, R&D, management):
  - <b>Green Zone (3 Top-Left Cells):</b> <i>Invest / Grow (Build)</i> — Allocate priority capital for expansion.
  - <b>Yellow Zone (3 Diagonal Middle Cells):</b> <i>Hold / Selectively Invest</i> — Maintain position and invest cautiously where returns are clear.
  - <b>Red Zone (3 Bottom-Right Cells):</b> <i>Harvest / Divest</i> — Minimize reinvestment, extract cash flow, or sell/liquidate.
  - <b>Why GE Matrix is Superior to BCG (10-Mark Justification):</b> (1) Uses multi-factor weighted composite indices instead of single variables; (2) Uses a 9-cell (3x3) grid with Medium/Average categories instead of a rigid 4-cell (2x2) dichotomy; (3) Visually shows both total industry size (circle area) and SBU market share (pie slice); (4) Works across diverse industries beyond simple volume/experience-curve manufacturing.

• <b>(C) Hofer's Product-Market Evolution Portfolio Matrix (Charles Hofer — 5x3 = 15 Cells):</b>
  Plots SBUs along <b>5 Stages of Product-Market Evolution</b> on the vertical axis (<i>1. Development, 2. Growth, 3. Shakeout, 4. Maturity/Saturation, 5. Decline</i>) and <b>3 Competitive Positions</b> on the horizontal axis (<i>Strong, Average, Weak</i>).
  - <i>Importance:</i> Captures the dynamic industry lifecycle (especially Development and Shakeout), diagnoses whether the company has a balanced pipeline of "Developing Winners" funded by mature "Cash Producers," and shows both industry size (circle) and market share (shaded wedge).""")

    story.append(PageBreak())

    # ==================== UNIT 4 ====================
    add_unit(story, "UNIT 4: STRATEGY IMPLEMENTATION (10 Lecture Hours)")

    add_topic(story, "4.1 Concept, Process & Strategy Formulation vs. Strategy Implementation")
    t_u4_fi = make_table([
        [P_hdr("Basis of Comparison"), P_hdr("Strategy Formulation"), P_hdr("Strategy Implementation")],
        [P("1. Timing & Action", True), P("<b>Positioning forces BEFORE the action</b> (Planning)."), P("<b>Managing forces DURING the action</b> (Execution).")],
        [P("2. Primary Focus", True), P("Focuses on <b>Effectiveness</b> (<i>'Doing the right things'</i>)."), P("Focuses on <b>Efficiency</b> (<i>'Doing things right'</i>).")],
        [P("3. Nature of Process", True), P("Primarily an <b>intellectual & analytical</b> process."), P("Primarily an <b>operational & administrative</b> process.")],
        [P("4. Key Skills Required", True), P("Requires strong intuitive, analytical, and conceptual skills."), P("Requires strong leadership, motivational, and interpersonal skills.")],
        [P("5. Number of People", True), P("Coordinates a <b>few</b> top executives and strategists."), P("Coordinates and mobilizes <b>thousands</b> of managers and employees.")],
    ], col_widths=[105, 195, 200])
    story.append(t_u4_fi)
    story.append(Spacer(1, 5))

    add_body(story, """<b>• Process & Basic Requirements of Strategy Implementation:</b>
1. <b>Activating the Strategy:</b> Communicating strategic intent, setting annual objectives, and formulating functional policies/SOPs.
2. <b>Structural Implementation ("Structure Follows Strategy" — Alfred Chandler):</b> Designing an organizational structure that matches the strategy's complexity and scope.
3. <b>Resource Allocation:</b> Translating strategy into capital budgets, operating budgets, technology deployment, and staffing.
4. <b>Behavioral & Cultural Implementation:</b> Exercising strategic leadership, managing change, overcoming organizational politics/resistance, and aligning corporate culture and reward systems.""")

    add_topic(story, "4.2 Organizational Structures for Strategy Implementation (Diagrams, Pros & Cons)")
    story.append(fig_org_structures())
    add_body(story, """<b>Detailed Analysis of Organizational Structure Types:</b>
• <b>1. Simple (Entrepreneurial) Structure:</b> Owner-manager directly supervises all staff with no formal departments. <i>Best Fit:</i> Small single-product startups. <i>Pros:</i> Fast, flexible, low cost. <i>Cons:</i> Overwhelms the founder as volume grows.
• <b>2. Functional Structure (U-Form):</b> Groups activities by specialized business functions (Production, Marketing, Finance, HR, R&D). <i>Best Fit:</i> Single-business firms or dominant-product firms pursuing Cost Leadership or Differentiation. <i>Pros:</i> High functional specialization, economies of scale, clear career paths. <i>Cons:</i> Creates vertical "silos," poor horizontal coordination, slow response to multi-product diversification.
• <b>3. Multidivisional (Divisional / M-Form) Structure:</b> Organizes self-contained divisions around distinct <b>Products, Geographic Regions, or Customer Groups</b>, each with its own functional departments. <i>Best Fit:</i> Growing firms with multiple products or regions. <i>Pros:</i> Clear P&L profit accountability per division; frees corporate HQ for long-term strategy. <i>Cons:</i> Duplication of functional resources across divisions; inter-divisional rivalry.
• <b>4. Strategic Business Unit (SBU) Structure:</b> When a large diversified corporation has too many divisions for the CEO to supervise directly, similar divisions are grouped into autonomous <b>Strategic Business Units (SBUs)</b> headed by an SBU Vice President. <i>Best Fit:</i> Large multi-industry corporations. <i>Pros:</i> Facilitates portfolio planning (BCG/GE) and strategic coordination across related divisions. <i>Cons:</i> Adds an extra layer of executive overhead.
• <b>5. Matrix Structure (Dual-Command Grid):</b> Combines vertical <b>Functional Departments</b> with horizontal <b>Project / Product / Client Teams</b> simultaneously, so employees report to two bosses (a Functional Manager and a Project Manager). <i>Best Fit:</i> IT/consulting firms, aerospace, construction, and R&D-intensive firms operating in complex, fast-changing environments.
  - <i>Advantages of Matrix Structure:</i> (i) Optimal sharing of scarce technical specialists across projects, (ii) Breaks down functional silos and boosts cross-functional innovation, (iii) High flexibility to start or close projects quickly, (iv) Broadens middle managers' perspective.
  - <i>Disadvantages of Matrix Structure:</i> (i) Violates Unity of Command (two bosses cause role conflict and confusion), (ii) Power struggles and turf wars between functional and project heads, (iii) High administrative cost and excessive coordination meetings ("decision strangulation").
• <b>6. Holding Company (Conglomerate) Structure:</b> Corporate parent holds controlling equity ownership in legally independent subsidiary companies that operate autonomously with minimal HQ staff. <i>Best Fit:</i> Unrelated (conglomerate) diversification. <i>Pros:</i> Very low corporate HQ overhead; legal liability ring-fencing; easy to buy or sell subsidiaries. <i>Cons:</i> Zero operational synergy across subsidiaries.
• <b>7. Project-Based, Team-Based & Network (Virtual) Structures:</b> Organizes work around temporary cross-functional project teams or a small central core ("hub") that outsources manufacturing, logistics, and distribution to external partner firms. <i>Pros:</i> Extreme agility, speed, and low fixed capital requirement.""")

    add_topic(story, "4.3 Strategic Leadership & Managing Strategic Change")
    add_body(story, """<b>1. Six Core Roles & Capabilities of Strategic Leadership (Hitt, Ireland & Hoskisson):</b>
• <b>(1) Determining Strategic Direction:</b> Articulating a clear, inspiring long-term Vision and strategic intent.
• <b>(2) Effectively Managing the Firm's Resource Portfolio:</b> Exploiting and maintaining core competencies (VRIO) and developing human capital and social capital.
• <b>(3) Sustaining an Effective Organizational Culture:</b> Shaping shared norms, entrepreneurial risk-taking, quality obsession, and customer orientation.
• <b>(4) Emphasizing Ethical Practices & Corporate Governance:</b> Instilling integrity, transparency, and regulatory compliance.
• <b>(5) Establishing Balanced Organizational Controls:</b> Implementing the <b>Balanced Scorecard (Kaplan & Norton)</b> across 4 perspectives: <i>Financial, Customer, Internal Business Process, and Learning & Growth</i>.
• <b>(6) Leading Strategic Change & Overcoming Resistance:</b> Diagnosing inertia, communicating the urgency of change (Kotter's 8 steps / Lewin's Unfreeze-Change-Refreeze), empowering champions, and aligning incentives.""")

    # ==================== UNIT 5 ====================
    add_unit(story, "UNIT 5: STRATEGIC EVALUATION AND CONTROL (7 Lecture Hours)")

    add_topic(story, "5.1 Concept, Importance & Types of Strategic Control (Schreyogg & Steinmann Model)")
    add_body(story, """<b>1. Concept of Strategic Evaluation and Control:</b>
Strategic evaluation and control is the final, continuous phase of strategic management in which top managers track the strategy as it is being implemented, detect changes in the internal and external premises on which the strategy is based, evaluate whether actual performance matches strategic targets, and make necessary adjustments.
• <b>Why Traditional Post-Action Control Is Insufficient for Strategy:</b> Waiting until the end of a 5-year strategic plan to check results ("post-mortem" feedback control) is like locking the stable door after the horse has bolted. Therefore, strategic control must be <b>feedforward (proactive) and concurrent (steering)</b> as well as feedback.

<b>2. The Four Types of Strategic Control (10-Mark / 5-Mark Exam Essential):</b>""")
    t_u5_types = make_table([
        [P_hdr("Type of Strategic Control"), P_hdr("Core Purpose & Mechanism"), P_hdr("Practical Business Example")],
        [P("1. Premise Control", True), P("Designed to check systematically and continuously whether the <b>key assumptions (premises)</b> about the macro-environment (inflation, interest rates, regulations) and industry made during planning are still valid."), P("A hydro-power developer monitoring whether NRB interest-rate and PPA tariff assumptions made in the project plan still hold true.")],
        [P("2. Strategic Surveillance", True), P("Broad, unfocused, open-minded <b>'radar scanning'</b> of the entire internal and external environment (via media, conferences, trade journals) to uncover unexpected emerging threats or opportunities overlooked by Premise Control."), P("A retail bank scanning global fintech trends and spotting generative AI chatbots or cross-border QR payment breakthroughs early.")],
        [P("3. Special Alert Control\n(Crisis Control)", True), P("The thorough, rapid, and immediate reconsideration of a firm's basic strategy triggered by a <b>sudden, unexpected, high-impact event or crisis</b>. Executed by a crisis management team."), P("Immediate strategic pivot during the COVID-19 lockdown, the 2015 Nepal earthquake, or Apple's emergency Town Hall response to the 2008 'MobileMess' outage.")],
        [P("4. Implementation Control", True), P("Assess whether the overall strategy should be changed in light of unfolding results of <b>incremental steps and actions</b> that implement the strategy. Uses two tools:\n• <b>(i) Monitoring Strategic Thrusts</b> (key new projects)\n• <b>(ii) Milestone Reviews</b> (critical time/cost checkpoints)."), P("XTP Nepal reviewing the first 6-month sales milestone of its Kingsway showroom, realizing assortment was too narrow, and relocating the outlet to Kumaripati.")],
    ], col_widths=[105, 225, 170])
    story.append(t_u5_types)
    story.append(Spacer(1, 5))

    add_topic(story, "5.2 Strategic Audit, Strategic Information System (SIS) & Guidelines for Effective Control")
    add_body(story, """<b>1. Strategic Audit (Concept & Importance):</b>
A <b>Strategic Audit</b> is a comprehensive, systematic, and objective examination of an organization's entire strategic posture—covering corporate governance, external environment, internal capabilities, corporate/business/functional strategies, implementation systems, and performance outcomes—using a standardized diagnostic checklist (developed by Wheelen & Hunger).
• <i>Importance:</i> (i) Acts as an objective 360-degree corporate health check, (ii) Detects strategic drift early, (iii) Improves board governance and resource allocation, and (iv) Institutionalizes organizational learning.

<b>2. Strategic Information System (SIS) & Role of Information in Control:</b>
A <b>Strategic Information System (SIS)</b> is an integrated information system (combining Enterprise Resource Planning [ERP], Point-of-Sale [POS], Customer Relationship Management [CRM], Supply Chain Management [SCM], and Executive Business Intelligence Dashboards) that directly shapes a firm's competitive strategy and provides real-time data for central strategic control across all branches and outlets.

<b>3. Guidelines (Characteristics) for Proper Strategic Evaluation and Control:</b>
• <b>1. Minimum Necessary Information (Economical):</b> Control systems should track critical strategic KPIs (the "vital few") without drowning managers in bureaucratic paperwork.
• <b>2. Meaningful & Linked to Strategic Objectives:</b> Metrics must directly reflect key success factors (balanced across financial, customer, process, and learning dimensions).
• <b>3. Timely & Future-Oriented:</b> Must provide early-warning signals in time for managers to take corrective action before damage occurs.
• <b>4. Balanced Long-Term and Short-Term View:</b> Must not pressure managers to sacrifice long-term R&D or brand building just to hit quarterly profit targets.
• <b>5. Emphasis on Rewarding & Correcting Rather Than Punishing:</b> Should foster constructive problem-solving and organizational learning.""")
    add_tip(story, "In any MGT 240 exam question on Strategic Evaluation & Control, always include: (1) The 6-step process, (2) The Strategic vs. Operational Control table, and (3) The 4 Types of Strategic Control (P-S-S-I: Premise, Surveillance, Special Alert, Implementation)!")
