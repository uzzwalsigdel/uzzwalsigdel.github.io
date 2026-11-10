from notes_base import (
    Paragraph, Spacer, PageBreak, add_unit, add_topic, add_subtopic,
    add_body, add_example, add_tip, make_table, P, P_hdr
)
from bnk209_figures import fig_life_insurance_types

def build_bnk209_u5_to_u7(story):
    # ==================== UNIT 5 ====================
    add_unit(story, "UNIT 5: LIFE INSURANCE & ACTUARIAL RATE MAKING (10 Lecture Hours)")

    add_topic(story, "5.1 Meaning, Importance, Premature Death & Financial Impact of Premature Death")
    add_body(story, """<b>1. Meaning and Importance of Life Insurance:</b>
Life insurance is a legal contract between a policyholder and a life insurer under which the insurer promises to pay a designated lump-sum benefit (Sum Assured plus accrued bonuses, if any) to the named beneficiary upon the death of the insured life, or to the insured upon survival to the maturity of an endowment policy, in exchange for periodic premium payments.
• <b>Importance:</b> (1) Immediate estate creation for young families, (2) Protection against loss of Human Life Value, (3) Mortgage and business debt redemption, (4) Disciplined long-term tax-advantaged savings for retirement and children's education, and (5) Mobilization of domestic capital for national economic development.

<b>2. Premature Death and Its Financial Implications (5-Mark Exam Classic):</b>
• <b>Definition:</b> Premature death is the death of a family head (breadwinner) who leaves behind unfulfilled financial obligations—such as dependent spouse, children, or aging parents to support, an unpaid home mortgage or auto loan, or unfunded children's college education.
• <b>Six Financial Implications (Costs) of Premature Death:</b>
  1. <i>Permanent Loss of Human Life Value:</i> The family loses its share of the deceased breadwinner's future net earning power.
  2. <i>Additional Immediate Cash Outflows (Clearance / Final Expenses):</i> High funeral/cremation expenses, uninsured final medical/ICU bills, estate settlement fees, and unpaid taxes.
  3. <i>Debt and Mortgage Default Risk:</i> Inability to service home loans, vehicle loans, or business loans, risking bank foreclosure of the family home.
  4. <i>Reduction in Standard of Living:</i> Because ongoing family income falls below family financial needs, surviving dependents suffer a permanent drop in living standards.
  5. <i>Disruption of Children's Higher Education Plans:</i> Lack of funds for school/university tuition.
  6. <i>Noneconomic Costs:</i> Intense emotional grief and loss of parental guidance and role modeling.""")

    add_topic(story, "5.2 Determining the Amount of Life Insurance to Own: Human Life Value (HLV) vs. Needs Approach")
    add_body(story, """<b>1. Method A — The Human Life Value (HLV) Approach (Solomon S. Huebner):</b>
Defines Human Life Value as the <b>present value of the family's share of the deceased breadwinner's future net earnings</b> over their remaining working career:
• <b>Step 1:</b> Calculate Remaining Working Years: <b>n = Planned Retirement Age - Current Age</b>.
• <b>Step 2:</b> Estimate Average Annual Gross Earnings over the remaining working career.
• <b>Step 3:</b> Deduct the breadwinner's personal self-maintenance expenses, income taxes, and personal life/health insurance premiums to find the <b>Net Annual Family Share</b>.
• <b>Step 4:</b> Discount the stream of annual family contributions to Present Value at a reasonable discount rate (i):
  <b>Human Life Value (HLV) = Net Annual Family Share x PVIFA(i%, n years)</b>
  where <b>PVIFA(i, n) = [ 1 - (1 + i)^(-n) ] / i</b>.

<b>2. Method B — The Financial Needs Approach:</b>
Estimates the total life insurance required by summing the specific financial needs of the surviving family and subtracting existing liquid financial assets:
• <b>(1) Estate Clearance Fund (Immediate Cash Needs):</b> Funeral expenses, uninsured medical bills, probate costs, and short-term installment debts.
• <b>(2) Readjustment Period Income (1–2 Years):</b> Temporary income to let the family adjust smoothly without drastic lifestyle cuts.
• <b>(3) Dependency Period Income:</b> Present value of annual living expenses needed until the youngest child reaches financial independence (age 18–22) or for the surviving spouse's/parents' lifetime.
• <b>(4) Mortgage / Bank Loan Redemption Fund:</b> Lump sum to pay off the outstanding home loan and vehicle loan immediately.
• <b>(5) Special Funds (Education & Emergency Funds):</b> Present value (or nominal corpus) for children's university education plus a family emergency reserve.
• <b>Formula:</b> <b>New Life Insurance Needed = Total Financial Needs - Existing Liquid Assets & Existing Life Insurance</b>.""")

    add_topic(story, "5.3 Types of Life Insurance Policies: Term Life vs. Cash-Value Life Insurance (10-Mark Favourite)")
    story.append(fig_life_insurance_types())
    t_u5_types = make_table([
        [P_hdr("Basis of Comparison"), P_hdr("Term Life Insurance"), P_hdr("Cash-Value Life Insurance (Whole Life / Endowment)")],
        [P("1. Period of Coverage", True), P("<b>Temporary:</b> Covers a fixed term (1, 5, 10, 20, or 30 years) and expires without value if the insured survives."), P("<b>Permanent / Long-Term:</b> Covers the entire lifetime (Whole Life) or pays out at a fixed maturity date (Endowment).")],
        [P("2. Savings / Cash Value", True), P("<b>Pure Protection Only (Zero Cash Value):</b> Has no investment or savings accumulation."), P("<b>Protection + Savings:</b> Builds a guaranteed <b>Cash Surrender Value (CSV)</b> plus vested reversionary bonuses.")],
        [P("3. Premium Level & Cost", True), P("<b>Lowest initial premium</b> per Rs 1,000 of death benefit; increases at each renewal as age rises."), P("<b>Much higher level premium</b> (3x to 8x higher initially) because excess early premiums build the cash reserve.")],
        [P("4. Maturity / Survival Benefit", True), P("Pays <b>only if death occurs</b> during the policy term (nothing paid on survival)."), P("Pays the full Sum Assured + Bonus on death OR upon surviving to maturity (Endowment) / age 100 (Whole Life).")],
        [P("5. Policy Loans & Surrender", True), P("Cannot be surrendered for cash and has no loan value."), P("Policyholder can surrender for cash or take a policy loan up to 80%–90% of accumulated surrender value.")],
        [P("6. Best Suitability", True), P("Young breadwinners with high mortgages/children and limited cash flow, or financially savvy investors who <b>'Buy Term and Invest the Difference'</b>."), P("Individuals wanting forced long-term savings, guaranteed child education/retirement corpus, or permanent estate liquidity.")],
    ], col_widths=[105, 198, 197])
    story.append(t_u5_types)
    story.append(Spacer(1, 5))

    add_body(story, """<b>• Major Sub-Types of Life Insurance Policies:</b>
  1. <b>Term Life Variants:</b> (i) <i>Yearly Renewable Term (YRT)</i>, (ii) <i>5/10/20/25-Year Level Term</i>, (iii) <i>Decreasing Term (Mortgage Protection)</i>, (iv) <i>Convertible Term</i> (can be converted into Whole Life/Endowment without medical exam), and (v) <i>Return-of-Premium Term</i>.
  2. <b>Whole Life Variants:</b> (i) <i>Ordinary (Straight) Whole Life</i> (level premiums paid until death/age 100), (ii) <i>Limited-Payment Whole Life</i> (coverage for whole life, but premiums paid for only 10, 15, or 20 years), and (iii) <i>Single-Premium Whole Life</i>.
  3. <b>Endowment & Money-Back Policies (Most Popular in Nepal):</b> Pays Sum Assured + Bonus either on death within the term or upon survival at the end of the term (Money-Back policies pay periodic survival installments every 4–5 years plus full death cover).
  4. <b>Universal Life, Variable Life & Group Life Insurance:</b> <i>Universal Life</i> unbundles protection and savings with flexible premiums; <i>Variable Life</i> invests cash value in mutual-fund subaccounts; <i>Group Life Insurance</i> covers all employees of a company under one master contract.""")

    add_topic(story, "5.4 Life Insurance Contractual Provisions, Options, Riders, Taxation & Premium Calculation")
    add_body(story, """<b>1. Standard Life Insurance Contractual Clauses:</b>
• <b>Incontestable Clause:</b> After the policy has been in force for a specified period (typically 2 years during the insured's lifetime), the insurer cannot contest or void the death claim on grounds of unintentional misrepresentation.
• <b>Suicide Clause:</b> If the insured commits suicide within the first 1–2 years of policy issue, the insurer does not pay the face value (only refunds premiums paid).
• <b>Grace Period Clause:</b> Grants a 30- or 31-day grace period after a renewal premium due date during which coverage stays in force.
• <b>Reinstatement (Revival) Clause:</b> Allows a lapsed policy to be revived within 2–5 years by paying overdue premiums with interest and providing evidence of insurability.
• <b>Misstatement of Age or Sex Clause:</b> Adjusts the benefit amount to what the premium paid would have purchased at the true age/sex.
• <b>Beneficiary Designation (Primary vs. Contingent; Revocable vs. Irrevocable).</b>

<b>2. Nonforfeiture Options, Dividend (Bonus) Options & Settlement Options:</b>
• <b>Three Nonforfeiture Options (If a Cash-Value Policyholder Stops Paying Premiums):</b> (1) <i>Cash Surrender Value</i> (take cash and terminate policy), (2) <i>Reduced Paid-Up Insurance</i> (keep permanent policy for a smaller face amount with no further premiums), and (3) <i>Extended Term Insurance</i> (keep full face value for a limited term).
• <b>Four Dividend (Participating Policy) Options:</b> (1) Take cash, (2) Reduce next premium, (3) Leave with insurer to accumulate at interest, or (4) Buy paid-up additions (reversionary bonus).
• <b>Five Settlement Options (How Death/Maturity Proceeds Are Paid):</b> (1) Lump-sum cash, (2) Interest option, (3) Fixed-period option, (4) Fixed-amount option, and (5) Life income (annuity) option.

<b>3. Additional Life Insurance Benefits (Riders — Very High Exam Frequency!):</b>
• <b>(1) Waiver of Premium Disability Rider:</b> If the insured becomes totally and permanently disabled before age 60/65, all future premiums are waived while the policy remains 100% in force.
• <b>(2) Accidental Death and Dismemberment (AD&D / Double Indemnity) & Permanent Total Disability (PTD) Rider:</b> Doubles the death benefit if death results from an accident, or pays monthly income/lump sum upon permanent disability.
• <b>(3) Critical Illness (CI) Rider (Accelerated Death Benefit):</b> Pays an immediate tax-free lump sum upon first diagnosis of specified dread diseases (cancer, heart attack, stroke, kidney failure, coronary bypass, organ transplant) to fund medical treatment and lost income.
• <b>(4) Guaranteed Purchase Option (Insured Insurability Rider):</b> Allows young insureds to buy additional life insurance at future milestones without a new medical exam.

<b>4. Taxation of Life Insurance in Nepal (Income Tax Act 2058):</b>
• <b>Tax Benefit on Premiums Paid:</b> A resident natural person can deduct annual life insurance premiums paid up to <b>Rs 40,000</b> from their taxable income (in addition to up to Rs 20,000 for health insurance and Rs 5,000 for personal house insurance).
• <b>Tax on Payouts:</b> Death benefit payouts to beneficiaries are <b>100% exempt from income tax</b>. For maturity/investment gains on policies issued by resident insurers, a <b>5% final withholding tax</b> applies on the net gain (Maturity Payout minus Total Premiums Paid).

<b>5. Actuarial Process of Calculating Life Insurance Premiums (5-Mark Question + Numerical):</b>
Life insurance premiums are calculated using the <b>Actuarial Equivalence Principle</b> (Present Value of Expected Premiums = Present Value of Expected Benefits) based on three factors: <b>(1) Mortality Rate (q_x)</b> from the Mortality Table, <b>(2) Assumed Interest Rate (i)</b>, and <b>(3) Loading</b> for expenses/contingencies:
• <b>Formula for 1-Year Term Net Single Premium (NSP):</b>
  <b>NSP = [ Policy Face Value x Probability of Death at Age x (q_x) ] / (1 + i)^1</b>
• <b>Formula for Gross (Office) Premium:</b>
  <b>Gross Premium = Net Premium + Loading for Expenses, Commissions, Taxes & Bonus</b>.""")

    story.append(PageBreak())

    # ==================== UNIT 6 ====================
    add_unit(story, "UNIT 6: NON-LIFE (GENERAL) INSURANCE & SOCIAL INSURANCE (12 Lecture Hours)")

    add_topic(story, "6.1 Commercial Property & Liability Insurance and Fire Insurance (Nature, Policies, Rating & Claims)")
    add_body(story, """<b>1. Life Insurance vs. Non-Life (General) Insurance (Comparison Table):</b>""")
    t_u6_lnl = make_table([
        [P_hdr("Basis of Difference"), P_hdr("Life Insurance"), P_hdr("Non-Life (General) Insurance")],
        [P("1. Subject Matter", True), P("Human life (health, longevity, mortality)."), P("Property, physical assets, cargo, motor vehicles, and third-party legal liability.")],
        [P("2. Nature of Contract", True), P("<b>Valued (Benefit) Contract:</b> Pays the agreed Sum Assured + Bonus; not a contract of strict indemnity."), P("<b>Strict Contract of Indemnity:</b> Pays only the actual financial loss suffered (up to sum insured).")],
        [P("3. Certainty of Event", True), P("Death is certain (only the timing of death is uncertain)."), P("Occurrence of the peril (fire, accident, flood) is uncertain and may never happen.")],
        [P("4. Policy Duration", True), P("Long-term contract (5, 10, 20, 30 years, or whole life)."), P("Short-term contract (typically <b>1 year</b>, renewable annually).")],
        [P("5. Savings / Investment Element", True), P("Cash-value policies (Endowment/Whole Life) include a major savings/bonus element."), P("No savings or surrender value; pure risk protection only.")],
        [P("6. Insurable Interest Timing", True), P("Must exist at the <b>inception</b> of the policy."), P("Must exist at the <b>time of loss</b> (and inception).")],
    ], col_widths=[105, 198, 197])
    story.append(t_u6_lnl)
    story.append(Spacer(1, 5))

    add_body(story, """<b>2. Fire Insurance: Nature, Types of Policies, Rate Fixation & Claim Settlement (10-Mark Essential):</b>
• <b>Legal Meaning of "Fire":</b> Under a Standard Fire Policy, "fire" requires: (1) <i>Actual ignition/flame</i> (mere heating, scorching, or fermentation is excluded), and (2) <i>Accidental "Hostile Fire"</i> that escapes its intended receptacle (as opposed to a <i>friendly fire</i> inside a stove/furnace).
• <b>Major Types of Fire Insurance Policies:</b>
  1. <i>Specific Policy:</i> Insures property for a specified sum without average clause.
  2. <i>Average Policy (Standard in Nepal):</i> Contains the Condition of Average (coinsurance clause) penalizing under-insurance proportionately.
  3. <i>Valued Policy:</i> Agreed value fixed at inception (for artworks, antiques, jewelry).
  4. <i>Floating (Floater) Policy:</i> Covers fluctuating inventory stored across multiple warehouses under a single sum insured.
  5. <i>Declaration Policy:</i> Designed for businesses with seasonal stock fluctuations; insured declares monthly stock values and premium is adjusted at year-end.
  6. <i>Reinstatement (Replacement Cost) Policy:</i> Pays the cost of replacing damaged machinery/buildings with new assets of the same kind without deducting depreciation.
  7. <i>Consequential Loss (Loss of Profits / Business Interruption) Policy:</i> Covers lost net profit and standing charges during post-fire rebuilding.
• <b>Factors Influencing Rate Fixation in Fire Insurance:</b>
  (1) <i>Construction Material & Design</i> (RCC Class A vs. timber/thatched), (2) <i>Occupancy / Nature of Goods</i> (office vs. chemical/garment factory), (3) <i>Location & Exposure Hazard</i> (proximity to hazardous neighbors), (4) <i>Internal Fire-Protection Appliances</i> (sprinklers, extinguishers, smoke alarms), (5) <i>Public Fire Brigade Access</i>, and (6) <i>Past Loss Experience & Housekeeping</i>.
• <b>Four Methods of Determining Rates in Fire Insurance:</b>
  1. <b>Judgment Rating:</b> Underwriter sets a custom rate for a unique risk based on professional judgment.
  2. <b>Class (Manual / Tariff) Rating:</b> Groups similar buildings (e.g., RCC residential homes) into homogeneous classes with a uniform manual rate.
  3. <b>Schedule Rating:</b> Starts with a baseline "basis rate" for a standard building, <b>adds debits (surcharges)</b> for physical hazards (bad wiring, flammable storage), and <b>subtracts credits (discounts)</b> for fire sprinklers, alarms, and watchmen.
  4. <b>Experience Rating:</b> Modifies the rate based on the large commercial client's own historical claims ratio.""")

    add_topic(story, "6.2 Marine Insurance, Auto (Motor) Insurance, Agriculture Insurance & Social Insurance")
    add_body(story, """<b>1. Marine Insurance (Nature, Policies & Role in International Trade):</b>
• <b>Subject Matter:</b> (i) <i>Hull Insurance</i> (vessel/ship), (ii) <i>Cargo Insurance</i> (goods in ocean/air/inland transit under Institute Cargo Clauses A [All Risks], B, and C), (iii) <i>Freight Insurance</i>, and (iv) <i>Marine Liability</i>.
• <b>Types of Marine Policies:</b> <i>Voyage Policy</i> (from Port A to Port B), <i>Time Policy</i> (for 1 year), <i>Mixed Policy</i>, <i>Open Cover / Floating Cargo Policy</i> (for regular importers/exporters), and <i>Valued vs. Unvalued Policy</i>.
• <b>Marine Losses:</b> <b>Actual Total Loss</b>, <b>Constructive Total Loss</b> (cost of salvage/repair exceeds insured value, so insured abandons vessel to insurer), <b>Particular Average</b> (partial loss borne by the specific cargo owner), and <b>General Average</b> (voluntary sacrifice like jettisoning cargo in a storm to save the whole voyage, shared proportionately by all parties).
• <b>Role in International Trade:</b> Mandatory for opening bank Letters of Credit (LC), enables CIF/CIP Incoterms trade, and protects landlocked importers (like Nepalese businesses importing via Kolkata/Visakhapatnam ports).

<b>2. Auto (Motor) Insurance & Compulsory Third-Party Liability Insurance:</b>
• <b>Coverages in a Comprehensive Motor Policy:</b>
  1. <i>Part A — Third-Party Liability Coverage (Compulsory by Law):</i> Covers bodily injury, permanent disability, death, and property damage caused by the insured vehicle (First Party) to innocent outsiders (Third Parties), plus legal defense costs.
  2. <i>Part B — Medical Payments / Driver, Helper & Passenger Personal Accident Coverage.</i>
  3. <i>Part C — Uninsured / Hit-and-Run Motorists Coverage.</i>
  4. <i>Part D — Own Damage (OD) Coverage:</i> Covers repair/replacement of the insured's own vehicle due to collision, overturning, fire, theft, flood, landslide, or riot (RSMD).

<b>3. Agriculture Insurance in Nepal & Social Insurance (SSF):</b>
• <b>Agriculture Insurance:</b> Covers crops (paddy, maize, vegetables, fruits), livestock (cattle, buffaloes, goats), poultry, fish, and herbs against natural perils and epidemics. In Nepal, the government provides up to an <b>80% subsidy on agriculture insurance premiums</b>—vital because &gt;60% of the population relies on farming, terrain is disaster-prone, and insured crops/cattle serve as bank loan collateral.
• <b>Social Insurance:</b> Compulsory government-mandated programs financed by earmarked payroll contributions to provide a floor of income security:
  1. <i>Old-Age, Survivors, and Disability Insurance (OASDI / Pension)</i>
  2. <i>Medicare / National Health Insurance</i>
  3. <i>Unemployment Insurance</i>
  4. <i>Workers' Compensation Insurance</i> (occupational injury/disease)
  5. <i>Nepal's Contribution-Based Social Security Fund (SSF):</i> 31% monthly contribution (20% employer + 11% employee of basic salary) funding Medical/Maternity, Accident/Disability, Dependent Family, and Old-Age Pension schemes.""")

    # ==================== UNIT 7 ====================
    add_unit(story, "UNIT 7: GOVERNMENT REGULATION OF INSURANCE & NEPAL INSURANCE AUTHORITY (5 Lecture Hours)")

    add_topic(story, "7.1 Reasons for Insurance Regulation, Methods & Areas of Regulation")
    add_body(story, """<b>1. Five Core Reasons Why Insurance is Heavily Regulated (10-Mark Exam Favourite):</b>
• <b>(1) Maintain Insurer Solvency (Protect Public Trust & Financial Stability):</b> Premiums are paid upfront while claims may arise decades later. If an insurer fails, widows, pensioners, and disaster victims lose their financial lifeline.
• <b>(2) Compensate for Inadequate Consumer Knowledge (Information Asymmetry):</b> Insurance policies are complex technical legal contracts of adhesion; ordinary citizens cannot judge policy exclusions or an insurer's financial reserves on their own.
• <b>(3) Ensure Reasonable, Adequate, and Non-Discriminatory Rates:</b>
  - <i>Adequate:</i> High enough to pay claims and prevent cut-throat price wars that bankrupt insurers.
  - <i>Not Excessive:</i> Prevent cartel price-gouging.
  - <i>Not Unfairly Discriminatory:</i> Similar risks must pay equitable rates.
• <b>(4) Make Insurance Available and Accessible (Social Inclusion Goals):</b> Expand micro-insurance, agriculture insurance, and rural branch coverage.
• <b>(5) Prevent Unfair Market Practices & Ensure Prompt Claim Settlement:</b> Stop misleading sales, rebating, and unreasonable claim delays.

<b>2. Three Methods of Regulating Insurers:</b>
• <b>(i) Legislation (Statutory Law):</b> Enacting comprehensive laws—such as the <b>Insurance Act, 2079 (2022)</b> and Insurance Regulations in Nepal.
• <b>(ii) Regulatory Authority (Administrative Supervision):</b> Empowering an autonomous regulator—the <b>Nepal Insurance Authority (NIA / Beema Pradhikaran)</b>—to issue directives, inspect insurers, and enforce solvency.
• <b>(iii) Judicial / Court Decisions & Ombudsman Rulings:</b> Interpreting ambiguous policy clauses and resolving claim disputes.

<b>3. Seven Major Areas of Insurance Regulation & Functions of Nepal Insurance Authority (NIA):</b>
• <b>1. Licensing & Minimum Paid-Up Capital:</b> Vetting promoters and enforcing paid-up capital floors (Rs 5 Billion for Life Insurers, Rs 2.5 Billion for Non-Life Insurers, Rs 750 Million for Micro-Insurers, and Rs 10–20 Billion for Reinsurers in Nepal).
• <b>2. Financial Solvency, Risk-Based Capital (RBC) & Technical Reserves:</b> Enforcing minimum solvency ratios, unearned premium reserves, catastrophe reserves, and annual actuarial valuations.
• <b>3. Investment Regulation:</b> Directing how insurers invest policyholder funds across government bonds, commercial/development bank FDs, infrastructure/hydropower, real estate, and listed shares.
• <b>4. Rate & Tariff Regulation:</b> Approving premium rates and setting tariffs for motor third-party, property/fire, and agriculture insurance.
• <b>5. Policy Form & Product Approval:</b> Vetting all policy wordings and riders before launch.
• <b>6. Licensing & Supervision of Market Intermediaries:</b> Licensing insurance agents, third-party facilitators, and loss surveyors, and enforcing corporate governance and AML/CFT compliance.
• <b>7. Policyholder Protection & Quasi-Judicial Claim Settlement:</b> Hearing policyholder complaints against insurers and ordering claim payments with interest when insurers delay unfairly.""")
