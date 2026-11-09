from past_pdf_base import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def build_past_paper2(story):
    story.append(Paragraph(
        "PAPER 2: TRIBHUVAN UNIVERSITY — BNK 221: CORPORATE FINANCING DECISION<br/>"
        "<font size=10>BBA / Eighth Semester | April 2026 | Full Marks: 100 | Pass Marks: 50 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group 'A': Brief Answer Questions [10 x 2 = 20]", group_header_style))

    add_q(story, "Q1. Define Corporate financing decisions.")
    add_a(story, """<b>Answer:</b> Corporate financing decisions are the strategic decisions made by financial managers concerning the raising of short-term and long-term funds from internal and external sources (debt, preferred stock, and common equity) to finance the firm's assets and operations, aiming to minimize the weighted average cost of capital (WACC) and maximize firm value.""")

    add_q(story, "Q2. State any two factors to be considered while choosing an appropriate source of short-term financing.")
    add_a(story, """<b>Answer:</b> Two primary factors to consider while selecting a source of short-term financing are:
• <b>1. Effective Annual Cost (Interest Rate & Fees):</b> Comparing the true after-tax effective annual interest cost across trade credit, commercial paper, and bank loans.
• <b>2. Availability, Flexibility & Matching Principle:</b> Ensuring the credit source is reliably available when seasonal working capital needs peak and matches the self-liquidating cash conversion cycle.""")

    add_q(story, "Q3. Differentiate between bankruptcy liquidation and reorganization.")
    add_a(story, """<b>Answer:</b>
• <b>Bankruptcy Liquidation (e.g., Chapter 7):</b> The permanent shutdown of an insolvent company where a court-appointed trustee sells off all the firm's assets and distributes the cash proceeds to creditors in strict order of legal priority (when the firm is worth more dead than alive).
• <b>Reorganization (e.g., Chapter 11):</b> A court-supervised restructuring of a financially distressed company's debt obligations (extending maturities, reducing interest rates, or swapping debt for equity) so the business continues operating as a going concern (when the firm is worth more alive than dead).""")

    add_q(story, "Q4. Write the meaning of private equity fund.")
    add_a(story, """<b>Answer:</b> A private equity (PE) fund is a pooled investment vehicle (typically organized as a Limited Partnership managed by a General Partner) that raises capital from institutional and accredited investors (Limited Partners) to acquire significant equity stakes in private companies or take public companies private (via Venture Capital, Growth Equity, or Leveraged Buyouts) with a 5-to-10-year investment horizon.""")

    add_q(story, "Q5. Define initial conversion premium.")
    add_a(story, """<b>Answer:</b> Initial conversion premium is the percentage (or Rupee amount) by which the conversion price (P_c) of a newly issued convertible bond or convertible preferred stock exceeds the current market price of the common stock (P_0) at the time of issuance:
<b>Conversion Premium (%) = [ (P_c - P_0) / P_0 ] x 100</b> (typically set between 15% and 30%).""")

    add_q(story, "Q6. What is warrants?")
    add_a(story, """<b>Answer:</b> A warrant is a long-term company-issued call option (often attached as an "equity sweetener" to a bond or preferred stock issue) that gives the holder the right to purchase a stated number of shares of the issuing company's common stock at a specified exercise price within a stated period of time.""")

    add_q(story, "Q7. Mention the major types of leases.")
    add_a(story, """<b>Answer:</b> The major types of leases are:
• <b>1. Operating Lease</b> (short-term, cancellable, maintained by lessor)
• <b>2. Financial / Capital Lease</b> (long-term, non-cancellable, fully amortized)
• <b>3. Sale and Leaseback</b> (selling an owned asset and leasing it back immediately)
• <b>4. Leveraged Lease</b> (three-party lease involving lessee, lessor, and long-term lender)
• <b>5. Direct Lease</b> (acquiring use of a new asset directly from manufacturer/lessor).""")

    add_q(story, "Q8. If you borrow Rs 100,000 face value at a nominal rate of 10 percent, discount interest, for 6 months, Calculate effective annual rate.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Face value of loan (Principal) = Rs 100,000
• Nominal annual interest rate (i) = 10% = 0.10 (Discount interest)
• Loan maturity = 6 months = 0.5 year (m = 12 / 6 = 2 periods per year)

<b>Step 1: Calculate 6-Month Discount Interest and Usable Proceeds:</b>
• 6-Month Interest = Rs 100,000 x 0.10 x (6 / 12) = <b>Rs 5,000</b>
• Net Usable Funds = Rs 100,000 - Rs 5,000 = <b>Rs 95,000</b>
• 6-Month Periodic Effective Rate (r_p) = Rs 5,000 / Rs 95,000 = <b>0.052632 (5.2632%)</b>

<b>Step 2: Calculate Effective Annual Rate (EAR) and Nominal Annual Rate (APR):</b>
• <b>Compounded Effective Annual Rate (EAR):</b>
  EAR = (1 + r_p)^m - 1 = (1 + 0.052632)^2 - 1 = (1.052632)^2 - 1 = 0.108033 = <b>10.80%</b>
• <b>Simple Annualized Percentage Rate (APR):</b>
  APR = r_p x 2 = 5.2632% x 2 = <b>10.53%</b>
<i>(Note: If 10% is treated as a full-year discount rate: EAR = 0.10 / (1 - 0.10) = <b>11.11%</b>; if 10% is treated as a 6-month rate: EAR = (1 + 10/90)^2 - 1 = <b>23.46%</b>. Showing all ensures full marks!)</i>""")
    add_hint(story, "For a 6-month discount loan at 10% p.a.: 6-month interest = 10% / 2 = 5% (Rs 5,000), usable proceeds = Rs 95,000, so 6-month rate = 5/95 = 5.2632%. Then EAR = (1 + 5/95)^2 - 1 = 10.80% (and APR = 2 x 5.2632% = 10.53%).")

    add_q(story, "Q9. Mr. Shyam Thapa, a dissatisfied stockholder of the Lumbini Company, desires representation on the board. The Lumbini Company, which has 7 directors, has 1 million shares outstanding. How many shares would Mr. Thapa have to control to be assured of 1 directorship under a majority rule (non-cumulative) voting system?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Total shares outstanding (N) = 1,000,000 shares
• Total number of directors (D) = 7 directors
• Voting system: <b>Majority Rule (Non-Cumulative / Straight Voting) System</b>

<b>Step 1: Formula Under Majority Rule (Non-Cumulative) Voting:</b>
Under majority (non-cumulative) voting, each director position is voted on separately, so a shareholder who controls <b>more than 50% of the shares</b> elects <b>every single director</b> (whether 1 director or all 7 directors).
Minimum Shares Required = (N / 2) + 1

<b>Step 2: Substitute the Values:</b>
Minimum Shares Required = (1,000,000 / 2) + 1 = 500,000 + 1 = <b>500,001 shares</b>

<i>(Note for comparison: Had the company used Cumulative Voting, the minimum shares for 1 director would have been [(1,000,000 x 1) / (7 + 1)] + 1 = 125,001 shares.)</i>""")
    add_hint(story, "Read the voting system carefully! Under MAJORITY (Non-Cumulative) voting, you ALWAYS need 50% + 1 shares = (N / 2) + 1 = 500,001 shares to guarantee even 1 director seat! Under CUMULATIVE voting, you need [(N x d) / (D + 1)] + 1.")

    add_q(story, "Q10. Determine the annual percentage interest cost for 2/15 net 60 term of sale assuming that the firm does not take the cash discount but pays on the 40th day.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Credit terms: 2/15, net 60 -> Discount rate (d) = 2% = 0.02; Discount period (DP) = 15 days
• Actual payment day (CP_actual) = 40th day

<b>Step 1: Formula for Annual Percentage Cost (APC) of Not Taking Discount:</b>
APC = [ d / (1 - d) ] x [ Days in Year / (Actual Payment Day - Discount Period) ]

<b>Step 2: Calculate Using 360-Day Year (and 365-Day Year):</b>
• <b>Assuming 360 days in a year:</b>
  APC = [ 0.02 / (1 - 0.02) ] x [ 360 / (40 - 15) ]
  APC = (0.02 / 0.98) x (360 / 25) = 0.020408 x 14.4 = 0.293878 = <b>29.39%</b>
  <i>(Compounded EAR = (1 + 0.02/0.98)^(360/25) - 1 = (1.020408)^14.4 - 1 = <b>33.77%</b>)</i>
• <b>Assuming 365 days in a year:</b>
  APC = (0.02 / 0.98) x (365 / 25) = 0.020408 x 14.6 = <b>29.80%</b>
  <i>(Compounded EAR = (1.020408)^14.6 - 1 = <b>34.31%</b>)</i>""")
    add_hint(story, "Even though the stated credit period is 60 days, the firm actually paid early on the 40th day! Always use the ACTUAL payment day (40 - 15 = 25 days of costly credit) in the denominator—paying on day 40 instead of day 60 after missing the discount makes the annualized percentage cost HIGHER (29.39%)!")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group 'B': Short Answer Questions (Attempt any SIX — ALL Solved) [6 x 5 = 30]", group_header_style))

    add_q(story, "Q11. What do you mean by going private? Write the motivation for going private.")
    add_a(story, """<b>Answer:</b>
<b>Meaning of Going Private:</b>
"Going private" refers to a transaction in which a publicly traded corporation's entire common stock is purchased by a small group of investors—typically existing senior management (in a Management Buyout, MBO) and/or a private equity firm (in a Leveraged Buyout, LBO)—so that the company's shares are delisted from the stock exchange and are no longer traded by the general public.

<b>Motivations (Reasons) for Going Private:</b>
• <b>1. Elimination of High Regulatory and Listing Compliance Costs:</b> Saves substantial annual outlays on securities regulator filings, public audits, quarterly reporting, shareholder meetings, and stock exchange listing fees.
• <b>2. Freedom from Short-Term Market Myopia:</b> Public managers face intense pressure to meet quarterly earnings targets. Going private allows management to focus on long-term strategic restructuring, R&D, and capital investments without worrying about daily stock price fluctuations.
• <b>3. Alignment of Ownership and Management Incentives (Reduced Agency Costs):</b> When managers become significant equity owners, agency conflicts disappear and managers work aggressively to cut waste and boost cash flows.
• <b>4. Tax Shield Benefits from High Leverage ( in LBOs):</b> Financing the buyout with substantial debt creates large tax-deductible interest shields.
• <b>5. Confidentiality and Protection from Hostile Takeovers:</b> Private companies do not have to disclose sensitive strategic and financial data to competitors and are immune from hostile takeover bids.""")

    add_q(story, "Q12. Describe the factors affecting of determining capital structure in a business organization.")
    add_a(story, """<b>Answer:</b> A firm's capital structure decision (the mix of debt and equity) is governed by several internal and external factors:
• <b>1. Stability and Predictability of Sales and Cash Flows:</b> Firms with stable, predictable revenues (e.g., utilities, consumer staples) can safely carry higher fixed-interest debt than cyclical firms.
• <b>2. Asset Structure (Tangibility of Assets):</b> Firms with large general-purpose tangible fixed assets (real estate, machinery) have strong collateral to secure low-cost long-term debt, whereas R&D/intangible-heavy firms rely more on equity.
• <b>3. Operating Leverage:</b> A firm with high fixed operating costs (high operating leverage) already has high business risk and should use less debt (lower financial leverage) to keep total risk manageable.
• <b>4. Corporate Tax Rate:</b> Because interest on debt is tax-deductible, firms in higher income-tax brackets gain a larger debt tax shield and favor higher leverage.
• <b>5. Profitability and Internal Cash Generation (Pecking Order):</b> Highly profitable firms with abundant retained earnings often require less external debt financing.
• <b>6. Management Attitude and Control Considerations:</b> Conservative managers or founders who fear losing voting control or violating debt covenants prefer debt or internal equity cautiously depending on control dilution.
• <b>7. Credit Rating, Lender Attitudes, and Capital Market Conditions:</b> Prevailing interest rates and bank/rating agency benchmarks cap how much debt a firm can issue without a rating downgrade.""")

    add_q(story, "Q13. Delphi shoes Company has warrants issued that allow the holder to purchase 4 shares of stock for a total of Rs 100 each for each warrant. Currently the market price per share of the company is Rs 20. Investor hold the following probabilistic benefit about the stock 6 month hence.\n[Market price per share: Rs 15 (Prob 0.30), Rs 20 (Prob 0.25), Rs 25 (Prob 0.20), Rs 30 (Prob 0.25)]\na. What is the present theoretical value of warrant?\nb. What is the expected value of stock price 6 month hence?\nc. What is the expected theoretical value of warrant 6 month hence? [1+2+2]")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Number of shares purchased per warrant (N) = 4 shares
• Total exercise price for 4 shares per warrant = Rs 100  =>  <b>Exercise price per share (E) = Rs 100 / 4 = Rs 25 per share</b>
  <i>(Formula for Theoretical Value of Warrant: TV = (P_0 x N) - Total Exercise Cost = (P_0 - E) x N)</i>
• Current market price per share (P_0) = Rs 20

<b>a. Present Theoretical Value of Warrant [1 Mark]:</b>
• Formula TV = (P_0 - E) x N = (20 - 25) x 4 = (20 x 4) - 100 = 80 - 100 = <b>-Rs 20</b>
• Since a warrant cannot have a negative market/exercise value, its effective <b>Present Theoretical Value (Floor Value) = Rs 0</b>.

<b>b. Expected Value of Stock Price 6 Months Hence, E(P) [2 Marks]:</b>
E(P) = Sum [ P_i x Prob(P_i) ]
E(P) = (Rs 15 x 0.30) + (Rs 20 x 0.25) + (Rs 25 x 0.20) + (Rs 30 x 0.25)
E(P) = 4.50 + 5.00 + 5.00 + 7.50 = <b>Rs 22.00 per share</b>

<b>c. Expected Theoretical Value of Warrant 6 Months Hence [2 Marks]:</b>
• <b>Method 1 (Probability-Weighted Expected Warrant Value Across All 4 Stock Price States — Exact Finance Method):</b>
  - If P = Rs 15 (Prob 0.30): TV = max(15 x 4 - 100, 0) = max(-40, 0) = <b>Rs 0</b>
  - If P = Rs 20 (Prob 0.25): TV = max(20 x 4 - 100, 0) = max(-20, 0) = <b>Rs 0</b>
  - If P = Rs 25 (Prob 0.20): TV = max(25 x 4 - 100, 0) = max(0, 0) = <b>Rs 0</b>
  - If P = Rs 30 (Prob 0.25): TV = max(30 x 4 - 100, 0) = max(120 - 100, 0) = <b>Rs 20</b>
  - <b>Expected Theoretical Value E(TV)</b> = (0 x 0.30) + (0 x 0.25) + (0 x 0.20) + (20 x 0.25) = <b>Rs 5.00</b>
• <b>Method 2 (Evaluated Directly at Expected Stock Price E(P) = Rs 22.00):</b>
  - Formula TV at E(P) = (22 x 4) - 100 = 88 - 100 = <b>-Rs 12.00</b> (or Minimum Floor Value = <b>Rs 0</b>).""")
    add_hint(story, "Read 'purchase 4 shares of stock for a total of Rs 100 for each warrant' carefully: Total Exercise Price = Rs 100 for 4 shares (i.e. E = Rs 25/share). In Part (c), write BOTH Method 1 (E(TV) = 20 x 0.25 = Rs 5.00) and Method 2 (Formula TV = 4(22) - 100 = -Rs 12 -> Floor Rs 0) so you get full marks under either marking scheme!")

    add_q(story, "Q14. Explain the concept and importance of venture capital.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Venture Capital:</b>
Venture capital (VC) is long-term, active risk equity (or convertible security) capital provided by professional institutional venture capital funds to young, rapidly growing, innovative private companies that have high growth potential but lack the operating history and tangible collateral needed to obtain conventional bank loans or access public capital markets.

<b>Importance of Venture Capital:</b>
• <b>1. Seed & Early-Stage Capital for Innovation:</b> Enables entrepreneurs to commercialize new technologies, software, biotech, and business models.
• <b>2. Value-Added Managerial Mentorship:</b> Venture capitalists sit on the board, assist in strategic planning, recruit key executives, and connect startups with customers, suppliers, and investment banks.
• <b>3. Patience and Risk Absorption:</b> Unlike bank loans that demand monthly interest from day one, VC shares business risk and waits 5–7 years to realize capital gains via an IPO or trade sale.
• <b>4. Certification Effect:</b> Backing from a respected VC fund signals credibility and helps the startup attract follow-on financing and top talent.
• <b>5. Macroeconomic Growth and Employment Generation:</b> Drives entrepreneurship, productivity, tax revenues, and skilled job creation.""")

    add_q(story, "Q15. Discuss merits and demerits of long term debt.")
    add_a(story, """<b>Answer:</b>
<b>Merits (Advantages) of Long-Term Debt:</b>
• <b>1. Tax Deductibility of Interest:</b> Interest expense reduces taxable income, providing a valuable tax shield and lowering the effective after-tax cost of debt: k_dt = k_d(1 - T).
• <b>2. Preservation of Ownership and Voting Control:</b> Creditors have no voting rights in general meetings, so existing shareholders retain 100% control.
• <b>3. Positive Financial Leverage (Trading on Equity):</b> When Return on Assets (ROA) exceeds the interest rate on debt, fixed-cost debt magnifies EPS and ROE for common stockholders.
• <b>4. Limited Claim on Profits:</b> Bondholders do not share in super-normal profits when the company is highly successful.

<b>Demerits (Disadvantages) of Long-Term Debt:</b>
• <b>1. Increased Financial Risk and Bankruptcy Threat:</b> Fixed interest and principal payments must be made regardless of earnings; default can trigger foreclosure or bankruptcy liquidation.
• <b>2. Restrictive Indenture Covenants:</b> Lenders impose strict limits on dividends, further borrowing, working capital, and asset sales.
• <b>3. Fixed Maturity & Sinking Fund Cash Drain:</b> Debt must be redeemed at maturity, requiring periodic cash outflows.
• <b>4. Loss of Future Financing Flexibility:</b> Mortgaging assets today reduces emergency borrowing capacity during future downturns.""")

    add_q(story, "Q16. The management of Seti Food Company Limited decided to buy a small equipment taking a loan Rs 100,000 for 3 years from Nepal Bank Limited. The loan bears an annual interest of 10 percent and calls for equal annual installment payments at the end of each of the 3 years.\na. Calculate amount of annual payment.\nb. Prepare Loan amortization schedule.\nc. Calculate equal monthly installment (EMI). [1+3+1]")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Loan Principal (P_0) = Rs 100,000; Term (n) = 3 years; Annual interest rate (i) = 10% = 0.10

<b>a. Calculation of Equal Annual Installment Payment (PMT) [1 Mark]:</b>
• Present Value Interest Factor of Annuity, PVIFA(10%, 3 years) = [ 1 - (1 + 0.10)^(-3) ] / 0.10 = <b>2.486852</b>
• Annual Installment (PMT) = P_0 / PVIFA(10%, 3 yrs) = Rs 100,000 / 2.486852 = <b>Rs 40,211.48</b> (or Rs 40,211.11 using 2.4869)

<b>b. Loan Amortization Schedule (3 Years) [3 Marks]:</b>""")
    t16_amort = make_table([
        [P_hdr("Year"), P_hdr("Beginning Principal (Rs)"), P_hdr("Annual Installment (PMT) (Rs)"), P_hdr("Interest @ 10% (Col 2 x 0.10) (Rs)"), P_hdr("Principal Repayment (Col 3 - Col 4) (Rs)"), P_hdr("Ending Balance (Col 2 - Col 5) (Rs)")],
        [P("1"), P("100,000.00"), P("40,211.48"), P("10,000.00"), P("30,211.48"), P("69,788.52")],
        [P("2"), P("69,788.52"), P("40,211.48"), P("6,978.85"), P("33,232.63"), P("36,555.89")],
        [P("3"), P("36,555.89"), P("40,211.48"), P("3,655.59"), P("36,555.89"), P("0.00")],
        [P("Total", True), P("—"), P("120,634.44", True), P("20,634.44", True), P("100,000.00", True), P("—")],
    ], col_widths=[35, 90, 95, 95, 95, 90])
    story.append(t16_amort)
    story.append(Spacer(1, 4))

    add_a(story, """<b>c. Calculation of Equal Monthly Installment (EMI) [1 Mark]:</b>
• Number of monthly payments (n_m) = 3 x 12 = <b>36 months</b>
• Monthly interest rate (i_m) = 10% / 12 = <b>0.0083333 (0.8333% per month)</b>
• PVIFA(0.8333%, 36 months) = [ 1 - (1 + 0.10/12)^(-36) ] / (0.10/12) = <b>30.991236</b>
• <b>Equal Monthly Installment (EMI)</b> = Rs 100,000 / 30.991236 = <b>Rs 3,226.72 per month</b>
  <i>(Note: Simple division of annual installment by 12 = Rs 40,211.48 / 12 = Rs 3,350.96.)</i>""")
    add_hint(story, "In a Loan Amortization Table, Ending Balance in Year 3 MUST be 0.00, and Total Principal Repayment MUST equal the original loan (Rs 100,000). For Monthly EMI, convert n = 3 x 12 = 36 months and r = 10%/12 = 0.8333%!")

    add_q(story, "Q17. Define Financial distress. Also write the common causes and signs of financial distress in companies. [2+3]")
    add_a(story, """<b>Answer:</b>
<b>1. Definition of Financial Distress [2 Marks]:</b>
Financial distress is a severe financial condition in which a business cannot generate sufficient operating cash flows to meet its maturing financial obligations (such as interest payments, principal repayments, wages, and supplier bills) as they fall due, forcing the firm toward asset sales, debt restructuring, or legal insolvency/bankruptcy.

<b>2. Common Causes and Warning Signs of Financial Distress [3 Marks]:</b>
• <b>Common Causes of Financial Distress:</b>
  1. <i>Excessive Financial Leverage (Over-Borrowing):</i> High fixed interest obligations that cannot be sustained when sales dip.
  2. <i>Poor Working Capital & Liquidity Management:</i> Over-investment in slow-moving inventory, uncollectible receivables, or financing long-term fixed assets with short-term loans.
  3. <i>High Operating Leverage & Declining Industry Demand:</i> Heavy fixed operating costs combined with intense competition, technological obsolescence, or macroeconomic downturns.
  4. <i>Managerial Incompetence & Unprofitable Expansion:</i> Overpaying for acquisitions or poor cost control.
• <b>Early Warning Signs (Symptoms) of Financial Distress:</b>
  1. Persistent negative operating cash flows and chronic working capital deficits.
  2. Delaying payments to trade creditors (stretching accounts payable 30–90 days past due) and defaulting on bank interest.
  3. Dividend reductions or complete omission of dividend payments.
  4. Deteriorating financial ratios (falling current ratio, interest coverage ratio < 1, rising debt-to-equity ratio) and credit rating downgrades.
  5. Resignation of key executives/auditors, plant shutdowns, and distress sales of core assets.""")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group 'C': Long Answer Questions (Attempt any THREE — ALL Solved) [3 x 10 = 30]", group_header_style))

    add_q(story, "Q18. Explain the methods of issuing securities. Also discuss the process of initial public offering (IPO).")
    add_a(story, """<b>Answer:</b>
<b>1. Methods of Issuing Securities in the Primary Market:</b>
• <b>(a) Public Issue via Prospectus (IPO & FPO):</b> Selling securities directly to the general public at large through an Initial Public Offering (first-time public sale by an unlisted company) or a Follow-on Public Offering (seasoned issue by an already listed company).
• <b>(b) Rights Offering (Privileged Subscription):</b> Offering new shares to existing shareholders on a pro-rata basis at a discounted subscription price to honour their preemptive rights.
• <b>(c) Private Placement:</b> Selling an entire issue of bonds or equity directly to a small group of institutional investors (insurance companies, mutual funds, pension funds, venture capital funds) without a public prospectus—saving time and flotation costs.
• <b>(d) Offer for Sale / Bought-Out Deal:</b> Selling the securities en bloc to an investment bank or issue house, which then resells them to the public.
• <b>(e) Book Building & Shelf Registration:</b> Discovering the issue price through institutional bidding (book building) or registering a master prospectus to sell securities in tranches over time (shelf registration).

<b>2. Step-by-Step Process of Initial Public Offering (IPO):</b>
• <b>Step 1: Internal Corporate Authorization:</b> Pass a Board of Directors resolution and obtain shareholder approval at the General Meeting to convert/issue public capital.
• <b>Step 2: Appointment of Issue Manager and Underwriter:</b> Select a licensed merchant banker (Issue Manager) to conduct due diligence, structure the issue, and underwrite the offering.
• <b>Step 3: Credit Rating and Preparation of Draft Prospectus:</b> Obtain an IPO grading/credit rating from a rating agency (e.g., ICRA/CARE Nepal) and draft the prospectus containing audited financials, risk factors, and use of proceeds.
• <b>Step 4: Filing & Approval from Securities Regulator (SEBON / SEC):</b> Submit the registration statement and prospectus to the regulator; address regulatory comments during the cooling-off period until final approval is granted.
• <b>Step 5: Publication of Offer Document & Opening of Subscription:</b> Publish the approved prospectus/notice in national daily newspapers and open public subscription (e.g., through C-ASBA participating banks).
• <b>Step 6: Issue Closure, Basis of Allotment & Refund:</b> Close subscription, verify applications, allot shares (minimum 10 units per applicant / lottery system in Nepal), and unblock/refund unallotted money.
• <b>Step 7: Demat Credit & Secondary Market Listing:</b> Credit allotted shares into investors' Demat accounts at CDSC and list the shares on the Stock Exchange (NEPSE) for secondary trading.""")

    add_q(story, "Q19. The Himal Company wishes to evaluate two plans, leasing and borrowing to purchase, for financing an oven. The firm is in the 40 percent tax bracket.\nLease: The company can lease the oven under a 5 years lease requiring annual end of year payment of Rs 14,000.\nPurchase: The oven costs Rs 50,000 and will have a 5-year life. It will be depreciated under straight line depreciation method. The total purchase price will be financed by a 5-years, 10% loan requiring equal annual end of year payments. The salvage value is zero.\na. Calculate the present value of leasing.\nb. Calculate the present value of purchasing.\nc. Which alternative, lease or purchase, would you recommend? Why? [4+4+2]")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Corporate tax rate (T) = 40% = 0.40
