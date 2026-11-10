from notes_base import (
    Paragraph, Spacer, PageBreak, add_unit, add_topic, add_subtopic,
    add_body, add_example, add_tip, make_table, P, P_hdr
)

def build_bnk209_exam_bank(story):
    story.append(PageBreak())
    add_unit(story, "SECTION 8: BNK 209 — WORKED ACTUARIAL NUMERICALS, QUESTION BANK & CASE PLAYBOOK")

    add_topic(story, "8.1 Complete Step-by-Step Worked Numerical Problems for BNK 209 Exams")

    add_subtopic(story, "Numerical 1: Human Life Value (HLV) Calculation (TU Model Question)")
    add_body(story, """<b>Question:</b> Mr. Suman Thapa, aged 40, is married and has two children. He earns Rs 600,000 annually and plans to retire at age 60. Of this amount, Rs 30,000 is used for taxes, life and health insurance, and his personal needs. The remaining amount is used to support his family. Using a discount rate of 6 percent, calculate the Human Life Value of Mr. Thapa. [PVIFA(6%, 20 yrs) = 11.4699]
<b>Step-by-Step Solution:</b>
• <b>Step 1: Remaining Working Years (n):</b> n = Planned Retirement Age - Current Age = 60 - 40 = <b>20 years</b>.
• <b>Step 2: Net Annual Income Contributed to Family:</b>
  Annual Family Share = Gross Annual Earnings - (Taxes + Insurance + Personal Self-Maintenance)
  Annual Family Share = Rs 600,000 - Rs 30,000 = <b>Rs 570,000 per year</b>.
• <b>Step 3: Present Value of Family's Share of Earnings (Human Life Value, HLV):</b>
  HLV = Annual Family Share x PVIFA(6%, 20 years)
  HLV = Rs 570,000 x 11.4699 = <b>Rs 6,537,843</b>.""")

    add_subtopic(story, "Numerical 2: Comprehensive HLV, Financial Needs Approach & 1-Year Term Net Single Premium (SDC Preboard 2026)")
    add_body(story, """<b>Question:</b> Shree Sharma (age 35, software engineer, retires at age 60) earns NPR 18,00,000/yr; after taxes and personal living costs, NPR 12,00,000/yr is available for family support. Obligations: Home loan = NPR 50,00,000; Daughter's education fund (in 10 yrs) = NPR 30,00,000; Emergency fund = NPR 10,00,000; Monthly family living expenses = NPR 60,000 (NPR 7,20,000/yr). Discount rate = 7%; Mortality probability at age 35 (q_35) = 0.0020.
<b>Step-by-Step Solution:</b>
• <b>(a) Human Life Value (HLV) Approach:</b>
  - Working years (n) = 60 - 35 = <b>25 years</b>;  PVIFA(7%, 25 yrs) = [ 1 - (1.07)^(-25) ] / 0.07 = <b>11.653583</b>
  - <b>HLV</b> = NPR 12,00,000 x 11.653583 = <b>NPR 1,39,84,300 (NPR 13,984,300)</b>.
• <b>(b) Financial Needs Approach:</b>
  - Immediate Home Loan Payoff = <b>NPR 50,00,000</b>
  - Emergency Fund = <b>NPR 10,00,000</b>
  - Daughter's Education Fund: PV at 7% for 10 yrs = 30,00,000 / (1.07)^10 = <b>NPR 15,25,048</b> (or Nominal = <b>NPR 30,00,000</b>)
  - PV of Family Living Expenses (NPR 7,20,000/yr for 25 yrs @ 7%) = 7,20,000 x 11.653583 = <b>NPR 83,90,580</b>
  - <b>Total Insurance Need</b> = 50,00,000 + 10,00,000 + 15,25,048 + 83,90,580 = <b>NPR 1,59,15,628</b> (or <b>NPR 1,73,90,580</b> with nominal education fund).
• <b>(c) 1-Year Term Net Single Premium (NSP) for Face Value of NPR 10,00,000:</b>
  - Expected Death Claim at Year-End = Face Value x q_35 = NPR 10,00,000 x 0.0020 = <b>NPR 2,000</b>
  - <b>Net Single Premium (NSP)</b> = Expected Claim / (1 + i) = NPR 2,000 / 1.07 = <b>NPR 1,869.16</b>.""")

    add_subtopic(story, "Numerical 3: Coinsurance (Condition of Average), Deductible & Pro-Rata Contribution")
    add_body(story, """<b>Question:</b> A factory building has a Replacement Cost of Rs 20,000,000 and an estimated physical depreciation of 25%. It is insured under a Fire Insurance Policy carrying an 80% Coinsurance Clause (based on Actual Cash Value) and a Rs 50,000 straight deductible. The owner carries Rs 9,000,000 of fire insurance. A fire causes a partial loss with a replacement cost of Rs 3,000,000.
<b>Step-by-Step Solution:</b>
• <b>Step 1: Actual Cash Value (ACV) of Building and Loss:</b>
  - ACV of Building = Rs 20,000,000 x (1 - 0.25) = <b>Rs 15,000,000</b>
  - ACV of Loss = Rs 3,000,000 x (1 - 0.25) = <b>Rs 2,250,000</b> (or if loss is already given in ACV = Rs 3,000,000).
• <b>Step 2: Insurance Required Under 80% Coinsurance:</b>
  - Insurance Required = 80% of Rs 15,000,000 = <b>Rs 12,000,000</b> (Owner carried only Rs 9,000,000 -> underinsured!).
• <b>Step 3: Coinsurance Recovery Before & After Deductible:</b>
  - Coinsurance Ratio = Carried / Required = 9,000,000 / 12,000,000 = <b>75% (0.75)</b>
  - Recovery on ACV Loss of Rs 2,250,000 = (0.75 x Rs 2,250,000) - Rs 50,000 deductible = Rs 1,687,500 - Rs 50,000 = <b>Rs 1,637,500</b>.""")

    add_topic(story, "8.2 Top 25 Rapid-Fire Group A (2-Mark) Definitions & Answers (BNK 209)")
    t_qa209 = make_table([
        [P_hdr("Q#"), P_hdr("Exam Brief Question (2 Marks)"), P_hdr("Concise Full-Marks Answer Key")],
        [P("1"), P("Define Risk, Peril & Hazard."), P("Risk is uncertainty concerning the occurrence of a loss; Peril is the direct cause of loss (fire, flood); Hazard is a condition increasing loss frequency or severity.")],
        [P("2"), P("Risk vs. Uncertainty?"), P("Risk has objectively measurable probabilities from historical data and is insurable; Uncertainty is subjective doubt whose probabilities cannot be quantified.")],
        [P("3"), P("List the 4 Types of Hazards."), P("(1) Physical Hazard, (2) Moral Hazard (dishonesty/fraud), (3) Attitudinal / Morale Hazard (carelessness), and (4) Legal Hazard.")],
        [P("4"), P("What is Systemic Risk?"), P("The risk of collapse of an entire financial system or market due to financial interlinkages, where one major institution's failure triggers a domino effect.")],
        [P("5"), P("What is Enterprise Risk?"), P("A holistic concept encompassing all pure, speculative/financial, operational, cyber, and strategic risks faced by an organization, managed via ERM.")],
        [P("6"), P("Define Risk Pooling."), P("Spreading unexpected losses incurred by a few individuals over a large group of homogeneous exposure units so that average loss substitutes for actual loss.")],
        [P("7"), P("Objectives of Risk Management?"), P("Pre-Loss: Economy, anxiety reduction, legal compliance. Post-Loss: Survival, continuity of operations, earnings stability, continued growth, social responsibility.")],
        [P("8"), P("What is Loss Forecasting & its 3 Tools?"), P("Predicting future loss frequency and severity using: (1) Probability Analysis, (2) Regression Analysis, and (3) Loss Distributions (Poisson/Lognormal).")],
        [P("9"), P("How does RMIS help Risk Management?"), P("A computerized database that tracks property exposures, policy limits, and claims histories to automate loss forecasting, trend analysis, and renewals.")],
        [P("10"), P("Risk Appetite vs. Risk Tolerance?"), P("Risk Appetite is the broad strategic level of risk a firm is willing to pursue; Risk Tolerance is the specific quantitative maximum acceptable deviation around a target.")],
        [P("11"), P("What is Value at Risk (VaR)?"), P("A statistical metric measuring the maximum expected financial loss on a portfolio or firm over a specified time horizon (e.g., 10 days) at a given confidence level (e.g., 99%).")],
        [P("12"), P("What is Risk Avoidance?"), P("A risk-control technique where a firm refuses to engage in or abandons a high-risk activity, reducing the probability (frequency) of loss to zero (0%).")],
        [P("13"), P("Define Insurance & its 4 Characteristics."), P("A legal arrangement transferring pure risk to an insurer for a premium. Characteristics: (1) Pooling of losses, (2) Fortuitous losses, (3) Risk transfer, (4) Indemnity.")],
        [P("14"), P("What is Adverse Selection?"), P("The tendency of higher-than-average risk applicants to seek insurance at standard rates more aggressively than low-risk persons, controlled via underwriting.")],
        [P("15"), P("Named-Perils vs. Open-Perils Coverage?"), P("Named-Perils covers only perils explicitly listed in the policy; Open-Perils (All-Risks) covers all accidental causes of loss except those specifically excluded.")],
        [P("16"), P("Endorsement vs. Rider?"), P("Both are written amendments modifying a standard policy—called an 'Endorsement' in Property/Casualty insurance and a 'Rider' in Life/Health insurance.")],
        [P("17"), P("Term Life vs. Cash-Value Life?"), P("Term Life offers temporary pure death protection with zero cash value at lowest cost; Cash-Value Life (Whole/Endowment) combines protection with a savings element.")],
        [P("18"), P("Life Insurance Tax Rules in Nepal?"), P("Under Income Tax Act 2058: Annual premiums up to Rs 40,000 are tax-deductible; Death benefits are 100% tax-exempt; Maturity net gain carries 5% final withholding tax.")],
        [P("19"), P("Meaning of 'Fire' in Fire Insurance?"), P("Must involve (1) actual ignition/flame (not mere heating/scorching) and (2) be accidental/fortuitous and a 'Hostile Fire' escaping its normal container.")],
        [P("20"), P("Third-Party Motor Liability Insurance?"), P("Compulsory auto coverage where the insurer (2nd party) pays compensation for bodily injury, death, or property damage caused by the insured's vehicle (1st party) to outsiders (3rd party).")],
        [P("21"), P("What is Professional Liability (E&O)?"), P("Errors & Omissions / Indemnity insurance protecting professionals (IT consultants, doctors, CAs, engineers) against client lawsuits and defense costs for negligence or mistakes.")],
        [P("22"), P("What is Personal Accident (PA) Insurance?"), P("A benefit policy paying fixed compensation for accidental death, permanent total disability (PTD), permanent partial disability (PPD), or temporary wage loss.")],
        [P("23"), P("What is Commercial Liability Insurance?"), P("Business insurance protecting firms against legal liability for bodily injury, property damage, or defective products/services caused to third parties.")],
        [P("24"), P("Two reasons NIA regulates insurers?"), P("(1) To maintain insurer financial solvency and protect policyholders' funds, and (2) To ensure fair, adequate rates and prompt claim settlement.")],
        [P("25"), P("What is Social Insurance in Nepal?"), P("Compulsory contribution-based protection (e.g., Nepal's SSF: 20% employer + 11% employee = 31% of basic pay) covering Medical/Maternity, Accident, Dependent, and Old-Age Pension.")],
    ], col_widths=[25, 150, 325])
    story.append(t_qa209)
    story.append(Spacer(1, 6))

    add_topic(story, "8.3 Master Guide to Group D Case Studies in BNK 209 (20-Mark Scoring Playbook)")
    add_body(story, """Across all TU Model, Past (April 2026), and SDC Preboard papers, Group D (20 Marks) in BNK 209 tests either:
• <b>Case Type A: Entrepreneur / Tech Consultancy / Professional Case (e.g., Aarav Sharma [Everest Tech Solutions] or Bikash Koirala [Horizon Digital Advisory]):</b>
  1. <b>Question (a) — Define & Identify All Pure Risks and Speculative Risks:</b>
     - Always start by defining <i>Pure Risk</i> (loss or no loss; insurable) and <i>Speculative Risk</i> (loss, no loss, or gain; uninsurable).
     - List <b>Personal Pure Risks</b> (premature death of founder, permanent disability, critical illness leaving family unable to pay living expenses, children's schooling, and home/car mortgages), <b>Property Pure Risks</b> (fire, lightning, earthquake, flood, or theft destroying office servers, networking equipment, and laptops), and <b>Liability / Operational Pure Risks</b> (client data breach or system failure from employee configuration error/negligence, business interruption, employee sickness).
     - List <b>Speculative Risks</b> (stock market investing/short-term trading gains or losses; entrepreneurial startup investment of personal savings into the consultancy).
  2. <b>Question (b) — Recommend Suitable Life Insurance Policy + Justification + Riders:</b>
     - Recommend a <b>Term Life Insurance Policy</b> (or a Term + Child Endowment combination).
     - <i>Justification:</i> Since the entrepreneur has tied up personal savings in the startup and carries heavy home/car loans and family dependencies, Term Life provides the maximum lump-sum death benefit at the lowest premium, preserving cash flow for the business. (And for a CA/investor like Ram Kumar Subedi, cite <i>"Buy Term and Invest the Difference"</i>!).
     - <i>Three Riders to Add:</i> (i) <b>Critical Illness (CI) Rider</b>, (ii) <b>Permanent Total Disability (PTD) & Accidental Death (AD&D) Rider</b>, and (iii) <b>Waiver of Premium Rider</b>.
  3. <b>Question (c) — Recommend Property / Fire / Professional Liability Insurance:</b>
     - For client data breaches & employee negligence: Recommend <b>Professional Liability (Errors & Omissions / Cyber Liability) Insurance</b> (pays both compensatory damages awarded to the client AND legal defense/court costs).
     - For office servers, laptops & furniture: Recommend a <b>Standard Fire and Allied Perils Policy (extended with Earthquake, Flood, and RSMD endorsements) + Electronic Equipment Insurance (EEI) & Burglary Coverage</b>.
  4. <b>Question (d) — Why Group Health Insurance for Staff is a Risk Management Tool (Not Just an Expense):</b>
     - Explain 4 points: (i) <b>Controls Human Resource & Operational Continuity Risk</b> (fast medical treatment reduces employee absenteeism and project delays in a small 5–6 person team), (ii) <b>Employee Retention & Talent Attraction</b> (prevents costly turnover of trained IT staff), (iii) <b>Reduces Attitudinal Hazard & Human Error</b> (employees free from family medical anxiety make fewer configuration mistakes), and (iv) <b>Predictable Tax-Deductible Budgeting</b> (converts unpredictable medical emergencies into a fixed, tax-deductible group premium).

• <b>Case Type B: Quantitative Family Financial Planning Case (e.g., Shree Sharma):</b>
  - Show clear step-by-step calculations for: (a) <b>Human Life Value (HLV)</b>, (b) <b>Financial Needs Approach Table</b>, (c) <b>Policy & Rider Recommendation</b>, and (d) <b>1-Year Term Net Single Premium (NSP)</b>.""")
