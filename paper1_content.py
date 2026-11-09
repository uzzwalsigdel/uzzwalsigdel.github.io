from generate_pdf import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def build_paper1(story):
    story.append(Paragraph(
        "PAPER 1: TRIBHUVAN UNIVERSITY — BNK 221: CORPORATE FINANCING DECISION<br/>"
        "<font size=10>BBA / Eighth Semester | Model Question 2026 | Full Marks: 100 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group - A: Brief Answer Questions (Attempt ALL Questions) [10 × 2 = 20]", group_header_style))

    add_q(story, "Q1. What do you mean by corporate financing decision?")
    add_a(story, """<b>Answer:</b> Corporate financing decision refers to the strategic financial decision made by a firm's management regarding how to raise funds to finance its long-term investments and short-term working capital needs. It determines the optimal mix of debt, preferred stock, and common equity (capital structure) that minimizes the firm's weighted average cost of capital (WACC) and maximizes the market value of the firm.""")

    add_q(story, "Q2. Define preemptive right.")
    add_a(story, """<b>Answer:</b> A preemptive right is a privilege granted by a company's charter to its existing common shareholders that allows them the first option to purchase a proportionate share of any new issue of common stock (through a rights offering) before it is offered to the general public. It protects existing shareholders from dilution of ownership control and dilution of wealth.""")

    add_q(story, "Q3. List out the major types of leases.")
    add_a(story, """<b>Answer:</b> The major types of leases are:
• <b>1. Operating Lease:</b> A short-term, cancellable lease where the lessor maintains and services the asset.
• <b>2. Financial (Capital) Lease:</b> A long-term, non-cancellable lease that fully amortizes the asset's cost and transfers substantially all risks and rewards of ownership to the lessee.
• <b>3. Sale and Leaseback:</b> An arrangement where a firm sells an owned asset to a financial institution and immediately leases it back for a specified period.
• <b>4. Leveraged Lease:</b> A three-party financial lease involving a lessee, a lessor (equity participant), and a third-party lender who provides the majority (60%–80%) of the financing.
• <b>5. Direct Lease:</b> A lease in which the lessee acquires the use of an asset it did not previously own directly from the manufacturer or a lessor.""")

    add_q(story, "Q4. Write the meaning of trust-receipt loan.")
    add_a(story, """<b>Answer:</b> A trust-receipt loan (also known as floor-plan financing) is a secured short-term inventory loan in which the borrower holds specific, serially numbered goods (such as automobiles, heavy equipment, or consumer durables) in trust for the lender. When the borrower sells an item from the inventory, they are legally obligated to immediately remit the proceeds of that sale to the lender to repay the corresponding portion of the loan plus accrued interest.""")

    add_q(story, "Q5. Define financial distress.")
    add_a(story, """<b>Answer:</b> Financial distress is a condition in which a company cannot meet, or has severe difficulty paying off, its financial obligations to its creditors as they come due. It arises from high fixed operating or financial costs (excessive debt leverage), illiquid assets, or declining operating cash flows, and if unresolved, can lead to debt restructuring, insolvency, or legal bankruptcy.""")

    add_q(story, "Q6. What is meant by call feature of bond?")
    add_a(story, """<b>Answer:</b> A call feature (or call provision) in a bond indenture gives the issuing corporation the right (option) to redeem or buy back the bonds before their stated maturity date at a predetermined price (the call price, usually set above par value by a call premium). Issuers typically exercise this feature when market interest rates decline significantly below the bond's coupon rate so they can refinance at a lower interest rate.""")

    add_q(story, "Q7. Write about founders and angels in financing.")
    add_a(story, """<b>Answer:</b>
• <b>Founders (Bootstrapping):</b> The entrepreneurs who establish the startup and provide the initial seed capital from their personal savings, credit, or sweat equity to validate the business idea and build an initial prototype.
• <b>Angel Investors:</b> Affluent individuals (often successful former entrepreneurs or executives) who invest their own personal funds into early-stage startups in exchange for convertible debt or ownership equity, bridging the financing gap between founders/friends-and-family and institutional venture capital.""")

    add_q(story, "Q8. What do you mean by moratorium period in a term loan?")
    add_a(story, """<b>Answer:</b> A moratorium period (or grace period) in a term loan is an initial specified period granted by the lender after loan disbursement during which the borrower is not required to make principal repayments (and sometimes interest payments). It is commonly provided for project loans or construction loans so that repayment begins only after the project becomes operational and starts generating cash inflows.""")

    add_q(story, "Q9. Star Traders buys under terms of 3/10 net 50. Star Trader does not take discount and pays on 60th day. What is the annual percentage cost of stretching accounts payable? Assume 360 days in a year.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Cash discount rate (d) = 3% = 0.03
• Discount period (DP) = 10 days
• Normal credit period = 50 days; Stretched payment day (CP_stretched) = 60 days
• Days in a year = 360 days

<b>Step 1: Formula for Annual Percentage Cost (Nominal Cost) of Stretching Accounts Payable:</b>
Annual Percentage Cost (APC) = [ d / (1 - d) ] × [ 360 / (Stretched Payment Day - Discount Period) ]

<b>Step 2: Substitute the given values:</b>
APC = [ 0.03 / (1 - 0.03) ] × [ 360 / (60 - 10) ]
APC = (0.03 / 0.97) × (360 / 50)
APC = 0.0309278 × 7.2 = 0.22268 = <b>22.27%</b>

<i>(Note: Effective Annual Rate, EAR = (1 + 0.03/0.97)^(360/50) - 1 = (1.030928)^7.2 - 1 = <b>24.52%</b>)</i>
<b>Conclusion:</b> The annual percentage cost of stretching accounts payable is <b>22.27%</b> (or <b>24.52%</b> on an effective compounded basis).""")
    add_hint(story, "When accounts payable are stretched from the normal net period (day 50) to day 60, always use the ACTUAL payment day (60) minus the discount period (10) in the denominator: Days of credit used beyond discount = 60 - 10 = 50 days.")

    add_q(story, "Q10. Shikhar Company has 500,000 shares outstanding and the firm’s charter provides for a cumulative voting procedure. The company has nine directors. What is the minimum number of shares needed to ensure the election of one director?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Total number of shares outstanding (N) = 500,000 shares
• Total number of directors to be elected (D) = 9 directors
• Desired number of directors to elect (d) = 1 director

<b>Step 1: Formula under Cumulative Voting:</b>
Minimum Shares Required = [ (N × d) / (D + 1) ] + 1

<b>Step 2: Substitute the values:</b>
Minimum Shares Required = [ (500,000 × 1) / (9 + 1) ] + 1
Minimum Shares Required = (500,000 / 10) + 1 = 50,000 + 1 = <b>50,001 shares</b>

<b>Conclusion:</b> A minimum of <b>50,001 shares</b> is required to guarantee the election of one director under cumulative voting.""")
    add_hint(story, "Under Cumulative Voting, Min Shares = [(Total Shares × Desired Directors) / (Total Directors + 1)] + 1. Never forget to add '+ 1' at the end to ensure a strict majority for that seat!")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group - B: Descriptive Answer Questions (Attempt any SIX — ALL Solved) [6 × 5 = 30]", group_header_style))

    add_q(story, "Q11. Describe the features of optimal capital structure.")
    add_a(story, """<b>Answer:</b> An optimal capital structure is the best proportion of debt and equity financing that minimizes a firm's overall weighted average cost of capital (WACC) and maximizes the market value of the firm (and share price). The major features of an optimal capital structure are:

• <b>1. Profitability (Return Maximization):</b> The capital structure should allow the company to utilize favorable financial leverage (trading on equity) to maximize earnings per share (EPS) and return on equity (ROE) with minimum cost.
• <b>2. Solvency and Liquidity (Risk Control):</b> It must avoid excessive debt that threatens the solvency of the firm. Fixed interest and principal repayment obligations should stay well within the firm's stable cash-flow generation capacity to avoid financial distress.
• <b>3. Flexibility:</b> The capital structure should be adaptable so the firm can easily raise additional funds or redeem costly securities when market conditions or business requirements change.
• <b>4. Minimum Cost of Capital:</b> By balancing tax-deductible cheaper debt against the rising cost of financial distress, the optimal capital structure achieves the lowest possible WACC.
• <b>5. Conservation of Control:</b> It should preserve the voting control of existing shareholders without giving excessive restrictive covenants to creditors or diluting equity unnecessarily.
• <b>6. Simplicity:</b> The financing mix should be easy to understand and manage without overly complex layers of securities that confuse investors.""")

    add_q(story, "Q12. Discuss the merits and demerits of long-term debt as a source of financing.")
    add_a(story, """<b>Answer:</b> Long-term debt (such as debentures, bonds, and long-term bank loans) is a primary external source of corporate financing.

<b>Merits (Advantages) of Long-Term Debt:</b>
• <b>1. Tax Shield Benefit:</b> Interest paid on debt is tax-deductible, which lowers the effective after-tax cost of debt: k_dt = k_d(1 - T).
• <b>2. No Dilution of Ownership Control:</b> Bondholders and term-loan lenders do not have voting rights, so existing common shareholders retain full control of the company.
• <b>3. Financial Leverage (Trading on Equity):</b> When the firm's return on assets (ROA) exceeds the interest rate on debt, fixed-cost debt magnifies the Earnings Per Share (EPS) and Return on Equity (ROE) for shareholders.
• <b>4. Fixed Claim on Income:</b> Creditors receive only a fixed interest rate regardless of how high the company's profits grow during prosperous years.
• <b>5. Callability / Flexibility:</b> Debt can include a call provision allowing the firm to retire the bonds early if interest rates fall.

<b>Demerits (Disadvantages) of Long-Term Debt:</b>
• <b>1. Financial Risk and Bankruptcy Threat:</b> Interest and principal repayments are legally binding fixed obligations; failure to pay can force the company into insolvency and liquidation.
• <b>2. Restrictive Covenants:</b> Debt indentures often impose strict limits on dividend payments, working capital ratios, further borrowing, and asset sales, reducing managerial flexibility.
• <b>3. Fixed Maturity and Sinking Fund Burden:</b> Unlike common stock, debt has a finite maturity and requires periodic sinking-fund cash outflows or refinancing.
• <b>4. Collateral Requirement:</b> Secured long-term debt requires pledging fixed assets, reducing the firm's future borrowing capacity during emergencies.""")

    add_q(story, "Q13. Explain the concept and importance of venture capital financing.")
    add_a(story, """<b>Answer:</b>
<b>Concept of Venture Capital Financing:</b>
Venture capital (VC) is a form of private equity financing provided by institutional venture capital firms or funds to high-growth-potential, early-stage, and innovative startup companies. Because such young companies lack tangible collateral and stable cash flows to obtain bank loans, venture capitalists invest long-term equity or quasi-equity (convertible preferred stock or convertible debentures) and actively participate in mentoring, strategic planning, and corporate governance until exiting via an IPO or acquisition.

<b>Importance of Venture Capital Financing:</b>
• <b>1. Financing Innovation and High-Risk Startups:</b> VC bridges the capital gap for technology, biotech, and innovative ventures that traditional commercial banks reject due to high uncertainty.
• <b>2. Managerial and Strategic Expertise:</b> Beyond capital, VCs provide experienced board guidance, industry networking, talent recruitment, and financial discipline.
• <b>3. Economic Growth and Job Creation:</b> Venture-backed firms commercialize new technologies, boost productivity, and generate skilled employment.
• <b>4. Credibility and Follow-On Funding:</b> Backing from a reputable VC firm signals quality to suppliers, customers, investment bankers, and future institutional investors.
• <b>5. No Immediate Debt Service Burden:</b> Since VC is provided as equity or convertible preferred stock, startups do not face fixed monthly interest payments during their cash-burn growth phase.""")

    add_q(story, "Q14. What is leveraged buyout? Describe the characteristics of successful LBO.")
    add_a(story, """<b>Answer:</b>
<b>Meaning of Leveraged Buyout (LBO):</b>
A Leveraged Buyout (LBO) is the acquisition of a public or private company (or a division of a company) by a small group of investors (typically a private equity sponsor and/or existing management, known as a Management Buyout or MBO) financed predominantly with borrowed funds (often 60% to 85% debt). The target company's own assets serve as collateral for the borrowed money, and its future operating cash flows are used to service and pay down the heavy debt load.

<b>Characteristics of a Successful LBO Candidate:</b>
• <b>1. Stable and Predictable Cash Flows:</b> Because the firm must meet heavy interest and principal schedules, a mature business with steady, non-cyclical operating cash flows is essential.
• <b>2. Strong, Experienced Management Team:</b> Capable managers with direct equity ownership incentives align their interests with debt reduction and operational efficiency.
• <b>3. Substantial Tangible Assets (Collateral Base):</b> High fixed assets and working capital allow the acquirer to secure lower-cost senior bank debt.
• <b>4. Low Existing Debt (Unused Debt Capacity):</b> A target with a clean balance sheet provides ample room to add new leverage.
• <b>5. Cost-Cutting and Efficiency Potential:</b> Opportunities to eliminate wasteful corporate overhead, improve working capital, and boost EBITDA margins.
• <b>6. Divestible Non-Core Assets:</b> Underperforming or non-core divisions that can be sold off immediately after the buyout to pay down a chunk of the acquisition debt.""")

    add_q(story, "Q15. Differentiate between operating lease and financial lease.")
    add_a(story, """<b>Answer:</b> The key differences between an Operating Lease and a Financial (Capital) Lease are presented below:""")
    t15 = make_table([
        [P_hdr("Basis of Difference"), P_hdr("Operating Lease"), P_hdr("Financial (Capital) Lease")],
        [P("1. Lease Duration", True), P("Short-term; significantly shorter than the useful economic life of the asset."), P("Long-term; covers the major part (usually 75% or more) of the asset's economic life.")],
        [P("2. Revocability (Cancellation)", True), P("Cancellable by the lessee upon giving short notice."), P("Non-cancellable during the primary lease period without heavy penalty.")],
        [P("3. Maintenance & Insurance", True), P("Borne by the lessor (owner)."), P("Borne by the lessee (user).")],
        [P("4. Obsolescence Risk", True), P("Rests with the lessor."), P("Transferred to the lessee.")],
        [P("5. Amortization of Cost", True), P("Single lease contract does not fully recover the asset's cost (not fully amortized)."), P("Lease payments fully amortize the lessor's capital cost plus a return.")],
        [P("6. Purchase Option at End", True), P("Usually no bargain purchase option at maturity."), P("Often includes an option to buy the asset at a nominal or residual value.")],
    ], col_widths=[110, 195, 195])
    story.append(t15)
    story.append(Spacer(1, 6))

    add_q(story, "Q16. The Mega Company has warrants outstanding that expire in three years. Each warrant entitles the holder to purchase two shares of common stock at an exercise price of Rs 150 per share. Determine theoretical value and premium over the theoretical value if the respective prices of common stock and warrants are:\na. Rs 140 per share and Rs 10 per warrant.\nb. Rs 160 per share and Rs 40 per warrant.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Number of shares per warrant (N) = 2 shares
• Exercise price per share (E) = Rs 150
• Formula for Theoretical Value of a Warrant (TV):
  TV = max[ (P_0 - E) × N , 0 ]   <i>(Note: Formula value is (P_0 - E) × N, and minimum theoretical value cannot be negative, i.e., Rs 0).</i>
• Formula for Warrant Premium = Market Price of Warrant (W_m) - Theoretical Value (TV)

<b>Case (a): When Stock Price (P_0) = Rs 140 and Warrant Market Price (W_m) = Rs 10:</b>
• <b>Step 1: Theoretical Value (TV):</b>
  Formula value = (P_0 - E) × N = (140 - 150) × 2 = -10 × 2 = <b>-Rs 20</b>
  Since a warrant is an option and need not be exercised when out-of-the-money, its minimum floor Theoretical Value = <b>Rs 0</b>.
• <b>Step 2: Premium over Theoretical Value:</b>
  Using minimum floor TV = Rs 0:
  Premium = W_m - TV = Rs 10 - Rs 0 = <b>Rs 10</b>
  <i>(Alternative convention using unfloored formula TV = -Rs 20: Premium = 10 - (-20) = <b>Rs 30</b>. Both are shown for completeness.)</i>

<b>Case (b): When Stock Price (P_0) = Rs 160 and Warrant Market Price (W_m) = Rs 40:</b>
• <b>Step 1: Theoretical Value (TV):</b>
  TV = (P_0 - E) × N = (160 - 150) × 2 = 10 × 2 = <b>Rs 20</b>
• <b>Step 2: Premium over Theoretical Value:</b>
  Premium = W_m - TV = Rs 40 - Rs 20 = <b>Rs 20</b>""")
    add_hint(story, "TV = (Market Price of Stock - Exercise Price) × Number of shares per warrant. When P_0 < E, formula value is negative (-Rs 20), so effective TV is Rs 0. Write BOTH the floor TV (Rs 0 -> Premium Rs 10) and formula TV (-Rs 20 -> Premium Rs 30) in the exam to guarantee full marks regardless of the examiner's key!")

    add_q(story, "Q17. Akash Food Company (AFC) projects an increase in sales from Rs 1,200,000 to Rs 1,800,000 but it needs an additional Rs 200,000 of current assets to support this expansion. The money can be obtained from the bank at an interest rate of 12 percent, discount interest; no compensating balance is required. Alternatively, AFC can finance the expansion by no longer taking discounts, thus increasing accounts payable. AFC purchases on the terms of 3/10, net 40, but it can delay payment for an additional 20 days and thus becoming 20 days past due without a penalty.\nBased strictly on effective annual interest rate comparisons, how should AFC finance its expansion?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Additional financing needed = Rs 200,000
• <b>Option 1 (Bank Loan):</b> Discount interest loan at stated rate (i) = 12% = 0.12, no compensating balance.
• <b>Option 2 (Stretching Trade Credit):</b> Terms 3/10, net 40, delayed by an extra 20 days → Actual payment day = 40 + 20 = 60th day.

<b>Step 1: Calculate Effective Annual Rate (EAR) of the Discount Bank Loan:</b>
EAR (Bank Loan) = i / (1 - i)
EAR (Bank Loan) = 0.12 / (1 - 0.12) = 0.12 / 0.88 = 0.136364 = <b>13.64%</b>

<b>Step 2: Calculate Cost of Stretching Trade Credit (3/10, net 60):</b>
• <b>Annual Percentage Cost (Nominal Rate, assuming 360-day year):</b>
  APC = [ d / (1 - d) ] × [ 360 / (CP_stretched - DP) ]
  APC = [ 0.03 / (1 - 0.03) ] × [ 360 / (60 - 10) ] = (0.03 / 0.97) × (360 / 50) = 0.030928 × 7.2 = <b>22.27%</b>
  <i>(Using 365 days: APC = (0.03 / 0.97) × (365 / 50) = <b>22.58%</b>)</i>
• <b>Effective Annual Rate (Compounded EAR):</b>
  EAR (Trade Credit, 360 days) = (1 + 0.03 / 0.97)^(360 / 50) - 1 = (1.030928)^7.2 - 1 = <b>24.52%</b>
  <i>(Using 365 days: EAR = (1.030928)^7.3 - 1 = <b>24.90%</b>)</i>

<b>Step 3: Decision / Recommendation:</b>
Since the effective annual cost of the discount bank loan (<b>13.64%</b>) is substantially lower than the cost of forgoing discounts and stretching accounts payable (<b>22.27% nominal / 24.52% EAR</b>), <b>AFC should finance its expansion by borrowing from the bank</b> and continue taking the 3% cash discount on its purchases.""")
    add_hint(story, "Discount loan EAR = Interest / (1 - Interest). Trade credit paid 20 days late on 3/10 net 40 means actual payment day is 40 + 20 = 60. Compare 13.64% (Bank) vs 22.27% / 24.52% (Trade Credit) and choose the lower cost!")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group - C: Analytical Answer Questions (Attempt any THREE — ALL Solved) [3 × 10 = 30]", group_header_style))

    add_q(story, "Q18. Explain the methods of issuing securities. Also discuss the process of initial public offering.")
    add_a(story, """<b>Answer:</b>
<b>Part 1: Methods of Issuing Securities</b>
Corporations raise long-term capital in the primary market through the following major methods:
• <b>1. Public Issue through Prospectus (Initial Public Offering & Follow-on Public Offering):</b>
  - <i>Initial Public Offering (IPO):</i> When an unlisted private company sells its shares to the general public for the first time.
  - <i>Follow-on Public Offering (FPO) / Seasoned Equity Offering:</i> When an already listed public company issues additional shares to the general public.
• <b>2. Rights Offering (Privileged Subscription):</b> Issuing new shares directly to existing shareholders in proportion to their current shareholding at a discounted subscription price (preserving their preemptive right).
• <b>3. Private Placement:</b> Selling securities directly to a small number of sophisticated institutional investors (such as pension funds, insurance companies, mutual funds, or venture capital firms) without a public prospectus. It is faster and has lower flotation costs.
• <b>4. Offer for Sale:</b> The issuing company sells the entire block of securities to an issue house or investment bank at an agreed price, which then resells the securities to the public.
• <b>5. Shelf Registration / Book Building / Dutch Auction:</b> Modern pricing and issuance mechanisms where institutional bids determine the cut-off price (book building) or pre-registered securities are sold gradually over time (shelf registration).

<b>Part 2: Process of Initial Public Offering (IPO)</b>
• <b>Step 1: Board & Shareholder Approval:</b> The Board of Directors and Annual/Special General Meeting pass a resolution approving the capital increase and public issue.
• <b>Step 2: Appointment of Issue Manager (Underwriter) & Due Diligence:</b> The company appoints a licensed merchant/investment banker to act as Issue Manager, Underwriter, and Registrar to the Issue.
• <b>Step 3: Credit Rating & Valuation:</b> Obtain a credit rating from an accredited rating agency (when required by regulations) and prepare audited financial statements and a draft prospectus.
• <b>Step 4: Regulatory Filing and Approval (SEBON / SEC):</b> Submit the registration statement and draft prospectus to the securities regulator (e.g., SEBON in Nepal) for review and approval during the cooling-off/waiting period.
• <b>Step 5: Publication of Prospectus & Issue Opening:</b> Once approved, publish the prospectus/announcement in national newspapers and open applications to the public (e.g., via ASBA/C-ASBA system).
• <b>Step 6: Subscription Closure, Allotment & Refund:</b> Close the issue, verify applications, allot shares proportionately or by lottery (as per securities allotment guidelines), and refund unallotted funds.
• <b>Step 7: Demat Credit & Stock Exchange Listing:</b> Credit allotted shares into investors' Demat accounts (CDSC) and list the shares on the stock exchange (e.g., NEPSE) for secondary market trading.""")

    add_q(story, "Q19. The Nepal Energy Company has announced a rights offer to raise Rs 600 million for a new Gas Station. The stock currently sells for Rs 600 per share, and there are 4.8 million shares outstanding. Par value is Rs 100.\na. What is the maximum possible subscription price? What is the minimum?\nb. If the subscription price is set at Rs 500 per share, how many shares must be sold?\nc. How many rights will it take to buy one share?\nd. What is the value of a right?\ne. What is the ex-rights price?\nf. Show how a shareholder with 1,000 shares before the offering and no desire (or money) to buy additional shares is not harmed by the rights offer.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Funds to be raised = Rs 600,000,000 (Rs 600 million)
• Rights-on market price of stock (P_0) = Rs 600 per share
• Existing shares outstanding (N_0) = 4,800,000 shares (4.8 million)
• Par value per share = Rs 100

<b>a. Maximum and Minimum Possible Subscription Price:</b>
• <b>Maximum Subscription Price:</b> Theoretically, the subscription price cannot exceed the current market price of the stock, i.e., <b>Rs 600 per share</b> (otherwise rational investors would buy shares directly in the market rather than exercising rights).
• <b>Minimum Subscription Price:</b> Legally, a company cannot issue shares at a discount below par value (or technically > Rs 0 in jurisdictions without par value restrictions, and in Nepal Corporate Law, minimum is the par value = <b>Rs 100 per share</b>).

<b>b. Number of New Shares to be Sold (if Subscription Price, P_s = Rs 500):</b>
New Shares (N_1) = Funds to be Raised / Subscription Price (P_s)
N_1 = Rs 600,000,000 / Rs 500 = <b>1,200,000 shares (or 1.2 million shares)</b>

<b>c. Number of Rights Required to Buy One New Share (#):</b>
Number of Rights per New Share (#) = Existing Shares (N_0) / New Shares (N_1)
# = 4,800,000 / 1,200,000 = <b>4 rights</b>

<b>d. Theoretical Value of One Right (V_r):</b>
V_r = (P_0 - P_s) / (# + 1)
V_r = (600 - 500) / (4 + 1) = 100 / 5 = <b>Rs 20 per right</b>

<b>e. Ex-Rights Price of Stock (P_e):</b>
P_e = P_0 - V_r = Rs 600 - Rs 20 = <b>Rs 580 per share</b>
<i>(Verification: P_e = [(N_0 × P_0) + (N_1 × P_s)] / (N_0 + N_1) = [(4.8M × 600) + (1.2M × 500)] / 6.0M = 3,480M / 6.0M = Rs 580)</i>

<b>f. Proof that a Shareholder with 1,000 Shares Who Does Not Exercise Rights is Not Harmed (by Selling Rights):</b>
• <b>Wealth BEFORE Rights Offering:</b>
  Value of 1,000 shares @ Rs 600 = 1,000 × Rs 600 = <b>Rs 600,000</b>
• <b>Wealth AFTER Rights Offering (Selling all 1,000 Rights):</b>
  - Value of 1,000 shares at Ex-Rights Price (Rs 580) = 1,000 × Rs 580 = Rs 580,000
  - Cash received from selling 1,000 rights @ Rs 20 each = 1,000 × Rs 20 = Rs 20,000
  - <b>Total Wealth After Offering</b> = Rs 580,000 + Rs 20,000 = <b>Rs 600,000</b>
Since total wealth remains unchanged at <b>Rs 600,000</b>, the shareholder is not harmed as long as they sell their rights rather than letting them expire worthless.""")
    add_hint(story, "Rights Offering 4-step chain: (1) New Shares = Funds / P_s; (2) Rights per new share (#) = Old Shares / New Shares; (3) Value of 1 Right (V_r) = (P_0 - P_s) / (# + 1); (4) Ex-rights price (P_e) = P_0 - V_r = P_s + (# × V_r).")

    add_q(story, "Q20. The Kathmandu Electronic Company (KEC) intends to borrow Rs 800,000 to support its short-term financing requirements during the next year. The financing alternatives offered by the bank include:\nAlternative 1: A discount interest loan with a simple interest of 15 percent and no compensating balance requirement.\nAlternative 2: A 14 percent simple interest loan that has a 15 percent compensating balance requirement.\nAlternative 3: Rs 1 million revolving line of credit with simple interest of 12 percent paid on the amount borrowed and a 1 percent commitment fee.\na. Compute the effective cost (rate) of each financing alternative assuming KEC borrows Rs 800,000. Which alternative should it use?\nb. Discuss the factors other than cost to be considered while choosing a bank for short-term loan.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b> Amount borrowed / usable funds required = Rs 800,000; Total credit line in Alt 3 = Rs 1,000,000.

<b>Part (a): Effective Cost of Each Financing Alternative:</b>
• <b>Alternative 1: 15% Discount Interest Loan (No Compensating Balance):</b>
  Effective Cost = Interest Rate / (1 - Interest Rate) = 0.15 / (1 - 0.15) = 0.15 / 0.85 = 0.176471 = <b>17.65%</b>

• <b>Alternative 2: 14% Simple Interest Loan with 15% Compensating Balance:</b>
  Effective Cost = Interest Rate / (1 - Compensating Balance Ratio) = 0.14 / (1 - 0.15) = 0.14 / 0.85 = 0.164706 = <b>16.47%</b>

• <b>Alternative 3: Rs 1,000,000 Revolving Line of Credit at 12% Interest + 1% Commitment Fee:</b>
  - Interest on Rs 800,000 borrowed @ 12% = Rs 800,000 × 0.12 = Rs 96,000
  - Commitment fee on unused credit (Rs 1,000,000 - Rs 800,000 = Rs 200,000) @ 1% = Rs 200,000 × 0.01 = Rs 2,000
  - Effective Cost (Commitment Fee on Unused Portion) = (Rs 96,000 + Rs 2,000) / Rs 800,000 = Rs 98,000 / Rs 800,000 = <b>12.25%</b>
  <i>(Note: Even if the 1% commitment fee applies to the total Rs 1,000,000 line = Rs 10,000, Effective Cost = (96,000 + 10,000) / 800,000 = <b>13.25%</b>.)</i>

• <b>Decision:</b> KEC should choose <b>Alternative 3 (Revolving Line of Credit)</b> because it has the lowest effective annual cost (<b>12.25%</b>, or 13.25%).

<b>Part (b): Factors Other Than Cost When Choosing a Bank for a Short-Term Loan:</b>
• <b>1. Reliability and Willingness to Assume Risk:</b> The bank's policies toward supporting clients during temporary industry downturns (loyalty during tight credit periods).
• <b>2. Maximum Loan Size (Lending Limit):</b> Whether the bank has sufficient capital and legal lending limits to meet the firm's growing borrowing needs.
• <b>3. Advisory and Ancillary Services:</b> Quality of cash management, letter of credit (LC), foreign exchange, and financial counseling services offered by the bank.
• <b>4. Specialization and Industry Experience:</b> Familiarity of the bank's loan officers with the borrower's specific industry and working capital cycle.
• <b>5. Flexibility of Loan Covenants and Collateral Terms:</b> Reasonableness of security requirements, compensating balances, and repayment schedules.""")
    add_hint(story, "Remember the 3 bank loan denominators: (1) Discount loan subtracts 'i' in denominator -> i/(1-i); (2) Simple loan with CB subtracts 'CB' -> i/(1-CB); (3) Discount loan WITH CB subtracts BOTH -> i/(1-i-CB). For Revolving Credit, add Interest + Commitment Fee in the numerator and divide by usable borrowed amount!")

    add_q(story, "Q21. Himalaya Company can lease equipment for three years, making annual payments of Rs 150,000 per year at the end of each year or they can buy the equipment for Rs 300,000. At the end of third years, the equipment will have Rs 60,000 salvage value. The firm's before tax cost of debt is 10 percent. The company uses straight-line depreciation and has a 40 percent tax rate.\na. Calculate cost of leasing.\nb. Calculate cost of purchasing. Should the machine be leased or purchased?\nc. The appropriate discount rate for cash flows used in the analysis is the firm’s after-tax cost of debt. Why?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Lease payment (L) = Rs 150,000 per year (at the end of Years 1, 2, and 3)
• Purchase price of equipment (I_0) = Rs 300,000; Life (n) = 3 years; Salvage value (SV) = Rs 60,000
• Before-tax cost of debt (k_d) = 10%; Corporate tax rate (T) = 40%
• <b>After-tax cost of debt (k_dt)</b> = k_d × (1 - T) = 10% × (1 - 0.40) = <b>6%</b>
• Present Value factors at 6% for 3 years:
  - PVIFA(6%, 3 yrs) = [1 - (1.06)^(-3)] / 0.06 = <b>2.6730</b>
  - PVIF(6%, 3 yrs) = (1.06)^(-3) = <b>0.8396</b>

<b>a. Cost of Leasing (Present Value of After-Tax Lease Outflows):</b>
• Annual after-tax lease payment = L × (1 - T) = Rs 150,000 × (1 - 0.40) = Rs 90,000 per year
• PV of Cost of Leasing = Rs 90,000 × PVIFA(6%, 3 yrs)
  = Rs 90,000 × 2.673012 = <b>Rs 240,571.08</b> (or Rs 240,570 using 2.6730)

<b>b. Cost of Purchasing (Borrow & Buy) and Decision:</b>
• Annual Straight-Line Depreciation = (Cost - Salvage Value) / Life = (300,000 - 60,000) / 3 = Rs 80,000 per year
• Annual Depreciation Tax Shield = Depreciation × T = Rs 80,000 × 0.40 = Rs 32,000 per year
• After-tax Salvage Value in Year 3 = Rs 60,000 (since Book Value = Salvage Value = Rs 60,000, no gain/loss tax)
• <b>PV of Cost of Purchasing (Owning):</b>
  PV(Purchasing) = Initial Cost - PV of Depreciation Tax Shield - PV of Salvage Value
  PV(Purchasing) = Rs 300,000 - (Rs 32,000 × 2.673012) - (Rs 60,000 × 0.839619)
  PV(Purchasing) = Rs 300,000 - Rs 85,536.38 - Rs 50,377.16 = <b>Rs 164,086.46</b> (or Rs 164,088 using 4-decimal tables)
• <b>Decision:</b> Since the Present Value of Cost of Purchasing (<b>Rs 164,086.46</b>) is significantly lower than the Present Value of Cost of Leasing (<b>Rs 240,571.08</b>) [Net Advantage to Leasing = -Rs 76,484.62], <b>the machine should be PURCHASED rather than leased</b>.
  <i>(Note: If you also draw a 3-year loan amortization table at 10% for Rs 300,000, the PV of net loan outflows discounted at 6% equals the exact same Rs 300,000 initial cost!)</i>

<b>c. Why After-Tax Cost of Debt is Used as the Discount Rate:</b>
Lease vs. borrow-and-buy analysis is a <b>financing decision</b> (not an operating investment decision), because the firm has already decided to acquire the use of the equipment. Lease payments, debt service payments, and depreciation tax shields are contractual, fixed cash flows with low risk closely matching the risk of the firm's debt obligations, and because debt interest is tax-deductible, the opportunity cost of leasing is the <b>after-tax cost of debt: k_d(1 - T)</b>.""")
    add_hint(story, "Shortcut for Cost of Purchasing: Because the PV of any loan's after-tax principal + interest payments discounted at the after-tax interest rate k_d(1-T) is ALWAYS equal to the Initial Loan Principal (Rs 300,000), you don't even need a loan amortization schedule unless asked! Just do: PV(Buy) = Purchase Price - PV(Dep Tax Shield) - PV(After-Tax Salvage Value), all discounted at k_d(1-T) = 6%.")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group - D: Comprehensive Answer Questions / Case Study [5 × 4 = 20]", group_header_style))

    add_q(story, "Q22. Case Study: Himalayan Herbal Company (HHC)\nHHC is contemplating raising Rs 10 million by means of a debt issue under two alternatives:\na. A 20-year, 8 percent convertible debenture issue with a Rs 50 conversion price and Rs 1,000 face value.\nb. A 20-year, 10 percent straight bond issue. Each Rs 1,000 bond has a detachable warrant to purchase four shares for Rs 50 a share.\nTax rate = 50%, Current stock price = Rs 40, EBIT = constant 20% of total capitalization.\nCurrent Capitalization: Common stock (par Rs 5) = Rs 5,000,000; Additional paid-in capital = Rs 10,000,000; Retained earnings = Rs 15,000,000; Total = Rs 30,000,000.\ni. Show the capitalizations before and after conversion of convertible.\nii. Show the capitalizations before and after exercise of warrants.\niii. Compute earnings per share currently and before and after conversion of convertible and exercise of warrant.\niv. Describe the reasons for issuing warrants and convertible.")
    add_a(story, """<b>Answer (Step-by-Step Case Study Solution):</b>
<b>Preliminary Working Notes:</b>
• Existing number of common shares = Common Stock Capital / Par Value = Rs 5,000,000 / Rs 5 = <b>1,000,000 shares</b>
• Number of Rs 1,000 bonds/debentures issued to raise Rs 10,000,000 = 10,000,000 / 1,000 = <b>10,000 bonds</b>
• <b>Under Alternative (a) Convertible Debentures (8%):</b>
  - Conversion Ratio (CR) = Face Value / Conversion Price = Rs 1,000 / Rs 50 = 20 shares per bond
  - Total new shares upon full conversion = 10,000 bonds × 20 shares = <b>200,000 new shares</b>
  - Upon conversion, Rs 10,000,000 debentures are extinguished and converted into:
    Common Stock (at Rs 5 par) = 200,000 × Rs 5 = Rs 1,000,000
    Additional Paid-in Capital (at Rs 45 premium) = 200,000 × Rs 45 = Rs 9,000,000
    <i>(Total Capitalization remains Rs 40,000,000 because debt is simply swapped for equity; no new cash enters on conversion.)</i>
• <b>Under Alternative (b) 10% Bonds with Warrants:</b>
  - Each of the 10,000 bonds carries warrants to buy 4 shares @ Rs 50 → Total new shares = 10,000 × 4 = <b>40,000 new shares</b>
  - When warrants are exercised, the 10% straight bonds (Rs 10,000,000) <b>remain on the balance sheet</b>, and the company receives fresh cash = 40,000 shares × Rs 50 = <b>Rs 2,000,000</b>:
    Common Stock increases by: 40,000 × Rs 5 = Rs 200,000 (to Rs 5,200,000)
    Additional Paid-in Capital increases by: 40,000 × Rs 45 = Rs 1,800,000 (to Rs 11,800,000)
    <i>(Total Capitalization increases to Rs 42,000,000.)</i>""")

    add_a(story, """<b>(i) & (ii) Capitalization Table Before and After Conversion of Convertibles and Exercise of Warrants:</b>""")
    t22_cap = make_table([
        [P_hdr("Capital Structure Items"), P_hdr("Current (Rs)"), P_hdr("Convertible: Before Conv. (Rs)"), P_hdr("Convertible: After Conv. (Rs)"), P_hdr("Warrants: Before Exercise (Rs)"), P_hdr("Warrants: After Exercise (Rs)")],
        [P("8% Convertible Debentures"), P("0"), P("10,000,000"), P("0"), P("0"), P("0")],
        [P("10% Straight Bonds"), P("0"), P("0"), P("0"), P("10,000,000"), P("10,000,000")],
        [P("Common Stock (Rs 5 par)"), P("5,000,000"), P("5,000,000"), P("6,000,000"), P("5,000,000"), P("5,200,000")],
        [P("Additional Paid-in Capital"), P("10,000,000"), P("10,000,000"), P("19,000,000"), P("10,000,000"), P("11,800,000")],
        [P("Retained Earnings"), P("15,000,000"), P("15,000,000"), P("15,000,000"), P("15,000,000"), P("15,000,000")],
        [P("Total Capitalization", True), P("30,000,000", True), P("40,000,000", True), P("40,000,000", True), P("40,000,000", True), P("42,000,000", True)],
    ], col_widths=[125, 65, 80, 75, 80, 75])
    story.append(t22_cap)
    story.append(Spacer(1, 6))

    add_a(story, """<b>(iii) Computation of Earnings Per Share (EPS) Under All Scenarios:</b>""")
    t22_eps = make_table([
        [P_hdr("Particulars"), P_hdr("Current"), P_hdr("Convertible: Before Conv."), P_hdr("Convertible: After Conv."), P_hdr("Warrants: Before Exercise"), P_hdr("Warrants: After Exercise")],
        [P("Total Capitalization (Rs)"), P("30,000,000"), P("40,000,000"), P("40,000,000"), P("40,000,000"), P("42,000,000")],
        [P("EBIT (20% of Total Cap.)"), P("6,000,000"), P("8,000,000"), P("8,000,000"), P("8,000,000"), P("8,400,000")],
        [P("Less: Interest (8% or 10%)"), P("0"), P("800,000"), P("0"), P("1,000,000"), P("1,000,000")],
        [P("Earnings Before Taxes (EBT)"), P("6,000,000"), P("7,200,000"), P("8,000,000"), P("7,000,000"), P("7,400,000")],
        [P("Less: Taxes @ 50%"), P("3,000,000"), P("3,600,000"), P("4,000,000"), P("3,500,000"), P("3,700,000")],
        [P("Net Income (EAT) (Rs)", True), P("3,000,000", True), P("3,600,000", True), P("4,000,000", True), P("3,500,000", True), P("3,700,000", True)],
        [P("Number of Common Shares"), P("1,000,000"), P("1,000,000"), P("1,200,000"), P("1,000,000"), P("1,040,000")],
        [P("Earnings Per Share (EPS)", True), P("Rs 3.00", True), P("Rs 3.60", True), P("Rs 3.33", True), P("Rs 3.50", True), P("Rs 3.56", True)],
    ], col_widths=[125, 65, 80, 75, 80, 75])
    story.append(t22_eps)
    story.append(Spacer(1, 6))

    add_a(story, """<b>(iv) Reasons for Issuing Warrants and Convertibles:</b>
• <b>1. Sweetener to Lower Interest Costs:</b> Attaching warrants or conversion privileges acts as an "equity kicker" that allows growing or riskier firms to issue debt at a lower coupon rate and with fewer restrictive covenants.
• <b>2. Deferred Sale of Common Stock at a Premium ("Delayed Equity"):</b> Since the current stock price is Rs 40 and the conversion/exercise price is set at Rs 50 (a 25% premium), the company effectively sells future common equity at a price higher than today's market price, resulting in fewer shares issued and less dilution.
• <b>3. Matching Cash Flows with Growth Stage:</b> During the construction/expansion phase of the new project, the firm enjoys low fixed interest payments; once the project succeeds and the stock price rises above Rs 50, conversion/exercise provides permanent equity capital.
• <b>4. Additional Cash Inflow upon Warrant Exercise:</b> Unlike convertibles (which extinguish debt), exercising detachable warrants brings fresh cash (Rs 2,000,000 here) into the firm while keeping the bond financing intact.""")
    add_hint(story, "Crucial difference in Case Q22: (1) On Conversion of Convertible Debentures, Debt becomes Rs 0, Interest becomes Rs 0, and Total Capitalization stays Rs 40M (EBIT = 20% of 40M = Rs 8M). (2) On Exercise of Warrants, the Rs 10M Straight Bond STAYS on the balance sheet (Interest = Rs 1M continues!), and new cash of 40,000 × Rs 50 = Rs 2M increases Total Capitalization to Rs 42M (so EBIT = 20% of 42M = Rs 8.4M)!")

    story.append(PageBreak())