• Annual lease payment (L) = Rs 14,000 at the end of Years 1 to 5
• Purchase cost of oven (I_0) = Rs 50,000; Useful life (n) = 5 years; Salvage value (SV) = Rs 0
• Before-tax cost of debt (k_d) = 10%  =>  <b>After-tax cost of debt (k_dt) = 10% x (1 - 0.40) = 6%</b>
• Present Value Annuity Factor at 6% for 5 years:
  PVIFA(6%, 5 yrs) = [ 1 - (1.06)^(-5) ] / 0.06 = <b>4.212364</b> (or 4.2124)

<b>a. Present Value of Cost of Leasing [4 Marks]:</b>
• Annual after-tax lease cash outflow = L x (1 - T) = Rs 14,000 x (1 - 0.40) = <b>Rs 8,400 per year</b>
• <b>Present Value of Leasing</b> = Rs 8,400 x PVIFA(6%, 5 yrs)
  = Rs 8,400 x 4.212364 = <b>Rs 35,383.86</b> (or Rs 35,384.16 using 4.2124)

<b>b. Present Value of Cost of Purchasing (Borrowing to Buy) [4 Marks]:</b>
• Annual Straight-Line Depreciation = (Rs 50,000 - 0) / 5 = <b>Rs 10,000 per year</b>
• Annual Depreciation Tax Shield = Rs 10,000 x 0.40 = <b>Rs 4,000 per year</b>
• <i>(Note on Loan Schedule: A 5-year 10% loan of Rs 50,000 has annual installment PMT = 50,000 / PVIFA(10%, 5) = 50,000 / 3.790787 = Rs 13,189.87. Because the loan is discounted at the after-tax debt rate k_dt = 6%, the Present Value of loan principal + after-tax interest payments is identically equal to the initial Rs 50,000 purchase price!)</i>
• <b>Present Value of Purchasing</b> = Initial Cost - PV of Depreciation Tax Shields
  = Rs 50,000 - [ Rs 4,000 x PVIFA(6%, 5 yrs) ]
  = Rs 50,000 - (Rs 4,000 x 4.212364)
  = Rs 50,000 - Rs 16,849.46 = <b>Rs 33,150.54</b> (or Rs 33,150.40 using 4.2124)"""),
    t19_loan = make_table([
        [P_hdr("Year"), P_hdr("Loan Payment (Rs)"), P_hdr("Interest @ 10% (Rs)"), P_hdr("Depreciation (Rs)"), P_hdr("Tax Shield 40% x (Int+Dep) (Rs)"), P_hdr("Net Cash Outflow (Col 2 - Col 5)"), P_hdr("PV @ 6% (Rs)")],
        [P("1"), P("13,189.87"), P("5,000.00"), P("10,000.00"), P("6,000.00"), P("7,189.87"), P("6,782.90")],
        [P("2"), P("13,189.87"), P("4,181.01"), P("10,000.00"), P("5,672.41"), P("7,517.46"), P("6,690.51")],
        [P("3"), P("13,189.87"), P("3,280.13"), P("10,000.00"), P("5,312.05"), P("7,877.82"), P("6,614.37")],
        [P("4"), P("13,189.87"), P("2,289.15"), P("10,000.00"), P("4,915.66"), P("8,274.21"), P("6,553.95")],
        [P("5"), P("13,189.87"), P("1,199.08"), P("10,000.00"), P("4,479.63"), P("8,710.24"), P("6,508.81")],
        [P("Total PV of Purchasing", True), P(""), P(""), P(""), P(""), P(""), P("33,150.54", True)],
    ], col_widths=[32, 72, 72, 72, 92, 85, 75])
    story.append(t19_loan)
    story.append(Spacer(1, 4))

    add_a(story, """<b>c. Recommendation [2 Marks]:</b>
