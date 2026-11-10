from notes_base import (
    Paragraph, Spacer, PageBreak, add_unit, add_topic, add_subtopic,
    add_body, add_example, add_tip, make_table, P, P_hdr
)
from mgt240_figures import (
    fig_sm_process, fig_levels_of_strategy, fig_porters_five_forces, fig_value_chain
)

def build_mgt240_u1_u2(story):
    # ==================== UNIT 1 ====================
    add_unit(story, "UNIT 1: INTRODUCTION TO STRATEGIC MANAGEMENT (9 Lecture Hours)")

    add_topic(story, "1.1 Concept, Definition & Characteristics of Strategy and Strategic Decisions")
    add_body(story, """<b>1. Etymology and Meaning of Strategy:</b>
The word <b>'Strategy'</b> is derived from the ancient Greek word <i>'Strategos'</i> (<i>Stratos</i> = army + <i>Ago</i> = to lead), which originally meant the art and science of military generalship—deploying troops and resources to defeat an enemy. In modern business management, strategy is the <b>unified, comprehensive, and integrated long-term master plan</b> designed by top management that relates the strategic advantages of the firm to the challenges of the external environment in order to achieve organizational objectives and sustain a competitive advantage over rivals.

<b>2. Scholarly Definitions to Quote in Exams:</b>
• <b>Alfred D. Chandler (1962):</b> <i>"Strategy is the determination of the basic long-term goals and objectives of an enterprise, and the adoption of courses of action and the allocation of resources necessary for carrying out these goals."</i>
• <b>Michael E. Porter (1996):</b> <i>"Strategy is about being different. It means deliberately choosing a different set of activities to deliver a unique mix of value."</i>
• <b>Gerry Johnson, Kevan Scholes & Richard Whittington:</b> <i>"Strategy is the direction and scope of an organization over the long term, which achieves advantage in a changing environment through its configuration of resources and competences with the aim of fulfilling stakeholder expectations."</i>

<b>3. Eight Key Characteristics (Features) of Strategic Decisions (Short/Brief Question Favourite):</b>
• <b>1. Long-Term Horizon & Future Orientation:</b> Strategic decisions focus on a 3-to-10+ year future timeframe rather than day-to-day routine operations.
• <b>2. Top-Management Involvement:</b> Formulated by the apex authority—the Board of Directors, Chief Executive Officer (CEO), and senior executive team.
• <b>3. Holistic / Organization-Wide Scope:</b> Affects the entire enterprise or a complete Strategic Business Unit (SBU), cutting across all functional departments.
• <b>4. Substantial Resource Commitment:</b> Requires major commitments of financial capital, physical plant, technology, and human talent that are costly and difficult to reverse once deployed.
• <b>5. External Environment Matching (Open-System Fit):</b> Aligns the organization's internal strengths and capabilities with external opportunities and threats in a turbulent environment.
• <b>6. Creation of Sustainable Competitive Advantage:</b> Aims to position the firm uniquely so competitors cannot easily copy its value proposition.
• <b>7. High Uncertainty, Complexity, and Non-Routine Nature:</b> Unlike programmable operational decisions, strategic decisions are novel, unstructured, and involve high risk.
• <b>8. Stakeholder Values and Expectations Driven:</b> Reflects the priorities and power of owners, lenders, customers, employees, regulators, and society.""")

    add_example(story, """• <b>Nepalese Example (Chaudhary Group — Wai Wai):</b> When Chaudhary Group decided to expand Wai Wai noodles from a domestic Nepalese snack into an international FMCG brand with manufacturing plants in India, Serbia, Bangladesh, and Kazakhstan, that was a <b>strategic decision</b> involving long-term vision, massive capital commitment, and global market development.
• <b>Banking Example (Nabil Bank Acquiring Nepal Bangladesh Bank):</b> Nabil Bank's decision to acquire Nepal Bangladesh Bank in 2022 was a corporate strategic decision that reshaped its capital base, branch network, and market leadership in Nepal's commercial banking sector.""")

    add_topic(story, "1.2 Concept, Elements, Need & Importance of Strategic Management")
    add_body(story, """<b>1. Concept of Strategic Management:</b>
Strategic management is that set of managerial decisions and actions that determines the long-run performance and survival of a corporation. It is a continuous, iterative process comprising four core elements:
• <b>Element 1 — Environmental Scanning (Analysis):</b> Monitoring, evaluating, and disseminating information from the external (PESTEL & Industry) and internal (Resources & Value Chain) environments.
• <b>Element 2 — Strategy Formulation (Strategic Planning):</b> Crafting Vision, Mission, Objectives, and Corporate, Business, and Functional strategies.
• <b>Element 3 — Strategy Implementation (Execution):</b> Putting strategies into action through organizational structure, budgets/resource allocation, functional policies, leadership, and corporate culture.
• <b>Element 4 — Strategic Evaluation and Control:</b> Monitoring actual performance against planned targets, auditing strategic premises, and taking corrective action.

<b>2. Need and Importance of Strategic Management (Why Organizations Need It):</b>
• <b>1. Proactive Rather Than Reactive Posture:</b> Enables organizations to anticipate and shape future environmental changes rather than being passive victims of market shocks.
• <b>2. Sense of Direction and Goal Alignment:</b> Provides a clear roadmap (Vision -> Mission -> Objectives) so all departments work toward common goals rather than conflicting departmental agendas.
• <b>3. Building Sustainable Competitive Advantage:</b> Identifies and nurtures rare, valuable core competencies that differentiate the firm from competitors.
• <b>4. Optimal Allocation of Scarce Resources:</b> Prevents waste by channeling capital, talent, and managerial attention toward high-growth, high-return opportunities ("Stars") and away from declining operations.
• <b>5. Risk Mitigation in a Turbulent Environment:</b> Helps navigate political instability, regulatory shifts (e.g., NRB directives), technological disruption (AI, fintech), and hyper-competition.
• <b>6. Improved Organizational Coordination and Communication:</b> Participation of line managers in strategic planning fosters commitment, reduces resistance to change, and improves cross-functional teamwork.
• <b>7. Superior Long-Term Financial & Non-Financial Performance:</b> Empirical studies confirm that strategically managed firms consistently outperform non-planning firms in profitability (ROE, ROA), market share, and longevity.""")

    add_topic(story, "1.3 Evolution of Strategic Management (Four Historical Phases)")
    t_u1_evol = make_table([
        [P_hdr("Phase & Era"), P_hdr("Dominant Theme / Focus"), P_hdr("Key Tools & Concepts"), P_hdr("Main Limitation That Led to Next Phase")],
        [P("Phase 1: 1950s\nBasic Financial Planning", True), P("Internal operational control & meeting annual budget."), P("1-year functional budgets (production, sales, cash)."), P("Too short-sighted (1 year); blind to long-term growth.")],
        [P("Phase 2: 1960s\nForecast-Based Planning", True), P("More effective planning for multi-year growth (Long-Range Planning)."), P("3-to-5 year trend extrapolation, capital budgeting, environmental forecasting."), P("Assumed the future would simply repeat past linear trends; shattered by 1970s oil shocks.")],
        [P("Phase 3: 1970s–1980s\nExternally Oriented Strategic Planning", True), P("Thinking strategically; industry positioning & defeating competitors."), P("Porter's 5 Forces, Generic Strategies, Value Chain, SBU concept, BCG & GE Portfolio Matrices."), P("Top-down 'ivory tower' planning; neglected implementation, culture, and internal resources.")],
        [P("Phase 4: 1990s–Present\nStrategic Management & Dynamic Capabilities", True), P("Creating the future; holistic integration of formulation, implementation & agility."), P("Resource-Based View (RBV/VRIO), Core Competence (Prahalad & Hamel), Balanced Scorecard, Blue Ocean, Hyper-competition."), P("Requires continuous learning, digital agility, and ethical governance.")],
    ], col_widths=[100, 125, 145, 130])
    story.append(t_u1_evol)
    story.append(Spacer(1, 6))

    add_topic(story, "1.4 The Strategic Management Process (Step-by-Step Model & Diagram)")
    story.append(fig_sm_process())
    add_body(story, """<b>Detailed Explanation of Each Step in the Strategic Management Process (10-Mark / 5-Mark Question):</b>
• <b>Step 1: Establishing Strategic Intent (Vision, Mission, Goals & Objectives):</b>
  Top management defines the aspirational long-term dream (Vision), the current business scope and purpose (Mission), and specific, quantifiable performance milestones (SMART Objectives).
• <b>Step 2: Environmental Scanning & Strategic Analysis (External + Internal):</b>
  - <i>External Analysis:</i> Scanning the Macro Environment (PESTEL) and Industry Environment (Porter's Five Forces, Strategic Groups, Competitor Analysis) to prepare an <b>Environmental Threat and Opportunity Profile (ETOP)</b>.
  - <i>Internal Analysis:</i> Auditing organizational resources (Threshold vs. VRIO Strategic Resources), Value Chain Activities, and Financial/Benchmark ratios to prepare a <b>Strategic Advantage Profile (SAP)</b>.
  - <i>SWOT Synthesis:</i> Matching external Opportunities & Threats with internal Strengths & Weaknesses.
• <b>Step 3: Strategy Formulation & Strategic Choice:</b>
  - Generating strategic alternatives at three levels: <b>Corporate Level</b> (Stability, Growth, Retrenchment, Combination), <b>Business/SBU Level</b> (Cost Leadership, Differentiation, Focus), and <b>Functional Level</b> (Marketing, Finance, Operations, HR, R&D).
  - Evaluating portfolio options using <b>BCG, GE 9-Cell, and Hofer's 15-Cell Matrices</b> and selecting the optimal strategy using Johnson & Scholes's <b>SFA Criteria (Suitability, Feasibility, Acceptability)</b>.
• <b>Step 4: Strategy Implementation (Action & Execution Stage):</b>
  Translating the chosen strategy into action by: (i) designing an appropriate <b>Organizational Structure</b> (Functional, Divisional, SBU, Matrix), (ii) <b>Allocating Resources</b> via budgets, (iii) instituting <b>Functional Policies & SOPs</b>, and (iv) providing <b>Strategic Leadership</b> and aligning <b>Corporate Culture</b>.
• <b>Step 5: Strategic Evaluation and Control (Feedback Loop):</b>
  Continuously monitoring underlying assumptions and actual results through <b>Premise Control, Strategic Surveillance, Special Alert Control, Implementation Control, and Strategic Audits</b>, taking corrective action whenever deviations occur.""")

    add_topic(story, "1.5 Levels of Strategy in an Organization (Corporate, Business & Functional)")
    story.append(fig_levels_of_strategy())
    t_u1_levels = make_table([
        [P_hdr("Basis of Comparison"), P_hdr("1. Corporate-Level Strategy"), P_hdr("2. Business-Level (SBU) Strategy"), P_hdr("3. Functional-Level (Operational) Strategy")],
        [P("1. Core Question", True), P("<b>'Where to compete?'</b> (What industries/businesses should the corporation be in?)"), P("<b>'How to compete?'</b> (How do we win customers and beat rivals in this specific industry?)"), P("<b>'How to execute?'</b> (How does each department use its resources to support the SBU?)")],
        [P("2. Formulated By", True), P("Board of Directors, CEO, and Corporate Headquarters."), P("SBU Heads / Divisional Vice Presidents & General Managers."), P("Functional Department Heads (Marketing, Finance, Production, HR, R&D).")],
        [P("3. Scope & Focus", True), P("Entire multi-business corporation; portfolio synergy and capital allocation across SBUs."), P("Single Strategic Business Unit (SBU) operating in a distinct product-market."), P("Specific functional area within an SBU; maximizing resource productivity.")],
        [P("4. Time Horizon & Risk", True), P("Long-term (5 to 10+ years); High risk and high strategic impact."), P("Medium-to-long term (3 to 5 years); Moderate-to-high competitive risk."), P("Short-term (daily to 1 year); Low, operational-level risk.")],
        [P("5. Major Frameworks", True), P("Grand Strategies (Stability, Growth, Retrenchment), Ansoff Matrix, BCG/GE/Hofer Matrices, M&A."), P("Porter's Generic Strategies (Cost Leadership, Differentiation, Focus), Bowman's Strategic Clock."), P("4Ps Marketing Mix, Capital Structure/Dividend Policy, JIT/TQM Operations, HR Training/Rewards.")],
    ], col_widths=[90, 138, 136, 136])
    story.append(t_u1_levels)
    story.append(Spacer(1, 5))

    add_topic(story, "1.6 Strategic Planning & The Hierarchy of Strategic Intent: Vision, Mission, Objectives & Values")
    add_body(story, """<b>1. Concept & Features of Strategic Planning:</b>
Strategic planning is the formal managerial process of defining an organization's strategy or direction and making decisions on allocating its resources to pursue this strategy. Its features are: (i) systematic and disciplined, (ii) future-oriented, (iii) links internal capabilities with external opportunities, and (iv) cascades from corporate goals down to departmental action plans.

<b>2. Vision Statement ("What do we want to become?"):</b>
• <b>Concept:</b> A concise, inspiring, future-oriented declaration of the organization's ultimate long-term aspiration (5 to 20+ years).
• <b>Components of Vision Statement (Jim Collins & Jerry Porras Framework — Exam Question!):</b>
  1. <b>Core Ideology (The Enduring Character that Never Changes):</b>
     - <i>Core Values:</i> 3 to 5 timeless guiding ethical principles (e.g., Disney's imagination & wholesomeness; 3M's innovation; Tata's integrity).
     - <i>Core Purpose:</i> The organization's deepest reason for being (why it exists beyond making profits).
  2. <b>Envisioned Future (What the Organization Aspires to Achieve and Become):</b>
     - <i>Big, Hairy, Audacious Goal (BHAG):</i> A bold, clear, 10-to-30-year goal that rallies people (e.g., Ford's early BHAG: "Democratize the automobile").
     - <i>Vivid Description:</i> A vibrant, engaging description of what it will be like to achieve the BHAG.

<b>3. Mission Statement ("What is our business and whom do we serve?"):</b>
• <b>Concept:</b> An enduring statement of purpose that distinguishes one organization from other similar enterprises and defines the present scope of its operations in product and market terms.
• <b>Nine Essential Components of a Complete Mission Statement (Fred R. David Framework):</b>
  1. <b>Customers:</b> Who are the firm's customers?
  2. <b>Products or Services:</b> What are the firm's major products or services?
  3. <b>Markets:</b> Geographically, where does the firm compete?
  4. <b>Technology:</b> Is the firm technologically current?
  5. <b>Concern for Survival, Growth, and Profitability:</b> Is the firm committed to financial soundness?
  6. <b>Philosophy (Company Values):</b> What are the basic beliefs, values, aspirations, and ethical priorities of the firm?
  7. <b>Self-Concept (Distinctive Competence):</b> What is the firm's major competitive strength?
  8. <b>Concern for Public Image:</b> Is the firm responsive to social, community, and environmental concerns?
  9. <b>Concern for Employees:</b> Are employees a valuable asset of the firm?""")

    t_u1_vm = make_table([
        [P_hdr("Basis of Difference"), P_hdr("Vision Statement"), P_hdr("Mission Statement"), P_hdr("Objectives & Goals")],
        [P("1. Core Question", True), P("<i>'Where do we want to be in the future?'</i>"), P("<i>'What is our business today and whom do we serve?'</i>"), P("<i>'How much of what will be accomplished by when?'</i>")],
        [P("2. Time Orientation", True), P("<b>Future-oriented</b> (5 to 20+ years ahead)."), P("<b>Present-oriented</b> leading into the future."), P("<b>Specific target dates</b> (1-year annual & 3–5 year long-term).")],
        [P("3. Specificity", True), P("Broad, aspirational, and inspirational."), P("Defines business scope, products, markets, and values."), P("Concrete, quantitative, and measurable (<b>SMART</b>).")],
        [P("4. Example (Banking)", True), P("<i>'To be the most trusted and digitally advanced bank in South Asia.'</i>"), P("<i>'To provide innovative, accessible banking and financial solutions to Nepalese households and businesses with integrity.'</i>"), P("<i>'Increase ROE from 14% to 18% and grow digital mobile banking users by 25% by fiscal year 2027.'</i>")],
    ], col_widths=[88, 135, 142, 135])
    story.append(t_u1_vm)
    story.append(Spacer(1, 5))

    add_body(story, """<b>4. Role of Information in Strategic Management:</b>
• <b>In Environmental Scanning:</b> Market intelligence, macroeconomic databases, and customer analytics detect early signals of opportunities and threats.
• <b>In Strategy Formulation:</b> Historical financial data, cost-driver information, and scenario models allow managers to evaluate strategic options objectively.
• <b>In Strategy Implementation:</b> Enterprise Resource Planning (ERP) and Point-of-Sale (POS) systems coordinate inventory, production, and sales across branches.
• <b>In Evaluation & Control:</b> Executive Information Systems (EIS) and Balanced Scorecard dashboards track KPI variances in real time.""")
    add_tip(story, "Use 'C-P-M-T-S-P-S-P-E' to remember Fred David's 9 Mission Components: Customers, Products, Markets, Technology, Survival/Growth/Profit, Philosophy, Self-concept, Public image, and Employees!")

    story.append(PageBreak())

    # ==================== UNIT 2 ====================
    add_unit(story, "UNIT 2: ENVIRONMENT AND STRATEGY ANALYSIS (10 Lecture Hours)")

    add_topic(story, "2.1 Concept of Business Environment: Internal vs. External (Micro/Task & Macro/General)")
    add_body(story, """<b>1. Concept of Environment in Strategic Management:</b>
No business operates in a vacuum. The business environment consists of the sum total of all internal and external factors, forces, institutions, and conditions that affect an organization's survival, operations, strategic decisions, and performance.
• <b>Characteristics of Business Environment:</b> (1) <b>Complexity</b> (many interconnected factors), (2) <b>Dynamism</b> (constantly changing), (3) <b>Uncertainty</b> (hard to predict), (4) <b>Multi-faceted</b> (perceived differently by different firms—one firm's threat is another's opportunity), and (5) <b>Far-reaching Impact</b>.

<b>2. Three Layers of the Business Environment:</b>
• <b>Layer 1 — Internal Environment (Controllable):</b> Factors inside the organization: Tangible & Intangible Resources, Capabilities, Core Competencies, Value Chain Activities, Organizational Structure, Corporate Culture, and Leadership. Analyzed to identify <b>Strengths (S)</b> and <b>Weaknesses (W)</b> -> Summarized in <b>SAP</b>.
• <b>Layer 2 — External Task / Operating / Industry Environment (Partially Influenced):</b> Immediate external actors that directly interact with the firm: Customers, Suppliers, Direct Competitors, Potential Entrants, Substitute Producers, Creditors, and Labor Unions. Analyzed via <b>Porter's Five Forces & Competitor Analysis</b>.
• <b>Layer 3 — External Macro / General / Remote Environment (Uncontrollable):</b> Broad societal forces affecting all industries: <b>PESTEL</b> (Political, Economic, Socio-Cultural, Technological, Environmental/Ecological, Legal). Layer 2 + Layer 3 are analyzed to identify <b>Opportunities (O)</b> and <b>Threats (T)</b> -> Summarized in <b>ETOP</b>.""")

    add_topic(story, "2.2 Techniques of External Environment Analysis: PESTEL, Porter's 5 Forces, ETOP, Scenario Planning & Competitor Analysis")
    add_subtopic(story, "A. PESTEL Analysis (Macro-Environmental Scanning Framework)")
    t_u2_pestel = make_table([
        [P_hdr("PESTEL Dimension"), P_hdr("Key Variables to Scan"), P_hdr("Nepalese Business Context Examples")],
        [P("1. Political (P)", True), P("Government stability, coalition changes, fiscal/tax policy, foreign trade tariffs, FDI policy, public infrastructure spending."), P("Federal/provincial taxation rules, import restrictions/LC margin rules, hydropower PPA policies, Belt & Road / MCC projects.")],
        [P("2. Economic (E)", True), P("GDP growth rate, inflation (CPI), interest rates, foreign exchange reserves, remittance inflows, per capita income, liquidity."), P("NRB monetary policy & interest rate corridors, remittance-fueled consumption, liquidity fluctuations in Nepalese banks.")],
        [P("3. Socio-Cultural (S)", True), P("Population growth, age distribution, youth migration, urbanization, education levels, changing lifestyles, women in workforce."), P("Youth out-migration affecting labor supply and increasing demand for online services, convenience foods, and remittance fintech.")],
        [P("4. Technological (T)", True), P("R&D spending, automation, e-commerce, digital payments, Artificial Intelligence (AI), cloud computing, rate of obsolescence."), P("Explosion of Fonepay QR, ConnectIPS, mobile banking, digital wallets (eSewa/Khalti), and EV adoption in Nepal.")],
        [P("5. Environmental / Ecological (E)", True), P("Climate change, carbon footprint, renewable energy transition, waste/pollution laws, natural disaster vulnerability."), P("High customs duty incentives on Electric Vehicles (EVs) vs. ICE cars in Nepal; glacial/monsoon flood risks to hydro projects.")],
        [P("6. Legal (L)", True), P("Companies Act, Labor & Social Security Act, Consumer Protection Act, Competition Law, Intellectual Property, sector regulators."), P("Insurance Act 2079 (NIA capital rules), Contribution-Based Social Security Fund (SSF 31% mandate), BAFIA, SEBON rules.")],
    ], col_widths=[95, 200, 205])
    story.append(t_u2_pestel)
    story.append(Spacer(1, 6))

    add_subtopic(story, "B. Michael Porter's Five Forces Model of Industry Analysis (10-Mark Exam Classic)")
    story.append(fig_porters_five_forces())
    add_body(story, """<b>In-Depth Explanation of Porter's Five Forces:</b>
• <b>Force 1 — Threat of New Entrants:</b> New entrants bring extra capacity and fight for market share, pushing down prices and margins. The threat is <b>LOW</b> when <b>Barriers to Entry</b> are high:
  1. <i>Economies of Scale:</i> Incumbents produce at large volume with low unit cost, forcing newcomers to either enter huge (risky) or suffer a cost disadvantage.
  2. <i>High Capital Requirements:</i> Billions needed to enter banking (Rs 8B paid-up capital in Nepal), cement, telecom, or airlines.
  3. <i>Product Differentiation & Brand Loyalty:</i> Strong incumbent brands (e.g., Wai Wai, Surya, Ncell/NTC) require massive advertising to overcome.
  4. <i>Customer Switching Costs:</i> High one-time costs (retraining, new software/equipment) of switching from an existing vendor.
  5. <i>Access to Distribution Channels:</i> Incumbents have tied up wholesale and retail dealers.
  6. <i>Cost Advantages Independent of Scale:</i> Proprietary patents, favorable raw material locations (e.g., limestone mines), and learning/experience curves.
  7. <i>Government Policy & Licensing:</i> Strict regulatory moratoriums on new bank or telecom licenses.
• <b>Force 2 — Bargaining Power of Buyers (Customers):</b> Buyers compete with the industry by forcing down prices and demanding higher quality or longer credit. Buyer power is <b>HIGH</b> when: (i) a few buyers purchase a large share of industry output, (ii) products are standardized/undifferentiated commodities, (iii) switching costs are low, (iv) buyers earn low profits (making them price-sensitive), and (v) buyers pose a credible threat of <b>backward vertical integration</b>.
• <b>Force 3 — Bargaining Power of Suppliers:</b> Suppliers squeeze industry profitability by raising input prices or reducing quality. Supplier power is <b>HIGH</b> when: (i) the supplier industry is dominated by a few firms (oligopoly), (ii) there are no close substitutes for the supplied input, (iii) the focal industry is not an important customer of the supplier, (iv) supplier's product is an essential input with high switching costs, and (v) suppliers pose a credible threat of <b>forward vertical integration</b>.
• <b>Force 4 — Threat of Substitute Products or Services:</b> Substitutes come from outside the industry but fulfill the same basic customer need (e.g., tea vs. coffee; domestic airlines vs. night-bus/highway travel; eye glasses vs. contact lenses/LASIK). Substitutes place a hard ceiling on industry prices. The threat is <b>HIGH</b> when substitutes offer a superior price-performance trade-off and buyer switching costs are low.
• <b>Force 5 — Intensity of Rivalry Among Existing Competitors:</b> Rivalry is <b>FIERCE</b> when: (i) competitors are numerous or roughly equal in size and power, (ii) industry growth is slow or stagnant, (iii) fixed costs or storage/perishability costs are high, (iv) product differentiation and switching costs are low, (v) capacity must be added in large increments, and (vi) <b>Exit Barriers are high</b> (specialized assets with low liquidation value, high labor redundancy costs, emotional/strategic barriers).""")

    add_subtopic(story, "C. Environmental Threat and Opportunity Profile (ETOP), Scenario Planning, Hyper-Competition & Strategic Groups")
    add_body(story, """<b>1. Environmental Threat and Opportunity Profile (ETOP):</b>
Proposed by Glueck, ETOP is a structured diagnostic table that summarizes the findings of external environmental scanning. Preparation steps: (1) Divide the environment into major sectors (Economic, Market, Technological, Political/Legal, Social, Supplier), (2) Analyze the impact of trends in each sector using arrows (<b>Up Arrow [+] = Favorable</b>, <b>Down Arrow [-] = Unfavorable</b>, <b>Horizontal [0] = Neutral</b>), and (3) Assess the magnitude of each Opportunity or Threat.""")

    t_u2_etop = make_table([
        [P_hdr("Environmental Sector"), P_hdr("Nature of Impact"), P_hdr("Impact Analysis & Classification as Opportunity (O) or Threat (T) [Example: Automobile Dealer in Nepal]")],
        [P("1. Economic / Tax Policy", True), P("<b>Favorable (+)</b>"), P("<b>Opportunity:</b> Lower customs & excise duty on Electric Vehicles (EVs) compared to 250%+ tax on petrol cars boosts EV demand.")],
        [P("2. Technological Sector", True), P("<b>Favorable (+)</b>"), P("<b>Opportunity:</b> Rapid expansion of NEA fast-charging stations across highways and longer-range LFP batteries reduce range anxiety.")],
        [P("3. Financial / Credit Sector", True), P("<b>Unfavorable (-)</b>"), P("<b>Threat:</b> Stricter NRB loan-to-value (LTV) caps and high auto-loan interest rates restrict middle-class vehicle financing.")],
        [P("4. Competitive / Market Sector", True), P("<b>Unfavorable (-)</b>"), P("<b>Threat:</b> Entry of over 25 Chinese and Indian EV brands into Kathmandu creates intense price wars and after-sales pressure.")],
    ], col_widths=[115, 85, 300])
    story.append(t_u2_etop)
    story.append(Spacer(1, 5))

    add_body(story, """<b>2. Scenario Planning:</b> A disciplined method for imagining possible futures in turbulent environments. Strategists select key external uncertainties (e.g., global oil prices, exchange rates, political stability) and build 3 to 4 internally consistent future scenarios (<i>Optimistic, Pessimistic, Status-Quo, Disruptive</i>), formulating a robust core strategy plus contingency triggers for each scenario.
<b>3. Strategic Groups & Mobility Barriers:</b> A <b>Strategic Group</b> is a set of firms within an industry that pursue similar strategies along dimensions such as price/quality, geographic coverage, degree of vertical integration, and product-line breadth (e.g., in Nepal's hospitality sector: 5-star international chain hotels [Soaltee, Marriott, Hyatt] form one strategic group, while budget tourist guest houses in Thamel form another). <i>Mobility barriers</i> prevent firms from easily jumping from one strategic group to another.
<b>4. Hyper-Competition (Richard D'Aveni):</b> An environment of intense, rapid competitive moves where rivals quickly copy or leapfrog any advantage, so firms must continuously disrupt their own advantages across four arenas: (i) Cost & Quality, (ii) Timing & Know-How, (iii) Strongholds, and (iv) Deep Pockets.""")

    add_topic(story, "2.3 Techniques of Internal Environment Analysis: RBV (VRIO), Value Chain Analysis, Benchmarking & SAP")
    add_subtopic(story, "A. Resource-Based View (RBV), Threshold vs. Strategic Resources & VRIO Framework")
    add_body(story, """<b>1. Resource-Based View (RBV — Wernerfelt, Barney, Prahalad & Hamel):</b>
RBV takes an <b>"Inside-Out" perspective</b>: it argues that superior long-term profitability comes not from merely choosing an attractive industry, but from possessing a unique bundle of internal <b>Resources, Capabilities, and Core Competencies</b>.
• <b>Resources (What the firm HAS):</b>
  - <i>Tangible Resources:</i> Physical plants, land, machinery, cash reserves, borrowing capacity, IT hardware.
  - <i>Intangible Resources:</i> Brand equity, reputation, patents, copyrights, trade secrets, proprietary customer databases, corporate culture.
• <b>Capabilities (What the firm DOES):</b> The organizational routines and skills in coordinating resources to perform activities effectively.
• <b>Core Competencies (Prahalad & Hamel):</b> Capabilities that serve as a source of competitive advantage over rivals because they (i) provide potential access to a wide variety of markets, (ii) make a significant contribution to perceived customer benefits, and (iii) are difficult for competitors to imitate (e.g., Honda's core competence in small high-efficiency engines; Sony's miniaturization; Apple's user-interface & ecosystem integration).
• <b>Threshold Resources vs. Strategic (Unique) Resources:</b>
  - <b>Threshold Resources:</b> Minimum resources required merely to exist and meet basic customer expectations in an industry (yield competitive parity only).
  - <b>Strategic Resources:</b> Rare, inimitable resources that satisfy the <b>VRIO Framework</b> and yield sustainable competitive advantage:""")

    t_u2_vrio = make_table([
        [P_hdr("Is the Resource Valuable (V)?"), P_hdr("Is it Rare (R)?"), P_hdr("Is it Inimitable (I)?"), P_hdr("Is the Firm Organized (O)?"), P_hdr("Competitive Implication"), P_hdr("Economic Performance")],
        [P("No"), P("—"), P("—"), P("No"), P("<b>Competitive Disadvantage</b>"), P("Below-Normal Returns")],
        [P("Yes"), P("No"), P("—"), P("Yes"), P("<b>Competitive Parity</b> (Threshold)"), P("Normal (Average) Returns")],
        [P("Yes"), P("Yes"), P("No (Easy to copy)"), P("Yes"), P("<b>Temporary Competitive Advantage</b>"), P("Above-Normal (Short-Run)")],
        [P("<b>Yes</b>", True), P("<b>Yes</b>", True), P("<b>Yes (Costly to copy)</b>", True), P("<b>Yes</b>", True), P("<b>Sustainable Competitive Advantage</b>", True), P("<b>Sustained Above-Normal Returns</b>", True)],
    ], col_widths=[72, 62, 82, 72, 112, 100])
    story.append(t_u2_vrio)
    story.append(Spacer(1, 5))

    add_subtopic(story, "B. Michael Porter's Value Chain Analysis (VCA) — Diagram & 5-Step Process")
    story.append(fig_value_chain())
    add_body(story, """<b>1. Classification of Value Chain Activities:</b>
• <b>Five Primary Activities (Directly involved in physical creation, sale, transfer, and after-sales service of the product):</b>
  1. <i>Inbound Logistics:</i> Receiving, warehousing, inventory control, and material handling of raw inputs from suppliers.
  2. <i>Operations:</i> Machining, assembling, packaging, testing, and equipment maintenance that transform inputs into finished products.
  3. <i>Outbound Logistics:</i> Finished goods warehousing, order processing, fleet scheduling, and physical delivery to buyers/dealers.
  4. <i>Marketing and Sales:</i> Advertising, promotion, sales force management, pricing, channel selection, and brand building.
  5. <i>After-Sales Service:</i> Installation, customer training, warranty repair, spare parts supply, and complaint handling.
• <b>Four Support Activities (Sustain and enable all five primary activities):</b>
  1. <i>Firm Infrastructure:</i> General management, strategic planning, finance, accounting, legal, quality assurance, and corporate governance.
  2. <i>Human Resource Management:</i> Recruiting, hiring, training, developing, appraising, and compensating personnel across the firm.
  3. <i>Technology Development:</i> R&D, product design, process engineering, automation, and ERP/telecommunications software.
  4. <i>Procurement:</i> Purchasing raw materials, machinery, laboratory equipment, office supplies, and buildings.

<b>2. Five-Step Process of Conducting Value Chain Analysis:</b>
• <b>Step 1: Segregate the Firm's Operations into Primary and Support Activities.</b>
• <b>Step 2: Allocate Costs and Identify Structural Cost Drivers</b> (economies of scale, learning curve, capacity utilization) for each activity.
• <b>Step 3: Identify Value/Differentiation Drivers</b> (activities that create unique customer satisfaction, quality, or speed).
• <b>Step 4: Evaluate Internal and External Linkages</b> (how optimizing one activity—like zero-defect Procurement—reduces rework costs in Operations and Warranty Service).
• <b>Step 5: Benchmark Against Rivals and Reconfigure/Outsource</b> non-core activities to achieve either Cost Leadership or Differentiation.""")

    add_subtopic(story, "C. Comparative Analysis (Historical, Industry Norms, Benchmarking), Financial Analysis, SAP & SWOT/TOWS Matrix")
    add_body(story, """<b>1. Three Methods of Comparative Analysis:</b>
• <b>(i) Historical Comparison:</b> Comparing the firm's current performance (margins, market share, productivity) with its own past years to spot trends.
• <b>(ii) Industry Standards (Norms):</b> Comparing ratios against the average of the industry.
• <b>(iii) Benchmarking:</b> Systematically comparing the firm's processes and performance metrics against the world's or industry's <b>"Best-in-Class"</b> leaders (whether competitors or non-competitors) to adopt best practices.
<b>2. Strategic Advantage Profile (SAP) & SWOT / TOWS Matrix:</b>
• <b>SAP:</b> A structured table summarizing the firm's internal functional strengths (+) and weaknesses (-) across Marketing, Finance, Operations, HR, R&D, and General Management.
• <b>SWOT / TOWS Matrix (Heinz Weihrich):</b> Pairs Internal Strengths (S) & Weaknesses (W) from SAP with External Opportunities (O) & Threats (T) from ETOP to formulate four strategic combinations:
  - <b>1. SO Strategies (Maxi-Maxi):</b> Use internal Strengths to take advantage of external Opportunities (Aggressive Growth).
  - <b>2. WO Strategies (Mini-Maxi):</b> Overcome internal Weaknesses by exploiting external Opportunities (e.g., forming a joint venture to acquire missing technology).
  - <b>3. ST Strategies (Maxi-Mini):</b> Use internal Strengths to avoid or reduce the impact of external Threats (Diversification / Defense).
  - <b>4. WT Strategies (Mini-Mini):</b> Defensive tactics directed at reducing internal Weaknesses and avoiding external Threats (Turnaround, Divestment, or Liquidation).""")

    story.append(PageBreak())
