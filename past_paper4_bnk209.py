from past_pdf_base import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def build_past_paper4(story):
    story.append(Paragraph(
        "PAPER 4: TRIBHUVAN UNIVERSITY — BNK 209: INSURANCE AND RISK MANAGEMENT<br/>"
        "<font size=10>BBA / Eighth Semester | April 2026 | Full Marks: 100 | Pass Marks: 50 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group 'A': Brief Answer Questions [10 x 2 = 20]", group_header_style))

    add_q(story, "Q1. Define the term insurance.")
    add_a(story, """<b>Answer:</b> Insurance is an economic device and legal contract whereby an individual or organization (the insured) transfers the financial burden of pure, fortuitous risks to an insurance company (the insurer) in exchange for a fixed consideration called a premium, through which the losses of the unfortunate few are pooled and shared among the many exposed to the same peril.""")

    add_q(story, "Q2. What do you mean by enterprise risk?")
    add_a(story, """<b>Answer:</b> Enterprise risk is a comprehensive concept that encompasses all major risks faced by an organization across its entire operations—combining <b>Pure Risks</b> (property, liability, personnel), <b>Speculative Financial Risks</b> (market, credit, interest rate, foreign exchange, liquidity), <b>Operational Risks</b> (supply chain, IT/cyber failure, fraud), and <b>Strategic Risks</b> (reputation, competition, regulatory shifts)—managed holistically under Enterprise Risk Management (ERM).""")

    add_q(story, "Q3. State any two reasons for regulating insurance company by NIA.")
    add_a(story, """<b>Answer:</b> Two primary reasons why the <b>Nepal Insurance Authority (NIA / Beema Pradhikaran)</b> regulates insurance companies are:
• <b>1. Protection of Policyholders & Maintaining Insurer Solvency:</b> Ensuring insurers maintain adequate paid-up capital, solvency margins, and technical reserves so they can pay future claims.
• <b>2. Ensuring Fair Rates and Prompt Claim Settlement:</b> Preventing excessive or discriminatory premium pricing and protecting consumers against unfair claim denials or delays.""")

    add_q(story, "Q4. Define loss forecasting and list out the common techniques of loss forecasting.")
    add_a(story, """<b>Answer:</b> Loss forecasting is the analytical process used by risk managers to estimate the expected frequency (number of occurrences) and severity (Rupee size) of future losses over an upcoming planning period.
<b>Common Techniques of Loss Forecasting:</b>
• <b>1. Probability Analysis</b> (using historical frequency and severity probability distributions)
• <b>2. Regression Analysis</b> (correlating losses with physical drivers like payroll, revenue, or fleet mileage)
• <b>3. Forecasting Based on Loss Distributions</b> (e.g., Poisson and Lognormal distributions).""")

    add_q(story, "Q5. Write the meaning of risk pooling.")
    add_a(story, """<b>Answer:</b> Risk pooling (loss sharing) is the spreading of unexpected losses incurred by a few individuals over a large group of homogeneous exposure units so that, in the process, <b>average loss is substituted for actual loss</b>. By applying the Law of Large Numbers, risk pooling reduces objective risk for the insurer.""")

    add_q(story, "Q6. State the meaning of third party insurance.")
    add_a(story, """<b>Answer:</b> Third-party insurance is a liability insurance policy under which the insurer (second party) agrees to indemnify the insured (first party) against legal liability to pay compensation for bodily injury, death, or property damage caused to an innocent outsider (the <b>third party</b>)—most commonly mandatory Third-Party Motor Liability Insurance.""")

    add_q(story, "Q7. Define 'endorsements' in relation to an insurance policy.")
    add_a(story, """<b>Answer:</b> An <b>endorsement</b> (also called a <b>rider</b> in life insurance) is a written amendment, addendum, or legal attachment added to a standard insurance policy contract that modifies its original terms—by expanding coverage, adding extra benefits (e.g., critical illness or earthquake coverage), restricting perils, or updating the sum insured, address, or beneficiary.""")

    add_q(story, "Q8. Distinguish between 'term life insurance' and 'cash value life insurance'.")
    add_a(story, """<b>Answer:</b>
• <b>Term Life Insurance:</b> Provides pure death protection for a temporary specified period (e.g., 10, 15, or 20 years); pays the sum assured only if the insured dies within the term, builds <b>no cash surrender value (no savings element)</b>, and has the lowest initial premium.
• <b>Cash Value Life Insurance (Whole Life / Endowment):</b> Combines life insurance protection with a tax-advantaged <b>savings/investment component</b> that accumulates a guaranteed <b>cash surrender value</b> (which the policyholder can borrow against or receive upon surrender/maturity) and charges a higher level premium.""")

    add_q(story, "Q9. Write the meaning of professional liability insurance.")
    add_a(story, """<b>Answer:</b> Professional liability insurance (also known as <b>Errors and Omissions [E&amp;O] Insurance</b> or <b>Professional Indemnity Insurance</b>, and Medical Malpractice Insurance for doctors) is a specialized liability policy that protects professionals (such as IT consultants, accountants, engineers, architects, lawyers, and physicians) against financial claims and legal defense costs arising from alleged negligence, errors, mistakes, or failure to perform professional duties.""")

    add_q(story, "Q10. What is meant by personal accident insurance?")
    add_a(story, """<b>Answer:</b> Personal Accident (PA) Insurance is a benefit policy that provides fixed financial compensation to the insured (or their nominee) in the event of accidental bodily injury resulting in <b>Accidental Death</b>, <b>Permanent Total Disability (PTD)</b>, <b>Permanent Partial Disability (PPD)</b>, or <b>Temporary Total Disability (TTD / weekly wage loss)</b>, as well as accidental medical expenses caused by violent, external, and visible means.""")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group 'B': Short Answer Questions (Attempt any SIX — ALL Solved) [6 x 5 = 30]", group_header_style))

    add_q(story, "Q11. Explain the burden of risk on society.")
    add_a(story, """<b>Answer:</b> Even if an actual loss never occurs, the mere presence of pure risk imposes heavy social and economic burdens on individuals, businesses, and society as a whole:
• <b>1. Requirement of Larger Emergency Reserves (Idle Capital):</b> Without insurance, households and businesses must hold large liquid cash reserves to prepare for potential fires, medical emergencies, or lawsuits. This ties up scarce capital in low-return liquid accounts instead of productive investments, reducing economic growth.
• <b>2. Deprivation of Goods and Services (Deterrence of Innovation):</b> High-risk but socially vital goods and services (such as pharmaceuticals, aviation, power plants, or surgical procedures) may not be produced or offered if businesses fear catastrophic liability or property losses.
• <b>3. Mental Fear, Worry, and Anxiety:</b> The constant psychological stress and insecurity regarding premature death, illness, old-age poverty, or loss of one's home reduces human welfare and workplace productivity.
• <b>4. Direct and Indirect Cost of Uncompensated Losses:</b> When uninsured disasters strike, businesses go bankrupt, workers lose jobs, families fall into poverty, and the state must bear higher public welfare burdens.""")

    add_q(story, "Q12. Define adverse selection. Describe the tools used by insurance companies to control the chance of adverse selection.")
    add_a(story, """<b>Answer:</b>
<b>Definition of Adverse Selection:</b>
Adverse selection is the tendency of applicants with a higher-than-average chance of loss to seek and purchase insurance coverage (or buy larger coverage amounts) at standard (average) premium rates to a greater extent than average- or low-risk individuals. It stems from asymmetric information between the applicant and the insurer, and if uncontrolled, drives average claims above collected premiums.

<b>Tools Used by Insurance Companies to Control Adverse Selection:</b>
• <b>1. Rigorous Underwriting and Risk Classification:</b> Screening applicants through medical exams, health declarations, financial statements, driving records, and property inspections, and placing them into appropriate rate classes (preferred, standard, substandard, or uninsurable).
• <b>2. Waiting Periods and Pre-Existing Condition Exclusions:</b> Including a waiting period (e.g., 30 days to 24 months in health/critical illness policies) and suicide exclusion clauses so people cannot buy policies immediately before a known claim.
• <b>3. Deductibles, Coinsurance, and Policy Limits:</b> Requiring the insured to share a portion of every loss discourages high-risk applicants seeking full indemnification.
• <b>4. Group Underwriting Rules:</b> Requiring minimum participation percentages (e.g., 75%–100% of eligible employees) in employer group plans so unhealthy individuals cannot self-select alone.
• <b>5. Strict Enforcement of Utmost Good Faith (Voiding for Concealment/Fraud):</b> Cancelling policies and denying claims when applicants intentionally conceal material health or risk facts.""")

    add_q(story, "Q13. Describe the role of insurance agent in insurance industry.")
    add_a(story, """<b>Answer:</b> An insurance agent is a licensed intermediary authorized by an insurance company (under the Insurance Act 2079 and NIA regulations in Nepal) to solicit, negotiate, and service insurance contracts on behalf of the insurer. Their major roles are:
• <b>1. Public Awareness, Education, and Risk Advisory:</b> Educating individuals and families about financial risks (premature death, health crises, property perils) and recommending suitable insurance policies based on client needs and budget.
• <b>2. Field Underwriting ("Eyes and Ears of the Insurer"):</b> As the first point of contact who meets the applicant in person, the agent verifies the applicant's health, occupation, moral hazard, and insurable interest, preventing adverse selection and fraud at the source.
• <b>3. Policy Solicitation, Proposal Completion, and Premium Collection:</b> Assisting clients in filling out proposal forms accurately, explaining policy terms and riders, and ensuring timely initial and renewal premium payments to prevent policy lapse.
• <b>4. Relationship Management and Policy Servicing:</b> Helping policyholders with nominations, address updates, policy loans, endorsements, and revival of lapsed policies.
• <b>5. Assistance in Smooth Claim Settlement:</b> Guiding the insured or bereaved family members through claim documentation, notification, and coordination with surveyors and the insurer's claim department during their time of distress.""")

    add_q(story, "Q14. Mr. Ram Kumar Subedi, a 32 years Chartered Accountant works as an Assistant Manager in a bank. He is living with his spouse and a daughter aged 4 years. He is the single breadwinner for his family. Mr. Subedi has taken home loan from a bank for Rs 4,000,000 and a vehicle loan for Rs 2,500,000. So, he is worried that if he dies suddenly, his family will be overburdened with the loans. Being a Chartered Accountant, Mr. Subedi has good idea of investment opportunities that yields him decent returns. Suggest the most appropriate type of life insurance policy to meet his need. Justify your answer.")
    add_a(story, """<b>Answer (Case/Situation Analysis):</b>
<b>1. Suggested Life Insurance Policy:</b>
The most appropriate life insurance policy for Mr. Ram Kumar Subedi is a <b>Term Life Insurance Policy</b> (specifically, a <b>Level Term Life Policy</b> of at least Rs 6,500,000 to Rs 10,000,000 covering his working/child-dependency years, or a <b>Decreasing Term / Mortgage Redemption Policy</b> matched to his Rs 6,500,000 total bank loans), follows the classic financial planning strategy: <b>"Buy Term and Invest the Difference."</b>

<b>2. Justification for Recommending Term Life Insurance:</b>
• <b>(a) High Immediate Debt & Dependency Protection at Lowest Cost:</b> Mr. Subedi is only 32, is the sole breadwinner for his wife and 4-year-old daughter, and carries heavy liabilities totaling <b>Rs 6,500,000</b> (Rs 4,000,000 home loan + Rs 2,500,000 vehicle loan). Term life insurance provides the largest pure death benefit coverage for a very small annual premium, ensuring that if he dies prematurely, his family can immediately pay off the Rs 6.5 million bank loans and fund his daughter's upbringing.
• <b>(b) Superior Investment Expertise as a Chartered Accountant ("Buy Term and Invest the Difference"):</b> Traditional Endowment or Whole Life policies bundle insurance with low-yielding savings (typically returning only 5%–7% p.a.) and charge very high premiums. Because Mr. Subedi is a skilled Chartered Accountant with deep knowledge of high-return investment opportunities (stocks, mutual funds, bonds), he does not need an insurance company to manage his savings. By buying low-cost Term Life Insurance for pure risk protection and investing the substantial premium savings himself, he will build far greater wealth for his family.
• <b>(c) Recommended Riders:</b> He should attach an <b>Accidental Death &amp; Permanent Total Disability (AD&amp;D/PTD) Rider</b>, a <b>Critical Illness Rider</b>, and a <b>Waiver of Premium Rider</b> so the loan obligations are also covered if disability or severe illness stops him from working.""")

    add_q(story, "Q15. Explain the role of marine insurance in international trade.")
    add_a(story, """<b>Answer:</b> Marine insurance (covering Marine Hull, Marine Cargo, and Freight against perils of the sea, inland transit, air cargo, piracy, jettison, and war/strikes under Institute Cargo Clauses A, B, and C) is the lifeblood of international trade:
• <b>1. Essential Requirement for Export-Import Financing (Letters of Credit):</b> Commercial banks will not open or negotiate an international Letter of Credit (LC) or discount export bills without a valid Marine Cargo Insurance Policy/Certificate assigned as collateral.
• <b>2. Protection Against Catastrophic Transit Perils:</b> International shipments travel thousands of miles across oceans, ports, and mountain highways (especially crucial for landlocked countries like Nepal importing via Kolkata/Visakhapatnam ports) and face perils of sinking, collision, storm, pilferage, and customs warehouse fire.
• <b>3. Facilitating Standardized Incoterms (CIF / CIP Trade):</b> Enables exporters and importers in different countries to clearly allocate transit risk under international commercial terms (such as CIF—Cost, Insurance, and Freight).
• <b>4. Coverage of General Average Losses:</b> Under maritime law, if cargo is intentionally jettisoned (thrown overboard) to save a ship in a storm, all cargo owners must share the loss proportionately (General Average); marine insurance pays these complex maritime contributions.
• <b>5. Expansion of Global Commerce:</b> By transferring catastrophic transit risk to insurers, exporters and importers can trade high-value shipments globally with confidence.""")

    add_q(story, "Q16. Highlight the major issues of auto insurance.")
    add_a(story, """<b>Answer:</b> Auto (motor) insurance—covering Third-Party Liability and Comprehensive Own-Damage—faces several major operational and economic challenges (particularly in developing markets like Nepal):
• <b>1. High Claim Frequency and Rising Loss Ratios:</b> Rapid growth of vehicles, congested roads, poor road infrastructure in hilly/mountainous terrain, and reckless driving result in high accident frequency and heavy claim payouts for insurers.
• <b>2. Moral Hazard and Fraudulent/Inflated Repair Claims:</b> Staged accidents, exaggerated garage repair bills, replacing old parts with new parts under accident claims, and collusion between workshops and vehicle owners inflate insurer costs.
• <b>3. Inadequate Third-Party Premium Rates & Tariff Rigidities:</b> Statutory third-party premiums and fixed motor tariffs often fail to reflect individual driver risk history (lack of telematics or strict driver-record merit rating).
• <b>4. Disputes and Delays in Claim Settlement:</b> Conflicts over depreciation rates on spare parts, surveyor assessment delays, unlicensed driving, or drunken driving exclusions create dissatisfaction among policyholders.
• <b>5. Uninsured Vehicles and Hit-and-Run Cases:</b> Many two-wheelers and rural vehicles fail to renew their annual third-party insurance on time, leaving accident victims uncompensated in hit-and-run incidents.
• <b>6. Rising Cost of Imported Spare Parts and EV Battery Repairs:</b> With the rapid adoption of Electric Vehicles (EVs), expensive imported battery and sensor replacements have sharply increased average claim severity.""")

    add_q(story, "Q17. Describe the process of calculating life insurance premium with suitable example.")
    add_a(story, """<b>Answer (Process + Step-by-Step Numerical Example):</b>
<b>1. Three Core Actuarial Elements of Life Insurance Premium Calculation:</b>
Actuaries calculate life insurance premiums using three fundamental factors:
• <b>(a) Mortality Rate (q_x from Mortality Table):</b> The probability that a person of exact age <i>x</i> will die within the next year, derived from a standard Mortality Table.
• <b>(b) Assumed Rate of Interest (Investment Return, i):</b> Because premiums are collected at the beginning of the year and death claims are paid at the end of the year, insurers discount future expected claims at a conservative interest rate <i>i</i>.
• <b>(c) Loading for Expenses, Contingencies, and Profit (Bonus):</b> Adding administrative expenses, agent commissions, taxes, and safety/bonus margins to the Net Premium to arrive at the <b>Gross (Office) Premium</b>.

<b>2. Step-by-Step Process with a Suitable Numerical Example:</b>
<b>Example:</b> Suppose an insurer issues a 1-year Term Life Insurance policy of <b>Rs 100,000</b> to a group of <b>10,000 people aged 35</b>. From the mortality table, out of 10,000 persons aged 35, <b>20 persons are expected to die</b> during the year (Mortality probability q_35 = 20 / 10,000 = <b>0.002</b>). The insurer earns <b>6% interest p.a.</b> on invested funds, and expense loading is <b>15% of Net Premium</b>.

• <b>Step 1: Calculate Total Expected Death Claims at Year-End:</b>
  Total Claims = 20 expected deaths x Rs 100,000 = <b>Rs 2,000,000</b> (or Expected Claim per person = 0.002 x Rs 100,000 = Rs 200).
• <b>Step 2: Discount Expected Claims by the Interest Rate to Find Net Single Premium (NSP):</b>
  Present Value of Claims per policy (Net Single Premium) = Expected Claim / (1 + i)^1
  NSP = Rs 200 / (1 + 0.06) = Rs 200 / 1.06 = <b>Rs 188.68 per policy</b>.
• <b>Step 3: Add Expense & Contingency Loading to Find Gross (Office) Premium:</b>
  Gross Premium = Net Premium + Loading (15% of Rs 188.68)
  Gross Premium = Rs 188.68 + Rs 28.30 = <b>Rs 216.98 per year</b>.
<i>(For multi-year policies, the Present Value of all future years' expected death benefits is divided by the Present Value of a Life Annuity Due of Re 1 to get the Net Level Annual Premium.)</i>""")
    add_hint(story, "Remember the 3 pillars of Life Insurance Rate Making: (1) Mortality Rate + (2) Interest Rate (Discounting) = Net Pure Premium; then Net Pure Premium + (3) Expense Loading = Gross (Office) Premium!")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group 'C': Long Answer Questions (Attempt any THREE — ALL Solved) [3 x 10 = 30]", group_header_style))

    add_q(story, "Q18. Describe the concept of risk management. Also discuss the process of risk management.")
    add_a(story, """<b>Answer:</b>
<b>1. Concept of Risk Management:</b>
Risk management is a proactive, scientific managerial process of identifying, analyzing, and evaluating pure (and enterprise) loss exposures faced by an organization or family, and selecting, implementing, and monitoring the most appropriate combination of risk control and risk financing techniques to minimize the adverse financial impact of losses and achieve pre-loss and post-loss objectives (survival, continuity of operations, earnings stability, and growth).

<b>2. Step-by-Step Process of Risk Management:</b>
• <b>Step 1: Establish Risk Management Objectives:</b>
  Define clear <i>Pre-Loss Objectives</i> (economy, reduction of anxiety, meeting legal/statutory obligations) and <i>Post-Loss Objectives</i> (survival of the firm, continuity of operations, stability of earnings, continued growth, and social responsibility).
• <b>Step 2: Identify Loss Exposures (Risk Identification):</b>
  Systematically uncover all property, liability, business interruption, human resource (death/disability/health), crime, and cyber exposures using risk analysis questionnaires, physical plant inspections, flowcharts, financial statements, and past loss histories.
• <b>Step 3: Measure and Analyze Loss Exposures (Risk Evaluation):</b>
  Estimate the <b>Loss Frequency</b> (how often a loss is likely to occur) and <b>Loss Severity</b> (Maximum Possible Loss and Probable Maximum Loss) for each exposure, categorizing them into a 4-cell Frequency-Severity Matrix.
• <b>Step 4: Select the Appropriate Combination of Risk Treatment Techniques:</b>
  - <b>(A) Risk Control Techniques (aimed at reducing frequency and severity):</b>
    1. <i>Avoidance:</i> Abandoning or refusing to enter a high-risk activity (100% elimination of frequency).
    2. <i>Loss Prevention:</i> Measures that reduce the <b>frequency</b> of losses (e.g., safety training, non-slip floors, cybersecurity firewalls).
    3. <i>Loss Reduction:</i> Measures that reduce the <b>severity</b> of a loss once it occurs (e.g., automatic fire sprinklers, emergency medical response, off-site cloud backups, duplication and separation of inventory).
  - <b>(B) Risk Financing Techniques (arranging funds to pay for losses that occur):</b>
    1. <i>Retention (Self-Insurance / Deductibles):</i> Retaining High-Frequency / Low-Severity predictable losses out of working capital, funded reserves, or a captive insurer.
    2. <i>Non-Insurance Transfer:</i> Shifting financial responsibility via hold-harmless contracts, leases, surety bonds, or derivative hedging.
    3. <i>Commercial Insurance:</i> Transferring Low-Frequency / High-Severity catastrophic risks to professional insurers.
• <b>Step 5: Implement the Risk Management Program:</b>
  Establish a formal Risk Management Policy Statement, coordinate with all functional departments, purchase selected insurance coverages, and install safety systems.
• <b>Step 6: Monitor, Review, and Evaluate the Program:</b>
  Continuously audit loss experience via a Risk Management Information System (RMIS) and adjust coverage as business operations evolve.""")

    add_q(story, "Q19. Insurance is a contract based on certain fundamental legal principles. Explain the principles of insurance contract.")
    add_a(story, """<b>Answer:</b>
An insurance policy is a special legal contract governed by general contract law (offer and acceptance, consideration, legal capacity, and lawful purpose) plus <b>six fundamental legal principles</b> unique to insurance:

• <b>1. Principle of Utmost Good Faith (Uberrimae Fidei):</b>
  Insurance contracts require a higher degree of honesty from both parties than ordinary commercial contracts. The applicant must voluntarily and truthfully disclose all material facts that would influence an underwriter's decision regarding premium rate or acceptance of risk. It is enforced through three legal doctrines:
  - <i>Representations:</i> Statements made by the applicant on the proposal form (if material and false, the contract is voidable).
  - <i>Concealment:</i> Intentional silence or failure to disclose a known material fact.
  - <i>Warranties:</i> Strict conditions promised in the policy that must be literally complied with.

• <b>2. Principle of Insurable Interest:</b>
  The insured must have a legally recognized pecuniary (financial) stake in the subject matter of insurance such that they benefit from its safety and suffer a direct financial loss upon its destruction, damage, or death.
  - In <i>Life Insurance</i>, insurable interest must exist at the <b>inception</b> of the policy.
  - In <i>Property &amp; Marine Insurance</i>, insurable interest must exist at the <b>time of loss</b>.
  - <i>Purpose:</i> Prevents gambling on strangers' lives/property and eliminates moral hazard.

• <b>3. Principle of Indemnity:</b>
  States that the insurer will compensate the insured only up to the actual financial loss suffered (never exceeding the sum insured), restoring the insured to the same financial position they occupied immediately prior to the loss. It prevents the insured from profiting from a disaster. Actual Cash Value (ACV = Replacement Cost - Depreciation) is the primary measure of indemnity. <i>(Note: Life and personal accident policies are valued benefit contracts, not contracts of strict indemnity.)</i>

• <b>4. Principle of Subrogation:</b>
  A corollary of indemnity: once the insurer pays a claim for a loss caused by the negligence or tort of a third party, the insurer steps into the legal shoes of the insured and acquires all legal rights to sue the negligent third party to recover the amount paid. This prevents the insured from collecting twice for the same loss.

• <b>5. Principle of Contribution:</b>
  A second corollary of indemnity: when an insured holds two or more property/liability policies covering the same interest, same subject matter, and same peril (double insurance), they cannot recover more than the total actual loss. Each insurer pays only its proportionate (pro-rata) share of the loss.

• <b>6. Principle of Proximate Cause (Causa Proxima):</b>
  When a loss results from a series of events, the insurer is liable only if the nearest, dominant, and efficient cause that set the chain of events in motion is an <b>insured peril</b> (and not an excluded peril).""")

    add_q(story, "Q20. Explain the role of insurance industry in financial development of Nepal.")
    add_a(story, """<b>Answer:</b>
The insurance industry in Nepal—comprising life insurers, non-life insurers, micro-insurers, and domestic reinsurance companies regulated by the Nepal Insurance Authority (NIA)—plays a vital catalyst role in the financial and economic development of the country:

• <b>1. Mobilization of Long-Term Domestic Savings & Capital Formation:</b>
  Life insurance policies (endowment, whole life, child plans) collect small, regular contractual savings from millions of Nepalese households across urban and rural areas, turning fragmented household savings into a massive pool of long-term investable capital.
• <b>2. Major Institutional Investor in Banks and Infrastructure:</b>
  Nepalese insurance companies are the largest institutional depositors in commercial and development banks (providing stable fixed deposits that strengthen banking sector liquidity) and invest heavily in government bonds, hydropower projects, agriculture, tourism infrastructure, and capital market securities (NEPSE).
• <b>3. Promoting Trade, Industry, and Banking Credit (Collateral Protection):</b>
  Banks in Nepal require property, fire, marine, or motor insurance before sanctioning home loans, auto loans, industrial project loans, or import Letters of Credit. By absorbing asset destruction risk, insurance enables the banking system to expand credit safely.
• <b>4. Protecting Rural Livelihoods through Agriculture and Micro-Insurance:</b>
  Subsidized crop and livestock insurance and dedicated micro-insurance companies protect low-income farmers and micro-entrepreneurs against natural disasters, preventing rural families from falling back into poverty.
• <b>5. Retaining Foreign Exchange via Domestic Reinsurance:</b>
  The establishment of domestic reinsurers (Nepal Reinsurance Company and Himalayan Reinsurance) retains billions of Rupees of reinsurance premiums within Nepal's financial system and earns foreign currency by accepting inward reinsurance from abroad.
• <b>6. Employment Generation, Tax Revenue, and Social Security:</b>
  Creates direct and indirect employment for thousands of employees, surveyors, and over 200,000 licensed agents, contributes substantial corporate and withholding taxes to the government, and reduces the state's post-disaster fiscal burden.""")

    add_q(story, "Q21. Regulators regulate various aspects of the insurance company operation. In light of this statement, explain the areas of insurance regulation.")
    add_a(story, """<b>Answer:</b>
Because insurance companies act as fiduciaries managing public funds to meet contingent future promises, insurance regulators (such as the Nepal Insurance Authority under the Insurance Act 2079) supervise virtually every major area of an insurer's operations:

• <b>1. Licensing and Formation of Insurers (Entry Regulation):</b>
  Setting minimum paid-up capital requirements (e.g., Rs 5 billion for life insurers and Rs 2.5 billion for non-life insurers in Nepal), vetting promoter fit-and-proper criteria, and issuing operating licenses for life, non-life, micro-insurance, and reinsurance businesses.
• <b>2. Financial Solvency, Capital Adequacy, and Reserve Regulation:</b>
  Mandating strict Risk-Based Capital (RBC) and solvency margin ratios, unearned premium reserves, statutory catastrophe reserves, and actuarial valuation of life funds to prevent insurer insolvency.
• <b>3. Regulation of Investment of Insurance Funds:</b>
  Issuing investment directives that specify minimum and maximum percentages of technical reserves that insurers may invest in government bonds, BFIs' fixed deposits, listed shares, debentures, real estate, and infrastructure/hydropower projects—ensuring safety, liquidity, and diversification.
• <b>4. Rate Making and Premium Tariff Regulation:</b>
  Ensuring that premium rates are adequate (to maintain solvency), not excessive (to protect consumers), and not unfairly discriminatory, including setting tariffs for compulsory third-party motor, property/fire, and subsidized agriculture insurance.
• <b>5. Policy Contract Forms and Product Approval:</b>
  Reviewing and approving all new life and non-life insurance policy wordings, endorsements, and actuarial product filings before they can be sold to the public so unfair exclusions or deceptive clauses are eliminated.
• <b>6. Regulation of Market Conduct, Intermediaries, and Corporate Governance:</b>
  Licensing and training insurance agents, brokers, and loss surveyors; enforcing anti-money laundering (AML/CFT) rules; capping CEO/board governance limits; and prohibiting rebating or misrepresentation.
• <b>7. Claim Settlement Supervision and Policyholder Grievance Redressal:</b>
  Enforcing mandatory timelines for surveyor reports and claim payments, and acting as a quasi-judicial body to resolve disputes between policyholders and insurers.""")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group 'D': Comprehensive Answer / Case / Situation Analysis [20 Marks]", group_header_style))

    add_q(story, "Q22. Case Study: Bikash Koirala & Horizon Digital Advisory\nBikash Koirala (39-year-old former Operations Director, sole financial provider for his spouse and two school-going children, active stock investor and short-term trader) resigned from his corporate job to launch Horizon Digital Advisory in Lalitpur (IT and digital consulting for microfinance institutions across Nepal, funded with personal savings, 6 employees, servers/networking devices/premium laptops, home and vehicle loans).\na. Define pure risk and speculative risk. Also identify all the pure risks and speculative risks faced by Mr. Koirala and his organization.\nb. Describe the type of life insurance policy that is suitable for Mr. Koirala. What additional benefits could be added to the policy to enhance the coverage?\nc. Suggest an insurance policy to cover the risk of fire and related perils.\nd. Why do you think is the decision to provide Group Health Insurance for the staffs considered as a risk management tool, rather than just an additional expense to the organization?")
    add_a(story, """<b>Answer (Comprehensive Case Study Solution):</b>

<b>a. Definitions and Identification of Pure Risks and Speculative Risks Faced by Mr. Koirala and Horizon Digital Advisory:</b>
• <b>Definition of Pure Risk:</b> A category of risk in which there are only two possible outcomes—<b>loss or no loss</b> (zero possibility of financial gain). Pure risks are generally accidental, unintentional, and <b>insurable</b> (e.g., fire, earthquake, premature death).
• <b>Definition of Speculative Risk:</b> A category of risk in which there are three possible outcomes—<b>loss, no loss (breakeven), or financial gain/profit</b>. Speculative risks are undertaken voluntarily in pursuit of profit and are generally not insurable through traditional insurance (handled instead via diversification and hedging).
• <b>Pure Risks Faced by Mr. Koirala and Horizon Digital Advisory:</b>
  1. <i>Personal / Family Pure Risks:</i> Untimely (premature) death of Mr. Koirala, permanent disability, or diagnosis of a critical illness—which would cut off his primary income and leave his family unable to pay daily living costs, two children's schooling, and ongoing home and vehicle loans.
  2. <i>Property Pure Risks:</i> Physical damage or destruction of the Lalitpur office premises, servers, networking devices, and premium laptops due to <b>fire, electrical damage, theft, or natural disasters like earthquakes</b>.
  3. <i>Liability &amp; Operational Pure Risks:</i> Breaches of sensitive client financial data or system failures caused by human error, omissions, or negligence during IT consulting delivery—exposing the firm to expensive client compensation claims and legal defense costs; employee sickness or medical emergencies among his six staff members.
• <b>Speculative Risks Faced by Mr. Koirala and His Organization:</b>
  1. <i>Stock Market Investment &amp; Short-Term Trading Risk:</i> Price fluctuations in Mr. Koirala's equity investments and short-term trading positions (can result in capital gains or trading losses).
  2. <i>Entrepreneurial Startup Venture Risk:</i> Committing a large share of his personal savings to launch Horizon Digital Advisory—the firm may prosper in the microfinance IT consulting market or incur operating losses due to market competition.

<b>b. Suitable Life Insurance Policy for Mr. Koirala and Additional Benefits (Riders) to Enhance Coverage:</b>
• <b>Recommended Life Insurance Policy:</b> A high-coverage <b>Term Life Insurance Policy</b> (or a combination of a 20–25 year Term Life Policy plus an Endowment/Whole Life base policy) sized to cover his home loan, vehicle loan, children's education fund, and family living expenses.
  - <i>Why Suitable:</i> Since Mr. Koirala has already committed a large share of his personal savings into launching his startup, a Term Life policy gives his family maximum lump-sum financial protection at the most affordable premium, keeping cash available for Horizon Digital Advisory.
• <b>Additional Benefits (Riders) to Add to the Policy:</b>
  1. <i>Critical Illness (CI) Benefit Rider:</i> Pays an immediate tax-free lump sum upon diagnosis of major critical illnesses (cancer, heart attack, stroke, kidney failure, organ transplant) to pay for specialized medical care and replace lost income during recovery.
  2. <i>Permanent Total Disability (PTD) &amp; Accidental Death and Dismemberment (AD&amp;D) Rider:</i> Provides income replacement / lump-sum payout if an accident or illness leaves him permanently unable to work.
  3. <i>Waiver of Premium Rider:</i> Automatically waives all future policy premiums if Mr. Koirala becomes permanently disabled, ensuring the life insurance policy remains active without financial burden.

<b>c. Suggested Insurance Policy to Cover the Risk of Fire and Related Perils (Office &amp; IT Equipment):</b>
Mr. Koirala should purchase a <b>Standard Fire and Allied Perils Insurance Policy (Commercial Property / Office Package Policy)</b> coupled with an <b>Electronic Equipment Insurance (EEI) / Burglary Endorsement</b>:
• <b>1. Standard Fire and Allied Perils Coverage:</b> Indemnifies the Lalitpur office premises, furniture, and fixtures against direct physical loss from fire, lightning, explosion, and electrical short-circuit damage, extended with allied perils endorsements for <b>Earthquake, Flood, Inundation, Landslide, Storm, and Riot/Strike/Malicious Damage (RSMD)</b>.
• <b>2. Electronic Equipment Insurance (EEI) &amp; Burglary/Theft Coverage:</b> Specifically covers high-value IT infrastructure—servers, networking switches, and premium laptops—against internal electrical/mechanical breakdown, power surges, and forcible theft/burglary.
• <b>3. Business Interruption (Consequential Loss) &amp; Professional Indemnity Add-on:</b> Covers lost revenue during post-fire recovery alongside a Professional Indemnity (E&amp;O) policy for client data-breach liabilities.

<b>d. Why Providing Group Health Insurance for Staff is a Risk Management Tool Rather Than Just an Additional Expense:</b>
• <b>1. Controlling Human Resource &amp; Operational Continuity Risk:</b> In a specialized 6-person IT consulting team serving microfinance institutions, losing even one key engineer to prolonged untreated illness disrupts client projects. Prompt access to quality healthcare ensures faster recovery and minimizes absenteeism.
• <b>2. Talent Retention and Reduction of Turnover Risk:</b> Young startups face high risk of losing trained IT staff to larger corporations. Group health insurance builds employee loyalty, job satisfaction, and retention, avoiding the high cost of recruiting and retraining replacements.
• <b>3. Reducing Attitudinal Hazard and Human Error:</b> Employees who are financially secure regarding their family's medical needs experience lower stress and higher concentration, directly reducing the human errors that cause system failures or client data breaches.
• <b>4. Predictable Budgeting &amp; Tax Efficiency:</b> Converts unpredictable employee medical emergency requests into a small, predictable, tax-deductible annual premium with pooled group underwriting benefits.""")