Since the Present Value of Cost of Purchasing (<b>Rs 33,150.54</b>) is lower than the Present Value of Cost of Leasing (<b>Rs 35,383.86</b>) by <b>Rs 2,233.32</b> (Net Advantage to Leasing = -Rs 2,233.32), Himal Company should <b>BORROW AND PURCHASE the oven</b>.""")
    add_hint(story, "Whether you use the quick formula [PV(Buy) = 50,000 - 4,000 x PVIFA(6%, 5) = Rs 33,150.54] or the full 5-year loan amortization schedule table above, both give the EXACT same answer: Rs 33,150.54! Use the quick formula to verify your table in 10 seconds!")

    add_q(story, "Q20. The Nepal textile company plans to raise an additional Rs 10 million through rights offering. Current market price of the company is Rs 250. It has 200,000 shares outstanding. Stockholders are offered a new share at a price of Rs 100 each. You are asked to answer following questions.\na. How many new shares will have to be sold to raise required funds?\nb. How many rights will be required to purchase a new share?\nc. What will be theoretical value of a right and ex-right price?\nd. Mr. Ram Shrestha's total assets consist of 100 shares of Nepal Textile Company and cash balance of Rs 15,000. Prepare statements of Mr. Shrestha's total assets before rights offerings.\ne. Prepare statement showing Mr. Shrestha total assets after right offerings for each of these course of actions if he:\n   i. Sell all his rights.\n   ii. Exercise all his rights. [1+1+3+2+3]")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Funds to be raised = Rs 10,000,000 (Rs 10 million)
• Rights-on market price per share (P_0) = Rs 250
• Existing shares outstanding (N_0) = 200,000 shares
• Subscription price per new share (P_s) = Rs 100

<b>a. Number of New Shares to Be Sold (N_1) [1 Mark]:</b>
N_1 = Funds to be Raised / Subscription Price (P_s) = Rs 10,000,000 / Rs 100 = <b>100,000 new shares</b>

<b>b. Number of Rights Required to Purchase One New Share (#) [1 Mark]:</b>
# = Existing Shares (N_0) / New Shares (N_1) = 200,000 / 100,000 = <b>2 rights per new share</b>

<b>c. Theoretical Value of a Right (V_r) and Ex-Rights Price (P_e) [3 Marks]:</b>
• <b>Theoretical Value of One Right (V_r):</b>
  V_r = (P_0 - P_s) / (# + 1) = (250 - 100) / (2 + 1) = 150 / 3 = <b>Rs 50 per right</b>
• <b>Ex-Rights Price of Stock (P_e):</b>
  P_e = P_0 - V_r = Rs 250 - Rs 50 = <b>Rs 200 per share</b>

<b>d. Statement of Mr. Ram Shrestha's Total Assets BEFORE Rights Offering [2 Marks]:</b>
• Value of 100 shares @ Rs 250 (rights-on price) = 100 x Rs 250 = Rs 25,000
• Cash balance = Rs 15,000
• <b>Total Assets Before Rights Offering = Rs 25,000 + Rs 15,000 = Rs 40,000</b>

<b>e. Statement of Mr. Ram Shrestha's Total Assets AFTER Rights Offering [3 Marks]:</b>
• <b>(i) If He Sells All His 100 Rights (@ Rs 50 each):</b>
  - Value of 100 existing shares at Ex-Rights Price (Rs 200) = 100 x Rs 200 = Rs 20,000
  - Existing Cash + Cash from selling 100 rights = Rs 15,000 + (100 x Rs 50) = Rs 20,000
  - <b>Total Assets After Selling Rights = Rs 20,000 + Rs 20,000 = Rs 40,000</b>
• <b>(ii) If He Exercises All His 100 Rights:</b>
  - Number of new shares purchased with 100 rights = 100 rights / 2 rights per share = <b>50 new shares</b>
  - Cash paid to subscribe to 50 new shares @ Rs 100 = 50 x Rs 100 = Rs 5,000
  - Value of Total Shares (100 + 50 = 150 shares) @ Ex-Rights Price (Rs 200) = 150 x Rs 200 = Rs 30,000
  - Remaining Cash Balance = Rs 15,000 - Rs 5,000 = Rs 10,000
  - <b>Total Assets After Exercising Rights = Rs 30,000 + Rs 10,000 = Rs 40,000</b>""")
    add_hint(story, "In Rights Offering wealth statements (parts d & e), Total Wealth MUST stay identical (Rs 40,000) Before, After Selling Rights, and After Exercising Rights! If your three totals match Rs 40,000, your math is 100% verified!")

    add_q(story, "Q21. The Delta company wishes to borrow Rs 100,000 for 1 year. It must choose one of the following alternatives.\na. 9 percent loan on a collect basis, with face value due at end.\nb. 8.4 percent loan on a discount basis, with face value due at the end.\nc. 6 percent loan on an add on basis, with equal quarterly payments required on the initial face value.\nCalculate the effective cost of each alternative, using annual compounding for the first two alternatives and quarterly compounding for the last. Which one alternative would you recommend? [3+3+3+1]")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b> Face value of loan = Rs 100,000; Maturity = 1 year.

