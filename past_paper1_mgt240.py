from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from past_pdf_base import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def make_sbu_diagram():
    d = Drawing(440, 145)
    # Top Box: Corporate HQ / CEO
    d.add(Rect(150, 110, 140, 26, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.HexColor('#1A365D')))
    d.add(String(165, 120, "Corporate HQ / CEO (Board)", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.white))

    # Middle Row: Corporate Staff Divisions
    d.add(Line(220, 110, 220, 68, strokeColor=colors.HexColor('#2D3748'), strokeWidth=1.2))
    d.add(Line(65, 68, 375, 68, strokeColor=colors.HexColor('#2D3748'), strokeWidth=1.2))

    # 3 SBU Boxes
    sbu_x = [20, 175, 330]
    sbu_titles = ["SBU 1 (e.g., Footwear)", "SBU 2 (e.g., Sportswear)", "SBU 3 (e.g., Accessories)"]
    for x, title in zip(sbu_x, sbu_titles):
        cx = x + 45
        d.add(Line(cx, 68, cx, 55, strokeColor=colors.HexColor('#2D3748'), strokeWidth=1.2))
        d.add(Rect(x, 30, 95, 25, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.HexColor('#1A365D')))
        d.add(String(x + 5, 39, title, fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
        # Functional units under each SBU
        d.add(Line(cx, 30, cx, 20, strokeColor=colors.HexColor('#4A5568'), strokeWidth=0.9))
        d.add(Rect(x, 4, 95, 16, fillColor=colors.HexColor('#EDF2F7'), strokeColor=colors.HexColor('#CBD5E0')))
        d.add(String(x + 4, 9, "R&D | Prod | Mktg | Fin", fontName="Helvetica", fontSize=7, fillColor=colors.HexColor('#1A202C')))

    # Corporate Staff Box on right/left of vertical stem
    d.add(Line(220, 90, 130, 90, strokeColor=colors.HexColor('#4A5568'), strokeWidth=1))
    d.add(Rect(25, 80, 105, 20, fillColor=colors.HexColor('#E2E8F0'), strokeColor=colors.HexColor('#A0AEC0')))
    d.add(String(30, 87, "Corporate Staff (HR, Legal)", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#1A202C')))
    return d

def build_past_paper1(story):
    story.append(Paragraph(
        "PAPER 1: TRIBHUVAN UNIVERSITY — MGT 240: STRATEGIC MANAGEMENT<br/>"
        "<font size=10>BBA / BBM / Eighth Semester | April 2026 | Full Marks: 100 | Pass Marks: 50 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group 'A': Brief Answer Questions [10 x 2 = 20]", group_header_style))

    add_q(story, "Q1. What is meant by organization's vision?")
    add_a(story, """<b>Answer:</b> An organization's vision (or strategic vision) is a forward-looking declaration of what the organization aspires to become and achieve in the long-term future (typically 5 to 20 years). It provides a mental picture of the desired future state, inspires stakeholders, and guides strategic direction.""")

    add_q(story, "Q2. Mention features of strategic decision.")
    add_a(story, """<b>Answer:</b> The major features of a strategic decision are:
• <b>1. Long-Term & Future-Oriented:</b> Determines the direction and survival of the firm over many years.
• <b>2. Top-Management Involvement:</b> Formulated by the Board of Directors and CEO with organization-wide scope.
• <b>3. Substantial Resource Commitment:</b> Requires major financial, physical, and human resource allocation and is costly to reverse.
• <b>4. Environment-Matching:</b> Aligns internal capabilities with external environmental opportunities and threats.""")

    add_q(story, "Q3. Write two strategic directions.")
    add_a(story, """<b>Answer:</b> Based on Igor Ansoff's Product-Market Matrix, two primary strategic directions for growth are:
• <b>1. Market Penetration / Market Development:</b> Increasing market share with existing products in current markets (Penetration) or entering new geographical/demographic markets (Market Development).
• <b>2. Product Development / Diversification:</b> Introducing new or modified products to existing markets (Product Development) or entering entirely new products and new markets (Diversification).""")

    add_q(story, "Q4. Differentiate between threshold resources and strategic resources.")
    add_a(story, """<b>Answer:</b>
• <b>Threshold Resources:</b> The minimum baseline tangible and intangible resources needed for an organization simply to exist, enter an industry, and meet basic customer requirements (they ensure survival/parity but do not give a competitive advantage).
• <b>Strategic (Unique) Resources:</b> Rare, valuable, inimitable, and non-substitutable (VRIO) resources owned by a firm that underpin its core competencies and create a sustainable competitive advantage over rivals.""")

    add_q(story, "Q5. Define scenario planning.")
    add_a(story, """<b>Answer:</b> Scenario planning is a structured strategic forecasting technique in which strategists construct several plausible, internally consistent alternative views ("scenarios"—such as optimistic, pessimistic, and most-likely futures) of how key external environmental drivers (political, economic, technological) might evolve, enabling the firm to prepare flexible contingency strategies.""")

    add_q(story, "Q6. Mention the resources that create competitive advantages.")
    add_a(story, """<b>Answer:</b> According to Barney's Resource-Based View (RBV / VRIO Framework), resources that create sustainable competitive advantage must possess four attributes:
• <b>1. Valuable (V):</b> Create customer value or exploit opportunities / neutralize threats.
• <b>2. Rare (R):</b> Possessed by only one or very few competing firms.
• <b>3. Inimitable (I):</b> Costly or impossible for competitors to copy or imitate (due to patents, brand heritage, or causal ambiguity).
• <b>4. Organized / Non-Substitutable (O/N):</b> Supported by organizational systems and having no strategic equivalent.""")

    add_q(story, "Q7. Sketch SBU structure with suitable labeling.")
    add_a(story, """<b>Answer:</b> A Strategic Business Unit (SBU) organizational structure groups similar divisions/product lines into autonomous business units, each headed by a VP/General Manager accountable for its own strategy, sales, and profits under Corporate HQ:""")
    story.append(make_sbu_diagram())

    add_q(story, "Q8. Give four characteristics of strategic evaluation.")
    add_a(story, """<b>Answer:</b> Four essential characteristics of effective strategic evaluation are:
• <b>1. Economical & Meaningful:</b> Should use minimum necessary information without overburdening managers.
• <b>2. Timely & Action-Oriented:</b> Must detect deviations promptly so corrective action can be taken before damage occurs.
• <b>3. True Picture of Performance:</b> Should measure both quantitative financial results and qualitative long-term strategic health.
• <b>4. Operational Flexibility:</b> Should adapt to changing environmental conditions rather than enforcing rigid controls.""")

    add_q(story, "Q9. Make a list of operational strategy for HR department.")
    add_a(story, """<b>Answer:</b> Operational (functional) strategies for the Human Resource (HR) department include:
• <b>1. Talent Acquisition & Recruitment Strategy:</b> Hiring right-skilled employees aligned with corporate strategy.
• <b>2. Training, Learning & Development Strategy:</b> Continuous upskilling and leadership development programs.
• <b>3. Performance Appraisal & Reward Strategy:</b> Linking compensation, incentives, and promotions to strategic KPIs.
• <b>4. Employee Retention & Quality of Work-Life Strategy:</b> Reducing turnover through career growth, safety, and employee engagement.""")

    add_q(story, "Q10. Suggest four ways to reduce cost of production.")
    add_a(story, """<b>Answer:</b> Four effective ways to reduce the cost of production are:
• <b>1. Economies of Scale & Experience Curve:</b> Producing in larger volumes to spread fixed overhead costs and leverage worker learning curves.
• <b>2. Process Automation & Modern Technology:</b> Adopting lean manufacturing, CAD/CAM, and automation to minimize labor hours and scrap/wastage.
• <b>3. Supply Chain Optimization & Just-in-Time (JIT) Inventory:</b> Negotiating bulk supplier discounts and using JIT to eliminate warehousing and holding costs.
• <b>4. Value Engineering & Product Redesign:</b> Simplifying product design and standardizing parts across product lines.""")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group 'B': Short Answer Questions (Attempt any SIX — ALL Solved) [6 x 5 = 30]", group_header_style))

    add_q(story, "Q11. Describe the process of strategic management.")
    add_a(story, """<b>Answer:</b> The strategic management process is a continuous, dynamic sequence of four core phases through which an organization defines and achieves its long-term mission and objectives:
• <b>1. Environmental Scanning & Strategic Analysis (Where are we now?):</b>
  - Setting/reviewing the Vision, Mission, and Objectives.
  - Conducting External Analysis (PESTEL macro-environment and Porter's Five Forces industry analysis) to identify Opportunities and Threats (OT) -> summarized in an ETOP / EFE matrix.
  - Conducting Internal Analysis (Resource-Based View, Value Chain, functional audit) to identify Strengths and Weaknesses (SW) -> summarized in a SAP / IFE matrix.
• <b>2. Strategy Formulation & Strategic Choice (Where do we want to go?):</b>
  - Developing strategic alternatives at Corporate level (Stability, Expansion, Retrenchment, Combination), Business/SBU level (Porter's Generic Strategies: Cost Leadership, Differentiation, Focus), and Functional level.
  - Evaluating alternatives using portfolio tools (BCG, GE Nine-Cell, SWOT/TOWS) and selecting the best strategy based on Suitability, Feasibility, and Acceptability.
• <b>3. Strategy Implementation (How do we get there?):</b>
  - Translating chosen strategy into action via organizational structure design, resource allocation, functional policies, corporate culture alignment, and strategic leadership.
• <b>4. Strategic Evaluation and Control (How are we doing?):</b>
  - Monitoring ongoing assumptions and actual performance against strategic targets (via Strategic Surveillance, Premise Control, Implementation Control, and Special Alert Control) and taking corrective actions.""")

    add_q(story, "Q12. Explain the value chain analysis process.")
    add_a(story, """<b>Answer:</b> Introduced by Michael E. Porter (1985), <b>Value Chain Analysis (VCA)</b> views a firm as a sequential chain of value-creating activities that transform inputs into outputs valued by customers, generating a profit margin (Total Value Created minus Total Cost of Activities).
<b>1. Classification of Value Chain Activities:</b>
• <b>Primary Activities (Direct production & delivery):</b> (i) Inbound Logistics, (ii) Operations, (iii) Outbound Logistics, (iv) Marketing & Sales, and (v) After-Sales Service.
• <b>Support Activities (Infrastructure & enablement):</b> (i) Firm Infrastructure, (ii) Human Resource Management, (iii) Technology Development (R&D), and (iv) Procurement.

<b>2. Step-by-Step Value Chain Analysis Process:</b>
• <b>Step 1: Identify and Segregate Activities:</b> Break down the firm's operations into distinct primary and support sub-activities.
• <b>Step 2: Allocate Costs and Identify Cost Drivers:</b> Assign operating costs and assets to each activity and identify the structural cost drivers (scale, capacity utilization, linkages) to find cost-reduction opportunities.
• <b>Step 3: Identify Value-Creating (Differentiation) Drivers:</b> Determine which activities create superior buyer value (quality, speed, innovation, customer service).
• <b>Step 4: Evaluate Internal and External Linkages:</b> Analyze how performance in one activity (e.g., quality inspection in Procurement) reduces costs in another (e.g., fewer warranty claims in Service), as well as vertical linkages with suppliers and distribution channels.
• <b>Step 5: Benchmark Against Competitors & Optimize:</b> Compare the firm's activity costs and value against industry best practices and outsource non-core activities where external specialists are cheaper.""")

    add_q(story, "Q13. What is meant by internal development? Describe the methods for internal development.")
    add_a(story, """<b>Answer:</b>
<b>Meaning of Internal Development (Organic Growth):</b>
Internal development is a strategic method of pursuing corporate growth by building upon and expanding a firm's own internal resources, capabilities, R&D, production capacity, and sales force—rather than acquiring or merging with external companies. It allows the firm to maintain cultural uniformity, spread investment outlays gradually over time, and avoid acquisition premiums.

<b>Methods for Internal Development:</b>
• <b>1. In-House Research & Development (R&D) and New Product Development:</b> Investing in internal laboratories and product engineering teams to invent and commercialize new products or upgrade existing products.
• <b>2. Capacity Expansion (Greenfield / Brownfield Investment):</b> Building new manufacturing plants, opening new company-owned retail showrooms/branches, and purchasing modern machinery to increase output.
• <b>3. Market Penetration and Geographic Expansion:</b> Intensifying advertising, expanding the internal sales force, launching e-commerce channels, and entering new regional or export markets using internal marketing teams.
• <b>4. Internal Human Capital & Core Competency Building:</b> Developing proprietary training programs, knowledge management systems, and cross-functional innovation teams (intrapreneurship / internal corporate venturing) to enter new business lines organically.""")

    add_q(story, "Q14. Develop a sample of strategic advantages profile (SAP) for a firm of your choice.")
    add_a(story, """<b>Answer:</b> A <b>Strategic Advantage Profile (SAP)</b> is a structured summary matrix resulting from an internal appraisal that assesses a firm's key functional areas and capabilities as competitive <b>Strengths (+)</b>, <b>Weaknesses (-)</b>, or <b>Neutral (0)</b> relative to industry competitors.
Below is a sample SAP prepared for <b>Chaudhary Group (CG Foods — Wai Wai Noodles Division)</b>:""")
    t14_sap = make_table([
        [P_hdr("Internal Functional Area / Capability Factor"), P_hdr("Assessment (+ / - / 0)"), P_hdr("Strategic Impact & Competitive Justification")],
        [P("1. Marketing & Distribution", True), P("<b>+ (Major Strength)</b>"), P("Dominant brand equity of 'Wai Wai' across Nepal & South Asia with an extensive nationwide dealer and retail network.")],
        [P("2. Operations & Manufacturing", True), P("<b>+ (Strength)</b>"), P("Multiple automated manufacturing plants across provinces (Bardiya, Nawalparasi, Sunsari) yielding economies of scale.")],
        [P("3. Research & Development (R&D)", True), P("<b>0 (Neutral)</b>"), P("Moderate product line extensions (cup noodles, seasoning variants), but limited breakthrough health-food innovation.")],
        [P("4. Finance & Accounting", True), P("<b>+ (Strength)</b>"), P("Strong operating cash flows, high creditworthiness, and easy access to institutional bank financing.")],
        [P("5. Supply Chain / Raw Materials", True), P("<b>- (Weakness)</b>"), P("Heavy reliance on imported wheat flour, palm oil, and packaging materials exposes margins to exchange rate & import shocks.")],
        [P("6. Human Resources & Culture", True), P("<b>+ (Strength)</b>"), P("Experienced professional management team blended with strong entrepreneurial leadership.")],
    ], col_widths=[135, 85, 280])
    story.append(t14_sap)
    story.append(Spacer(1, 5))

    add_q(story, "Q15. Explain the criteria for strategic choice.")
    add_a(story, """<b>Answer:</b> According to Gerry Johnson, Kevan Scholes, and Richard Whittington, evaluating and selecting the best strategic option (<b>Strategic Choice</b>) relies on three primary criteria—known as the <b>SFA Framework (Suitability, Feasibility, and Acceptability)</b>:
• <b>1. Suitability (Does the strategy fit our situation?):</b>
  Assesses the strategic logic of an option—whether it addresses the key external opportunities and threats (ETOP), builds on the firm's internal strengths and core competencies, remedies its weaknesses (SAP), and aligns with the company's vision and mission.
• <b>2. Feasibility (Can the strategy be implemented with our resources?):</b>
  Evaluates whether the organization possesses (or can realistically obtain) the practical resources and capabilities required to execute the strategy—including <i>Financial feasibility</i> (cash flow and capital funding), <i>Human/Skill feasibility</i>, <i>Technological feasibility</i>, and <i>Supply-chain/Market access</i>.
• <b>3. Acceptability (Will stakeholders support the expected return and risk?):</b>
  Measures whether the expected performance outcomes of the strategy meet the expectations of powerful stakeholders across three dimensions:
  - <i>Return:</i> Profitability (ROI, NPV, EPS, shareholder value creation).
  - <i>Risk:</i> Financial ratios, liquidity, sensitivity to downturns, and break-even risk.
  - <i>Stakeholder Reactions:</i> Political and cultural acceptability to shareholders, lenders, employees, regulators, and society.""")

    add_q(story, "Q16. What are the basic requirements for effective implementation of strategy? Describe.")
    add_a(story, """<b>Answer:</b> Strategy formulation is only half the battle; translating a chosen strategy into action requires the following basic requirements (aligned with McKinsey's 7S and implementation frameworks):
• <b>1. Matching Organizational Structure to Strategy:</b> As Alfred Chandler proved ("Structure follows Strategy"), a new strategy requires an appropriate structure (functional, divisional, SBU, matrix, or network) with clear lines of authority and accountability.
• <b>2. Adequate Resource Allocation (Budgeting):</b> Financial capital, physical facilities, technology, and human talent must be reallocated toward strategic priorities through strategy-driven capital and operating budgets.
• <b>3. Supportive Corporate Culture:</b> Shared values, norms, and beliefs of employees must be aligned with the new strategic direction (e.g., fostering an innovation culture for a differentiation strategy or a cost-conscious culture for cost leadership).
• <b>4. Effective Strategic Leadership:</b> Top leaders must communicate the vision clearly, champion change, overcome organizational resistance/inertia, and role-model commitment.
• <b>5. Functional Policies, Procedures, and Information Systems:</b> Standard operating procedures (SOPs), ERP/management information systems, and functional policies (in HR, Marketing, Operations) must guide daily employee decisions.
• <b>6. Performance-Linked Reward and Incentive Systems:</b> Tying bonuses, promotions, and recognition directly to the achievement of annual strategic milestones and Balanced Scorecard KPIs.""")

    add_q(story, "Q17. Write the meaning of strategic audit and explain its importance.")
    add_a(story, """<b>Answer:</b>
<b>Meaning of Strategic Audit:</b>
A strategic audit is a comprehensive, systematic, and objective diagnostic examination of an organization's entire strategic management process—covering its external environment, internal resources, mission/objectives, corporate/business/functional strategies, implementation systems, and performance outcomes—using a standardized checklist of strategic questions.

<b>Importance of Strategic Audit:</b>
• <b>1. Holistic Diagnostic Tool:</b> Provides top management and the Board of Directors with a complete 360-degree health check of the company's strategic posture, ensuring no critical external threat or internal weakness is overlooked.
• <b>2. Early Detection of Strategic Drift:</b> Identifies gaps between formulated plans and actual execution before minor operational problems escalate into financial crises.
• <b>3. Objective Resource Allocation:</b> Evaluates whether capital and managerial talent are being invested in high-return strategic business units rather than decaying legacy operations.
• <b>4. Improved Corporate Governance & Accountability:</b> Gives independent directors, institutional investors, and auditors a structured benchmark to evaluate executive management's stewardship.
• <b>5. Continuous Organizational Learning:</b> Institutionalizes feedback from past successes and failures to refine future strategy formulation.""")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group 'C': Long Answer Questions (Attempt any THREE — ALL Solved) [3 x 10 = 30]", group_header_style))

    add_q(story, "Q18. 'GE matrix is useful tool for evaluating strategy in an organization than BCG'. Justify.")
    add_a(story, """<b>Answer:</b>
<b>1. Overview of BCG and GE Nine-Cell Portfolio Matrices:</b>
Both the Boston Consulting Group (BCG) Growth-Share Matrix and the General Electric (GE) / McKinsey Nine-Cell Matrix are corporate portfolio analysis tools used by multi-business firms to evaluate their Strategic Business Units (SBUs) and allocate capital across them.
• The <b>BCG Matrix</b> is a <b>2x2 (4-cell)</b> matrix that plots SBUs using only two single-variable dimensions: <i>Market Growth Rate</i> (High/Low) and <i>Relative Market Share</i> (High/Low), classifying SBUs into Stars, Cash Cows, Question Marks, and Dogs.
• The <b>GE Nine-Cell Matrix</b> is a <b>3x3 (9-cell)</b> matrix developed by McKinsey & Co. for General Electric that plots SBUs along two composite, multi-factor dimensions: <b>Industry Attractiveness</b> (High, Medium, Low) and <b>Business Unit Competitive Strength</b> (Strong, Average, Weak), prescribing three broad zones:
  - <i>Green Zone (3 top-left cells):</i> Invest / Grow (Build)
  - <i>Yellow Zone (3 diagonal middle cells):</i> Hold / Selectively Invest
  - <i>Red Zone (3 bottom-right cells):</i> Harvest / Divest.

<b>2. Justification: Why GE Nine-Cell Matrix is Superior to the BCG Matrix:</b>
• <b>1. Multi-Factor Composite Measurement vs. Single-Variable Oversimplification:</b>
  - BCG assumes that Market Growth Rate is the sole indicator of industry attractiveness and Relative Market Share is the sole indicator of competitive strength.
  - In reality, a fast-growing industry may have intense price wars and low profit margins, and a low-market-share niche firm can be highly profitable through differentiation.
  - The <b>GE Matrix</b> overcomes this by using weighted composite scores of multiple factors: <i>Industry Attractiveness</i> includes market size, growth rate, industry profitability, Porter's five forces, and PESTEL factors; <i>Business Strength</i> includes market share, brand equity, R&D, product quality, cost structure, and managerial competence.
• <b>2. Inclusion of Middle/Intermediate Categories (3x3 vs. 2x2):</b>
  - BCG forces an artificial High/Low dichotomy with no middle ground.
  - The GE Matrix introduces <b>Medium</b> Industry Attractiveness and <b>Average</b> Business Strength, providing 9 finer gradations that reflect real-world business positions much more accurately.
• <b>3. Richer, More Nuanced Strategic Prescriptions:</b>
  - Instead of branding every low-share/low-growth unit a "Dog" to be liquidated, the GE Matrix provides tailored prescriptions across 9 cells (e.g., selective specialization, niche defense, managed harvesting) and visually displays both total industry size (circle area) and the SBU's market share (pie slice inside the circle).
• <b>4. Applicability Across Diverse Industries and Lifecycle Stages:</b>
  - BCG fails in mature or differentiated industries where scale economies are less important; the GE Matrix allows managers to customize factor weights to fit each specific industry context.""")

    add_q(story, "Q19. Explain the Porter's Five Forces Model of environmental analysis.")
    add_a(story, """<b>Answer:</b>
Developed by Harvard Professor <b>Michael E. Porter (1979)</b>, the <b>Five Forces Model</b> is the most widely used framework for analyzing the competitive structure and long-term profit attractiveness of an industry (task environment). Porter argues that industry profitability is determined not just by direct competitors, but by the collective strength of five competitive forces:

• <b>1. Threat of New Entrants (Potential Competitors):</b>
  New entrants bring additional production capacity, desire to gain market share, and downward pressure on prices. The height of <b>Barriers to Entry</b> determines this threat:
  - Economies of scale and high capital requirements
  - Brand loyalty and high customer switching costs
  - Access to distribution channels and proprietary technology/patents
  - Government licensing, tariffs, and regulatory barriers
  - Expected retaliation by entrenched incumbents.

• <b>2. Bargaining Power of Buyers (Customers):</b>
  Powerful buyers can force down industry prices, demand higher quality or extra services, and play competitors against each other. Buyer power is high when:
  - A few large buyers purchase a high volume of the seller's output
  - The industry's products are standardized or undifferentiated commodities
  - Switching costs to another supplier are low
  - Buyers pose a credible threat of <i>backward vertical integration</i>.

• <b>3. Bargaining Power of Suppliers:</b>
  Powerful suppliers can squeeze industry profitability by raising input prices or reducing the quality/reliability of raw materials and components. Supplier power is high when:
  - The supplier industry is dominated by a few companies (oligopoly)
  - The supplied input is unique, differentiated, or has no close substitutes
  - The focal industry is not an important customer of the supplier group
  - Suppliers pose a credible threat of <i>forward vertical integration</i>.

• <b>4. Threat of Substitute Products or Services:</b>
  Substitutes are products from outside the industry that perform the same or similar function for customers (e.g., tea vs. coffee, airlines vs. high-speed rail, plastic vs. glass packaging). Substitutes place a ceiling on the prices firms in an industry can charge. The threat is high when substitutes offer an attractive price-performance trade-off and buyer switching costs are low.

• <b>5. Intensity of Rivalry Among Existing Competitors:</b>
  The central force where incumbent firms jockey for position using price cuts, advertising battles, new product introductions, and extended warranties. Rivalry is fierce when:
  - Numerous or equally balanced competitors exist in the industry
  - Industry growth is slow or stagnant (turning competition into a fight for market share)
  - Fixed costs or storage costs are high
  - Product differentiation and switching costs are low
  - High <b>exit barriers</b> (specialized assets, labor agreements, emotional attachment) keep unprofitable firms trapped in the industry.""")

    add_q(story, "Q20. Strategic leadership is vital in effective implementation of strategies. Comment on the statement with roles and responsibilities of strategic leadership.")
    add_a(story, """<b>Answer:</b>
<b>Comment on the Statement:</b>
The statement is completely valid. Even the most brilliantly formulated strategy will fail during execution without strong <b>strategic leadership</b>. Strategy implementation requires mobilizing thousands of employees, overcoming organizational inertia and political resistance, reallocating scarce resources, and reshaping corporate culture. Strategic leaders—the CEO, top management team, and SBU heads—act as the bridge between strategic intent (formulation) and operational reality (implementation).

<b>Key Roles and Responsibilities of Strategic Leadership in Strategy Implementation:</b>
• <b>1. Determining Strategic Direction and Articulating a Compelling Vision:</b>
  Strategic leaders craft and continuously communicate a clear long-term vision and mission so employees at every level understand why the strategy matters and how their daily work contributes to it.
• <b>2. Exploiting and Maintaining Core Competencies:</b>
  Leaders ensure that the firm's unique resources and core capabilities (R&D, customer service, supply-chain agility) are nurtured, shared across business units, and leveraged in executing the strategy.
• <b>3. Developing Human Capital and Empowering Managers:</b>
  Recruiting, training, coaching, and retaining talented executives and frontline workers, and delegating authority to middle and operational managers so they can make fast, aligned decisions.
• <b>4. Building and Sustaining an Effective Organizational Culture:</b>
  Shaping shared values, entrepreneurial mindset, customer orientation, and adaptability through visible leadership behavior, stories, symbols, and reward systems.
• <b>5. Emphasizing Ethical Practices and Corporate Governance:</b>
  Instilling integrity, transparency, regulatory compliance, and ethical codes of conduct to protect the organization's reputation and stakeholder trust.
• <b>6. Establishing Balanced Organizational Controls (Balanced Scorecard):</b>
  Designing balanced financial and non-financial controls (customer, internal process, learning & growth metrics) that keep execution on track without stifling innovation and autonomy.""")

    add_q(story, "Q21. Write the concept of strategic control and explain its process.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Strategic Control:</b>
Strategic control is a specialized form of organizational control that focuses on monitoring and evaluating the strategic management process itself to ensure that the strategy is being implemented as planned, that the underlying environmental and internal premises remain valid, and that the results produced by the strategy are achieving corporate goals.
Unlike traditional operational (post-action) control—which asks <i>"Did we do things right?"</i> after the year ends—strategic control is forward-looking (feedforward and concurrent) and asks <i>"Are we still moving in the right direction?"</i> across four types (Schreyogg & Steinmann): <b>Premise Control</b>, <b>Strategic Surveillance</b>, <b>Special Alert Control</b>, and <b>Implementation Control</b>.

<b>Step-by-Step Process of Strategic Control:</b>
• <b>Step 1: Determine What to Control (Identify Key Strategic Areas):</b>
  Select the critical success factors, strategic milestones, and key environmental assumptions (premises) that are most vital to the success of the strategy.
• <b>Step 2: Set Strategic Standards and Benchmarks (KPIs):</b>
  Establish clear quantitative standards (ROI, market share, cost per unit, revenue growth) and qualitative standards (brand reputation, product quality, employee morale, innovation rate) using tools like the Balanced Scorecard.
• <b>Step 3: Measure Actual Performance and Monitor Environmental Premises:</b>
  Continuously gather internal performance data through Management Information Systems (MIS/ERP) and strategic audits while scanning the external environment for changes in premises or sudden crises.
• <b>Step 4: Compare Actual Performance and Premises Against Standards:</b>
  Evaluate whether actual outcomes fall within acceptable tolerance limits of the planned targets.
• <b>Step 5: Analyze Deviations and Diagnose Root Causes:</b>
  If a significant variance occurs, determine whether it was caused by poor operational execution, unrealistic targets, or an unexpected shift in the external environment.
• <b>Step 6: Take Corrective Action:</b>
  Reformulate implementation plans, reallocate resources, revise functional tactics, or—if environmental premises have fundamentally changed—update the strategy itself.""")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group 'D': Comprehensive Answer / Case / Situation Analysis [4 x 5 = 20]", group_header_style))

    add_q(story, "Q22. Case Study: XTP Nepal (Distributor of Chinese Footwear Brand ABC / Xtep)\nXTP Nepal was established in Kathmandu with NRs 8 million investment by Ganesh Gautam and Shiva Shrestha (previously operating GS Enterprises wholesale footwear) after winning the distributorship of Chinese brand ABC (parallel to Adidas, Nike, Anta, Li-Ning, Xtep, Skechers) in 2013. Adidas has 4 showrooms with brand warranty; Anta closed 5 showrooms and partnered with KTM brand; Li-Ning dropped 4 showrooms; Rainbow has 85 outlets across Nepal plus 1 Newroad retail shop. Local unbranded footwear copies branded designs. Language barrier (Chinese/English) and quarterly business plan/progress reporting requirements from China HQ stress Gautam and Shrestha. Kingsway showroom had frustrating sales due to limited selection, while Bouddha showroom performed above expectations; Kingsway was shifted to Kumaripati (Lalitpur).\na. Conduct an industry analysis for XTP Nepal.\nb. Prepare generic strategy for XTP Nepal to increase the sales of Xtep in Nepal.\nc. What organizational structure do you suggest to fit the ABC branding in Nepal? Why?\nd. XTP is planning the central control of all strategies of all outlets. What components of strategic information systems do you suggest to XTP? Why?")
    add_a(story, """<b>Answer (Comprehensive Case Study Solution):</b>

<b>a. Industry Analysis for XTP Nepal (Porter's Five Forces & Competitive Environment Analysis):</b>
• <b>1. Intensity of Competitive Rivalry (High):</b> The branded sportswear and footwear industry in Nepal is fiercely competitive. Global giants like Adidas (4 exclusive showrooms with brand warranty) and Skechers compete at the premium end, while Chinese/regional peers like Anta (partnered with local garment producer KTM CTY), Li-Ning, and Rainbow (85 multi-brand outlets nationwide) compete aggressively for urban youth and sports enthusiasts.
• <b>2. Threat of Substitutes and Counterfeit/Imitation Products (Very High):</b> Numerous local branded and unbranded footwear makers in Kathmandu rapidly copy the designs of international brands and sell them at much lower prices, eroding the sales of genuine imported brands.
• <b>3. Bargaining Power of Suppliers / Brand Principal (High):</b> ABC/Xtep Head Office in China holds strong bargaining power over XTP Nepal—demanding strict quarterly business plans, progress reports, and company-owned showroom expansion, and has already replaced distributors in other countries.
• <b>4. Bargaining Power of Buyers (Moderate to High):</b> Nepalese urban customers are brand-conscious (responding to sports trends and celebrity endorsements like cricketers Sandeep Lamichhane and Gyanendra Malla) but demand wide variety/selection and value-for-money; as seen at the Kingsway showroom, buyers walk away if product assortment is narrow.
• <b>5. Industry Growth & Opportunities (Favorable):</b> Rising sports culture, youth population, fitness awareness, and expanding commercial hubs (such as Bouddha and Kumaripati in Lalitpur) offer strong growth potential for complete sports apparel and footwear lines.

<b>b. Recommended Generic Strategy for XTP Nepal to Increase Sales of Xtep/ABC in Nepal:</b>
Based on Michael Porter's Generic Strategies, XTP Nepal should pursue an <b>Integrated Cost-Conscious Differentiation Strategy (Best-Cost Provider / Focused Differentiation Strategy)</b>:
• <b>1. Product-Mix Differentiation (Broad Assortment of Footwear + Sportswear):</b> The Kingsway showroom failed because buyers had limited selection. XTP must stock the full range of shoes alongside sports apparel (t-shirts, trousers, socks, bags, footballs, volleyballs) in all showrooms.
• <b>2. Brand Positioning & Warranty Assurance ("International Quality at Mid-Premium Price"):</b> Position ABC/Xtep between ultra-expensive Adidas/Nike and cheap local counterfeits by offering an official authenticity guarantee and warranty (matching Adidas's trust factor) so buyers prefer genuine Xtep over local design copies.
• <b>3. Strategic Showroom Location & Hybrid Distribution:</b> Focus company-owned flagship showrooms in high-footfall youth/residential hubs like Bouddha and Kumaripati, while leveraging GS Enterprises' existing wholesale dealer network across major cities outside Kathmandu (similar to Rainbow's 85-outlet reach) to achieve volume scale.

<b>c. Suggested Organizational Structure to Fit ABC Branding in Nepal & Justification:</b>
• <b>Recommended Structure:</b> A <b>Functional-cum-Divisional (Hybrid / Geographic-Channel) Organizational Structure</b> separating the Wholesale Business (GS Enterprises) from XTP Nepal's Branded Retail Operations, supported by dedicated functional departments:
  - <b>Managing Directors (Gautam & Shrestha)</b> at the top.
  - <b>Three Core Operational Divisions/Departments:</b>
    1. <i>Retail Showroom Operations Division</i> (Store Managers for Newroad, Bouddha, Kumaripati, and future outlets).
    2. <i>Wholesale & Dealer Distribution Division</i> (managing regional multi-brand outlets).
    3. <i>Professional Corporate Support Functions:</i> (i) <b>International Liaison, Planning & Reporting Officer</b> (fluent in English/Chinese and skilled in preparing quarterly business plans and financial reports for China HQ), (ii) <b>Marketing & Brand Promotion Unit</b>, and (iii) <b>Finance & Inventory Control Unit</b>.
• <b>Why This Structure Fits Best:</b> Currently, Mr. Gautam is distracted by the legacy wholesale business while Mr. Shrestha is overwhelmed handling ABC issues and China HQ's quarterly reports with limited language and technical planning skills. Separating wholesale from retail and hiring a professional Planning & International Liaison Manager eliminates executive stress, satisfies China HQ's professional standards, and prevents loss of the distributorship.

<b>d. Recommended Components of Strategic Information Systems (SIS) for Central Control of All Outlets:</b>
To centrally control strategies, sales, and inventory across all showrooms and wholesale outlets, XTP Nepal should implement an integrated <b>Retail Enterprise Resource Planning (ERP) & Strategic Information System</b> comprising four key components:
• <b>1. Centralized Point-of-Sale (POS) & Real-Time Inventory Management System:</b> Connects Newroad, Bouddha, Kumaripati, and warehouse stock in real time using barcode/SKU scanning. <i>Why:</i> Immediately identifies fast-moving vs. slow-moving sizes/designs, prevents stockouts (solving the "limited selection" problem seen in Kingsway), and automates stock transfers between outlets.
• <b>2. Financial & Quarterly Management Reporting System (MIS / BI Dashboard):</b> Automatically compiles daily and quarterly sales, gross margins, outlet-wise profitability, and budget vs. actual variance reports in English. <i>Why:</i> Directly solves Mr. Gautam and Mr. Shrestha's biggest headache—generating accurate, professional quarterly business plans and progress reports required by ABC Head Office in China.
• <b>3. Customer Relationship Management (CRM) & Loyalty System:</b> Tracks customer preferences, repeat purchases, warranty claims, and promotional campaign effectiveness. <i>Why:</i> Builds brand loyalty against local counterfeit footwear.
• <b>4. Supply Chain & Import Procurement Portal (SCM):</b> Links XTP Nepal's order forecasting directly with ABC China's supply portal. <i>Why:</i> Reduces lead times for seasonal sportswear and footwear launches.""")

    story.append(PageBreak())
