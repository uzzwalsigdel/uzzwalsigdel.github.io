from generate_pdf import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def build_paper2(story):
    story.append(Paragraph(
        "PAPER 2: TRIBHUVAN UNIVERSITY — BNK 209: INSURANCE AND RISK MANAGEMENT<br/>"
        "<font size=10>BBA / Eighth Semester | Model Question 2026 | Full Marks: 100 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group - A: Brief Answer Questions (Attempt ALL Questions) [10 × 2 = 20]", group_header_style))

    add_q(story, "Q1. Define risk, peril and hazard.")
    add_a(story, """<b>Answer:</b>
• <b>Risk:</b> Uncertainty concerning the occurrence of a financial loss (or variation between actual and expected outcomes).
• <b>Peril:</b> The direct, immediate cause of a loss (such as fire, earthquake, flood, theft, or auto collision).
• <b>Hazard:</b> A condition that creates or increases the frequency or severity of a loss arising from a given peril (classified into Physical hazard, Moral hazard, Attitudinal/Morale hazard, and Legal hazard).""")

    add_q(story, "Q2. What do you mean by systemic risk?")
    add_a(story, """<b>Answer:</b> Systemic risk is the risk of collapse of an entire financial system or entire market, as opposed to risk associated with any one individual entity, group, or component of a system. Because of financial interlinkages, the failure of a single large bank or financial institution can trigger a domino (cascade) effect that destabilizes the entire economy.""")

    add_q(story, "Q3. List out the objectives of risk management.")
    add_a(story, """<b>Answer:</b> Risk management objectives are divided into two categories:
• <b>Pre-Loss Objectives:</b> (1) Economy (preparing for potential losses in the most cost-effective way), (2) Reduction of anxiety and fear, and (3) Meeting legal and regulatory obligations.
• <b>Post-Loss Objectives:</b> (1) Survival of the firm, (2) Continuity of operations, (3) Stability of earnings, (4) Continued growth of the firm, and (5) Social responsibility toward employees, customers, and society.""")

    add_q(story, "Q4. Define risk pooling.")
    add_a(story, """<b>Answer:</b> Risk pooling (or loss sharing) is the spreading of losses incurred by a few individuals over the entire group of exposure units, so that in the process, average loss is substituted for actual loss. Through risk pooling and the Law of Large Numbers, insurers combine a large number of independent, homogeneous exposure units to make aggregate future losses accurately predictable.""")

    add_q(story, "Q5. Define insurance and list down its basic characteristics.")
    add_a(story, """<b>Answer:</b> Insurance is a financial arrangement and legal contract that redistributes the cost of unexpected losses by transferring pure risk from an insured individual or entity to an insurer in exchange for a known consideration called a premium.
<b>Basic Characteristics of Insurance:</b>
• 1. Pooling of losses (sharing losses across a large group)
• 2. Payment of fortuitous (accidental and unintentional) losses
• 3. Risk transfer from the insured to the insurer
• 4. Indemnification (restoring the insured to their pre-loss financial position)""")

    add_q(story, "Q6. Differentiate life insurance and non-life insurance.")
    add_a(story, """<b>Answer:</b>
• <b>1. Nature of Contract:</b> Life insurance is a <i>valued (benefit) contract</i> (not strictly a contract of indemnity, as human life cannot be measured exactly in money), whereas non-life (general) insurance is strictly a <i>contract of indemnity</i>.
• <b>2. Duration & Certainty of Event:</b> Life insurance is typically a long-term contract where the event (death) is certain (only timing is uncertain) and often includes a savings/investment element; non-life insurance is a short-term (usually 1-year) contract covering uncertain perils (like fire, marine, or motor accidents) with no savings element.""")

    add_q(story, "Q7. Define loss forecasting. List out the common techniques of loss forecasting.")
    add_a(story, """<b>Answer:</b> Loss forecasting is the quantitative process used by risk managers to predict the frequency (how often) and severity (dollar size) of future losses that an organization may experience over an upcoming period.
<b>Common Techniques of Loss Forecasting:</b>
• 1. <b>Probability Analysis</b> (using historical frequency and severity probability distributions)
• 2. <b>Regression Analysis</b> (predicting losses using causal independent variables such as payroll, sales, or vehicle miles)
• 3. <b>Forecasting Based on Loss Distributions</b> (such as Poisson distribution for frequency and Lognormal distribution for severity / Monte Carlo simulation).""")

    add_q(story, "Q8. How does Risk Management Information System help in risk management?")
    add_a(story, """<b>Answer:</b> A Risk Management Information System (RMIS) is a computerized database and software system that collects, stores, and analyzes risk, exposure, policy, and claims data. It helps risk management by automating loss tracking, identifying loss trends and high-risk locations, forecasting future claims accurately, monitoring insurance policy limits and renewals, and generating management reports for better risk-control and retention decisions.""")

    add_q(story, "Q9. What are the tax benefits and payout taxes for life insurance in Nepal?")
    add_a(story, """<b>Answer:</b> Under the Income Tax Act 2058 (2002) of Nepal:
• <b>Tax Benefit on Premium Paid:</b> A resident natural person can claim a tax deduction from their taxable income for annual life insurance premiums paid up to <b>Rs 40,000</b> (or the actual annual premium paid, whichever is lower).
• <b>Payout Taxes (Maturity / Death Claim):</b> Death benefit payouts received by beneficiaries are completely exempt from income tax. For maturity/investment payouts on life insurance policies issued by resident insurers, a final withholding tax of <b>5%</b> is levied on the net investment gain (payout minus cumulative premiums paid).""")

    add_q(story, "Q10. Define third-party liability insurance in terms of auto (motor) insurance.")
    add_a(story, """<b>Answer:</b> Third-party liability insurance in auto (motor) insurance is a legally mandatory insurance coverage under which the insurer agrees to pay compensation for bodily injury, permanent disability, death, or property damage caused by the insured's vehicle (the first party) to another person or their property (the third party). It does not cover damage to the insured's own vehicle.""")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group - B: Descriptive Answer Questions (Attempt any SIX — ALL Solved) [6 × 5 = 30]", group_header_style))

    add_q(story, "Q11. Differentiate between insurance and gambling.")
    add_a(story, """<b>Answer:</b> Although both insurance and gambling involve uncertainty and money changing hands contingent on a future event, they are fundamentally opposite in purpose and effect:""")
    t_b11 = make_table([
        [P_hdr("Basis of Difference"), P_hdr("Insurance"), P_hdr("Gambling")],
        [P("1. Creation vs. Transfer of Risk", True), P("Handles an <b>existing pure risk</b> by transferring it to an insurer."), P("Creates a <b>new speculative risk</b> that did not exist before the bet.")],
        [P("2. Type of Risk Involved", True), P("Deals strictly with <b>pure risk</b> (only chance of loss or no loss)."), P("Deals with <b>speculative risk</b> (chance of financial gain or loss).")],
        [P("3. Social & Economic Utility", True), P("Socially productive; reduces anxiety, protects families/businesses, and stabilizes the economy."), P("Socially unproductive; merely redistributes wealth from losers to winners without restoring losses.")],
        [P("4. Insurable Interest", True), P("Requires strict legal <b>insurable interest</b> in the subject matter."), P("No insurable interest is required beyond the bet itself.")],
        [P("5. Principle of Indemnity", True), P("Restores the insured to their pre-loss financial position (never meant for profit)."), P("Both parties seek to make a profit at the other's expense.")],
    ], col_widths=[115, 192, 193])
    story.append(t_b11)
    story.append(Spacer(1, 6))

    add_q(story, "Q12. Explain the concept and significance of law of large number in risk pooling?")
    add_a(story, """<b>Answer:</b>
<b>Concept of the Law of Large Numbers:</b>
The Law of Large Numbers is a fundamental mathematical principle of probability which states that as the number of independent and homogeneous (similar) exposure units increases, the actual observed loss experience will increasingly approach the expected (true underlying probability) loss experience.

<b>Significance of the Law of Large Numbers in Risk Pooling:</b>
• <b>1. Reduction of Objective Risk:</b> For an insurer, objective risk is the relative variation of actual loss from expected loss. As the pool size (N) increases, standard deviation of average loss decreases by a factor of √N, reducing the insurer's objective risk toward zero.
• <b>2. Accurate Actuarial Rate Making (Premium Calculation):</b> Because aggregate losses become highly predictable in a large pool, actuaries can charge a fair, stable pure premium equal to the expected average loss plus a small loading for expenses and contingencies.
• <b>3. Substitution of Average Loss for Actual Loss:</b> Each policyholder replaces an unpredictable, potentially catastrophic actual loss with a small, predictable average premium cost.
• <b>4. Financial Solvency and Lower Capital Reserves:</b> When actual claims closely match expected claims, the insurance company needs smaller safety capital buffers per policy and remains financially solvent.""")

    add_q(story, "Q13. Define adverse selection. Explain the tools used by insurance companies to control the chance of adverse selection.")
    add_a(story, """<b>Answer:</b>
<b>Definition of Adverse Selection:</b>
Adverse selection (anti-selection) is the tendency of individuals or businesses with a higher-than-average probability of loss to seek insurance coverage (or buy larger policy limits) at standard (average) premium rates more aggressively than low-risk individuals. It arises from asymmetric information—where the applicant knows more about their own health, habits, or risk level than the insurer. Left unchecked, adverse selection forces insurers to raise premiums, driving out healthy/low-risk insureds and creating a "death spiral."

<b>Tools Used by Insurance Companies to Control Adverse Selection:</b>
• <b>1. Strict Underwriting and Risk Classification:</b> Selecting and classifying applicants into homogeneous rating classes (preferred, standard, substandard, or declined) based on age, occupation, health history, medical exams, driving records, and safety inspections so each group pays a rate commensurate with its risk.
• <b>2. Waiting Periods and Pre-Existing Condition Exclusions:</b> Imposing a waiting period (e.g., 30 days to 2 years in health insurance) or excluding pre-existing illnesses and suicide within the first 1–2 years so people cannot buy insurance only after falling sick.
• <b>3. Policy Provisions (Deductibles, Coinsurance, and Policy Limits):</b> Requiring the insured to bear an initial deductible or coinsurance percentage discourages high-risk applicants from exploiting full coverage.
• <b>4. Group Insurance Underwriting:</b> Insuring an entire employer group automatically (where insurance is incidental to employment) prevents individuals from self-selecting into the pool solely due to poor health.
• <b>5. Application Warranties and Utmost Good Faith Enforcement:</b> Voiding policies if the applicant conceals or misrepresents material facts on the proposal form.""")

    add_q(story, "Q14. Explain about premature death. Also explain its financial implications.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Premature Death:</b>
In risk management and insurance, premature death is defined as the death of a family head or breadwinner with unfulfilled financial obligations—such as dependent spouse and children to support, an unpaid home mortgage or business loan, or unfunded children's college education.

<b>Financial Implications (Costs) of Premature Death:</b>
• <b>1. Loss of Human Life Value (Future Earned Income):</b> The family permanently loses its share of the deceased breadwinner's future net earning capacity, creating an immediate deficit between ongoing family living expenses and surviving income.
• <b>2. Immediate Lump-Sum Cash Expenses (Clearance Fund Needs):</b> High funeral and burial expenses, uninsured final medical/hospital bills, estate settlement costs, probate legal fees, and unpaid taxes or debts.
• <b>3. Debt and Mortgage Foreclosure Risk:</b> Without the breadwinner's income, the family may default on home mortgages, auto loans, or business loans, risking loss of the family home.
• <b>4. Reduction in Standard of Living and Educational Disruption:</b> Surviving dependents may be forced to relocate, liquidate savings at a loss, or abandon higher education plans for children.
• <b>5. Additional Household & Childcare Expenses:</b> If the deceased parent also performed childcare and household management, the surviving spouse incurs extra costs to replace those services.
• <b>6. Non-Economic (Emotional) Grief:</b> Severe psychological trauma and loss of parental guidance for surviving family members.""")

    add_q(story, "Q15. Mr. Suman Thapa, aged 40, is married and has two children. He earns Rs.600,000 annually and plans to retire at age 60. Of this amount, Rs.30,000 is used for taxes, life and health insurance, and his personal needs. The remaining amount is used to support his family. Using a discount rate of 6 percent, calculate the human life value of Mr. Shrestha. Note that the present value of Re.1 received annually for 20 years at 6% is Rs.11.4699.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current age = 40 years; Planned retirement age = 60 years
• Remaining working life (n) = 60 - 40 = <b>20 years</b>
• Average annual gross earnings = Rs 600,000
• Annual taxes, insurance premiums, and personal self-maintenance expenses = Rs 30,000
• Discount rate (i) = 6%
• Present Value Interest Factor of Annuity, PVIFA(6%, 20 years) = 11.4699

<b>Step 1: Calculate Net Annual Income Contribution to Family:</b>
Net Annual Family Share = Annual Gross Earnings - Personal Expenses, Taxes & Insurance
Net Annual Family Share = Rs 600,000 - Rs 30,000 = <b>Rs 570,000 per year</b>

<b>Step 2: Calculate Human Life Value (HLV):</b>
Human Life Value (HLV) = Net Annual Family Share × PVIFA(6%, 20 years)
HLV = Rs 570,000 × 11.4699 = <b>Rs 6,537,843</b>

<b>Conclusion:</b> The Human Life Value (HLV) of Mr. Suman Thapa (Shrestha) is <b>Rs 6,537,843</b>.""")
    add_hint(story, "Human Life Value (HLV) 3-Step Formula: (1) Working years n = Retirement Age - Current Age; (2) Family's Annual Share = Annual Income - (Taxes + Personal Consumption + Insurance Premiums); (3) HLV = Family's Annual Share × PVIFA(r%, n years).")

    add_q(story, "Q16. Explain the third-party liability insurance in terms of auto (motor) insurance.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Third-Party Liability in Motor Insurance:</b>
In motor insurance, there are three parties:
1. <b>First Party:</b> The insured (vehicle owner/policyholder).
2. <b>Second Party:</b> The insurance company (insurer).
3. <b>Third Party:</b> Any other person (pedestrians, passengers in other vehicles, or owners of damaged third-party property) who suffers injury, death, or property damage due to an accident involving the insured vehicle.

<b>Key Features and Importance of Third-Party Motor Liability Insurance:</b>
• <b>1. Statutory (Compulsory) Requirement:</b> In almost all countries, including Nepal (under the Motor Vehicles and Transport Management Act 2049), no motor vehicle may be driven on public roads without valid third-party liability insurance.
• <b>2. Coverage Provided:</b>
  - <i>Bodily Injury and Death:</i> Covers medical treatment expenses, permanent disability compensation, and accidental death benefits for third-party victims (e.g., statutory limits prescribed by Nepal Insurance Authority).
  - <i>Third-Party Property Damage (TPPD):</i> Covers repair or replacement costs of damaged third-party vehicles, buildings, or public infrastructure up to policy limits.
  - <i>Legal Defense Costs:</i> Pays legal fees and court expenses incurred with the insurer's consent in defending liability claims.
• <b>3. Exclusions:</b> It does <b>not</b> cover damage to the insured's own vehicle (Own Damage requires a Comprehensive Motor Policy), nor does it cover accidents occurring while driving without a valid license or under the influence of alcohol/drugs.
• <b>4. Social Protection Objective:</b> Ensures that innocent road accident victims and their families receive prompt financial compensation even if the vehicle owner or driver is personally insolvent.""")

    add_q(story, "Q17. Explain social insurance with few examples.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Social Insurance:</b>
Social insurance consists of government-mandated, compulsory insurance programs designed to provide a basic floor of income security and financial protection to workers and their families against major economic insecurities such as old age, disability, work-related injury, maternity, sickness, and unemployment. It is financed primarily through earmarked payroll contributions from employers and employees (and sometimes government subsidies) rather than private individual underwriting.

<b>Key Characteristics of Social Insurance:</b>
• Compulsory participation by law
• Financed by statutory contributions from employers and employees
• Benefits are prescribed by statute and emphasize social adequacy (helping lower-income workers proportionately more) rather than strict individual equity
• Administered or supervised by a public agency (such as the Social Security Fund).

<b>Examples of Social Insurance:</b>
• <b>1. Contribution-Based Social Security Fund (SSF) in Nepal:</b> Administered under the Contribution-Based Social Security Act 2074, where employers contribute 20% and employees contribute 11% (total 31% of basic salary) covering four schemes:
  - <i>Medical Treatment, Health, and Maternity Protection Scheme</i>
  - <i>Accident and Disability Protection Scheme</i>
  - <i>Dependent Family Protection Scheme</i>
  - <i>Old-Age Protection (Pension and Gratuity) Scheme</i>
• <b>2. Workers' Compensation Insurance:</b> Provides medical care and wage replacement to employees injured on the job.
• <b>3. Unemployment Insurance:</b> Provides temporary cash benefits to workers who involuntarily lose their jobs (e.g., US OASDI/UI programs).""")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group - C: Analytical Answer Questions (Attempt any THREE — ALL Solved) [3 × 10 = 30]", group_header_style))

    add_q(story, "Q18. Explain the concept and process of risk management.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Risk Management:</b>
Risk management is a systematic, scientific process of identifying, analyzing, and evaluating pure (and enterprise) loss exposures faced by an organization or individual, and selecting and monitoring the most appropriate techniques for treating such exposures so that organizational objectives can be achieved at minimum total cost of risk.

<b>Step-by-Step Process of Risk Management:</b>
• <b>Step 1: Determination of Objectives:</b> Establish clear pre-loss objectives (economy, anxiety reduction, legal compliance) and post-loss objectives (survival, continuity of operations, earnings stability, growth).
• <b>Step 2: Identification of Risk (Loss Exposures):</b> Systematically identify all potential pure loss exposures (property, liability, business interruption, human resources, cyber/crime) using tools such as risk questionnaires, physical inspections, flowcharts, financial statement analysis, and historical loss data.
• <b>Step 3: Evaluation and Measurement of Risk:</b> Estimate the <b>loss frequency</b> (probability of occurrence in a given period) and <b>loss severity</b> (probable maximum loss and average loss size) for each identified exposure, ranking risks on a Risk Matrix (Low/High Frequency vs. Low/High Severity).
• <b>Step 4: Consideration and Selection of Risk Treatment Techniques:</b> Choose the optimal combination of:
  1. <b>Risk Control Techniques (reduce frequency/severity):</b>
     - <i>Avoidance:</i> Refusing to engage in the high-risk activity.
     - <i>Loss Prevention:</i> Measures that reduce loss frequency (e.g., safety training, firewall, driver training).
     - <i>Loss Reduction:</i> Measures that reduce loss severity after a peril occurs (e.g., fire sprinklers, data backups, separation/duplication of exposures).
  2. <b>Risk Financing Techniques (pay for losses that occur):</b>
     - <i>Retention (Active or Passive):</i> Self-insuring or absorbing High-Frequency / Low-Severity losses through deductibles, reserves, or captive insurers.
     - <i>Non-Insurance Transfer:</i> Shifting risk via hold-harmless clauses, leases, hedging, or outsourcing.
     - <i>Commercial Insurance:</i> Transferring Low-Frequency / High-Severity catastrophic risks to an insurer.
• <b>Step 5: Implementation of the Risk Management Program:</b> Draft a risk management policy statement, purchase required insurance coverages, install safety systems, and train personnel.
• <b>Step 6: Regular Review and Monitoring:</b> Periodically audit loss records, review changing business operations, and update risk control and insurance limits.""")

    add_q(story, "Q19. Explain the fundamental legal principles of insurance contract.")
    add_a(story, """<b>Answer:</b> Insurance contracts are governed by six fundamental legal principles that prevent moral hazard, wagering, and unjust enrichment:

• <b>1. Principle of Utmost Good Faith (Uberrimae Fidei):</b>
  Unlike ordinary commercial contracts (which follow <i>caveat emptor</i> or "let the buyer beware"), insurance contracts require both the applicant and the insurer to maintain a higher standard of honesty. They must voluntarily disclose all material facts affecting the risk through the legal doctrines of <b>Representations</b> (statements made by the applicant), <b>Concealment</b> (intentional withholding of a material fact), and <b>Warranties</b> (strict conditions in the policy).
• <b>2. Principle of Insurable Interest:</b>
  The insured must stand in a legally recognized financial relationship to the subject matter of insurance such that they will suffer a direct pecuniary (financial) loss if the insured event occurs and benefit from its safety.
  - In <i>Life Insurance</i>, insurable interest must exist at the <b>inception</b> of the policy.
  - In <i>Property/Non-Life Insurance</i>, insurable interest must exist at the <b>time of loss</b> (and generally at inception).
  This prevents gambling and reduces moral hazard (murder or arson for insurance money).
• <b>3. Principle of Indemnity:</b>
  The insurer agrees to pay no more than the actual financial loss suffered by the insured, restoring them to the same financial position they occupied immediately before the loss—preventing the insured from profiting from a loss. Indemnity is measured via Actual Cash Value (Replacement Cost minus Depreciation). <i>(Exceptions: Life insurance, valued policies, and replacement cost policies.)</i>
• <b>4. Principle of Subrogation (Corollary of Indemnity):</b>
  Once the insurer indemnifies the insured for a covered loss caused by a negligent third party, the insurer steps into the legal shoes of the insured and acquires the right to recover the claim amount from the negligent third party. This prevents the insured from collecting twice for the same loss and holds negligent tortfeasors accountable.
• <b>5. Principle of Contribution (Corollary of Indemnity):</b>
  If an insured holds two or more property/liability policies covering the same subject matter and same peril (double insurance), they cannot recover more than the total actual loss. Each insurer contributes proportionately (pro-rata) to the loss.
• <b>6. Principle of Proximate Cause (Causa Proxima):</b>
  For a claim to be payable, the active, efficient cause that sets in motion an unbroken chain of events leading to the loss must be an <b>insured peril</b> (and not an excluded peril).""")

    add_q(story, "Q20. Explain about agriculture insurance. Why do you think agriculture insurance is important for countries like Nepal?")
    add_a(story, """<b>Answer:</b>
<b>Concept of Agriculture Insurance:</b>
Agriculture insurance is a specialized class of property insurance purchased by farmers and agricultural producers to protect against the financial loss of their crops, livestock, poultry, aquaculture (fish), or medicinal herbs due to natural perils (hail, drought, flood, frost, landslide, windstorm) or biological perils (pests, plant diseases, livestock epidemics, and accidental mortality). It includes indemnity-based Multi-Peril Crop Insurance (MPCI), Livestock Insurance, and Weather Index-Based Insurance.

<b>Why Agriculture Insurance is Crucial for Countries Like Nepal:</b>
• <b>1. High Dependence on Agriculture for Livelihood and GDP:</b> Over 60% of Nepal's population depends on agriculture for employment, and agriculture contributes roughly one-fourth of Nepal's GDP. Protecting farmers stabilizes the entire rural economy.
• <b>2. Extreme Vulnerability to Climate Change and Geographic Hazards:</b> Nepal's fragile topography (mountains, hills, and Terai plains) exposes farmers to erratic monsoons, flash floods, landslides, droughts, hailstorms, and diseases like lumpy skin disease in cattle or fall armyworm in maize.
• <b>3. Income Stabilization and Poverty Prevention:</b> Smallholder and subsistence farmers operate on razor-thin margins; a single crop failure or death of a dairy buffalo can push a rural family into severe debt and poverty. Insurance provides timely compensation to restart production.
• <b>4. Facilitating Access to Agricultural Credit (Collateral Substitute):</b> Banks and microfinance institutions are reluctant to lend to farmers due to high default risk after crop failures. With an agriculture insurance policy backing the crop/livestock, banks readily extend priority-sector agricultural loans.
• <b>5. Encouraging Commercialization and Modern Farming Investments:</b> When catastrophic downside risk is transferred to insurers (supported by the Government of Nepal's 80% premium subsidy on crop and livestock insurance), youth and agri-entrepreneurs are encouraged to invest in commercial farming, high-yield seeds, and modern technology.""")

    add_q(story, "Q21. Insurance is one of the heavily regulated area of the overall financial system. In light of this statement, explain the reasons for insurance regulations.")
    add_a(story, """<b>Answer:</b>
The insurance industry (regulated in Nepal by the <b>Nepal Insurance Authority / Beema Pradhikaran</b> under the Insurance Act 2079) is one of the most heavily regulated sectors of the financial system because insurance involves an inverted production cycle—customers pay premiums upfront in exchange for an intangible promise of future payment that may occur years or decades later.

<b>Major Reasons for Insurance Regulation:</b>
• <b>1. Maintain Insurer Solvency (Protect Financial Stability):</b>
  If an insurance company goes bankrupt after collecting premiums for decades, millions of policyholders, widows, and injured victims are left unprotected. Regulators enforce minimum paid-up capital, risk-based solvency margins, technical reserves, reinsurance mandates, and investment guidelines.
• <b>2. Compensate for Inadequate Consumer Knowledge (Information Asymmetry):</b>
  Insurance policies are complex legal contracts of adhesion written in technical language. Ordinary citizens cannot easily evaluate policy exclusions or an insurer's financial health, so regulators approve policy wordings and license agents/surveyors.
• <b>3. Ensure Reasonable, Adequate, and Non-Discriminatory Rates:</b>
  - <i>Adequate:</i> Rates must be high enough to avoid cut-throat price wars that cause insurer insolvency.
  - <i>Not Excessive:</i> Rates must not allow monopoly price-gouging of consumers.
  - <i>Not Unfairly Discriminatory:</i> Exposures with similar risk profiles must be charged equitable premiums.
• <b>4. Make Insurance Available and Accessible (Social Goals):</b>
  Regulators promote financial inclusion by mandating micro-insurance quotas, rural branch expansion, agriculture insurance schemes, and compulsory third-party motor pools.
• <b>5. Prevent Unfair Market Practices and Ensure Prompt Claim Settlement:</b>
  Regulators protect policyholders against misleading sales tactics, rebating, churning, and unreasonable delays or denials in settling legitimate insurance claims.""")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group - D: Comprehensive Answer Questions / Case Study [4 × 5 = 20]", group_header_style))

    add_q(story, "Q22. Case Study: Aarav Sharma & Everest Tech Solutions\nAarav Sharma (42, primary breadwinner with spouse and two children, stock investor/trader) quit his job to start Everest Tech Solutions (digital transformation consultancy with 5 employees, leased office, expensive servers/laptops, home & car mortgage).\na) Identify all the pure risks and speculative risks faced by Aarav or his organization.\nb) Which type of life insurance policy do you suggest to Aarav? Justify your answer. What additional benefits could be added to the policy to enhance the coverage?\nc) How can a Professional Liability Insurance protect Everest Tech Solutions?\nd) Why do you think is the decision to provide Group Health Insurance for the staffs considered a risk management tool, rather than just an additional expense to the organization?")
    add_a(story, """<b>Answer (Comprehensive Case Study Solution):</b>

<b>a) Identification of Pure Risks and Speculative Risks Faced by Aarav and Everest Tech Solutions:</b>
• <b>Pure Risks (Only chance of loss or no loss; insurable):</b>
  1. <i>Personal / Human Resource Pure Risks:</i> Premature death of Aarav (leaving family without income to pay living costs, children's education, and home/car mortgages); permanent total disability due to an accident; diagnosis of a critical illness; illness or medical emergencies of his five employees.
  2. <i>Property Pure Risks:</i> Destruction or damage to office servers, high-end laptops, furniture, and electronics from fire, lightning, earthquakes, or floods.
  3. <i>Liability & Business Interruption Pure Risks:</i> Client data breach caused by employee configuration error; legal liability lawsuits from clients for negligence, errors, and omissions; business interruption (loss of revenue during downtime after a fire, disaster, or cyber incident).
• <b>Speculative Risks (Chance of both financial gain/profit or loss; handled via hedging/diversification):</b>
  1. <i>Stock Market Investment & Trading Risk:</i> Price fluctuations in Aarav's stock investments and trading portfolio (can yield capital gains or losses).
  2. <i>Entrepreneurial / Startup Business Venture Risk:</i> Investing his personal savings into Everest Tech Solutions—the consultancy could succeed and earn high profits or fail due to market competition and lack of clients.

<b>b) Recommended Life Insurance Policy, Justification, and Riders (Additional Benefits):</b>
• <b>Recommended Policy:</b> A <b>Term Life Insurance Policy</b> (or a combination of a high-coverage Term Life Policy plus an Endowment/Whole Life base policy) matching the duration of his mortgage and children's education dependency (e.g., 20-year Term up to age 62).
• <b>Justification:</b> Since Aarav has just invested a large portion of his personal savings into his startup and carries heavy financial obligations (family living expenses, two children's education, and house/car mortgages), Term Life Insurance provides the <b>maximum lump-sum death benefit protection at the lowest possible premium</b>, preserving his cash flow for his growing business.
• <b>Additional Benefits (Riders) to Enhance Coverage:</b>
  1. <i>Permanent Total Disability (PTD) & Accidental Death and Dismemberment (AD&D) Rider:</i> Provides lump-sum/income replacement if an accident leaves him permanently disabled.
  2. <i>Critical Illness (CI) Rider:</i> Pays an immediate lump sum upon diagnosis of major illnesses (such as cancer, heart attack, stroke, or kidney failure) to cover treatment and lost income.
  3. <i>Waiver of Premium Rider:</i> Waives all future life insurance premiums if Aarav becomes permanently disabled so the policy never lapses.

<b>c) How Professional Liability Insurance (Errors & Omissions / Cyber Liability) Protects Everest Tech Solutions:</b>
• <b>1. Coverage for Negligence and Configuration Errors:</b> Protects the firm when a client suffers financial harm due to a software bug, server misconfiguration, data breach, or professional oversight committed by Aarav or his five employees.
• <b>2. Legal Defense Costs:</b> Pays expensive attorney fees, court costs, and expert witness fees required to defend the consultancy in court, even if a client's lawsuit turns out to be groundless.
• <b>3. Settlements and Court Judgments:</b> Pays the compensatory damages awarded to the client up to policy limits, preventing a single data-breach lawsuit from bankrupting the startup and wiping out Aarav's personal savings.
• <b>4. Client Trust and Contractual Compliance:</b> Financial institution clients typically require IT consultants to carry Professional Indemnity / Cyber Liability insurance before awarding transformation contracts.

<b>d) Why Group Health Insurance for Staff is a Strategic Risk Management Tool Rather Than Just an Expense:</b>
• <b>1. Mitigating Human Resource Risk (Key-Person Turnover & Absenteeism):</b> In a small 5-person IT consultancy, every employee is critical. Access to prompt, quality medical care ensures sick employees recover quickly, reducing prolonged absenteeism and project delays.
• <b>2. Employee Retention and Talent Attraction:</b> Startups compete with larger firms for skilled tech talent; offering group health insurance builds loyalty and prevents costly employee turnover and recruitment disruptions.
• <b>3. Productivity and Morale Enhancement:</b> Employees who are free from anxiety over family medical bills stay focused and productive, reducing workplace errors (attitudinal hazard).
• <b>4. Cost Efficiency and Tax Deductibility:</b> Group insurance provides broad coverage (often without individual medical underwriting) at much lower per-capita rates than individual policies, and premiums paid by the company are tax-deductible business expenses.""")

    story.append(PageBreak())