<b>a. 9% Loan on a Collect (Simple Interest) Basis [3 Marks]:</b>
• Interest paid at year-end = Rs 100,000 x 0.09 = Rs 9,000; Usable funds = Rs 100,000
• <b>Effective Annual Cost (EAR_a)</b> = Rs 9,000 / Rs 100,000 = <b>9.00%</b>

<b>b. 8.4% Loan on a Discount Basis [3 Marks]:</b>
• Discount interest deducted upfront = Rs 100,000 x 0.084 = Rs 8,400
• Usable proceeds received = Rs 100,000 - Rs 8,400 = Rs 91,600
• <b>Effective Annual Cost (EAR_b)</b> = Interest / Usable Funds = 8,400 / 91,600 = 0.091703 = <b>9.17%</b>

<b>c. 6% Add-On Loan with Equal Quarterly Payments (Quarterly Compounding) [3 Marks]:</b>
• Total Add-On Interest for 1 year = Rs 100,000 x 0.06 = Rs 6,000
• Total Amount Repayable over 4 quarters = Rs 100,000 + Rs 6,000 = Rs 106,000
• Equal Quarterly Installment (PMT) = Rs 106,000 / 4 = <b>Rs 26,500 per quarter</b>
• <b>Exact TVM / IRR Method:</b>
  Rs 100,000 = Rs 26,500 x PVIFA(r_q, 4 quarters)  =>  PVIFA(r_q, 4) = 100,000 / 26,500 = <b>3.773585</b>
  Solving for quarterly periodic rate r_q (by interpolation between 2% [3.8077] and 3% [3.7171]):
  r_q = <b>2.3722% per quarter</b> (or nominal APR = 2.3722% x 4 = <b>9.49%</b>)
  <b>Effective Annual Rate (Quarterly Compounding, EAR_c)</b> = (1 + 0.023722)^4 - 1 = <b>9.83%</b>
  <i>(Note: Using standard Approximate Add-On Formula: Nominal APR = (2 x m x I) / [P x (m + 1)] = (2 x 4 x 6,000) / [100,000 x (4 + 1)] = 48,000 / 500,000 = <b>9.60%</b> [quarterly rate = 2.40%], and Compounded EAR = (1 + 0.024)^4 - 1 = <b>9.95%</b>.)</i>

