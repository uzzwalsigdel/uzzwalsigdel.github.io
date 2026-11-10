from notes_base import (
    Paragraph, Spacer, PageBreak, add_unit, add_topic, add_subtopic,
    add_body, add_example, add_tip, make_table, P, P_hdr
)
from bnk209_figures import (
    fig_risk_classification, fig_rm_process_and_matrix, fig_legal_principles
)

def build_bnk209_u1_to_u4(story):
    # ==================== UNIT 1 ====================
    add_unit(story, "UNIT 1: INTRODUCTION TO RISK & LOSS EXPOSURES (5 Lecture Hours)")

    add_topic(story, "1.1 Meaning of Risk, Uncertainty, Objective vs. Subjective Risk, Peril & Hazard")
    add_body(story, """<b>1. Meaning of Risk and Uncertainty:</b>
In insurance and risk management (George E. Rejda), <b>Risk</b> is defined as <i>uncertainty concerning the occurrence of a financial loss</i> (or the variation between actual outcomes and expected outcomes in a situation where probabilities can be estimated).
• <b>Risk vs. Uncertainty (2-Mark / 5-Mark Distinction):</b>""")
    t_u1_ru = make_table([
        [P_hdr("Basis of Distinction"), P_hdr("Risk"), P_hdr("Uncertainty")],
        [P("1. Measurability", True), P("<b>Objectively Measurable:</b> Probabilities of possible outcomes can be calculated from historical data or actuarial tables."), P("<b>Not Objectively Measurable:</b> Probabilities cannot be quantified due to lack of historical precedent.")],
        [P("2. Nature", True), P("Objective phenomenon existing in the external world."), P("Subjective state of mind (personal doubt or mental anxiety).")],
        [P("3. Insurability", True), P("Can be pooled and transferred through commercial insurance."), P("Generally cannot be insured through standard actuarial policies.")],
        [P("4. Example", True), P("Probability of fire in 10,000 houses or mortality rate at age 35."), P("Whether a brand-new revolutionary product will succeed in 2035.")],
    ], col_widths=[105, 198, 197])
    story.append(t_u1_ru)
    story.append(Spacer(1, 5))

    add_body(story, """<b>2. Objective Risk vs. Subjective Risk:</b>
• <b>Objective Risk (Degree of Risk):</b> The relative variation of actual loss from expected loss:
  <b>Objective Risk = Standard Deviation of Losses / Expected Loss</b>.
  By the <b>Law of Large Numbers</b>, as the number of independent exposure units (N) increases, Objective Risk decreases inversely with the square root of N (1 / sqrt(N)). This is why insurance companies strive to build large pools of policyholders.
• <b>Subjective (Perceived) Risk:</b> Uncertainty based on an individual's mental condition or state of mind. Two individuals facing the exact same objective risk (e.g., a 1% chance of an accident) may perceive it differently depending on their personal risk aversion.

<b>3. Peril vs. Hazard (And the Four Types of Hazards — Exam Essential):</b>
• <b>Peril:</b> The direct, immediate, and specific <b>cause of a loss</b> (e.g., fire, lightning, windstorm, flood, earthquake, theft, auto collision, premature death, sickness).
• <b>Hazard:</b> Any condition or situation that <b>creates or increases the frequency (probability) or severity (size)</b> of a loss arising from a given peril. There are four distinct types of hazards:
  1. <b>Physical Hazard:</b> A tangible physical condition of the property, person, or environment that increases the chance of loss. <i>Examples: Icy or unpaved mountain roads (increases auto collision peril); faulty electrical wiring or storing kerosene in a warehouse (increases fire peril); obesity or high blood pressure (increases premature death peril).</i>
  2. <b>Moral Hazard:</b> Dishonesty or character defects in an individual that increase the frequency or severity of loss—where the insured intentionally causes a loss or exaggerates a claim to defraud the insurer. <i>Examples: Deliberately setting fire to an unprofitable factory (arson) to collect fire insurance; staging a fake burglary; inflating hospital or garage repair bills.</i>
  3. <b>Attitudinal Hazard (Morale Hazard):</b> Carelessness or indifference to a loss simply because one knows the loss is covered by insurance. <i>Examples: Leaving car keys in an unlocked car, failing to lock warehouse doors, or visiting expensive hospitals for minor ailments because health insurance pays 100%.</i>
  4. <b>Legal Hazard:</b> Characteristics of the legal system or regulatory environment that increase the frequency or severity of liability losses. <i>Examples: Sympathetic juries awarding huge punitive damages against corporations; consumer protection laws expanding strict liability.</i>""")

    add_topic(story, "1.2 Classification of Risk (Pure vs. Speculative, Diversifiable vs. Non-Diversifiable, Enterprise vs. Systemic)")
    story.append(fig_risk_classification())
    t_u1_class = make_table([
        [P_hdr("Classification Pair"), P_hdr("First Category (Definition & Examples)"), P_hdr("Second Category (Definition & Examples)")],
        [P("1. Pure Risk vs.\nSpeculative Risk", True),
         P("<b>Pure Risk:</b> A situation in which there are only two possible outcomes—<b>Loss or No Loss</b> (zero chance of financial gain). Accidental, involuntary, and <b>insurable</b> via pooling.\n<i>Examples:</i> Fire, earthquake, flood, premature death, permanent disability, auto accident, server data breach."),
         P("<b>Speculative Risk:</b> A situation in which there are three possible outcomes—<b>Loss, No Loss (Breakeven), or Financial Gain/Profit</b>. Undertaken voluntarily and <b>not insurable</b> (handled via derivative hedging or portfolio diversification).\n<i>Examples:</i> Investing/trading in NEPSE stocks, launching a new startup venture, betting, foreign exchange speculation.")],
        [P("2. Diversifiable vs.\nNon-Diversifiable Risk", True),
         P("<b>Diversifiable (Particular / Nonsystematic) Risk:</b> Affects only individuals or small groups and is not correlated with the macro-economy. Can be reduced or eliminated through diversification and insurance pooling.\n<i>Examples:</i> House fire, car theft, single-factory machinery breakdown."),
         P("<b>Non-Diversifiable (Fundamental / Systemic) Risk:</b> Affects the entire economy or large numbers of persons/groups simultaneously; cannot be eliminated by simple diversification.\n<i>Examples:</i> Hyperinflation, mass cyclical unemployment, global pandemic, war, catastrophic earthquake.")],
        [P("3. Enterprise Risk vs.\nSystemic Risk", True),
         P("<b>Enterprise Risk:</b> Encompasses all major risks faced by a single business firm across its operations: Pure risk + Speculative financial risk (interest, FX, credit, commodity) + Operational risk (IT/supply chain failure) + Strategic & Reputational risk."),
         P("<b>Systemic Risk:</b> The risk of collapse of an entire financial system or entire market (as opposed to a single entity), where the failure of one major interconnected bank or institution triggers a chain-reaction domino collapse across the economy.")],
    ], col_widths=[95, 202, 203])
    story.append(t_u1_class)
    story.append(Spacer(1, 5))

    add_topic(story, "1.3 Major Personal Risks, Commercial Risks & Burden of Risk on Society")
    add_body(story, """<b>1. Major Personal Risks (Loss Exposures Affecting Individuals & Families):</b>
• <b>(1) Risk of Premature Death:</b> Death of a family breadwinner with unfulfilled financial obligations (dependent spouse/children, unpaid home mortgage or auto loan, unfunded college education).
• <b>(2) Risk of Insufficient Income During Retirement (Old-Age / Longevity Risk):</b> Outliving one's accumulated savings upon retirement, leading to a sharp drop in standard of living.
• <b>(3) Risk of Poor Health (Medical Expense & Disability Risk):</b> Catastrophic hospital/surgical bills combined with loss of earned income during prolonged disability.
• <b>(4) Risk of Involuntary Unemployment:</b> Loss of earned income due to economic recessions, technological automation, or corporate downsizing.
• <b>(5) Personal Property & Liability Risks:</b> Damage to one's home/car or legal liability for injuring others.

<b>2. Major Commercial Risks (Loss Exposures Affecting Business Firms):</b>
• <b>(1) Property Risk:</b> Direct physical damage to plants, offices, high-end servers, laptops, furniture, and inventory from fire, lightning, earthquake, flood, or burglary.
• <b>(2) Loss of Business Income (Business Interruption / Consequential Loss Risk):</b> Loss of net profit plus continuing fixed expenses (rent, salaries, loan interest) while the business is shut down for repairs after a physical loss, plus extra expense of renting temporary facilities.
• <b>(3) Liability Risk (Third-Party Legal Liability):</b> Lawsuits for bodily injury, property damage, defective products, motor accidents, workplace injuries, or professional errors & omissions (E&O).
• <b>(4) Cyber Security, Data Breach & Identity Theft Risk:</b> Loss or corruption of sensitive customer data due to hacker attacks, ransomware, or employee server misconfiguration, triggering massive regulatory fines and client lawsuits.
• <b>(5) Human Resource (Personnel) Risk:</b> Death, disability, illness, or turnover of key executives and technical specialists.

<b>3. Burden of Risk on Society (5-Mark Short Answer Classic):</b>
• <b>1. Larger Emergency Funds Required (Idle Capital):</b> Without insurance, households and businesses must hold huge precautionary cash reserves, diverting capital away from productive investment.
• <b>2. Loss of Needed Goods and Services:</b> Fear of catastrophic liability or property loss discourages companies from producing vital high-risk products (e.g., vaccines, aviation, infrastructure).
• <b>3. Mental Worry, Fear, and Anxiety:</b> Psychological stress over potential disasters reduces human happiness and workplace focus.
• <b>4. Direct & Indirect Social Costs of Uncompensated Losses:</b> Uninsured business failures cause unemployment, family poverty, loan defaults, and higher government welfare burdens.""")

    story.append(PageBreak())

    # ==================== UNIT 2 ====================
    add_unit(story, "UNIT 2: RISK MANAGEMENT PROCESS & QUANTITATIVE TOOLS (6 Lecture Hours)")

    add_topic(story, "2.1 Concept, Objectives, Benefits & 6-Step Process of Risk Management")
    story.append(fig_rm_process_and_matrix())
    add_body(story, """<b>1. Pre-Loss and Post-Loss Objectives of Risk Management:</b>
• <b>Pre-Loss Objectives (Before a Loss Occurs):</b>
  1. <i>Economy:</i> Prepare for potential losses in the most cost-effective way (minimizing safety costs, insurance premiums, and uncompensated losses).
  2. <i>Reduction of Anxiety:</i> Give peace of mind to managers, owners, and families.
  3. <i>Meeting Legal & Contractual Obligations:</i> Comply with mandatory laws (third-party motor insurance, SSF/workers' compensation, safety codes) and bank loan covenants.
• <b>Post-Loss Objectives (After a Catastrophic Loss Occurs):</b>
  1. <i>Survival of the Firm:</i> The most important post-loss objective—being able to resume operations after a major disaster.
  2. <i>Continuity of Operations:</i> Resuming partial or full service quickly so customers do not defect to competitors.
  3. <i>Stability of Earnings:</i> Maintaining steady EPS and cash flows without violent post-loss deficits.
  4. <i>Continued Growth of the Firm:</i> Preserving capital for R&D and market expansion.
  5. <i>Social Responsibility:</i> Minimizing the adverse impact of a disaster on employees, suppliers, customers, and the community.

<b>2. Detailed 6-Step Process of Risk Management (10-Mark Exam Classic):</b>
• <b>Step 1: Determination of Objectives:</b> Establish formal pre-loss and post-loss objectives in a written corporate Risk Management Policy Statement.
• <b>Step 2: Identification of Loss Exposures:</b> Systematically uncover all pure and enterprise loss exposures (Property, Liability, Business Interruption, Human Resources, Crime/Cyber) using five identification tools: (i) <i>Risk Analysis Questionnaires/Checklists</i>, (ii) <i>Physical Plant Inspections</i>, (iii) <i>Flowcharts of Production & Delivery</i>, (iv) <i>Financial Statement Analysis</i>, and (v) <i>Historical Loss/Claims Records</i>.
• <b>Step 3: Measurement and Evaluation of Loss Exposures (Loss Forecasting):</b> Estimate for each exposure:
  - <b>Loss Frequency:</b> Probable number of losses during the budget period.
  - <b>Loss Severity:</b> Probable size of losses—measuring both <b>Maximum Possible Loss</b> (worst-case total catastrophe) and <b>Probable Maximum Loss (PML)</b> (worst loss likely to happen under normal protection). Severity is more critical than frequency because a single catastrophic loss can wipe out a firm!
• <b>Step 4: Selection of Appropriate Risk Treatment Techniques:</b> Choose the optimal combination of <b>Risk Control</b> (Avoidance, Loss Prevention, Loss Reduction [Duplication & Separation]) and <b>Risk Financing</b> (Retention/Self-Insurance/Captives, Non-Insurance Transfer, Commercial Insurance) based on the 2x2 Frequency-Severity Matrix (Figure 2.2).
• <b>Step 5: Implementation of the Risk Management Program:</b> Purchase selected insurance policies, set up retention reserves, install fire/cyber safety systems, and train employees across all departments.
• <b>Step 6: Regular Monitoring, Review, and Evaluation:</b> Periodically audit claims, safety compliance, and policy limits using a <b>Risk Management Information System (RMIS)</b>.""")

    add_topic(story, "2.2 Loss Forecasting, Financial Analysis in Risk Management, RMIS, VaR & ERM")
    add_body(story, """<b>1. Loss Forecasting as a Fundamental Activity in Risk Management (10-Mark / 5-Mark Question):</b>
Loss forecasting is the quantitative prediction of future loss frequency and severity so the risk manager can budget retention funds, evaluate insurance quotes, and perform cost-benefit analysis of safety equipment. The three primary techniques of loss forecasting are:
• <b>(i) Probability Analysis:</b> Uses historical loss frequency and severity probabilities to calculate the <b>Expected Loss [E(L) = Sum (Loss_i x Prob_i)]</b> and standard deviation for independent and dependent events.
• <b>(ii) Regression Analysis:</b> Establishes a statistical relationship between a dependent loss variable <i>Y</i> (e.g., annual number of workers' compensation claims or auto accidents) and an independent physical exposure variable <i>X</i> (e.g., total payroll hours or fleet kilometers driven): <b>Y = a + bX</b>. When next year's budgeted payroll or mileage <i>X</i> is plugged in, regression forecasts expected losses <i>Y</i>.
• <b>(iii) Forecasting Based on Theoretical Loss Distributions:</b> Models loss frequency using the <b>Poisson or Binomial distribution</b> and loss severity using the <b>Lognormal or Pareto distribution</b> (often via Monte Carlo simulation) to estimate tail risk and Probable Maximum Loss.

<b>2. Financial Analysis in Risk Management Decision Making (Time Value of Money / NPV):</b>
Because safety investments (e.g., installing an automatic fire sprinkler system or backup server) require an immediate cash outflow today while generating cash inflows (reduced uninsured losses and lower fire insurance premiums) over many future years, risk managers use <b>Net Present Value (NPV)</b> and <b>Internal Rate of Return (IRR)</b> to evaluate risk control projects.

<b>3. Risk Appetite vs. Risk Tolerance, Value at Risk (VaR), RMIS & Enterprise Risk Management (ERM):</b>
• <b>Risk Appetite vs. Risk Tolerance:</b> <i>Risk Appetite</i> is the broad, qualitative strategic level of risk an organization is willing to accept in pursuit of value; <i>Risk Tolerance</i> is the specific, quantitative maximum acceptable deviation around a particular objective.
• <b>Value at Risk (VaR):</b> A statistical measure that summarizes the <b>worst expected financial loss</b> over a target time horizon (e.g., 1 day, 10 days, or 1 year) at a given confidence level (e.g., 95% or 99%) under normal market conditions.
• <b>Risk Management Information System (RMIS):</b> A computerized database that stores property values, policy schedules, premiums, and claims histories, enabling automated loss forecasting, trend detection, and renewal tracking.
• <b>Traditional Risk Management (TRM) vs. Enterprise Risk Management (ERM):</b> TRM manages only <i>insurable pure risks</i> in fragmented departmental silos; ERM holistically manages <i>all risks</i> (Pure, Speculative Financial, Operational, Cyber, Strategic) across the entire enterprise under a <b>Chief Risk Officer (CRO)</b>, using natural hedges, derivatives, and insurance together.""")

    # ==================== UNIT 3 ====================
    add_unit(story, "UNIT 3: THE INSURANCE DEVICE & RISK POOLING (5 Lecture Hours)")

    add_topic(story, "3.1 Definition & Basic Characteristics of Insurance, Law of Large Numbers & Insurable Risk")
    add_body(story, """<b>1. Four Basic Characteristics of Insurance:</b>
• <b>(1) Pooling of Losses (Risk Pooling / Loss Sharing):</b> Spreading losses incurred by the few over the entire group, so that in the process, <b>average loss is substituted for actual loss</b>.
• <b>(2) Payment of Fortuitous Losses:</b> A fortuitous loss is one that is unforeseen, unexpected, and occurs as a result of chance (accidental, not intentional).
• <b>(3) Risk Transfer:</b> A pure risk is transferred from the insured to the insurer, who is in a stronger financial position to pay the loss.
• <b>(4) Indemnification:</b> The insured is restored to their approximate pre-loss financial position after a loss occurs.

<b>2. Six Requirements of an Ideally Insurable Risk (And Why Catastrophic Losses Pose a Challenge):</b>
• <b>1. Large Number of Exposure Units:</b> Needed so the Law of Large Numbers can predict average loss accurately.
• <b>2. Accidental and Unintentional Loss:</b> Intentional losses create moral hazard and violate actuarial randomness.
• <b>3. Determinable and Measurable Loss:</b> Cause, time, place, and dollar amount must be verifiable.
• <b>4. No Catastrophic Loss:</b> Ideally, a large proportion of exposure units should not suffer loss at the same time. <i>(Why Catastrophes Challenge Insurance: Earthquakes, widespread floods, wars, and pandemics hit thousands of insured units simultaneously—breaking the independence assumption of the Law of Large Numbers, threatening insurer solvency, and requiring global reinsurance, catastrophe bonds, and government pools.)</i>
• <b>5. Calculable Chance of Loss:</b> Average frequency and average severity must be estimable.
• <b>6. Economically Feasible Premium:</b> The insured must be able to afford the premium (chance of loss cannot be too high, e.g., &gt;40%).""")

    add_topic(story, "3.2 Adverse Selection, Insurance vs. Gambling, Insurance vs. Hedging & Benefits/Costs to Society")
    add_body(story, """<b>1. Adverse Selection & Tools to Control It (5-Mark Exam Favourite):</b>
• <b>Definition:</b> Adverse selection is the tendency of persons with a higher-than-average probability of loss to seek insurance at standard (average) rates, which—if uncontrolled—results in higher-than-expected claims.
• <b>Five Tools Used by Insurers to Control Adverse Selection:</b>
  1. <i>Careful Underwriting & Risk Classification:</i> Selecting and classifying applicants into standard, preferred, substandard, or declined categories based on age, medical history, occupation, and property inspections.
  2. <i>Waiting Periods & Pre-Existing Condition Clauses:</i> Imposing waiting periods (e.g., 30 days to 2 years in health insurance) and suicide exclusions.
  3. <i>Deductibles, Coinsurance & Policy Limits:</i> Requiring cost-sharing by the insured.
  4. <i>Group Insurance Underwriting Rules:</i> Requiring automatic enrollment or high participation (e.g., 75%+) across an employer group.
  5. <i>Enforcing Utmost Good Faith:</i> Rescinding policies where applicants conceal material health/risk facts.

<b>2. Benefits and Costs of Insurance to Society:</b>
• <b>Social & Economic Benefits of Insurance:</b> (1) Indemnification for losses (restores families and businesses), (2) Reduction of worry and fear, (3) Source of long-term investment funds (mobilizes savings for banks, infrastructure, and hydropower), (4) Loss prevention incentives (schedule rating discounts for fire sprinklers, workplace safety), and (5) Enhancement of credit (collateral protection for mortgages, auto loans, and import LCs).
• <b>Social Costs of Insurance:</b> (1) Cost of doing business (operating expenses and commissions—loading), (2) Fraudulent claims (moral hazard), and (3) Inflated claims (attitudinal hazard).""")

    story.append(PageBreak())

    # ==================== UNIT 4 ====================
    add_unit(story, "UNIT 4: LEGAL PRINCIPLES & CONTRACT PROVISIONS IN INSURANCE (5 Lecture Hours)")

    add_topic(story, "4.1 The Six Fundamental Legal Principles of Insurance Contracts (10-Mark Exam Essential)")
    story.append(fig_legal_principles())
    add_body(story, """<b>In-Depth Explanation of the Six Fundamental Legal Principles:</b>
• <b>1. Principle of Utmost Good Faith (Uberrimae Fidei):</b>
  - <i>Concept:</i> Unlike ordinary commercial sales (<i>caveat emptor</i>), an insurance contract requires the highest degree of honesty from both the applicant and the insurer. They must voluntarily disclose all material facts relating to the risk.
  - <i>Three Supporting Legal Doctrines (5-Mark Question!):</i>
    1. <b>Representations:</b> Statements made by the applicant on the proposal form before policy issuance. A contract is voidable if a representation is (a) <i>material</i>, (b) <i>false</i>, and (c) <i>relied upon by the insurer</i>.
    2. <b>Concealment:</b> Intentional silence or failure of the applicant to disclose a known material fact. To void a policy, the insurer must prove the concealed fact was material and intentionally hidden.
    3. <b>Warranties:</b> Statements or promises incorporated directly into the policy contract that guarantee a condition exists (<i>affirmative warranty</i>) or will be maintained throughout the policy term (<i>promissory warranty</i>—e.g., maintaining a burglar alarm or working fire sprinklers). Strict compliance is required.

• <b>2. Principle of Insurable Interest:</b>
  - <i>Concept:</i> The insured must stand in a legally recognized financial relationship to the subject matter of insurance such that they will suffer a direct pecuniary (financial) loss if the insured event occurs.
  - <i>Three Purposes:</i> (i) To prevent gambling/wagering on strangers' lives or property, (ii) To reduce moral hazard (murder or arson for insurance money), and (iii) To measure the amount of the insured's loss in property insurance.
  - <i>When Insurable Interest Must Exist:</i>
    • In <b>Life Insurance</b>, insurable interest must exist <b>only at the inception of the policy</b> (not necessarily at the time of death).
    • In <b>Property and Marine Insurance</b>, insurable interest must exist <b>at the time of the loss</b> (and generally at inception).

• <b>3. Principle of Indemnity:</b>
  - <i>Concept:</i> The insurer agrees to pay no more than the actual amount of the loss; stated differently, the insured should not profit from a loss, but should be restored to the same financial position that existed prior to the loss.
  - <i>Methods of Determining Actual Cash Value (ACV):</i>
    1. <b>Replacement Cost Minus Depreciation:</b> <b>ACV = Current Replacement Cost - Physical Depreciation</b>.
    2. <b>Fair Market Value</b> (what a willing buyer would pay a willing seller before the loss).
    3. <b>Broad Evidence Rule</b> (considering all relevant factors: replacement cost, market value, rental income, expert appraisal).
  - <i>Four Exceptions to the Principle of Indemnity:</i> (1) <b>Valued Policies</b> (pays full face value upon total loss, e.g., fine art or marine hull), (2) <b>Valued Policy Laws</b>, (3) <b>Replacement Cost Insurance</b> (pays new replacement cost without deducting depreciation), and (4) <b>Life Insurance</b> (a valued benefit contract, since human life cannot be measured by replacement cost minus depreciation).

• <b>4. Principle of Subrogation (Corollary of Indemnity):</b>
  - <i>Concept:</i> Substitution of the insurer in place of the insured for the purpose of claiming indemnity from a negligent third party for a loss covered by insurance. Once the insurer pays the insured's claim, the insurer steps into the legal shoes of the insured and can sue the negligent tortfeasor to recover the amount paid.
  - <i>Key Rules:</i> (i) Applies only to property and liability contracts of indemnity (<b>never applies to Life Insurance</b>), (ii) The insurer is entitled to recover only up to the amount it paid out to the insured, and (iii) The insured cannot impair the insurer's subrogation rights by releasing the negligent party.

• <b>5. Principle of Contribution (Other-Insurance Provision / Corollary of Indemnity):</b>
  - <i>Concept:</i> Applies when two or more property/liability policies cover the <b>same insurable interest, same subject matter, and same peril</b> at the same time (Double Insurance). To prevent the insured from collecting more than 100% of the actual loss, each insurer contributes proportionately:
  - <b>Pro-Rata Contribution Formula:</b>
    <b>Insurer A's Share = Actual Loss x [ Policy A Limit / Sum of All Policies' Limits ]</b>.

• <b>6. Principle of Proximate Cause (Causa Proxima):</b>
  - <i>Concept:</i> Proximate cause is the active, efficient cause that sets in motion an unbroken chain of events which brings about a result, without the intervention of any new and independent force. For a claim to be payable, the proximate cause of the loss must be an <b>insured peril</b>.""")

    add_topic(story, "4.2 Requirements, Distinct Legal Characteristics, Agency Law, Basic Parts & Policy Provisions")
    add_body(story, """<b>1. Four Legal Requirements of a Valid Insurance Contract:</b>
  (1) <b>Offer and Acceptance</b> (applicant submits proposal + first premium; insurer accepts/issues binder), (2) <b>Consideration</b> (insured pays premium + complies with conditions; insurer promises to indemnify), (3) <b>Competent Parties</b> (legal age, sound mind, licensed insurer), and (4) <b>Legal Purpose</b> (must have insurable interest; not a wagering contract).

<b>2. Five Distinct Legal Characteristics of Insurance Contracts:</b>
  (1) <b>Aleatory Contract</b> (unequal dollar exchange depending on an uncertain event), (2) <b>Unilateral Contract</b> (only the insurer makes an enforceable legal promise after premium payment), (3) <b>Conditional Contract</b> (insurer's duty to pay depends on fulfilling policy conditions), (4) <b>Personal Contract</b> (in property insurance, insures the owner—cannot be assigned without insurer consent), and (5) <b>Contract of Adhesion</b> (drafted by the insurer; any ambiguity is construed in favor of the insured).

<b>3. Law and the Insurance Agent (Role of Insurance Agent):</b>
  An insurance agent is the legal representative of the principal (insurer) acting under Express, Implied, and Apparent authority. Under agency law: (i) Knowledge of the agent is imputed to the insurer, (ii) The agent performs field underwriting ("eyes and ears of the insurer"), educates clients, collects premiums, services policies, and assists families during claim settlement.

<b>4. Basic Parts of an Insurance Policy (D-I-C-E) & Key Provisions (Endorsements, Deductibles, Coinsurance):</b>
• <b>Four Basic Parts:</b> <b>(1) Declarations</b> (identity of insured, property description, policy period, sum insured, premium), <b>(2) Insuring Agreement</b> (<i>Named-Perils</i> vs. <i>Open-Perils / All-Risk</i> coverage), <b>(3) Exclusions</b>, and <b>(4) Conditions</b>.
• <b>Endorsements vs. Riders:</b> Written provisions that add, delete, or modify coverage in the standard policy (called <b>Endorsements</b> in Property/Casualty insurance and <b>Riders</b> in Life/Health insurance).
• <b>Deductibles (Straight, Aggregate, Waiting-Period):</b> Provision by which a specified amount is subtracted from the loss payment otherwise payable to the insured—eliminates small administrative claims, lowers premiums, and reduces moral/attitudinal hazard.
• <b>Coinsurance (Condition of Average in Commercial Property Insurance) — Numerical Formula:</b>
  Requires the insured to insure property for at least a stated percentage (e.g., 80% or 100%) of its true insurable value at the time of loss:
  <b>Amount of Recovery = Actual Loss x [ Amount of Insurance Carried / Amount of Insurance Required ]</b>  (never exceeding the policy face limit or actual loss).""")

    add_example(story, """<b>Worked Numerical Example on Coinsurance & Contribution:</b>
• <b>Coinsurance Example:</b> A commercial building has a Replacement Cost (True Value) of Rs 10,000,000 and an 80% coinsurance clause (so Insurance Required = 80% x 10M = Rs 8,000,000). The owner carries only Rs 6,000,000 of fire insurance. If a fire causes a Rs 2,000,000 loss:
  <b>Claim Paid = Rs 2,000,000 x (6,000,000 / 8,000,000) = Rs 1,500,000</b> (the owner bears the remaining Rs 500,000 as a coinsurance penalty!).
• <b>Pro-Rata Contribution Example:</b> A warehouse is insured against fire with Insurer A for Rs 3,000,000 and Insurer B for Rs 2,000,000 (Total Insurance = Rs 5,000,000). A fire causes an actual loss of Rs 1,000,000:
  - <b>Insurer A pays:</b> 1,000,000 x (3,000,000 / 5,000,000) = <b>Rs 600,000</b>
  - <b>Insurer B pays:</b> 1,000,000 x (2,000,000 / 5,000,000) = <b>Rs 400,000</b> (Total = Rs 1,000,000).""")

    story.append(PageBreak())
