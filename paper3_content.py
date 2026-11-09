from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Line, String, PolyLine
from generate_pdf import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def make_long_put_diagram():
    d = Drawing(420, 175)
    # Axes
    d.add(Line(50, 20, 50, 160, strokeColor=colors.HexColor('#2D3748'), strokeWidth=1.2))
    d.add(Line(30, 80, 390, 80, strokeColor=colors.HexColor('#2D3748'), strokeWidth=1.2))
    # Zero line label
    d.add(String(35, 77, "0", fontName="Helvetica-Bold", fontSize=8.5))
    d.add(String(12, 148, "Profit (+)", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.HexColor('#1A365D')))
    d.add(String(12, 25, "Loss (-)", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.HexColor('#C53030')))
    d.add(String(320, 67, "Stock Price at Expiration (S_T)", fontName="Helvetica-Bold", fontSize=8.5))

    # Key coordinates:
    # S_T = 0 -> x=50, Profit = +550 -> y=145
    # S_T = 550 (Breakeven) -> x=210, Profit = 0 -> y=80
    # S_T = 600 (Strike X) -> x=250, Profit = -50 -> y=50
    # S_T > 600 -> x=360, Profit = -50 -> y=50
    d.add(PolyLine([50, 145, 210, 80, 250, 50, 365, 50], strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=2.2))

    # Dashed helper lines
    d.add(Line(50, 50, 250, 50, strokeColor=colors.HexColor('#A0AEC0'), strokeWidth=0.8, strokeDashArray=[3, 3]))
    d.add(Line(250, 50, 250, 80, strokeColor=colors.HexColor('#A0AEC0'), strokeWidth=0.8, strokeDashArray=[3, 3]))

    # Labels
    d.add(String(10, 142, "+Rs 550", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#2B6CB0')))
    d.add(String(12, 47, "-Rs 50", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#C53030')))
    d.add(String(175, 86, "BEP = Rs 550", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#2F855A')))
    d.add(String(235, 86, "X = Rs 600", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    d.add(String(265, 38, "Max Loss = -Rs 50 (Premium)", fontName="Helvetica", fontSize=8, fillColor=colors.HexColor('#C53030')))
    d.add(String(95, 130, "Long Put Profit Line", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.HexColor('#2B6CB0')))
    return d

def build_paper3(story):
    story.append(Paragraph(
        "PAPER 3: TRIBHUVAN UNIVERSITY — BNK 202: FINANCIAL DERIVATIVES<br/>"
        "<font size=10>BBA / Eighth Semester | Model Question 2026 | Full Marks: 100 | Pass Marks: 50 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group - A: Brief-Answer Questions (Attempt ALL Questions) [10 × 2 = 20]", group_header_style))

    add_q(story, "Q1. Why is a derivative instrument known as a zero-sum game?")
    add_a(story, """<b>Answer:</b> A derivative instrument (such as a forward, futures, option, or swap contract) is known as a zero-sum game because every contract has two counterparties—a long position and a short position—whose cash flows exactly mirror each other. The profit gained by one party (e.g., the long position) is exactly equal to the loss suffered by the other party (e.g., the short position), so the net change in wealth between the two parties sums to zero (ignoring transaction costs).""")

    add_q(story, "Q2. Why do investors pay more for an American option than similar European option?")
    add_a(story, """<b>Answer:</b> An American option can be exercised at <b>any time on or before</b> its expiration date, whereas a European option can be exercised <b>only on the expiration date</b>. Because the American option gives the holder everything a European option offers plus the valuable flexibility of early exercise (for example, exercising an American call right before a large dividend or exercising a deep-in-the-money American put early to invest the strike proceeds at interest), an American option is always worth at least as much as—and often more than—an otherwise identical European option: C_American ≥ C_European and P_American ≥ P_European.""")

    add_q(story, "Q3. An investor who wants to achieve maximum gain and accept a higher maximum loss selects a call option with a lower exercise price. Justify.")
    add_a(story, """<b>Answer:</b> A call option with a <b>lower exercise price (X_1 < X_2)</b> has a higher intrinsic value and higher probability of finishing in-the-money, so it commands a <b>higher upfront option premium (C_1 > C_2)</b>.
• <b>Higher Maximum Dollar Loss:</b> If the stock price finishes below the strike price, the call expires worthless and the buyer loses the entire premium paid, which is larger (C_1) for the lower-strike call.
• <b>Higher Payoff / Gain at Expiration:</b> For any stock price above the strike price, the lower exercise price allows the holder to buy the stock at a cheaper strike (S_T - X_1 > S_T - X_2), generating the highest gross payoff.""")

    add_q(story, "Q4. A longer-lived option has a higher price. Do you agree? Give reasons.")
    add_a(story, """<b>Answer:</b> <b>Yes, I agree</b> (particularly for American options and non-dividend-paying European calls).
<b>Reasons:</b>
• <b>1. Greater Time Value and Volatility Opportunity:</b> More time to expiration gives the underlying stock price more opportunity to move deep into the money while downside loss remains strictly capped at the premium.
• <b>2. Lower Present Value of Exercise Price (for Calls):</b> For a call option, paying the exercise price X further in the future reduces its present value: PV(X) = X·e^(-rT), increasing call value.
<i>(Note: The only exception can be a deep-in-the-money European put or a European call on a stock paying a very large dividend during the extended period.)</i>""")

    add_q(story, "Q5. Define future contract.")
    add_a(story, """<b>Answer:</b> A futures contract is a standardized, legally binding agreement traded on an organized futures exchange to buy (long) or sell (short) a specified quantity and quality of an underlying asset (commodity or financial instrument) at a predetermined futures price on a specified future delivery date, subject to daily marking-to-market and margin requirements guaranteed by a clearinghouse.""")

    add_q(story, "Q6. What do you mean by upside capture in portfolio insurance?")
    add_a(story, """<b>Answer:</b> In portfolio insurance (such as a protective put strategy where an investor holds a stock plus a put option), <b>upside capture</b> measures the percentage of the uninsured stock portfolio's positive value (or capital gain) that the insured portfolio captures when the market rises. Because the investor paid an upfront put premium to guarantee a floor value, the insured portfolio captures slightly less than 100% of the bull-market upside.""")

    add_q(story, "Q7. Under what conditions is a long hedge using futures suitable?")
    add_a(story, """<b>Answer:</b> A <b>long hedge</b> (taking a long position in futures contracts) is suitable under the following two conditions:
• <b>1. Anticipated Future Purchase:</b> A firm or investor knows they will need to <b>purchase</b> an underlying commodity or financial asset in the future and wants to lock in the purchase price today to protect against a <b>rise in spot prices</b>.
• <b>2. Covering an Existing Short Spot Position:</b> An investor who has short-sold an asset in the spot market wants to hedge against price increases.""")

    add_q(story, "Q8. Write the meaning of synthetic instruments.")
    add_a(story, """<b>Answer:</b> Synthetic instruments are engineered financial positions created by combining two or more existing securities (such as underlying stocks, risk-free bonds, and options/forwards) via <b>Put-Call Parity (S_0 + P_0 = C_0 + X·e^(-rT))</b> to replicate the exact cash flows and risk-return payoff of another security. For example:
• <b>Synthetic Long Call</b> = Long Stock + Long Put - Risk-Free Borrowing
• <b>Synthetic Long Put</b> = Long Call + Short Stock + Risk-Free Lending.""")

    add_q(story, "Q9. Why do investors prefer bull spreads from call options over those from put options?")
    add_a(story, """<b>Answer:</b> Although a bull call spread and a bull put spread with the same strike prices (X_1 < X_2) have the same shape of expiration profit diagram, investors often prefer a <b>bull call spread</b> because:
• 1. <b>Limited Early Assignment Risk:</b> In a bull put spread, the short higher-strike put (X_2) is initially in-the-money and faces high risk of early exercise (assignment) if American-style, whereas in a bull call spread the short call (X_2) is initially out-of-the-money.
• 2. <b>Intuitive Debit Structure & Higher Liquidity:</b> Call options in bullish markets often have tighter bid-ask spreads and a clear maximum risk equal to the net initial debit paid.""")

    add_q(story, "Q10. If you want to change the fixed-rate liability in to floating-rate liability using a swap, how would you do it?")
    add_a(story, """<b>Answer:</b> To transform an existing <b>fixed-rate liability</b> into a <b>floating-rate liability</b>, you should enter into an interest rate swap as the <b>Fixed-Rate Receiver and Floating-Rate Payer</b> (i.e., receive fixed rate and pay floating rate such as SOFR):
• The fixed rate received from the swap counterparty offsets your existing fixed-rate loan interest payment.
• You are left paying the floating interest rate on the swap, effectively converting your fixed-rate debt into a floating-rate liability.""")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group - B: Short-Answer Questions (Attempt any SIX — ALL Solved) [6 × 5 = 30]", group_header_style))

    add_q(story, "Q11. Describe the role of the derivative market.")
    add_a(story, """<b>Answer:</b> The derivative market plays five vital economic functions in a modern financial system:
• <b>1. Risk Management (Hedging and Risk Transfer):</b> Derivatives allow producers, corporations, farmers, and financial institutions (hedgers) to shift unwanted price, interest-rate, exchange-rate, and equity risks to speculators who are willing to bear them.
• <b>2. Price Discovery:</b> Futures and forward markets aggregate global information and expectations of thousands of buyers and sellers to reveal consensus expectations of future spot prices for commodities, currencies, and interest rates.
• <b>3. Market Completeness and Operational Advantages:</b> Options and swaps allow investors to create payoff profiles (like portfolio insurance or volatility straddles) that cannot be replicated easily in spot markets, with much lower transaction costs, higher liquidity, and easier short-selling.
• <b>4. Market Efficiency and Arbitrage Linkages:</b> Arbitrageurs monitor tiny price discrepancies between spot and derivative markets, ensuring that spot and derivative prices stay aligned at fair no-arbitrage values.
• <b>5. Capital Allocation and Leverage:</b> Margin trading in derivatives allows participants to manage large notional exposures with a small capital outlay, freeing up capital for productive investment.""")

    add_q(story, "Q12. An investor purchased a June put option with an exercise price of Rs 600 by paying a premium of Rs 50 and is holding it until June. Under what circumstances will the option be exercised? Under what circumstances will the holder of the option make a profit? With the help of a diagram, explain how the profit from a long position in the option depends on the stock price at the maturity of the option.")
    add_a(story, """<b>Answer (Step-by-Step Numerical & Graphical Solution):</b>
<b>Given:</b>
• Position: Long Put Option
• Exercise Price (X) = Rs 600
• Put Option Premium paid (P) = Rs 50

<b>1. Circumstances Under Which the Put Option Will Be Exercised:</b>
A put option gives the holder the right to sell the stock at the exercise price X = Rs 600. Therefore, the investor will exercise the option at maturity whenever the <b>stock price at expiration is less than the exercise price (S_T < Rs 600)</b>, i.e., when the put option is <i>in-the-money</i>. (Even when Rs 550 < S_T < Rs 600, exercising recovers part of the Rs 50 premium paid).

<b>2. Circumstances Under Which the Holder Will Make a Net Profit:</b>
• Profit Formula: π = max(X - S_T, 0) - P = max(600 - S_T, 0) - 50
• Breakeven Stock Price (S_T*): X - P = Rs 600 - Rs 50 = <b>Rs 550</b>
• Thus, the holder makes a positive net profit whenever the <b>stock price at maturity falls strictly below Rs 550 (S_T < Rs 550)</b>.

<b>3. Payoff & Profit Schedule and Diagram at Maturity:</b>
• If S_T ≥ Rs 600: Option expires worthless; Loss = <b>-Rs 50</b> (maximum loss = premium paid).
• If Rs 550 < S_T < Rs 600: Option is exercised; net loss is between -Rs 50 and Rs 0.
• If S_T = Rs 550: Breakeven point (Profit = <b>Rs 0</b>).
• If S_T < Rs 550: Positive profit; increases Rupee-for-Rupee as S_T falls, reaching a maximum profit of 600 - 50 = <b>+Rs 550</b> if S_T = Rs 0.""")
    story.append(make_long_put_diagram())
    add_hint(story, "For a Long Put (Strike X = 600, Premium P = 50): Exercise whenever S_T < X (S_T < 600), and make a Profit whenever S_T < X - P (S_T < 550). Notice that between 550 and 600 you STILL exercise to reduce your loss!")

    add_q(story, "Q13. An equity swap between the Employee Provident Fund (EPF) and Nabil Dealer is entered into. EPF pays floating interest payments based on SOFR, and Nabil pays a return on the NEPSE index. The payments are made quarterly, assuming a 30-day month and a 360-day year. The NEPSE index at the time of swap initiation was 2745.63, and the 90-day SOFR was 8 percent. Now, assume it is 50 days into the life of the swap. The NEPSE is now 2825.02, and the 40-day SOFR rate is 7.8 percent. Find the value of the swap today. Assume a notional principal of Rs 50,000,000.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Notional Principal (NP) = Rs 50,000,000
• EPF pays 90-day floating SOFR and receives NEPSE index return; Nabil Dealer pays NEPSE index return and receives floating SOFR.
• At swap initiation (t = 0): Initial NEPSE index (I_0) = 2745.63; initial 90-day SOFR (r_0) = 8% = 0.08
• Valuation date (t = 50 days): Remaining days in the 90-day quarter = 90 - 50 = <b>40 days</b>
• Current NEPSE index (I_50) = 2825.02; current 40-day SOFR (r_50) = 7.8% = 0.078

<b>Step 1: Value of the Equity Leg (per Re 1 of Notional Principal) at Day 50:</b>
V_equity = I_50 / I_0 = 2825.02 / 2745.63 = <b>1.02891504</b>

<b>Step 2: Value of the Floating-Rate Bond Leg (per Re 1 of Notional Principal) at Day 50:</b>
• Coupon + Principal at Day 90 (per Re 1) = 1 + [ r_0 × (90 / 360) ] = 1 + [ 0.08 × (90 / 360) ] = 1 + 0.02 = 1.02
• Discounted back 40 days to Day 50 at 40-day SOFR (7.8%):
  V_floating = 1.02 / [ 1 + 0.078 × (40 / 360) ] = 1.02 / [ 1 + 0.00866667 ] = 1.02 / 1.00866667 = <b>1.01123596</b>

<b>Step 3: Total Value of the Swap at Day 50:</b>
• <b>Value of Swap to EPF (Receives Equity, Pays Floating):</b>
  V_EPF = NP × (V_equity - V_floating)
  V_EPF = Rs 50,000,000 × (1.02891504 - 1.01123596)
  V_EPF = Rs 50,000,000 × 0.01767908 = <b>+Rs 883,954.22</b> (or approx. Rs 883,954)
• <b>Value of Swap to Nabil Dealer (Pays Equity, Receives Floating):</b>
  V_Nabil = -V_EPF = <b>-Rs 883,954.22</b>""")
    add_hint(story, "Equity vs. Floating Swap Valuation at day t (with m = 90 - t days left): Value per Re 1 = [ (I_t / I_0) - (1 + r_0*(90/360)) / (1 + r_t*(m/360)) ]. Multiply by Notional Principal!")

    add_q(story, "Q14. People's Power Company (PCC), a Nepalese hydro-power company, purchased equipment from Baltimore Heavy Industry, a U. S. firm, for $5 million payable in one year. The current spot rate is Rs 140 per dollar, and the one-year forward rate is 130 per dollar. The annual interest rate is 5% in Nepal, and 8% in the U.S. PCC can also buy a one-year call option on the dollar at the strike price of Rs 125 per dollar for a premium of Rs 14 per dollar.\na. Assuming that the forward exchange rate is the best predictor of the future spot rate, compute the expected future rupee cost of meeting this obligation when the option hedge is used.\nb. At what future spot rate do you think PCC may be indifferent between the option and forward hedge?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Payable amount = $5,000,000 due in 1 year
• Current spot rate (S_0) = Rs 140/$; 1-year forward rate (F) = Rs 130/$
• Interest rate in Nepal (r_NPR) = 5% p.a.; Interest rate in U.S. (r_USD) = 8% p.a.
• 1-year Call Option on USD: Strike price (X) = Rs 125/$; Call premium (C) = Rs 14/$

<b>Part (a): Expected Future Rupee Cost Using the Option Hedge:</b>
• Since the forward rate is the unbiased predictor of the future spot rate, Expected Future Spot Rate E(S_1) = F = <b>Rs 130/$</b>.
• At E(S_1) = Rs 130/$, since S_1 (Rs 130) > Strike Price X (Rs 125), PCC <b>will exercise the call option</b> and purchase USD at the strike price of <b>Rs 125/$</b>.
• <b>Method 1 (Including 5% Nepalese Opportunity Interest Cost on Option Premium — Standard Textbook Method):</b>
  - Future value of call premium per dollar after 1 year = Rs 14 × (1 + 0.05) = <b>Rs 14.70/$</b>
  - Effective cost per dollar under option hedge = Strike Price + FV(Premium) = Rs 125 + Rs 14.70 = <b>Rs 139.70/$</b>
  - Total Expected Future Rupee Cost for $5,000,000 = 5,000,000 × Rs 139.70 = <b>Rs 698,500,000 (Rs 698.50 million)</b>
• <i><b>Method 2 (Uncompounded Option Premium):</b>
  - Cost per dollar = Rs 125 + Rs 14 = <b>Rs 139.00/$</b> → Total Rupee Cost = 5,000,000 × Rs 139 = <b>Rs 695,000,000 (Rs 695 million)</b>.</i>

<b>Part (b): Indifference Future Spot Rate Between Option Hedge and Forward Hedge:</b>
• Cost under Forward Hedge = F = <b>Rs 130/$</b> (or Rs 650,000,000 total).
• Notice that if the option is exercised (S_1 ≥ 125), the option hedge costs Rs 139.70/$ (or Rs 139/$), which is above Rs 130/$. However, if the future spot rate S_1 falls <b>below the strike price of Rs 125/$</b>, PCC will let the call option expire unexercised and buy dollars in the spot market at S_1:
  - <b>With Interest on Premium (Rs 14.70/$):</b>
    S_1 + 14.70 = 130  ⇒  <b>S_1 = Rs 115.30 per dollar</b>
  - <b>Without Interest on Premium (Rs 14.00/$):</b>
    S_1 + 14.00 = 130  ⇒  <b>S_1 = Rs 116.00 per dollar</b>
<b>Conclusion:</b> PCC will be indifferent between the option hedge and the forward hedge if the future spot rate falls to <b>Rs 115.30/$</b> (including interest on premium) or <b>Rs 116.00/$</b> (excluding interest on premium).""")
    add_hint(story, "In FX Option Hedging, show BOTH with domestic interest on the upfront premium [C × (1 + r_domestic) = 14 × 1.05 = Rs 14.70] and without interest [Rs 14.00]. For indifference with Forward (Rs 130), set Spot + Premium = Forward => S_1 + 14.70 = 130 => Rs 115.30/$ (or Rs 116/$).")

    add_q(story, "Q15. HDL stock is currently selling at Rs 900. A put option on HDL has an exercise price of Rs 1000 and matures in one year. The annually compounded interest rate is 8 percent. The quoted price of the put option is Rs 60. Identify the appropriate arbitrage opportunity and show the arbitrage profit for the stock price of Rs 800 and Rs 1200 after one year.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 900; Put Exercise price (X) = Rs 1,000
• Time to maturity (T) = 1 year; Annually compounded risk-free rate (r) = 8% = 0.08
• Quoted market price of put option (P_mkt) = Rs 60

<i><b>Important Note on Two Standard Exam Interpretations of Q15:</b></i>
<b>Case A: Intrinsic Value / American Lower Bound Comparison (or when Put is Underpriced relative to Intrinsic Value X - S_0 = Rs 100):</b>
• Intrinsic value of the put today = max(X - S_0, 0) = 1,000 - 900 = <b>Rs 100</b>.
• Since the quoted put price (Rs 60) is less than its intrinsic value (Rs 100), an American put offers an immediate arbitrage profit of Rs 100 - Rs 60 = <b>Rs 40 per share</b> today (invested at 8% for 1 year = <b>Rs 43.20</b>).
• Furthermore, in Nepalese exam solutions that compare the undiscounted payoff with the initial outlay (Buy 1 Stock @ Rs 900 + Buy 1 Put @ Rs 60 = Rs 960 total outlay vs. guaranteed minimum Rs 1,000 floor):
  - At S_T = Rs 800: Put is exercised (sell stock at Rs 1,000); Unadjusted gain over Rs 960 outlay = 1,000 - 960 = +Rs 40.
  - At S_T = Rs 1,200: Put expires worthless; sell stock at Rs 1,200; Gain over Rs 960 outlay = 1,200 - 960 = +Rs 240.

<b>Case B: Strict European Put Lower-Bound Analysis (Incorporating 8% Interest Rate):</b>
• Theoretical Minimum Price (Lower Bound) of a 1-year European Put:
  P_min = max[ X / (1 + r)^T - S_0 , 0 ] = (1,000 / 1.08) - 900 = 925.93 - 900 = <b>Rs 25.93</b>.
• Notice that if an arbitrageur borrows Rs 960 at 8% to buy the stock (Rs 900) and the put (Rs 60), the loan repayment at T = 1 is Rs 960 × 1.08 = <b>Rs 1,036.80</b>:
  - If S_T = Rs 800: Exercise put to receive Rs 1,000; less loan repayment Rs 1,036.80 = <b>-Rs 36.80</b>.
  - If S_T = Rs 1,200: Put expires (0); sell stock for Rs 1,200; less loan repayment Rs 1,036.80 = <b>+Rs 163.20</b>.
  <i>(Conversely, if the question intended S_0 = Rs 850 or r = 2% so that PV(X) - S_0 > 60, borrowing S_0 + P locks in PV(X) - S_0 - P > 0 at every S_T.)</i>""")
    t_b15 = make_table([
        [P_hdr("Transaction / Position"), P_hdr("Cash Flow Today (t = 0)"), P_hdr("Cash Flow at T = 1 if S_T = Rs 800"), P_hdr("Cash Flow at T = 1 if S_T = Rs 1,200")],
        [P("1. Buy 1 share of HDL Stock"), P("-Rs 900.00"), P("+Rs 800.00"), P("+Rs 1,200.00")],
        [P("2. Buy 1 Put Option (X = 1,000)"), P("-Rs 60.00"), P("+Rs 200.00 (1,000 - 800)"), P("Rs 0 (Expires)")],
        [P("Combined Portfolio Value", True), P("-Rs 960.00", True), P("+Rs 1,000.00", True), P("+Rs 1,200.00", True)],
        [P("Net Gain Before Financing Interest"), P("—"), P("+Rs 40.00 (1,000 - 960)"), P("+Rs 240.00 (1,200 - 960)")],
        [P("3. Less: Loan Repayment (960 × 1.08)"), P("+Rs 960.00"), P("-Rs 1,036.80"), P("-Rs 1,036.80")],
        [P("Net Cash Flow After 8% Financing", True), P("Rs 0.00", True), P("-Rs 36.80", True), P("+Rs 163.20", True)],
    ], col_widths=[145, 110, 120, 125])
    story.append(t_b15)
    story.append(Spacer(1, 4))
    add_hint(story, "In Q15, the exam paper set S_0 = 900, X = 1,000, P = 60 (where S_0 + P = 960 < 1,000, but 960 × 1.08 = 1,036.80 > 1,000). Showing the table above with BOTH the unadjusted gain (+Rs 40 and +Rs 240) and the 8% interest-adjusted cash flow (-Rs 36.80 and +Rs 163.20, plus P_min = 1000/1.08 - 900 = Rs 25.93) guarantees 5/5 marks!")

    add_q(story, "Q16. The stock of Birat Company is currently selling for Rs 650. A 6-month call option on the stock has an exercise price of Rs 660. The standard deviation of returns on Birat stock has been estimated to be 50 percent. Currently, the 6-month T-bill rate is 10 percent. Using the BSM model, calculate the price of the call option on Birat.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 650
• Exercise price (X) = Rs 660
• Time to expiration (T) = 6 months = 6 / 12 = <b>0.5 years</b>
• Standard deviation of returns (σ) = 50% = <b>0.50</b>
• Risk-free interest rate (r) = 10% p.a. = <b>0.10</b>

<b>Step 1: Calculate d_1 and d_2 under the Black-Scholes-Merton (BSM) Formula:</b>
d_1 = [ ln(S_0 / X) + (r + 0.5 × σ²) × T ] / (σ × √T)
• ln(650 / 660) = ln(0.984848) = <b>-0.015267</b>
• (r + 0.5 × σ²) × T = [ 0.10 + 0.5 × (0.50)² ] × 0.5 = (0.10 + 0.125) × 0.5 = 0.225 × 0.5 = <b>0.1125</b>
• σ × √T = 0.50 × √0.5 = 0.50 × 0.707107 = <b>0.353553</b>
• <b>d_1</b> = (-0.015267 + 0.1125) / 0.353553 = 0.097233 / 0.353553 = <b>0.2750</b> (or 0.28)
• <b>d_2</b> = d_1 - σ × √T = 0.2750 - 0.353553 = <b>-0.0785</b> (or -0.08)

<b>Step 2: Find Cumulative Standard Normal Probabilities N(d_1) and N(d_2) from Z-Table:</b>
• For d_1 = 0.2750 (interpolating between Z = 0.27 and Z = 0.28):
  <b>N(d_1) = N(0.2750) = 0.6083</b>   <i>(At Z = 0.28, N(0.28) = 0.6103)</i>
• For d_2 = -0.0785 (interpolating between Z = -0.07 and Z = -0.08):
  <b>N(d_2) = N(-0.0785) = 0.4687</b>   <i>(At Z = -0.08, N(-0.08) = 0.4681)</i>

<b>Step 3: Calculate Call Option Price (C_0):</b>
C_0 = S_0 × N(d_1) - X × e^(-rT) × N(d_2)
• S_0 × N(d_1) = 650 × 0.60834 = <b>Rs 395.42</b>
• X × e^(-rT) × N(d_2) = 660 × e^(-0.10 × 0.5) × 0.4687 = 660 × 0.951229 × 0.4687 = 627.811 × 0.4687 = <b>Rs 294.25</b>
• <b>C_0</b> = 395.42 - 294.25 = <b>Rs 101.17</b>
<i>(Note: Using rounded 2-decimal Z-table values d_1 = 0.28 [N = 0.6103] and d_2 = -0.08 [N = 0.4681], C_0 = 650(0.6103) - 627.81(0.4681) = 396.70 - 293.88 = <b>Rs 102.82</b>.)</i>""")
    add_hint(story, "BSM 3-Step Routine: (1) Compute σ√T first (0.5 × √0.5 = 0.3536) because it appears in BOTH the denominator of d_1 and in d_2 = d_1 - σ√T! (2) Remember N(-z) = 1 - N(z) if your Z-table only shows positive values: N(-0.08) = 1 - 0.5319 = 0.4681.")

    add_q(story, "Q17. An investor enters into two long futures contracts on orange. Each contract has a contract size of 10,000 pounds. The current futures price is Rs 100 per pound. The initial margin is Rs 3,00,000 per contract, and the maintenance margin is Rs 1,50,000.\na. What price change would lead to a margin call?\nb. What happens if the margin call money is not deposited?\nc. Under what circumstances could Rs 1,00,000 be withdrawn from the margin account?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Position: <b>2 Long Futures Contracts</b> on orange
• Contract size per contract = 10,000 pounds → <b>Total quantity (Q) = 2 × 10,000 = 20,000 pounds</b>
• Initial futures price (F_0) = Rs 100 per pound
• Initial Margin (IM) = Rs 300,000 per contract → <b>Total Initial Margin = 2 × Rs 300,000 = Rs 600,000</b>
• Maintenance Margin (MM) = Rs 150,000 per contract → <b>Total Maintenance Margin = 2 × Rs 150,000 = Rs 300,000</b>

<b>a. Price Change That Would Lead to a Margin Call:</b>
• A margin call is triggered when the margin account balance falls below the Maintenance Margin.
• Maximum allowable loss per contract before margin call = IM - MM = Rs 300,000 - Rs 150,000 = Rs 150,000 per contract (or Rs 300,000 total across 2 contracts).
•Since this is a <b>long position</b>, losses occur when the futures price <b>falls</b>:
  Price Drop per pound (ΔP) = (IM - MM) / Contract Size = Rs 150,000 / 10,000 pounds = <b>Rs 15 per pound</b>
• Therefore, a <b>price decrease of more than Rs 15 per pound (i.e., if the futures price falls below Rs 100 - Rs 15 = Rs 85 per pound)</b> will trigger a margin call.

<b>b. What Happens If the Margin Call Money (Variation Margin) Is Not Deposited:</b>
If the investor fails to deposit the required variation margin (to restore the account balance back up to the Initial Margin of Rs 300,000 per contract) within the specified time, the broker/clearinghouse will <b>immediately liquidate (close out) the investor's long futures position</b> by selling two offsetting futures contracts in the market, deduct the losses and commission fees, and return any remaining balance to the investor.

<b>c. Circumstances Under Which Rs 100,000 Could Be Withdrawn from the Margin Account:</b>
• An investor can withdraw any excess funds above the Initial Margin requirement.
• <b>Case 1 (Rs 100,000 withdrawn in total from the 2-contract account):</b>
  Required Price Rise = Total Withdrawal / Total Pounds = Rs 100,000 / 20,000 pounds = <b>Rs 5 per pound</b> (i.e., futures price rises to <b>Rs 105 per pound</b> or higher).
• <b>Case 2 (Rs 100,000 withdrawn per contract, i.e., Rs 200,000 total):</b>
  Required Price Rise = Rs 100,000 / 10,000 pounds = <b>Rs 10 per pound</b> (i.e., futures price rises to <b>Rs 110 per pound</b> or higher).""")
    add_hint(story, "Long Futures Margin Call Trigger Price = F_0 - [(IM - MM) / Contract Size] = 100 - (150,000 / 10,000) = Rs 85/lb. For Withdrawal in part (c), show BOTH for the total account (Rs 100,000 / 20,000 lbs = +Rs 5/lb -> Rs 105) and per contract (Rs 100,000 / 10,000 lbs = +Rs 10/lb -> Rs 110)!")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group - C: Long-Answer Questions (Attempt any THREE — ALL Solved) [3 × 10 = 30]", group_header_style))

    add_q(story, "Q18. NRIC stock is currently trading at Rs 1200 per share. At-the-money options on NRIC with 180 days to expiration are actively traded in the option exchange. You want to use the binomial model to value this option and expect that either the stock price increases by 25 percent or it decreases by 20 percent at the end of six months. You can borrow money at 8 percent per annum. Assume a 360-day year.\na. Calculate the fair price of the call option today.\nb. Calculate the arbitrage return in percentage if the actual price of this call option in the market is Rs 140.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 1,200
• Exercise price (X) = Rs 1,200 (since the option is <b>at-the-money</b>, X = S_0 = Rs 1,200)
• Time to expiration (T) = 180 days; Year = 360 days → Period fraction = 180 / 360 = <b>0.5 year</b>
• Up-move factor (u) = 1 + 0.25 = <b>1.25</b> → S_u = 1,200 × 1.25 = <b>Rs 1,500</b>
• Down-move factor (d) = 1 - 0.20 = <b>0.80</b> → S_d = 1,200 × 0.80 = <b>Rs 960</b>
• Periodic risk-free rate for 180 days (r_p) = 8% × (180 / 360) = <b>4% = 0.04</b> (so 1 + r_p = 1.04)

<b>Part (a): Fair Price of the Call Option Today (Single-Period Binomial Model):</b>
• <b>Step 1: Call Option Payoffs at Expiration (180 days):</b>
  - If stock moves up (S_u = Rs 1,500): C_u = max(S_u - X, 0) = max(1,500 - 1,200, 0) = <b>Rs 300</b>
  - If stock moves down (S_d = Rs 960): C_d = max(S_d - X, 0) = max(960 - 1,200, 0) = <b>Rs 0</b>
• <b>Step 2: Risk-Neutral Probability of Up Move (p):</b>
  p = (1 + r_p - d) / (u - d) = (1.04 - 0.80) / (1.25 - 0.80) = 0.24 / 0.45 = <b>0.5333 (or 8/15)</b>
  1 - p = 1 - 0.5333 = <b>0.4667 (or 7/15)</b>
• <b>Step 3: Fair Value of Call Option Today (C_0):</b>
  C_0 = [ p × C_u + (1 - p) × C_d ] / (1 + r_p)
  C_0 = [ (8/15) × 300 + (7/15) × 0 ] / 1.04 = 160 / 1.04 = <b>Rs 153.85</b>
  <i>(Note: If annual compounding (1.08)^(180/360) = 1.03923 is used, p = 0.5316 and C_0 = <b>Rs 153.47</b>.)</i>

<b>Part (b): Arbitrage Process and Percentage Return When Market Call Price (C_mkt) = Rs 140:</b>
• Since Market Price (Rs 140) < Fair Value (Rs 153.85), the call option is <b>underpriced</b>!
• <b>Strategy:</b> Buy the underpriced Call Option and Short the Replicating Hedge Ratio (h) of Stock (Delta Hedging):
  - <b>Hedge Ratio (h)</b> = (C_u - C_d) / (S_u - S_d) = (300 - 0) / (1,500 - 960) = 300 / 540 = <b>0.5556 shares per call (or 5 shares for every 9 calls)</b>.
• <b>Portfolio Construction (Per 1 Share Shorted & 1/h = 1.8 Calls Bought, or Per 1 Call Bought & 0.5556 Share Shorted):</b>
  - Let us form the hedge portfolio with <b>1 Call Purchased</b> (cost = Rs 140) and <b>h = 5/9 share Shorted</b> (inflow = 5/9 × 1,200 = Rs 666.67):
    Net Initial Cash Inflow (or Synthetic Borrowing) = Rs 666.67 - Rs 140.00 = <b>Rs 526.67</b>
  - At expiration (both S_u = 1,500 and S_d = 960), the terminal obligation of the short stock minus long call is fixed at:
    Terminal Obligation = (5/9) × 960 - 0 = <b>Rs 533.33</b> (or (5/9)×1,500 - 300 = 833.33 - 300 = Rs 533.33).
• <b>Implied 6-Month Borrowing Rate vs. Risk-Free Rate & Arbitrage Return:</b>
  - Present value of Rs 533.33 at r_p = 4% is 533.33 / 1.04 = Rs 512.82, yielding an instant arbitrage profit today of Rs 153.85 - Rs 140 = <b>Rs 13.85 per call</b> (or Rs 13.85 × 1.04 = <b>Rs 14.40</b> at maturity).
  - <b>Arbitrage Return (%) on Call Investment:</b> (153.85 - 140) / 140 = 13.85 / 140 = <b>9.89%</b> instant return (or on the hedged portfolio outlay of Rs 526.67: 6-month synthetic financing rate is (533.33 - 526.67) / 526.67 = <b>1.265%</b> for 6 months [<b>2.53% p.a.</b>] vs. investing at 4% for 6 months [8% p.a.], earning a net arbitrage spread of 4% - 1.265% = <b>2.735% for 6 months [5.47% p.a.]</b>).""")
    add_hint(story, "In Binomial Option Pricing, always compute Hedge Ratio h = (C_u - C_d)/(S_u - S_d) = 300/540 = 5/9 = 0.5556. If Market Call (140) < Fair Call (153.85), BUY Call and SHORT h shares of Stock!")

    add_q(story, "Q19. A one-year swap with quarterly payment and notional principal of Rs 100 million is entered between Citizen Investment Trust (CIT) and Global Bank. Payments will be based on a 30-day month and a 360-day year. The CIT agreed to make interest payments based on the 90-day T-bill rate, and Global Bank agreed to make interest payments based on the 90-day SOFR minus a spread.\na. Find the spread that should be deducted from the SOFR rate on each payment date.\n[Init Term Structure: 90d: SOFR 7.50%, T-bill 5.50%; 180d: SOFR 7.95%, T-bill 5.87%; 270d: SOFR 8.52%, T-bill 6.30%; 360d: SOFR 9.00%, T-bill 6.90%]\nb. Assume it is 60 days into the life of the swap. Find the value of the swap for both counterparties.\n[New Term Structure at 60d: 30d: SOFR 8.00%, T-bill 6.00%; 120d: SOFR 8.45%, T-bill 6.47%; 210d: SOFR 9.00%, T-bill 6.95%; 300d: SOFR 9.55%, T-bill 7.40%]")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Notional Principal (NP) = Rs 100,000,000 (Rs 100 million)
• Swap Type: 1-year quarterly Basis Swap (CIT pays 90-day T-bill rate; Global Bank pays 90-day SOFR minus a fixed spread).

<b>Part (a): Calculation of the Spread to be Deducted from SOFR at Initiation (t = 0):</b>
• <b>Step 1: Compute Discount Factors B_i = 1 / [1 + R_i × (Days_i / 360)] at Initiation:</b>
  - <b>SOFR Discount Factors (B_SOFR):</b>
    B_1(90d)  = 1 / [1 + 0.0750 × (90/360)]  = 1 / 1.01875 = <b>0.981595</b>
    B_2(180d) = 1 / [1 + 0.0795 × (180/360)] = 1 / 1.03975 = <b>0.961770</b>
    B_3(270d) = 1 / [1 + 0.0852 × (270/360)] = 1 / 1.06390 = <b>0.939938</b>
    B_4(360d) = 1 / [1 + 0.0900 × (360/360)] = 1 / 1.09000 = <b>0.917431</b>
    Sum of SOFR Discount Factors (ΣB_SOFR) = 0.981595 + 0.961770 + 0.939938 + 0.917431 = <b>3.800734</b>

  - <b>T-Bill Discount Factors (B_Tbill):</b>
    B_1(90d)  = 1 / [1 + 0.0550 × (90/360)]  = 1 / 1.01375 = <b>0.986436</b>
    B_2(180d) = 1 / [1 + 0.0587 × (180/360)] = 1 / 1.02935 = <b>0.971487</b>
    B_3(270d) = 1 / [1 + 0.0630 × (270/360)] = 1 / 1.04725 = <b>0.954882</b>
    B_4(360d) = 1 / [1 + 0.0690 × (360/360)] = 1 / 1.06900 = <b>0.935454</b>
    Sum of T-Bill Discount Factors (ΣB_Tbill) = 0.986436 + 0.971487 + 0.954882 + 0.935454 = <b>3.848259</b>

• <b>Step 2: Compute Fixed Swap Rates Equivalent to SOFR and T-Bill Legs:</b>
  - Quarterly Fixed Rate for SOFR = (1 - B_4,SOFR) / ΣB_SOFR = (1 - 0.917431) / 3.800734 = 0.082569 / 3.800734 = <b>0.021724 (2.1724% per quarter)</b>
    Annualized SOFR Swap Fixed Rate (R_SOFR) = 2.1724% × (360 / 90) = <b>8.6898% (or 8.69% p.a.)</b>
  - Quarterly Fixed Rate for T-Bill = (1 - B_4,Tbill) / ΣB_Tbill = (1 - 0.935454) / 3.848259 = 0.064546 / 3.848259 = <b>0.016773 (1.6773% per quarter)</b>
    Annualized T-Bill Swap Fixed Rate (R_Tbill) = 1.6773% × (360 / 90) = <b>6.7091% (or 6.71% p.a.)</b>

• <b>Step 3: Required Spread to Deduct from SOFR:</b>
  - <b>Quarterly Spread</b> = 2.1724% - 1.6773% = <b>0.4952% (or 0.50% per quarter)</b>
  - <b>Annualized Spread</b> = 8.6898% - 6.7091% = <b>1.9806% (or 1.98% p.a.)</b>

<b>Part (b): Value of the Swap 60 Days into the Life of the Swap (Remaining Days: 30, 120, 210, 300):</b>
• <b>Step 1: New Discount Factors at Day 60:</b>
  - <b>New SOFR Discount Factors (B'_SOFR):</b>
    B'_1(30d)  = 1 / [1 + 0.0800 × (30/360)]  = <b>0.993377</b>
    B'_2(120d) = 1 / [1 + 0.0845 × (120/360)] = <b>0.972607</b>
    B'_3(210d) = 1 / [1 + 0.0900 × (210/360)] = <b>0.950119</b>
    B'_4(300d) = 1 / [1 + 0.0955 × (300/360)] = <b>0.926282</b>
    Sum (ΣB'_SOFR) = <b>3.842385</b>
  - <b>New T-Bill Discount Factors (B'_Tbill):</b>
    B'_1(30d)  = 1 / [1 + 0.0600 × (30/360)]  = <b>0.995025</b>
    B'_2(120d) = 1 / [1 + 0.0647 × (120/360)] = <b>0.978889</b>
    B'_3(210d) = 1 / [1 + 0.0695 × (210/360)] = <b>0.961038</b>
    B'_4(300d) = 1 / [1 + 0.0740 × (300/360)] = <b>0.941915</b>
    Sum (ΣB'_Tbill) = <b>3.876867</b>

• <b>Step 2: Present Value of Both Legs at Day 60 (per Re 1 Notional):</b>
  - First quarterly coupon (at Day 90, fixed at Day 0):
    SOFR coupon = 0.0750 × (90/360) = 0.01875;  T-Bill coupon = 0.0550 × (90/360) = 0.01375
  - Value of Pure Floating SOFR Leg = (1 + 0.01875) × B'_1,SOFR = 1.01875 × 0.993377 = <b>1.012003</b>
  - Value of Pure Floating T-Bill Leg = (1 + 0.01375) × B'_1,Tbill = 1.01375 × 0.995025 = <b>1.008706</b>
  - Present Value of Spread Payments (0.004952 per quarter):
    PV(Spread) = 0.004952 × ΣB'_SOFR = 0.004952 × 3.842385 = <b>0.019026</b>
    <i>(Note: If only the net difference between pure floating legs is compared before spread PV: (1.012003 - 1.008706) × 100M = +Rs 329,700; or if next coupon includes spread 0.01875 - 0.004952 = 0.013798: V_SOFR-spread = 1.013798 × 0.993377 = 1.007084 → Net Value to CIT = (1.007084 - 1.008706) × 100M = <b>-Rs 162,200</b>; or with full remaining spread stream: (1.012003 - 0.019026 - 1.008706) × 100M = <b>-Rs 1,572,902</b>.)</i>""")
    add_hint(story, "In a Basis Swap (SOFR vs. T-Bill), first find the Fixed Rate for a SOFR swap and the Fixed Rate for a T-Bill swap using R = [(1 - B_4) / Sum(B)] × (360/90). The Spread is simply R_SOFR - R_Tbill = 8.69% - 6.71% = 1.98% p.a. (or 0.495% per quarter)!")

    add_q(story, "Q20. A stock is expected to pay a dividend of Rs 10 per share in two months and five months from today. The stock price is Rs 500, and the risk-free interest rate is 8% p.a. with continuous compounding for all maturities. An investor has just taken a short position in a six-month forward contract on the stock.\na. What are the forward price and the initial value of the forward contract?\nb. Show the arbitrage process if the market price of the forward is Rs 515.\nc. Three months later, the stock price is Rs 480, and the risk-free rate of interest is still 8% p.a. What are the forward price and the value of the short position in the forward contract?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 500
• Dividends: D_1 = Rs 10 in 2 months (t_1 = 2/12 yr); D_2 = Rs 10 in 5 months (t_2 = 5/12 yr)
• Risk-free interest rate (r) = 8% p.a. = 0.08 (continuously compounded)
• Maturity of forward contract (T) = 6 months = 6/12 = <b>0.5 year</b>

<b>Part (a): Forward Price (F_0) and Initial Value of the Forward Contract:</b>
• <b>Step 1: Present Value of Expected Dividends (I):</b>
  I = D_1 × e^(-r × t_1) + D_2 × e^(-r × t_2)
  I = 10 × e^(-0.08 × 2/12) + 10 × e^(-0.08 × 5/12)
  I = 10 × e^(-0.013333) + 10 × e^(-0.033333)
  I = 9.86755 + 9.67216 = <b>Rs 19.5397 (or Rs 19.54)</b>
• <b>Step 2: Fair 6-Month Forward Price (F_0):</b>
  F_0 = (S_0 - I) × e^(r × T)
  F_0 = (500 - 19.5397) × e^(0.08 × 0.5)
  F_0 = 480.4603 × e^(0.04) = 480.4603 × 1.040811 = <b>Rs 500.07</b>
• <b>Step 3: Initial Value of the Forward Contract (V_0):</b>
  At the time of initiation, the value of a forward contract is always <b>Rs 0</b>.

<b>Part (b): Arbitrage Process If Market Forward Price (F_mkt) = Rs 515:</b>
• Since F_mkt (Rs 515) > Fair F_0 (Rs 500.07), the forward contract is <b>overpriced</b> → Execute <b>Cash-and-Carry Arbitrage</b> (Borrow, Buy Spot Stock, Short Forward):
  - <b>Today (t = 0):</b>
    1. Borrow Rs 500 at 8% continuous interest:
       - Loan 1: Borrow Rs 9.8676 for 2 months (to be repaid using the first Rs 10 dividend at t = 2 months).
       - Loan 2: Borrow Rs 9.6722 for 5 months (to be repaid using the second Rs 10 dividend at t = 5 months).
       - Loan 3: Borrow the remaining Rs 480.4603 (= 500 - 19.5397) for 6 months.
    2. Use the Rs 500 borrowed to buy 1 share of the stock in the spot market.
    3. Enter into a <b>short</b> 6-month forward contract at F_mkt = Rs 515.
  - <b>At 2 Months & 5 Months:</b> Collect each Rs 10 dividend and pay off Loan 1 and Loan 2 completely.
  - <b>At Maturity (6 Months):</b>
    1. Deliver the share under the short forward contract and receive <b>Rs 515.00</b>.
    2. Repay Loan 3 with interest: Rs 480.4603 × e^(0.08 × 0.5) = <b>Rs 500.07</b>.
    3. <b>Riskless Arbitrage Profit at Maturity</b> = Rs 515.00 - Rs 500.07 = <b>Rs 14.93 per share</b>.

<b>Part (c): Forward Price and Value of Short Position Three Months Later (t = 3/12 = 0.25 yr):</b>
• After 3 months, the first dividend (at 2 months) has already been paid! Only the second dividend of Rs 10 (at 5 months, which is now 5 - 3 = <b>2 months away</b>) remains, and remaining time to maturity is T - t = 6 - 3 = <b>3 months (0.25 year)</b>.
• Present value of remaining dividend at t = 3 months (I_t):
  I_t = 10 × e^(-0.08 × 2/12) = 10 × e^(-0.013333) = <b>Rs 9.8676 (or Rs 9.87)</b>
• <b>New Forward Price at t = 3 months (F_t):</b>
  F_t = (S_t - I_t) × e^[r × (T - t)]
  F_t = (480 - 9.8676) × e^(0.08 × 3/12) = 470.1324 × e^(0.02) = 470.1324 × 1.020201 = <b>Rs 479.63</b>
• <b>Value of the Short Forward Position at t = 3 months (V_short):</b>
  V_short = (F_0 - F_t) × e^[-r × (T - t)]
  V_short = (500.07 - 479.63) × e^(-0.08 × 0.25) = 20.44 × 0.980199 = <b>+Rs 20.03 per share</b>
  <i>(Alternative direct formula: V_short = F_0 × e^[-r(T-t)] - (S_t - I_t) = 500.07 × e^(-0.02) - (480 - 9.8676) = 490.168 - 470.132 = <b>+Rs 20.04</b>.)</i>""")
    add_hint(story, "Three months into a 6-month forward (Part c), watch out for two things: (1) The 2-month dividend is ALREADY gone; only the 5-month dividend remains, and it is now 5 - 3 = 2 months away! (2) Since the investor holds a SHORT position and the forward price dropped from Rs 500.07 to Rs 479.63, the short position has a POSITIVE value: (F_0 - F_t) × e^(-r(T-t)) = +Rs 20.03!")

    add_q(story, "Q21. Explain the margin rule and the margin operation process by a clearinghouse in option trading.")
    add_a(story, """<b>Answer:</b>
<b>1. Concept of Margin Rules in Option Trading:</b>
In option trading, margin rules differ fundamentally between option <b>buyers (long positions)</b> and option <b>writers (short positions)</b> because their risk profiles are asymmetric:
• <b>Long Option Positions (Buyers of Calls and Puts):</b>
  Generally, option buyers must pay 100% of the option premium upfront in cash. Once the premium is paid, the buyer has <b>no further margin requirement</b> because the buyer's maximum possible loss is limited to the premium already paid, and they have no future obligation to perform.
• <b>Short Option Positions (Writers of Naked or Covered Calls and Puts):</b>
  An option writer receives the premium upfront but assumes a contingent liability to buy or sell the underlying asset if the option is exercised against them. Because potential losses on naked short calls are unlimited (and very large on short puts), exchanges and clearinghouses require option writers to post and maintain performance margin.
  - <i>Naked (Uncovered) Option Writing Margin:</i> Typically calculated as the greater of two exchange formulas:
    Formula 1: 100% of Option Proceeds + 20% of Underlying Stock Value - Out-of-the-Money Amount (if any).
    Formula 2: 100% of Option Proceeds + 10% of Underlying Stock Value (for calls) or 10% of Exercise Price (for puts).
  - <i>Covered Call Writing:</i> If the writer of a call option already owns and deposits the underlying shares in escrow with the broker, no separate cash margin is required on the short call because the shares guarantee delivery.

<b>2. Margin Operation Process by a Clearinghouse in Option Trading:</b>
• <b>Step 1: Novation by the Options Clearinghouse (e.g., OCC):</b> Once a trade is executed on the options exchange, the Clearinghouse steps in as the central counterparty—becoming the buyer to every option writer and the writer to every option buyer, eliminating bilateral credit risk.
• <b>Step 2: Initial Margin Deposit:</b> Option writers deposit Initial Margin with their brokerage firm (clearing member), which in turn posts clearing margin with the Clearinghouse in cash or Treasury securities.
• <b>Step 3: Daily Valuation and Marking-to-Market of Short Options:</b> At the end of each trading day, the Clearinghouse recalculates the required margin based on the closing stock price and closing option price.
• <b>Step 4: Maintenance Margin and Margin Calls:</b> If the underlying stock moves against the option writer (e.g., stock price rises sharply against a naked call writer), the required maintenance margin increases. If the writer's account equity falls below the maintenance requirement, the broker issues a <b>margin call</b> requiring immediate cash deposit.
• <b>Step 5: Forced Liquidation or Exercise Settlement:</b> If the writer fails to meet the margin call, the broker closes out the short option position by buying back the option in the market. When an option holder chooses to exercise, the Clearinghouse randomly assigns the exercise notice to a clearing member with a short position, using the margin/collateral to guarantee settlement.""")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group - D: Comprehensive-Answer / Case / Situation Analysis [20 Marks]", group_header_style))

    add_q(story, "Q22. Case Study: Krishna Pauroti Company\nStock closed at S_0 = Rs 240 today. Call and Put options with Exercise Price X = Rs 240 and T = 3 months to expiration closed at C = Rs 40 and P = Rs 20, respectively. Risk-free rate r = 6% p.a. Total investment budget = Rs 240,000.\na. If you believe the court verdict will favor the company and want to speculate on the option, which option do you buy? Why? How much will you earn/lose if the stock price after three months increases to Rs 350? What will be your annual rate of return?\nb. If you believe that the court verdict will come against the company and want to speculate on the option, which option do you buy? Why? How much will you earn/lose if the stock price after three months decreases to Rs 250 [also solved for Rs 150]? What will be your annual rate of return? Compare the risk and return of your investment with that of your stock investment.\nc. Assume you cannot guess whether the court verdict may come in favor of or against the company. Is a long straddle beneficial in such conditions? Why? Calculate gain/loss from long straddle for expiration stock prices of Rs 160, Rs 180, … Rs 320. After three months, calculate the maximum possible gain, maximum possible loss, and breakeven stock price(s) for your strategy.\nd. Considering the uncertainty of the verdict, you want to ensure your portfolio of stocks using put options. How many stocks and put options do you need to hold? What will be the ensured value of your portfolio? What will be the value of the ensured portfolio if the verdict came in favor of the company, and the stock price increased to Rs 350? Also, calculate the cost of insurance and the upside capture. [4+4+6+6]")
    add_a(story, """<b>Answer (Step-by-Step Comprehensive Case Solution):</b>
<b>Given Summary:</b>
• Current Stock Price (S_0) = Rs 240; Exercise Price (X) = Rs 240; Time (T) = 3 months (0.25 year)
• Call Premium (C) = Rs 40; Put Premium (P) = Rs 20; Risk-free rate (r) = 6% p.a.
• Total Capital to Invest = <b>Rs 240,000</b>

<b>Part (a): Bullish Speculation (Court Verdict Favors the Company) [4 Marks]:</b>
• <b>Which Option to Buy & Why:</b> You should <b>buy Call Options</b> on Krishna stock. If the court verdict favors the company, the stay order will be lifted, capacity expansion will proceed, and the stock price will surge above Rs 240. Call options give high leveraged upside participation with limited downside risk.
• <b>Number of Call Options Purchased:</b> Rs 240,000 / Rs 40 = <b>6,000 call options</b>.
• <b>Total Dollar Gain/Loss if S_T = Rs 350 after 3 Months:</b>
  - Profit per call = max(S_T - X, 0) - C = (350 - 240) - 40 = 110 - 40 = <b>Rs 70 per call</b>
  - <b>Total Net Profit</b> = 6,000 calls × Rs 70 = <b>+Rs 420,000</b>
• <b>Annual Rate of Return:</b>
  - 3-Month Holding Period Return (HPR) = Rs 420,000 / Rs 240,000 = 70 / 40 = <b>175%</b>
  - <b>Simple Annualized Rate of Return</b> = 175% × (12 / 3) = <b>700% per annum</b>
  <i>(Compound Effective Annual Return = (1 + 1.75)^4 - 1 = <b>5,618.75% p.a.</b>)</i>

<b>Part (b): Bearish Speculation (Court Verdict Comes Against the Company) [4 Marks]:</b>
• <b>Which Option to Buy & Why:</b> You should <b>buy Put Options</b> on Krishna stock because an adverse verdict will permanently ban the popular bread brand, causing the stock price to plunge below the strike price of Rs 240.
• <b>Number of Put Options Purchased:</b> Rs 240,000 / Rs 20 = <b>12,000 put options</b>.
• <b>Gain/Loss and Annual Return After 3 Months:</b>
  - <b>Case 1 (At literally printed S_T = Rs 250):</b>
    Since S_T = Rs 250 > Strike X = Rs 240, the put option is out-of-the-money and expires worthless!
    - Loss per put = -Rs 20 → <b>Total Loss = -Rs 240,000</b> (100% of investment lost).
    - 3-Month HPR = <b>-100%</b>; Simple Annualized Return = -100% × (12/3) = <b>-400% p.a.</b>
    - Meanwhile, an investor who bought 1,000 shares of stock at Rs 240 would have Rs 250,000 (+Rs 10,000 profit; +4.17% in 3 months or +16.67% p.a.).
  - <b>Case 2 (If "decreases to Rs 250" in the question paper is a misprint for "decreases to Rs 150"):</b>
    At S_T = Rs 150:
    - Profit per put = max(240 - 150, 0) - 20 = 90 - 20 = <b>+Rs 70 per put</b>
    - <b>Total Net Profit</b> = 12,000 puts × Rs 70 = <b>+Rs 840,000</b>
    - 3-Month HPR = 840,000 / 240,000 = <b>+350%</b>; Simple Annualized Return = 350% × 4 = <b>+1,400% p.a.</b>
    - Meanwhile, buying 1,000 shares of stock at Rs 240 and holding to Rs 150 results in a loss of (150 - 240) × 1,000 = <b>-Rs 90,000</b> (-37.5% in 3 months or -150% p.a.).
• <b>Risk & Return Comparison (Options vs. Stock):</b> Options provide extreme financial leverage—magnifying positive percentage returns when the forecast is right, but carrying a 100% loss risk of the entire Rs 240,000 capital if the option finishes out-of-the-money, whereas direct stock ownership has much lower volatility and only loses 100% if the company's share price drops to zero.

<b>Part (c): Long Straddle Strategy Under Verdict Uncertainty [6 Marks]:</b>
• <b>Is a Long Straddle Beneficial & Why?</b>
  <b>Yes, a Long Straddle is highly beneficial.</b> A long straddle involves buying 1 Call (X = 240, C = 40) and 1 Put (X = 240, P = 20) simultaneously at a combined cost of C + P = 40 + 20 = <b>Rs 60 per straddle</b>. Because the court verdict is a binary event that will either send the stock soaring (if favorable) or crashing (if unfavorable), volatility will be huge, allowing one leg to generate large profits that more than offset the Rs 60 combined premium.
• <b>Number of Straddles with Rs 240,000:</b> Rs 240,000 / Rs 60 = <b>4,000 straddles</b> (4,000 calls + 4,000 puts).
• <b>Maximum Possible Gain, Maximum Possible Loss, and Breakeven Stock Prices:</b>
  - <b>Maximum Possible Gain:</b> <b>Unlimited</b> on the upside (as S_T → ∞, profit → ∞); on the downside (if S_T falls to Rs 0), max downside gain is Rs 240 - Rs 60 = <b>Rs 180 per straddle</b> (or 4,000 × 180 = <b>Rs 720,000</b>).
  - <b>Maximum Possible Loss:</b> <b>Rs 60 per straddle</b> (or <b>Rs 240,000 total</b>), occurring only if S_T = Rs 240 at expiration.
  - <b>Two Breakeven Stock Prices (BEP):</b>
    1. Lower Breakeven Price = X - (C + P) = 240 - 60 = <b>Rs 180</b>
    2. Upper Breakeven Price = X + (C + P) = 240 + 60 = <b>Rs 300</b>""")

    t_c22 = make_table([
        [P_hdr("Expiration Stock Price (S_T)"), P_hdr("Call Payoff max(S_T-240, 0)"), P_hdr("Put Payoff max(240-S_T, 0)"), P_hdr("Combined Payoff (Rs)"), P_hdr("Initial Cost C + P (Rs)"), P_hdr("Net Gain/Loss per Straddle (Rs)"), P_hdr("Total Gain/Loss (4,000 Straddles)")],
        [P("Rs 160"), P("0"), P("80"), P("80"), P("60"), P("+Rs 20", True), P("+Rs 80,000", True)],
        [P("Rs 180 (Lower BEP)"), P("0"), P("60"), P("60"), P("60"), P("Rs 0", True), P("Rs 0", True)],
        [P("Rs 200"), P("0"), P("40"), P("40"), P("60"), P("-Rs 20"), P("-Rs 80,000")],
        [P("Rs 220"), P("0"), P("20"), P("20"), P("60"), P("-Rs 40"), P("-Rs 160,000")],
        [P("Rs 240 (Max Loss)"), P("0"), P("0"), P("0"), P("60"), P("-Rs 60", True), P("-Rs 240,000", True)],
        [P("Rs 260"), P("20"), P("0"), P("20"), P("60"), P("-Rs 40"), P("-Rs 160,000")],
        [P("Rs 280"), P("40"), P("0"), P("40"), P("60"), P("-Rs 20"), P("-Rs 80,000")],
        [P("Rs 300 (Upper BEP)"), P("60"), P("0"), P("60"), P("60"), P("Rs 0", True), P("Rs 0", True)],
        [P("Rs 320"), P("80"), P("0"), P("80"), P("60"), P("+Rs 20", True), P("+Rs 80,000", True)],
    ], col_widths=[80, 68, 68, 68, 62, 74, 80])
    story.append(t_c22)
    story.append(Spacer(1, 6))

    add_a(story, """<b>Part (d): Portfolio Insurance Using Protective Put [6 Marks]:</b>
• <b>1. Number of Stocks and Put Options to Hold (Protective Put Strategy):</b>
  - Cost of 1 Insured Unit (1 Share of Stock @ Rs 240 + 1 Put Option @ Rs 20) = Rs 240 + Rs 20 = <b>Rs 260 per unit</b>.
  - With a fixed budget of Rs 240,000:
    Number of Shares and Put Options = Rs 240,000 / Rs 260 = <b>923.08 shares and 923.08 put options</b> (or <b>923 shares and 923 puts</b> with Rs 20 cash left over).
    <i>(Note: If an investor already holds 1,000 shares worth Rs 240,000 and buys 1,000 puts for an extra Rs 20,000 [total outlay Rs 260,000], the corresponding figures are also shown below!)</i>
• <b>2. Ensured (Floor) Value of the Portfolio:</b>
  - Regardless of how low the stock price falls, each share can be sold at the put strike price X = Rs 240:
    <b>Ensured Floor Value</b> = 923.0769 × Rs 240 = <b>Rs 221,538.46</b> (or 923 × Rs 240 = <b>Rs 221,520</b>; and for 1,000 shares = <b>Rs 240,000</b>).
• <b>3. Value of the Ensured Portfolio if S_T Increases to Rs 350:</b>
  - At S_T = Rs 350, the put options expire worthless (0) and each share is worth Rs 350:
    <b>Value of Ensured Portfolio at S_T = Rs 350</b> = 923.0769 × Rs 350 = <b>Rs 323,076.92</b> (or 923 × Rs 350 = <b>Rs 323,050</b>; and for 1,000 shares, net value after Rs 20,000 put cost = Rs 350,000 - Rs 20,000 = <b>Rs 330,000</b>).
• <b>4. Cost of Insurance and Upside Capture:</b>
  - <b>Uninsured Stock Portfolio Value at S_T = Rs 350:</b> Investing Rs 240,000 solely in stock buys 1,000 shares (240,000 / 240), which grows to 1,000 × Rs 350 = <b>Rs 350,000</b> (Gain = Rs 110,000 or +45.83%).
  - <b>Cost of Insurance:</b>
    • In total Put Premium paid (for 923.08 units) = 923.0769 × Rs 20 = <b>Rs 18,461.54</b> (or <b>Rs 20 per share</b> / <b>Rs 20,000</b> for 1,000 shares, which is 20/260 = <b>7.69%</b> of portfolio value).
    • In terms of foregone upside terminal wealth at S_T = 350: Rs 350,000 - Rs 323,076.92 = <b>Rs 26,923.08</b>.
  - <b>Upside Capture:</b>
    • <b>Terminal Wealth Upside Capture Ratio</b> = (Insured Portfolio Terminal Value / Uninsured Portfolio Terminal Value) × 100
      = (Rs 323,076.92 / Rs 350,000) × 100 = <b>92.31%</b> (or on 1,000 shares net of premium: 330,000 / 350,000 = <b>94.29%</b>).
    • <b>Capital Gain / Return Upside Capture Ratio</b> = (Insured Net Gain / Uninsured Net Gain) × 100
      = (Rs 83,076.92 / Rs 110,000) × 100 = <b>75.52%</b> (or on 1,000 shares: (330,000 - 240,000) / 110,000 = 90,000 / 110,000 = <b>81.82%</b>).""")
    add_hint(story, "In Protective Put Portfolio Insurance (Q22d) with Rs 240,000 budget: Cost per insured share = S_0 + P = 240 + 20 = Rs 260, so Shares = Puts = 240,000 / 260 = 923.08! Ensured Floor = 923.08 × 240 = Rs 221,538.46, and Terminal Value Upside Capture = S_0 / (S_0 + P) = 240 / 260 = 92.31%!")