<b>d. Recommendation [1 Mark]:</b>
Comparing the effective annual costs: Alternative (a) = <b>9.00%</b>, Alternative (b) = <b>9.17%</b>, and Alternative (c) = <b>9.83% (or 9.95%)</b>. Delta Company should select <b>Alternative (a) (9% Collect Basis Loan)</b> because it has the lowest effective annual cost (<b>9.00%</b>).""")
    add_hint(story, "An Add-On installment loan looks cheap (6% stated rate), but because you repay principal every quarter, your average usable balance is only about half the loan! Quick formula for Add-On APR = (2 x m x I) / [P x (m + 1)] = (2 x 4 x 6,000) / (100,000 x 5) = 9.60%, and quarterly compounded EAR = (1 + 0.096/4)^4 - 1 = 9.95% (or exact IRR = 9.83%).")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group 'D': Comprehensive Answer / Case / Situation Analysis [20 Marks]", group_header_style))

    add_q(story, "Q22. Case Study: The Himalaya Herbal Company (HHC)\nBank loan under line of credit has risen to Rs 250,000 (carrying 8% interest), and HHC is 30–60 days late paying trade creditors. HHC decides to raise Rs 500,000 long-term capital:\nAlternative 1: Sell 8% convertible bonds, convertible into 100 shares per Rs 1,000 bond (conversion price = Rs 10/share).\nAlternative 2: Sell 8% debentures, each Rs 1,000 bond carrying 100 warrants to buy common stock at Rs 10.\nCurrent Balance Sheet: Current liabilities = Rs 400,000; Common stock (par Re 1) = Rs 100,000 (100,000 shares); Retained earnings = Rs 50,000; Total assets = Total claims = Rs 550,000.\nIncome Statement: Sales = Rs 1,100,000; All costs except interest = Rs 990,000; EBIT = Rs 110,000; Interest = Rs 20,000; EBT = Rs 90,000; Taxes (40%) = Rs 36,000; Net income = Rs 54,000; Shares = 100,000; EPS = Rs 0.54; P/E = 15.83x; Market price = Rs 8.55.\na. Discuss the reasons for using convertible bond and bond with warrants to raise long-term fund.\nb. Show the new balance sheet before and after conversion of the convertible bonds.\nc. Show the new balance sheet before and after exercise of warrant.\nd. What is the earnings per share of each alternative, if it is assumed that profits before interest and taxes will be 20 percent of total assets?\ne. Which of the three alternatives would you recommend? [4+4+4+6+2]")
    add_a(story, """<b>Answer (Comprehensive Case Study Solution):</b>

<b>a. Reasons for Using Convertible Bonds and Bonds with Warrants [4 Marks]:</b>
• <b>1. Lower Coupon Rate ("Equity Sweetener"):</b> Because HHC is small, rapidly growing, and currently stretched on short-term credit, straight long-term debt would demand a very high interest rate. Attaching conversion rights or warrants allows HHC to borrow at a modest 8% rate.
• <b>2. Selling Common Stock at a Premium Over Current Market Price:</b> HHC's stock currently trades at Rs 8.55, whereas the conversion/warrant exercise price is Rs 10.00 (a 17% premium), issuing fewer shares than an immediate common stock sale at Rs 8.55.
• <b>3. Replacing Urgent Short-Term Bank Debt & Trade Payables:</b> Raising Rs 500,000 pays off the Rs 250,000 8% bank credit line (and overdue trade creditors) while funding growth.
• <b>4. Future Equity Inflow (Under Warrants):</b> When the 50,000 warrants are exercised at Rs 10, HHC receives an additional Rs 500,000 in fresh cash while retaining the Rs 500,000 debentures.

<b>Working Notes for Balance Sheets (Parts b & c):</b>
• Number of Rs 1,000 bonds issued = Rs 500,000 / Rs 1,000 = <b>500 bonds</b>.
• New shares upon Conversion (Alt 1) or Warrant Exercise (Alt 2) = 500 bonds x 100 shares = <b>50,000 new shares</b> at Rs 10/share (Par Re 1 -> Common Stock increases by Rs 50,000; Paid-in Capital/Share Premium increases by 50,000 x Rs 9 = Rs 450,000).
• <b>Application of the Rs 500,000 Raised:</b>
  - <b>Standard Case (Retiring Rs 250,000 Bank Loan + Rs 250,000 Asset Expansion):</b> Out of Rs 500,000 raised, Rs 250,000 pays off the 8% bank loan (reducing Current Liabilities from Rs 400,000 to <b>Rs 150,000</b> and eliminating the Rs 20,000 bank loan interest), and the remaining Rs 250,000 increases Total Assets from Rs 550,000 to <b>Rs 800,000</b>. Upon exercise of warrants, an additional Rs 500,000 cash enters, raising Total Assets to <b>Rs 1,300,000</b>.
  - <i>(Alternative Textbook Assumption where Current Liabilities stay Rs 400,000 and Total Assets become Rs 550,000 + Rs 500,000 = Rs 1,050,000 [and Rs 1,550,000 after warrant exercise] is also noted below!)</i>

<b>b & c. New Balance Sheets Before and After Conversion (Alt 1) and Warrant Exercise (Alt 2) [4+4 = 8 Marks]:</b>""")
    t22_bs = make_table([
        [P_hdr("Claims / Liabilities & Equity"), P_hdr("Current (Rs)"), P_hdr("Alt 1 Conv: Before Conv. (Rs)"), P_hdr("Alt 1 Conv: After Conv. (Rs)"), P_hdr("Alt 2 Warrant: Before Ex. (Rs)"), P_hdr("Alt 2 Warrant: After Ex. (Rs)")],
        [P("Current Liabilities (Bank loan paid)"), P("400,000"), P("150,000"), P("150,000"), P("150,000"), P("150,000")],
        [P("8% Convertible Bonds"), P("0"), P("500,000"), P("0"), P("0"), P("0")],
        [P("8% Debentures (Straight Debt)"), P("0"), P("0"), P("0"), P("500,000"), P("500,000")],
        [P("Common Stock (Par Re 1)"), P("100,000"), P("100,000"), P("150,000"), P("100,000"), P("150,000")],
        [P("Additional Paid-in Capital (Rs 9/sh)"), P("0"), P("0"), P("450,000"), P("0"), P("450,000")],
        [P("Retained Earnings"), P("50,000"), P("50,000"), P("50,000"), P("50,000"), P("50,000")],
        [P("Total Assets = Total Claims", True), P("550,000", True), P("800,000", True), P("800,000", True), P("800,000", True), P("1,300,000", True)],
    ], col_widths=[135, 63, 78, 74, 78, 72])
    story.append(t22_bs)
    story.append(Spacer(1, 5))

    add_a(story, """<b>d. Computation of Earnings Per Share (EPS) Under Each Alternative (EBIT = 20% of Total Assets) [6 Marks]:</b>""")
    t22_eps = make_table([
        [P_hdr("Income Statement Items"), P_hdr("Current"), P_hdr("Alt 1: Before Conversion"), P_hdr("Alt 1: After Conversion"), P_hdr("Alt 2: Before Exercise"), P_hdr("Alt 2: After Exercise")],
        [P("Total Assets (Rs)"), P("550,000"), P("800,000"), P("800,000"), P("800,000"), P("1,300,000")],
        [P("EBIT (20% of Total Assets)"), P("110,000"), P("160,000"), P("160,000"), P("160,000"), P("260,000")],
        [P("Less: Interest (8% on Debt)"), P("20,000"), P("40,000"), P("0"), P("40,000"), P("40,000")],
        [P("Earnings Before Taxes (EBT)"), P("90,000"), P("120,000"), P("160,000"), P("120,000"), P("220,000")],
        [P("Less: Taxes @ 40%"), P("36,000"), P("48,000"), P("64,000"), P("48,000"), P("88,000")],
        [P("Net Income (EAT) (Rs)", True), P("54,000", True), P("72,000", True), P("96,000", True), P("72,000", True), P("132,000", True)],
        [P("Common Shares Outstanding"), P("100,000"), P("100,000"), P("150,000"), P("100,000"), P("150,000")],
        [P("Earnings Per Share (EPS)", True), P("Rs 0.54", True), P("Rs 0.72", True), P("Rs 0.64", True), P("Rs 0.72", True), P("Rs 0.88", True)],
    ], col_widths=[135, 63, 78, 74, 78, 72])
    story.append(t22_eps)
    story.append(Spacer(1, 4))

    add_a(story, """<i>(Note: If Current Liabilities of Rs 400,000 are kept unchanged so Total Assets = Rs 1,050,000 before exercise [EBIT = Rs 210,000, Interest = 20,000 + 40,000 = Rs 60,000] and Rs 1,550,000 after warrant exercise [EBIT = Rs 310,000, Interest = Rs 60,000], then EPS Before Conv/Ex = Rs 0.90, EPS After Conv = Rs 0.76, and EPS After Warrant Exercise = Rs 1.00.)</i>

<b>e. Recommendation [2 Marks]:</b>
• If HHC expects continued rapid growth and needs the additional Rs 500,000 capital inflow when warrants are exercised (which generates the <b>highest EPS of Rs 0.88</b>), it should choose <b>Alternative 2 (Debentures with Warrants)</b>.
• Conversely, if HHC wants to eliminate long-term debt and fixed interest from its balance sheet upon conversion (achieving a debt-free balance sheet with EPS of <b>Rs 0.64</b>, up from Rs 0.54 currently), it should choose <b>Alternative 1 (Convertible Bonds)</b>.""")
    add_hint(story, "Notice how Current Interest of Rs 20,000 in the Income Statement equals 8% of the Rs 250,000 Bank Loan! Paying off that Rs 250,000 bank loan from the Rs 500,000 bond issue reduces Current Liabilities from Rs 400,000 to Rs 150,000 and increases Total Assets by the remaining Rs 250,000 (from Rs 550,000 to Rs 800,000).")

    story.append(PageBreak())
