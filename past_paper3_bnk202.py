from past_pdf_base import (
    Paragraph, Spacer, PageBreak, paper_header_style, group_header_style,
    add_q, add_a, add_hint, make_table, P, P_hdr
)

def build_past_paper3(story):
    story.append(Paragraph(
        "PAPER 3: TRIBHUVAN UNIVERSITY — BNK 202: FINANCIAL DERIVATIVES<br/>"
        "<font size=10>BBA / Eighth Semester | April 2026 | Full Marks: 100 | Pass Marks: 50 | Time: 3 Hrs</font>",
        paper_header_style
    ))

    # ==================== GROUP A ====================
    story.append(Paragraph("Group 'A': Brief Answer Questions [10 x 2 = 20]", group_header_style))

    add_q(story, "Q1. State the types of financial derivatives markets.")
    add_a(story, """<b>Answer:</b> Financial derivatives markets are classified into two main types:
• <b>1. Exchange-Traded Derivatives Market:</b> Standardized contracts (such as futures and listed options) traded on organized exchanges (e.g., CME, CBOE) with a central clearinghouse, daily marking-to-market, and zero counterparty default risk.
• <b>2. Over-the-Counter (OTC) Derivatives Market:</b> Customized, privately negotiated contracts (such as forwards, swaps, and exotic options) arranged directly between financial institutions and corporate clients without an exchange floor.""")

    add_q(story, "Q2. Define the term call option.")
    add_a(story, """<b>Answer:</b> A call option is a financial derivative contract that gives the buyer (holder) the <b>right, but not the obligation</b>, to <b>buy</b> a specified quantity of an underlying asset at a predetermined price (the exercise or strike price, X) on or before a specified expiration date, in exchange for paying an upfront fee called the call premium (C).""")

    add_q(story, "Q3. State the meaning of minimum value of put option.")
    add_a(story, """<b>Answer:</b> The minimum value (or lower bound) of a put option is the lowest theoretical price at which the put can trade without creating a riskless arbitrage opportunity:
• <b>For a European Put:</b> P_min = max[ X * e^(-rT) - S_0 , 0 ]  (or max[ X / (1 + r)^T - S_0 , 0 ])
• <b>For an American Put:</b> P_min = max[ X - S_0 , 0 ] (its intrinsic value, since it can be exercised immediately).""")

    add_q(story, "Q4. Write the meaning of overpriced put with one example.")
    add_a(story, """<b>Answer:</b> An <b>overpriced put option</b> is a put option whose actual market price (P_mkt) exceeds its fair theoretical value (as determined by Black-Scholes, Binomial model, or Put-Call Parity) or exceeds its upper bound (X).
• <b>Example:</b> If the Black-Scholes fair value of a put option on ABC stock is Rs 18, but the put is currently trading in the market at Rs 25, the put option is overpriced by Rs 7, and an arbitrageur/trader should <b>sell (write) the overpriced put</b> and hedge with the underlying stock.""")

    add_q(story, "Q5. List out any four assumptions of Black Scholes option pricing model.")
    add_a(story, """<b>Answer:</b> Four core assumptions of the Black-Scholes-Merton (BSM) option pricing model are:
• <b>1. European-Style Exercise & No Dividends:</b> The option can only be exercised at expiration, and the underlying stock pays no dividends during the option's life.
• <b>2. Lognormal Stock Price & Constant Volatility:</b> Stock prices follow a continuous geometric Brownian motion with constant return volatility (sigma).
• <b>3. Constant Risk-Free Interest Rate:</b> The continuously compounded risk-free rate (r) is known and constant across all maturities.
• <b>4. Frictionless Markets:</b> There are no transaction costs or taxes, short selling is permitted without penalty, and trading is continuous.""")

    add_q(story, "Q6. What is butterfly spread?")
    add_a(story, """<b>Answer:</b> A <b>butterfly spread</b> is a neutral four-option combination strategy using three strike prices (X_1 &lt; X_2 &lt; X_3, equidistant) with the same expiration date—constructed by <b>buying 1 low-strike option (X_1), selling (writing) 2 middle-strike at-the-money options (X_2), and buying 1 high-strike option (X_3)</b>. A long butterfly spread profits when the underlying stock price stays stable near the middle strike price (X_2) and has strictly limited downside risk.""")

    add_q(story, "Q7. Outline any two differences between futures and options.")
    add_a(story, """<b>Answer:</b>
• <b>1. Obligation vs. Right (Symmetry):</b> In a <b>futures contract</b>, both the buyer (long) and seller (short) have a legally binding <b>obligation</b> to perform at maturity (symmetric payoff). In an <b>option contract</b>, the buyer has the <b>right (no obligation)</b> to exercise, while the seller has the obligation if assigned (asymmetric payoff).
• <b>2. Upfront Cost & Risk Profile:</b> Entering a futures contract requires no upfront premium (only a refundable margin deposit) and carries unlimited gain/loss potential for both sides; buying an option requires paying a non-refundable upfront <b>premium</b>, which caps the buyer's maximum loss at the premium paid.""")

    add_q(story, "Q8. Mention two common types of cash flows exchanged in swaps.")
    add_a(story, """<b>Answer:</b> Two common types of cash flows exchanged in swap contracts are:
• <b>1. Fixed vs. Floating Interest Cash Flows (in a Plain Vanilla Interest Rate Swap):</b> One party pays a fixed interest rate while the other pays a floating benchmark rate (such as SOFR) on the same notional principal in the same currency.
• <b>2. Principal and Interest Cash Flows in Two Different Currencies (in a Currency Swap):</b> Or Equity Index Return vs. Floating Interest Cash Flows (in an Equity Swap).""")

    add_q(story, "Q9. State the meaning of basis risk in hedging.")
    add_a(story, """<b>Answer:</b> In futures hedging, <b>Basis</b> is defined as the difference between the Spot Price of the hedged asset and the Futures Price of the contract used: <b>Basis = Spot Price (S_t) - Futures Price (F_t)</b>.
<b>Basis risk</b> is the uncertainty (risk) that the basis will change unpredictably between the time a hedge is initiated and the time it is closed out—arising from mismatches in asset quality/grade, delivery location, or maturity date—preventing a hedge from being 100% perfect.""")

    add_q(story, "Q10. You take a long futures contract on the S&P 500 when the futures price is 1,107.40, and close it out three days later at a futures price of 1,131.75. One futures contract is for 250 the index. Ignoring interest, what are your losses/gains?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Position: 1 Long S&P 500 Futures Contract
• Initial entry futures price (F_0) = 1,107.40
• Closing futures price after 3 days (F_t) = 1,131.75
• Contract multiplier = $250 (or Rs 250) per index point

<b>Calculation of Net Gain:</b>
Gain = (F_t - F_0) x Index Multiplier x Number of Contracts
Gain = (1,131.75 - 1,107.40) x 250 x 1
Gain = 24.35 x 250 = <b>6,087.50 (Gain of $6,087.50 or Rs 6,087.50)</b>""")
    add_hint(story, "Long Futures Gain/Loss = (Ending Futures Price - Beginning Futures Price) x Contract Multiplier = (1,131.75 - 1,107.40) x 250 = +6,087.50.")

    # ==================== GROUP B ====================
    story.append(Paragraph("Group 'B': Short Answer Questions (Attempt any SIX — ALL Solved) [6 x 5 = 30]", group_header_style))

    add_q(story, "Q11. What is financial derivatives? Write its key characteristics.")
    add_a(story, """<b>Answer:</b>
<b>Meaning of Financial Derivatives:</b>
A financial derivative is a bilateral financial contract or instrument whose value is <b>derived from</b> (depends upon) the price or value of an underlying asset, reference rate, or index—such as stocks, bonds, foreign currencies, commodities, market indices, or interest rates. The main types of derivatives are Forwards, Futures, Options, and Swaps.

<b>Key Characteristics of Financial Derivatives:</b>
• <b>1. Value Derived from an Underlying Asset:</b> Has no independent intrinsic value of its own; its price fluctuates directly with changes in the spot price of the underlying asset.
• <b>2. Future Settlement Date:</b> Performance or cash settlement takes place at a specified future date (or period) agreed upon today.
• <b>3. Zero or Small Initial Net Investment (High Leverage):</b> Requires little or no upfront cash outlay compared to buying the underlying asset outright, magnifying percentage returns and risks.
• <b>4. Zero-Sum Game Nature:</b> Every long position is matched by an equal and opposite short position, so one counterparty's gain equals the other's loss.
• <b>5. Settlement Flexibility:</b> Most financial derivatives can be closed out prior to maturity via an offsetting trade or settled in cash rather than physical delivery.""")

    add_q(story, "Q12. Define a forward contract. Also write its essential features.")
    add_a(story, """<b>Answer:</b>
<b>Definition of a Forward Contract:</b>
A forward contract is a customized, privately negotiated Over-the-Counter (OTC) agreement between two parties in which one party (the buyer, holding the <b>long position</b>) agrees to buy and the other party (the seller, holding the <b>short position</b>) agrees to sell a specific quantity and quality of an underlying asset at a fixed price (the <b>forward price</b>) on a specified future date (the <b>maturity/delivery date</b>).

<b>Essential Features of a Forward Contract:</b>
• <b>1. Bilateral Over-the-Counter (OTC) Negotiation:</b> Privately negotiated directly between two counterparties (e.g., a bank and an importer) without an exchange floor.
• <b>2. Complete Customization:</b> The contract size, underlying asset quality, delivery date, and settlement procedure are tailored to the exact needs of the two parties.
• <b>3. No Upfront Premium or Daily Marking-to-Market:</b> At initiation, the value of a forward contract is zero and no money changes hands; gains or losses are settled only once at maturity.
• <b>4. Counterparty Default (Credit) Risk:</b> Because there is no central clearinghouse or daily margining, each party bears the credit risk that the other party may default at maturity.
• <b>5. Low Secondary Liquidity:</b> Cannot be easily transferred or closed out with a third party without the consent of the original counterparty.""")

    add_q(story, "Q13. The current price of ABC stock is Rs 300 per share. The call option is available on this stock with exercise price of Rs 300 per share. The expiration date is 3 month. The call premium is Rs 10 per share. The possible ending prices are Rs 260, Rs 270, Rs 280, Rs 290, Rs 300, Rs 310, Rs 320, Rs 330, and Rs 340.\na. Calculate the breakeven point of call option.\nb. Calculate the value of call at each ending prices.\nc. Calculate the gain or loss for call buyer at each ending prices.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 300; Exercise price (X) = Rs 300; Call premium (C) = Rs 10

<b>a. Breakeven Point (BEP) of the Call Option:</b>
Breakeven Stock Price (S_T*) = Exercise Price (X) + Call Premium (C)
S_T* = Rs 300 + Rs 10 = <b>Rs 310 per share</b>

<b>b & c. Value (Payoff) of Call at Expiration [V_C = max(S_T - 300, 0)] and Net Gain/Loss for Call Buyer [Profit = V_C - 10]:</b>""")
    t13_call = make_table([
        [P_hdr("Ending Stock Price (S_T)"), P_hdr("Exercise Decision"), P_hdr("(b) Value of Call at Expiration V_C = max(S_T - 300, 0)"), P_hdr("Call Premium Paid (C)"), P_hdr("(c) Net Gain / Loss for Call Buyer (V_C - 10)")],
        [P("Rs 260"), P("Do Not Exercise"), P("Rs 0"), P("Rs 10"), P("-Rs 10 (Loss)")],
        [P("Rs 270"), P("Do Not Exercise"), P("Rs 0"), P("Rs 10"), P("-Rs 10 (Loss)")],
        [P("Rs 280"), P("Do Not Exercise"), P("Rs 0"), P("Rs 10"), P("-Rs 10 (Loss)")],
        [P("Rs 290"), P("Do Not Exercise"), P("Rs 0"), P("Rs 10"), P("-Rs 10 (Loss)")],
        [P("Rs 300 (ATM)"), P("Indifferent / No"), P("Rs 0"), P("Rs 10"), P("-Rs 10 (Loss)")],
        [P("Rs 310 (BEP)", True), P("Exercise", True), P("Rs 10", True), P("Rs 10", True), P("Rs 0 (Breakeven)", True)],
        [P("Rs 320"), P("Exercise"), P("Rs 20"), P("Rs 10"), P("+Rs 10 (Gain)", True)],
        [P("Rs 330"), P("Exercise"), P("Rs 30"), P("Rs 10"), P("+Rs 20 (Gain)", True)],
        [P("Rs 340"), P("Exercise"), P("Rs 40"), P("Rs 10"), P("+Rs 30 (Gain)", True)],
    ], col_widths=[95, 90, 125, 80, 110])
    story.append(t13_call)
    story.append(Spacer(1, 4))
    add_hint(story, "'Value of Call at Ending Price' (part b) is the Intrinsic Payoff max(S_T - X, 0) (which is never negative!), whereas 'Gain or Loss for Call Buyer' (part c) subtracts the Rs 10 premium: Payoff - C.")

    add_q(story, "Q14. Suppose, the current price of the Himal stock is Rs 200, the exercise price of call is Rs 180, the annual risk-free interest rate is 10% and the time to expiration is one year.\na. Calculate the lower bound of European call\nb. Calculate arbitrage profit if call is selling at Rs 15 in the market.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 200; Exercise price (X) = Rs 180
• Annual risk-free interest rate (r) = 10% = 0.10; Time to expiration (T) = 1 year
• Market price of call option (C_mkt) = Rs 15

<b>a. Lower Bound (Minimum Value) of the European Call Option:</b>
• <b>Method 1 (Continuous Compounding — Standard BSM/Hull Formula):</b>
  C_min = max[ S_0 - X * e^(-rT) , 0 ]
  C_min = 200 - 180 * e^(-0.10 * 1) = 200 - (180 * 0.904837) = 200 - 162.87 = <b>Rs 37.13</b>
• <b>Method 2 (Annual Discrete Compounding — Standard Chance Formula):</b>
  C_min = max[ S_0 - X / (1 + r)^T , 0 ]
  C_min = 200 - (180 / 1.10) = 200 - 163.64 = <b>Rs 36.36</b>

<b>b. Arbitrage Profit and Strategy When Call is Selling at Rs 15 in the Market:</b>
• Since Market Price (Rs 15) &lt; Lower Bound (Rs 37.13 or Rs 36.36), the call option is severely <b>underpriced</b>!
• <b>Arbitrage Profit Today (at t = 0):</b>
  - Under Continuous Compounding: Arbitrage Profit = Rs 37.13 - Rs 15.00 = <b>Rs 22.13 per share today</b> (or Rs 22.13 * e^(0.10) = <b>Rs 24.46 at maturity</b>).
  - Under Annual Compounding: Arbitrage Profit = Rs 36.36 - Rs 15.00 = <b>Rs 21.36 per share today</b> (or Rs 21.36 * 1.10 = <b>Rs 23.50 at maturity</b>).
• <b>How to Lock In the Arbitrage (Today at t = 0):</b>
  1. <b>Buy 1 underpriced Call Option</b> for -Rs 15.00.
  2. <b>Short-sell 1 share of Himal Stock</b> for +Rs 200.00.
  3. <b>Invest the Present Value of X</b> (Rs 162.87 continuous or Rs 163.64 discrete) at 10% risk-free rate (which grows to exactly Rs 180 in 1 year to exercise the call and cover the short stock), pocketing the riskless net cash inflow of <b>Rs 22.13</b> (or <b>Rs 21.36</b>) immediately today!""")
    add_hint(story, "Show BOTH continuous discounting [200 - 180*e^(-0.10) = Rs 37.13 -> Arbitrage Profit Rs 22.13] and annual discounting [200 - 180/1.10 = Rs 36.36 -> Arbitrage Profit Rs 21.36] so your answer matches any marking key!")

    add_q(story, "Q15. Suppose that a stock is priced at Rs 80 and has a standard deviation of 30 percent. You buy a call option with an exercise price of Rs 80 that expires in 3 months. The risk-free rate is 5 percent. Determine the theoretical value of the call. Suppose that the actual call is selling for Rs 5. Suggest your investment strategy.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 80; Exercise price (X) = Rs 80
• Standard deviation (sigma) = 30% = 0.30; Time to expiration (T) = 3 / 12 = <b>0.25 year</b>
• Risk-free rate (r) = 5% = 0.05; Actual market price of call (C_mkt) = Rs 5.00

<b>Step 1: Compute d_1 and d_2 under Black-Scholes-Merton (BSM) Model:</b>
• ln(S_0 / X) = ln(80 / 80) = ln(1) = <b>0</b>
• sigma * sqrt(T) = 0.30 * sqrt(0.25) = 0.30 * 0.50 = <b>0.15</b>
• <b>d_1</b> = [ ln(S_0 / X) + (r + 0.5 * sigma^2) * T ] / (sigma * sqrt(T))
  d_1 = [ 0 + (0.05 + 0.5 * 0.09) * 0.25 ] / 0.15 = (0.095 * 0.25) / 0.15 = 0.02375 / 0.15 = <b>0.1583 (or 0.16)</b>
• <b>d_2</b> = d_1 - sigma * sqrt(T) = 0.1583 - 0.15 = <b>0.0083 (or 0.01)</b>

<b>Step 2: Cumulative Normal Probabilities N(d_1) and N(d_2):</b>
• N(d_1) = N(0.1583) = <b>0.5629</b>   <i>(Using rounded Z = 0.16: N(0.16) = 0.5636)</i>
• N(d_2) = N(0.0083) = <b>0.5033</b>   <i>(Using rounded Z = 0.01: N(0.01) = 0.5040)</i>

<b>Step 3: Theoretical Value of the Call Option (C_0):</b>
C_0 = S_0 * N(d_1) - X * e^(-rT) * N(d_2)
• S_0 * N(d_1) = 80 * 0.5629 = <b>Rs 45.032</b>
• X * e^(-rT) * N(d_2) = 80 * e^(-0.05 * 0.25) * 0.5033 = 80 * 0.987578 * 0.5033 = 79.006 * 0.5033 = <b>Rs 39.764</b>
• <b>C_0</b> = 45.032 - 39.764 = <b>Rs 5.27</b>  <i>(Using 2-decimal Z-table: 80(0.5636) - 79.006(0.5040) = 45.088 - 39.819 = <b>Rs 5.27</b>)</i>

<b>Step 4: Recommended Investment Strategy (When Actual Call Price = Rs 5.00):</b>
Since the actual market price of the call (<b>Rs 5.00</b>) is less than its theoretical fair value (<b>Rs 5.27</b>), the call option is <b>undervalued (underpriced) by Rs 0.27</b>. Therefore, the investor should <b>BUY the call option</b> (and, if hedging to lock in riskless arbitrage, short N(d_1) = 0.5629 shares of the stock per call bought).""")
    add_hint(story, "When S_0 = X (At-The-Money), ln(S_0/X) = ln(1) = 0! That simplifies d_1 to [(r + 0.5*sigma^2)*T] / (sigma*sqrt(T)). Compare Market Call (Rs 5.00) with Fair BSM Call (Rs 5.27): Market < Fair => Underpriced => BUY Call!")

    add_q(story, "Q16. An investor enters into a short futures position in 10 contracts in gold at a futures price of $276.50 per ounce. The size of one futures contract is 100 ounce. The initial margin per contract is $1,500, and the maintenance margin is $1,100. Suppose the futures settlement price on the first day is $278.00 per ounce, second day is $281.00 per ounce, third day is $276.00, fourth day is $280.00, and fifth day is $275.00.\na. Calculate daily gain or loss, cumulative gain or loss, margin account balance, and margin call.\nb. If investor does not deposit margin call, what will happen?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Position: <b>Short 10 Gold Futures Contracts</b>
• Contract size = 100 ounces per contract  =>  <b>Total Quantity = 10 x 100 = 1,000 ounces</b>
• Initial Futures Price (F_0) = $276.50 per ounce
• <b>Total Initial Margin (IM)</b> = 10 contracts x $1,500 = <b>$15,000</b>
• <b>Total Maintenance Margin (MM)</b> = 10 contracts x $1,100 = <b>$11,000</b>
• Since the investor holds a <b>SHORT position</b>:
  - When futures price <b>rises</b>, the investor suffers a <b>Loss</b>: Daily Gain/Loss = (Previous F - Current F) x 1,000 oz.
  - Whenever Ending Balance falls <b>below $11,000 (MM)</b>, a Margin Call (Variation Margin) is triggered to restore the balance to <b>$15,000 (IM)</b>.

<b>a. Daily Marking-to-Market Schedule (for 10 Short Contracts = 1,000 Ounces):</b>""")
    t16_gold = make_table([
        [P_hdr("Day"), P_hdr("Settlement Price ($/oz)"), P_hdr("Daily Price Change ($/oz)"), P_hdr("Daily Gain / Loss for Short ($)"), P_hdr("Cumulative Gain / Loss ($)"), P_hdr("Margin Balance Before Call ($)"), P_hdr("Margin Call (Variation Margin) ($)"), P_hdr("Ending Margin Balance ($)")],
        [P("Day 0 (Init)"), P("$276.50"), P("—"), P("—"), P("$0"), P("$15,000"), P("$0"), P("$15,000")],
        [P("Day 1"), P("$278.00"), P("+$1.50"), P("-$1,500"), P("-$1,500"), P("$13,500"), P("$0 (>=11,000)"), P("$13,500")],
        [P("Day 2", True), P("$281.00", True), P("+$3.00"), P("-$3,000", True), P("-$4,500"), P("$10,500 (<11,000)", True), P("+$4,500", True), P("$15,000", True)],
        [P("Day 3"), P("$276.00"), P("-$5.00"), P("+$5,000"), P("+$500"), P("$20,000"), P("$0"), P("$20,000")],
        [P("Day 4"), P("$280.00"), P("+$4.00"), P("-$4,000"), P("-$3,500"), P("$16,000"), P("$0"), P("$16,000")],
        [P("Day 5"), P("$275.00"), P("-$5.00"), P("+$5,000"), P("+$1,500"), P("$21,000"), P("$0"), P("$21,000")],
    ], col_widths=[48, 58, 58, 66, 66, 72, 68, 64])
    story.append(t16_gold)
    story.append(Spacer(1, 4))

    add_a(story, """<b>b. What Happens If the Investor Does Not Deposit the Margin Call Money on Day 2:</b>
If the investor fails to deposit the $4,500 variation margin call on Day 2, the broker/clearinghouse will <b>immediately close out (liquidate) the investor's short position</b> by buying 10 gold futures contracts in the market at the prevailing price, deduct the accumulated loss ($4,500) and brokerage fees from the margin account, and return the remaining $10,500 balance to the investor.""")
    add_hint(story, "Two critical rules for Q16: (1) Because it is a SHORT futures position, price UP = LOSS and price DOWN = GAIN! (2) On Day 2, balance drops to $10,500 (which is below Maintenance Margin $11,000), triggering a Margin Call of $15,000 - $10,500 = $4,500 to bring the account back up to Initial Margin ($15,000)!")

    add_q(story, "Q17. Consider a long forward contract to buy a non-dividend-paying stock with a maturity of three months. The current stock price is Rs 400, and the annual risk-free interest rate for three months is 5%.\na. Determine the forward price of the stock.\nb. If the forward price is Rs 430, calculate the arbitrage profit.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 400 (non-dividend-paying stock)
• Time to maturity (T) = 3 months = 3 / 12 = <b>0.25 year</b>
• Annual risk-free interest rate (r) = 5% = 0.05

<b>a. Theoretical Forward Price of the Stock (F_0):</b>
• <b>Method 1 (Continuous Compounding):</b>
  F_0 = S_0 * e^(r * T) = 400 * e^(0.05 * 0.25) = 400 * e^(0.0125) = 400 * 1.012578 = <b>Rs 405.03</b>
• <b>Method 2 (Simple Periodic Interest):</b>
  F_0 = S_0 * [ 1 + r * (3 / 12) ] = 400 * (1 + 0.0125) = <b>Rs 405.00</b>
• <b>Method 3 (Annual Discrete Compounding):</b>
  F_0 = S_0 * (1 + r)^T = 400 * (1.05)^0.25 = 400 * 1.012272 = <b>Rs 404.91</b>

<b>b. Arbitrage Profit If Market Forward Price (F_mkt) = Rs 430:</b>
• Since Market Forward Price (Rs 430) &gt; Theoretical Forward Price (Rs 405.03), the forward contract is <b>overpriced</b>.
• <b>Cash-and-Carry Arbitrage Strategy:</b>
  1. <b>At t = 0 (Today):</b> Borrow Rs 400 at the 5% risk-free rate for 3 months, buy 1 share of the stock at S_0 = Rs 400, and enter a <b>short forward contract</b> to sell the stock in 3 months at Rs 430.
  2. <b>At T = 3 Months:</b> Deliver the stock under the forward contract for <b>Rs 430.00</b> and repay the loan plus interest of <b>Rs 405.03</b> (or Rs 405.00 / Rs 404.91).
  3. <b>Riskless Arbitrage Profit at Maturity:</b>
     - Under Continuous Compounding: Rs 430.00 - Rs 405.03 = <b>Rs 24.97 per share</b>
     - Under Simple Interest: Rs 430.00 - Rs 405.00 = <b>Rs 25.00 per share</b>
     - Under Annual Compounding: Rs 430.00 - Rs 404.91 = <b>Rs 25.09 per share</b>""")
    add_hint(story, "Whenever Market Forward Price (Rs 430) > Fair Forward Price (Rs 405.03), use Cash-and-Carry Arbitrage: Borrow cash -> Buy Spot Asset -> Sell (Short) Forward Contract. Arbitrage Profit = F_mkt - F_0 = 430 - 405.03 = Rs 24.97!")

    # ==================== GROUP C ====================
    story.append(Paragraph("Group 'C': Long Answer Questions (Attempt any THREE — ALL Solved) [3 x 10 = 30]", group_header_style))

    add_q(story, "Q18. Discuss how options can be used to hedge equity risk, including the strategies involved and their advantages and limitations.")
    add_a(story, """<b>Answer:</b>
<b>1. Concept of Hedging Equity Risk with Options:</b>
Equity investors and portfolio managers face downside market risk (the risk that stock prices or the overall stock index will decline). Options provide asymmetric risk protection—functioning like an insurance policy that establishes a guaranteed floor value against market crashes while preserving upside participation when stock prices rise.

<b>2. Major Option Strategies Used to Hedge Equity Risk:</b>
• <b>Strategy 1: Protective Put (Portfolio Insurance: Long Stock + Long Put):</b>
  - <i>Mechanism:</i> An investor who holds a stock (or equity portfolio) purchases a put option with strike price X.
  - <i>Payoff at Expiration:</i> Value = max(S_T, X) - P_0. If the stock price crashes below X, the investor exercises the put and sells the stock at X (limiting maximum loss to S_0 - X + P_0). If the stock price surges above X, the put expires worthless and the investor enjoys unlimited upside gain minus the put premium P_0.
• <b>Strategy 2: Covered Call (Income & Partial Downside Cushion: Long Stock + Short Call):</b>
  - <i>Mechanism:</i> An investor holding a stock writes (sells) an out-of-the-money call option against the stock and collects the call premium C_0.
  - <i>Payoff:</i> The call premium C_0 provides a partial buffer against small declines in the stock price (reducing the effective cost basis to S_0 - C_0), in exchange for capping upside gains at the strike price X.
• <b>Strategy 3: Equity Collar (Zero-Cost Collar: Long Stock + Long OTM Put + Short OTM Call):</b>
  - <i>Mechanism:</i> The investor buys a protective put at a lower strike (X_1) and finances the put premium by simultaneously writing a covered call at a higher strike (X_2 &gt; X_1).
  - <i>Payoff:</i> Locks the portfolio value within a safe band between X_1 and X_2 at virtually zero net upfront option cost.
• <b>Strategy 4: Hedge for a Short Stock Position (Short Stock + Long Call):</b>
  - Buying a call option protects a short-seller against unlimited losses if the stock price rises sharply above X.

<b>3. Advantages of Using Options to Hedge Equity Risk:</b>
• <b>Asymmetric Protection (Downside Floor with Upside Potential):</b> Unlike futures/forwards (which lock in a fixed price and eliminate upside gains), a protective put insures against losses while retaining upside capital appreciation.
• <b>Flexibility of Strike Prices (Deductible Choice):</b> Investors can choose deep out-of-the-money puts (cheaper premium, higher deductible) or at-the-money puts (full protection, higher premium).
• <b>No Margin Calls on Long Puts:</b> Once the put premium is paid, the hedger faces no daily margin calls.

<b>4. Limitations of Hedging with Options:</b>
• <b>Upfront Premium Cost (Insurance Drag):</b> Buying protective puts requires paying an upfront premium that reduces portfolio return ("upside capture" drag) if the market remains calm or rises.
• <b>Time Decay (Theta) and Expiration Roll Risk:</b> Options have finite maturities and lose time value rapidly as expiration approaches, requiring costly periodic rollovers.
• <b>Capped Upside in Covered Calls and Collars:</b> Reducing hedge cost by writing calls sacrifices large bull-market gains above the call strike.""")

    add_q(story, "Q19. A currency swap with semiannual payments for two years between hypothetical U.S. firm and Global Swaps, Inc. was entered into on 1 Jan 2007. Both counterparties agreed to pay fixed rate. The notional principals were EUR 10,000,000 and $9.804 million which were equivalent with exchange rate of swap initiation date. Assuming 30-day month and 360-day year.\n[Init Term Structure: 180d: USD 5.5%, EUR 3.8%; 360d: USD 5.5%, EUR 4.2%; 540d: USD 6.2%, EUR 4.4%; 720d: USD 6.4%, EUR 4.5%]\na. Determine the fixed rates in dollars and euro.\nb. Assume it is 90 days into the life of swap. The exchange rate now is $0.9790/EUR and the term structures are as given below:\n[New Term Structure at 90d: 90d: USD 5.7%, EUR 3.9%; 270d: USD 6.1%, EUR 4.3%; 450d: USD 6.4%, EUR 4.5%; 630d: USD 6.6%, EUR 4.6%]\nDetermine the value of the swap.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• 2-year Semiannual Fixed-for-Fixed Currency Swap (4 payments at 180, 360, 540, and 720 days)
• Notional Principals: NP_EUR = EUR 10,000,000;  NP_USD = $9,804,000 (Initial spot rate S_0 = $0.9804/EUR)

<b>Part (a): Determination of Fixed Swap Rates in US Dollars and Euros at Initiation (t = 0):</b>
• <b>Step 1: Compute Discount Factors B_i = 1 / [1 + R_i * (Days_i / 360)] at Initiation:</b>
  - <b>US Dollar Discount Factors (B_USD):</b>
    B_1(180d) = 1 / [1 + 0.055 * (180/360)] = 1 / 1.0275 = <b>0.973236</b>
    B_2(360d) = 1 / [1 + 0.055 * (360/360)] = 1 / 1.0550 = <b>0.947867</b>
    B_3(540d) = 1 / [1 + 0.062 * (540/360)] = 1 / 1.0930 = <b>0.914913</b>
    B_4(720d) = 1 / [1 + 0.064 * (720/360)] = 1 / 1.1280 = <b>0.886525</b>
    Sum (Sum B_USD) = 0.973236 + 0.947867 + 0.914913 + 0.886525 = <b>3.722541</b>

  - <b>Euro Discount Factors (B_EUR):</b>
    B_1(180d) = 1 / [1 + 0.038 * (180/360)] = 1 / 1.0190 = <b>0.981354</b>
    B_2(360d) = 1 / [1 + 0.042 * (360/360)] = 1 / 1.0420 = <b>0.959693</b>
    B_3(540d) = 1 / [1 + 0.044 * (540/360)] = 1 / 1.0660 = <b>0.938086</b>
    B_4(720d) = 1 / [1 + 0.045 * (720/360)] = 1 / 1.0900 = <b>0.917431</b>
    Sum (Sum B_EUR) = 0.981354 + 0.959693 + 0.938086 + 0.917431 = <b>3.796564</b>

• <b>Step 2: Calculate Semiannual and Annualized Fixed Rates:</b>
  - <b>US Dollar Fixed Rate:</b>
    Semiannual Rate (c_USD) = (1 - B_4,USD) / Sum B_USD = (1 - 0.886525) / 3.722541 = 0.113475 / 3.722541 = <b>0.030483 (3.0483% per half-year)</b>
    <b>Annualized USD Fixed Rate (R_USD)</b> = 3.0483% x (360 / 180) = <b>6.0967% (or 6.10% p.a.)</b>
  - <b>Euro Fixed Rate:</b>
    Semiannual Rate (c_EUR) = (1 - B_4,EUR) / Sum B_EUR = (1 - 0.917431) / 3.796564 = 0.082569 / 3.796564 = <b>0.021748 (2.1748% per half-year)</b>
    <b>Annualized EUR Fixed Rate (R_EUR)</b> = 2.1748% x (360 / 180) = <b>4.3497% (or 4.35% p.a.)</b>

<b>Part (b): Valuation of the Currency Swap 90 Days Later (Remaining Days: 90, 270, 450, 630; Spot = $0.9790/EUR):</b>
• <b>Step 1: Compute New Discount Factors at Day 90:</b>
  - <b>New USD Discount Factors (B'_USD):</b>
    B'_1(90d)  = 1 / [1 + 0.057 * (90/360)]  = <b>0.985950</b>
    B'_2(270d) = 1 / [1 + 0.061 * (270/360)] = <b>0.956252</b>
    B'_3(450d) = 1 / [1 + 0.064 * (450/360)] = <b>0.925926</b>
    B'_4(630d) = 1 / [1 + 0.066 * (630/360)] = <b>0.896459</b>
    Sum (Sum B'_USD) = <b>3.764587</b>
  - <b>New EUR Discount Factors (B'_EUR):</b>
    B'_1(90d)  = 1 / [1 + 0.039 * (90/360)]  = <b>0.990344</b>
    B'_2(270d) = 1 / [1 + 0.043 * (270/360)] = <b>0.968758</b>
    B'_3(450d) = 1 / [1 + 0.045 * (450/360)] = <b>0.946746</b>
    B'_4(630d) = 1 / [1 + 0.046 * (630/360)] = <b>0.925497</b>
    Sum (Sum B'_EUR) = <b>3.831345</b>

• <b>Step 2: Present Value of USD Fixed-Rate Leg and EUR Fixed-Rate Leg at Day 90:</b>
  - <b>Value of USD Fixed Leg (per $1 Notional):</b>
    V_USD(per $1) = c_USD * Sum B'_USD + B'_4,USD = (0.030483 * 3.764587) + 0.896459 = 0.114756 + 0.896459 = <b>$1.011215</b>
    <b>Total Value of USD Leg (for $9,804,000 Notional)</b> = $9,804,000 x 1.011215 = <b>$9,913,952 (or $9,913,960)</b>
  - <b>Value of EUR Fixed Leg (per EUR 1 Notional):</b>
    V_EUR(per EUR 1) = c_EUR * Sum B'_EUR + B'_4,EUR = (0.021748 * 3.831345) + 0.925497 = 0.083324 + 0.925497 = <b>EUR 1.008821</b>
    <b>Total Value of EUR Leg in Euros (for EUR 10,000,000 Notional)</b> = EUR 10,000,000 x 1.008821 = <b>EUR 10,088,210 (or EUR 10,088,227)</b>
    <b>Total Value of EUR Leg Converted into USD (@ $0.9790/EUR)</b> = EUR 10,088,227 x 0.9790 = <b>$9,876,374</b>

• <b>Step 3: Net Value of the Currency Swap at Day 90:</b>
  - <b>For the Party Paying EUR Fixed and Receiving USD Fixed (U.S. Firm):</b>
    V_swap = V_USD - V_EUR(in USD) = $9,913,960 - $9,876,374 = <b>+$37,586 (or +EUR 38,392)</b>
  - <b>For the Party Paying USD Fixed and Receiving EUR Fixed (Global Swaps, Inc.):</b>
    V_swap = $9,876,374 - $9,913,960 = <b>-$37,586 (or -EUR 38,392)</b>""")
    add_hint(story, "In a Fixed-for-Fixed Currency Swap, value each currency leg just like a fixed-coupon bond: V = [ Semiannual Coupon Rate x Sum(New Discount Factors) + Last Discount Factor ] x Notional Principal. Then convert the foreign leg into domestic currency using the NEW spot exchange rate ($0.9790/EUR) and subtract!")

    add_q(story, "Q20. The current price of Himal Company stock is Rs 500 per share. Both call and put options are available on this stock with an exercise price of Rs 500. The call option premium is Rs 20 per share, and the put option premium is Rs 10 per share. Both options have a maturity of one month. An investor decides to buy one call and one put on Himal Company stock because the stock price has been hovering around Rs 500 for a long time, and the investor expects a significant price movement in either direction.\na. What is the name of the option position the investor is taking?\nb. What is the total cost of the investor's combined position?\nc. Calculate the profit or loss for the investor at expiration if the stock price ends at Rs 450, Rs 460, Rs 470, Rs 480, Rs 490, Rs 500, Rs 510, Rs 520, Rs 530, or Rs 540. Calculate maximum gain and loss of the strategy.")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 500; Exercise price (X) = Rs 500
• Call premium (C) = Rs 20; Put premium (P) = Rs 10; Maturity = 1 month

<b>a. Name of the Option Position:</b>
Buying 1 Call Option and 1 Put Option simultaneously on the same stock with the same exercise price (Rs 500) and same expiration date is called a <b>Long Straddle (or Bottom Straddle)</b>.

<b>b. Total Cost of the Investor's Combined Position:</b>
Total Cost = Call Premium (C) + Put Premium (P) = Rs 20 + Rs 10 = <b>Rs 30 per share (per straddle)</b>.

<b>c. Profit or Loss at Expiration for Each Stock Price, Maximum Gain, and Maximum Loss:</b>
• <b>Maximum Possible Loss:</b> <b>Rs 30 per share</b> (the combined premium paid), which occurs if the stock price at expiration equals the strike price (S_T = Rs 500).
• <b>Maximum Possible Gain:</b> <b>Unlimited on the upside</b> (as S_T -> Infinity, profit -> Infinity); on the downside (if S_T falls to Rs 0), maximum gain is Rs 500 - Rs 30 = <b>Rs 470 per share</b>.
• <b>Breakeven Points:</b> Lower BEP = 500 - 30 = <b>Rs 470</b>; Upper BEP = 500 + 30 = <b>Rs 530</b>.""")
    t20_straddle = make_table([
        [P_hdr("Ending Stock Price (S_T)"), P_hdr("Call Payoff max(S_T - 500, 0)"), P_hdr("Put Payoff max(500 - S_T, 0)"), P_hdr("Total Payoff (Rs)"), P_hdr("Combined Cost C + P (Rs)"), P_hdr("Net Profit / Loss (Payoff - 30)")],
        [P("Rs 450"), P("Rs 0"), P("Rs 50"), P("Rs 50"), P("Rs 30"), P("+Rs 20 (Profit)", True)],
        [P("Rs 460"), P("Rs 0"), P("Rs 40"), P("Rs 40"), P("Rs 30"), P("+Rs 10 (Profit)", True)],
        [P("Rs 470 (Lower BEP)", True), P("Rs 0"), P("Rs 30"), P("Rs 30"), P("Rs 30"), P("Rs 0 (Breakeven)", True)],
        [P("Rs 480"), P("Rs 0"), P("Rs 20"), P("Rs 20"), P("Rs 30"), P("-Rs 10 (Loss)")],
        [P("Rs 490"), P("Rs 0"), P("Rs 10"), P("Rs 10"), P("Rs 30"), P("-Rs 20 (Loss)")],
        [P("Rs 500 (Max Loss)", True), P("Rs 0"), P("Rs 0"), P("Rs 0"), P("Rs 30"), P("-Rs 30 (Max Loss)", True)],
        [P("Rs 510"), P("Rs 10"), P("Rs 0"), P("Rs 10"), P("Rs 30"), P("-Rs 20 (Loss)")],
        [P("Rs 520"), P("Rs 20"), P("Rs 0"), P("Rs 20"), P("Rs 30"), P("-Rs 10 (Loss)")],
        [P("Rs 530 (Upper BEP)", True), P("Rs 30"), P("Rs 0"), P("Rs 30"), P("Rs 30"), P("Rs 0 (Breakeven)", True)],
        [P("Rs 540"), P("Rs 40"), P("Rs 0"), P("Rs 40"), P("Rs 30"), P("+Rs 10 (Profit)", True)],
    ], col_widths=[90, 82, 82, 76, 80, 90])
    story.append(t20_straddle)
    story.append(Spacer(1, 4))
    add_hint(story, "Long Straddle = Buy 1 Call + Buy 1 Put at the SAME strike price (X = 500). Total cost = C + P = 30. Two Breakevens = X - 30 (470) and X + 30 (530). Max Loss = -30 at S_T = 500.")

    add_q(story, "Q21. The current market price of XYZ stock is Rs 490 per share. A call option on this stock has an exercise price of Rs 500 and expires in one year. The time to expiration is divided into two binomial periods. In each period, the stock price may either rise by 20% or fall by 20%. The risk-free interest rate is 10% per annum, or 5% per period.\na. Using a two-period binomial model, compute the current value of the American call option.\nb. If the market price of the call option is Rs 50, what investment strategy would you recommend?")
    add_a(story, """<b>Answer (Step-by-Step Numerical Solution):</b>
<b>Given:</b>
• Current stock price (S_0) = Rs 490; Exercise price (X) = Rs 500
• Number of binomial periods (n) = 2 periods (each period = 6 months)
• Up factor (u) = 1 + 0.20 = <b>1.20</b>; Down factor (d) = 1 - 0.20 = <b>0.80</b>
• Risk-free rate per period (r_p) = 5% = <b>0.05</b>

<b>Part (a): Current Value of the Two-Period American Call Option:</b>
• <b>Step 1: Risk-Neutral Probability (p):</b>
  p = (1 + r_p - d) / (u - d) = (1.05 - 0.80) / (1.20 - 0.80) = 0.25 / 0.40 = <b>0.625</b>
  1 - p = 1 - 0.625 = <b>0.375</b>

• <b>Step 2: Two-Period Binomial Stock Price Tree:</b>
  - <b>Period 0 (Today):</b> S_0 = <b>Rs 490.00</b>
  - <b>Period 1 (After 1st Period):</b>
    • S_u = 490 x 1.20 = <b>Rs 588.00</b>
    • S_d = 490 x 0.80 = <b>Rs 392.00</b>
  - <b>Period 2 (At Expiration):</b>
    • S_uu = 588 x 1.20 = <b>Rs 705.60</b>  =>  Call Payoff C_uu = max(705.60 - 500, 0) = <b>Rs 205.60</b>
    • S_ud = 588 x 0.80 = <b>Rs 470.40</b>  =>  Call Payoff C_ud = max(470.40 - 500, 0) = <b>Rs 0.00</b>
    • S_dd = 392 x 0.80 = <b>Rs 313.60</b>  =>  Call Payoff C_dd = max(313.60 - 500, 0) = <b>Rs 0.00</b>

• <b>Step 3: Backward Induction to Period 1 (Checking Early Exercise for American Call):</b>
  - <b>At Node U (S_u = Rs 588):</b>
    • Value if held (unexercised): C_u(hold) = [ p * C_uu + (1 - p) * C_ud ] / (1 + r_p)
      = [ (0.625 x 205.60) + (0.375 x 0) ] / 1.05 = 128.50 / 1.05 = <b>Rs 122.38</b>
    • Value if exercised early at Period 1: C_u(exercise) = S_u - X = 588 - 500 = <b>Rs 88.00</b>
    • Since Rs 122.38 &gt; Rs 88.00, it is NOT optimal to exercise early! Thus, <b>C_u = Rs 122.38</b>.
  - <b>At Node D (S_d = Rs 392):</b>
    • C_d(hold) = [ 0.625(0) + 0.375(0) ] / 1.05 = Rs 0;  C_d(exercise) = max(392 - 500, 0) = Rs 0  =>  <b>C_d = Rs 0.00</b>.

• <b>Step 4: Backward Induction to Period 0 (Today):</b>
  C_0 = [ p * C_u + (1 - p) * C_d ] / (1 + r_p)
  C_0 = [ (0.625 x 122.381) + (0.375 x 0) ] / 1.05 = 76.488 / 1.05 = <b>Rs 72.85</b>

<b>Part (b): Recommended Investment Strategy If Market Price of Call = Rs 50:</b>
Since the market price of the call option (<b>Rs 50.00</b>) is significantly lower than its fair theoretical value (<b>Rs 72.85</b>), the call option is <b>underpriced by Rs 22.85 per share</b>.
• <b>Recommendation:</b> The investor should <b>BUY the underpriced call option at Rs 50</b> (and to lock in riskless arbitrage, short-sell the delta hedge ratio h_0 = (C_u - C_d)/(S_u - S_d) = (122.38 - 0)/(588 - 392) = 122.38 / 196 = <b>0.6244 shares of XYZ stock</b> per call purchased).""")
    add_hint(story, "Key theorem to remember in Exam: An American Call Option on a NON-dividend-paying stock is NEVER optimally exercised early (here C_u(hold) = Rs 122.38 > Early Exercise 588 - 500 = Rs 88), so American Call Value = European Call Value = Rs 72.85!")

    # ==================== GROUP D ====================
    story.append(Paragraph("Group 'D': Comprehensive Answer / Case / Situation Analysis [20 Marks]", group_header_style))

    add_q(story, "Q22. Case Study: Naya Bank Limited (NBL) Stock & Options\nToday's closing price of NBL stock is S_0 = Rs 400. Call options on NBL with Exercise Price X_C = Rs 400 and 2 months to expiration sell for C = Rs 20. Put options on NBL with Exercise Price X_P = Rs 390 and 2 months to expiration sell for P = Rs 10.\na. Suggest your investment strategy with stock position only in the expectation of positive economic condition. Calculate the gain on your strategy if your expectation is true and price will increases to Rs 500 per share.\nb. Suggest your investment strategy with option only in the expectation of positive economic condition. Calculate the gain or loss if stock price after two months increased to Rs 500 per share? Calculate the breakeven point of the investment strategy.\nc. Suggest your hedging investment strategy of stock with put option. Calculate the profit (or loss) from your strategy at expiration. What stock price at expiration will make you breakeven? Possible stock prices at the expiration are Rs 350, Rs 360, Rs 370, Rs 380, Rs 390, Rs 400, Rs 410, Rs 420, Rs 430, Rs 440, and Rs 450.\nd. Suggest your option combination strategy if you think there will be big move in stock market but you don't know the direction of movement. Calculate the profit or loss from your strategy at expiration. Possible stock prices at the expiration are Rs 350, Rs 360, Rs 370, Rs 380, Rs 390, Rs 400, Rs 410, Rs 420, Rs 430, Rs 440, and Rs 450.")
    add_a(story, """<b>Answer (Comprehensive Case Study Solution):</b>
<b>Given Summary:</b>
• NBL Current Stock Price (S_0) = Rs 400
• 2-Month Call Option: Strike Price (X_C) = Rs 400; Call Premium (C) = Rs 20
• 2-Month Put Option: Strike Price (X_P) = Rs 390; Put Premium (P) = Rs 10

<b>Part (a): Stock-Only Strategy Under Positive Economic Expectation:</b>
• <b>Suggested Strategy:</b> Take a <b>Long Stock Position</b> (buy shares of NBL in the spot market at S_0 = Rs 400 per share) to benefit from capital appreciation.
• <b>Gain if Stock Price Increases to S_T = Rs 500 after 2 Months:</b>
  - <b>Gain per share</b> = S_T - S_0 = Rs 500 - Rs 400 = <b>+Rs 100 per share</b>
  - <b>Holding Period Return (2 months)</b> = (Rs 100 / Rs 400) x 100 = <b>25%</b> (or annualized = 25% x 12/2 = <b>150% p.a.</b>).

<b>Part (b): Option-Only Strategy Under Positive Economic Expectation:</b>
• <b>Suggested Strategy:</b> Take a <b>Long Call Option Position</b> (buy 2-month NBL Call Options with strike X_C = Rs 400 at a premium of C = Rs 20 per share).
  <i>(Note: For every Rs 400 equivalent to 1 share of stock, you can buy 400 / 20 = 20 call options!)</i>
• <b>Gain if Stock Price Increases to S_T = Rs 500 after 2 Months:</b>
  - Call Payoff at S_T = Rs 500: max(500 - 400, 0) = Rs 100 per call
  - <b>Net Gain per Call Option</b> = Payoff - Call Premium = Rs 100 - Rs 20 = <b>+Rs 80 per call option</b>
    <i>(On a Rs 400 investment buying 20 calls: Total Net Gain = 20 x Rs 80 = <b>+Rs 1,600</b>!)</i>
  - <b>2-Month Holding Period Return</b> = (Rs 80 / Rs 20) x 100 = <b>400%</b> (or annualized = 400% x 6 = <b>2,400% p.a.</b>).
• <b>Breakeven Point (BEP) of the Long Call Strategy:</b>
  BEP = X_C + C = Rs 400 + Rs 20 = <b>Rs 420 per share</b>.

<b>Part (c): Hedging Strategy of Stock with Put Option (Protective Put Strategy):</b>
• <b>Suggested Strategy:</b> <b>Protective Put (Portfolio Insurance)</b>—Buy 1 share of NBL stock at S_0 = Rs 400 and simultaneously buy 1 Put Option (X_P = Rs 390) at P = Rs 10.
• <b>Total Initial Outlay:</b> S_0 + P = Rs 400 + Rs 10 = <b>Rs 410 per share</b>.
• <b>Minimum Guaranteed Floor Value at Expiration:</b> X_P = Rs 390 (so maximum possible loss is capped at 390 - 410 = <b>-Rs 20 per share</b>).
• <b>Breakeven Stock Price at Expiration (BEP):</b>
  Profit = S_T + max(390 - S_T, 0) - 410 = 0  =>  <b>BEP = S_0 + P = Rs 400 + Rs 10 = Rs 410 per share</b>.

<b>Part (d): Option Combination Strategy for a Big Move in Either Direction (Long Strangle / Volatility Combination):</b>
• <b>Suggested Strategy:</b> Buy 1 Call Option (X_C = Rs 400, C = Rs 20) and Buy 1 Put Option (X_P = Rs 390, P = Rs 10).
  <i>(Note: Because the Call strike [Rs 400] and Put strike [Rs 390] differ by Rs 10, this combination is technically a <b>Long Strangle</b>—or a Long Straddle/Strangle volatility combination!)</i>
• <b>Total Combined Premium Cost:</b> C + P = Rs 20 + Rs 10 = <b>Rs 30 per unit</b>.
• <b>Maximum Loss:</b> <b>-Rs 30</b> (for any ending stock price between Rs 390 and Rs 400).
• <b>Two Breakeven Points:</b>
  - Lower Breakeven = X_P - (C + P) = Rs 390 - Rs 30 = <b>Rs 360 per share</b>
  - Upper Breakeven = X_C + (C + P) = Rs 400 + Rs 30 = <b>Rs 430 per share</b>

<b>Combined Payoff & Profit Schedule for Part (c) Protective Put and Part (d) Long Strangle/Combination (S_T = Rs 350 to Rs 450):</b>""")
    t22_nbl = make_table([
        [P_hdr("Ending Stock Price (S_T)"), P_hdr("Part (c): Put Payoff max(390-S_T,0)"), P_hdr("Part (c): Protective Put Value (S_T + Put)"), P_hdr("Part (c): Protective Put Net Profit/Loss (Value - 410)"), P_hdr("Part (d): Call Payoff max(S_T-400,0)"), P_hdr("Part (d): Combined Option Payoff (Call + Put)"), P_hdr("Part (d): Option Combo Net Profit/Loss (Payoff - 30)")],
        [P("Rs 350"), P("Rs 40"), P("Rs 390"), P("-Rs 20 (Max Loss)"), P("Rs 0"), P("Rs 40"), P("+Rs 10 (Profit)", True)],
        [P("Rs 360"), P("Rs 30"), P("Rs 390"), P("-Rs 20 (Max Loss)"), P("Rs 0"), P("Rs 30"), P("Rs 0 (Lower BEP)", True)],
        [P("Rs 370"), P("Rs 20"), P("Rs 390"), P("-Rs 20 (Max Loss)"), P("Rs 0"), P("Rs 20"), P("-Rs 10 (Loss)")],
        [P("Rs 380"), P("Rs 10"), P("Rs 390"), P("-Rs 20 (Max Loss)"), P("Rs 0"), P("Rs 10"), P("-Rs 20 (Loss)")],
        [P("Rs 390"), P("Rs 0"), P("Rs 390"), P("-Rs 20 (Max Loss)"), P("Rs 0"), P("Rs 0"), P("-Rs 30 (Max Loss)", True)],
        [P("Rs 400"), P("Rs 0"), P("Rs 400"), P("-Rs 10 (Loss)"), P("Rs 0"), P("Rs 0"), P("-Rs 30 (Max Loss)", True)],
        [P("Rs 410"), P("Rs 0"), P("Rs 410"), P("Rs 0 (BEP)", True), P("Rs 10"), P("Rs 10"), P("-Rs 20 (Loss)")],
        [P("Rs 420"), P("Rs 0"), P("Rs 420"), P("+Rs 10 (Profit)", True), P("Rs 20"), P("Rs 20"), P("-Rs 10 (Loss)")],
        [P("Rs 430"), P("Rs 0"), P("Rs 430"), P("+Rs 20 (Profit)", True), P("Rs 30"), P("Rs 30"), P("Rs 0 (Upper BEP)", True)],
        [P("Rs 440"), P("Rs 0"), P("Rs 440"), P("+Rs 30 (Profit)", True), P("Rs 40"), P("Rs 40"), P("+Rs 10 (Profit)", True)],
        [P("Rs 450"), P("Rs 0"), P("Rs 450"), P("+Rs 40 (Profit)", True), P("Rs 50"), P("Rs 50"), P("+Rs 20 (Profit)", True)],
    ], col_widths=[58, 68, 70, 82, 68, 72, 82])
    story.append(t22_nbl)
    story.append(Spacer(1, 4))
    add_hint(story, "Look closely at the strike prices in Q22: Call Strike X_C = Rs 400 (C = 20), whereas Put Strike X_P = Rs 390 (P = 10)! Because X_P = 390 != X_C = 400, (1) in Protective Put (Part c), max loss is S_0 - X_P + P = 400 - 390 + 10 = Rs 20 (for all S_T <= 390) and BEP = 400 + 10 = Rs 410; (2) in Part d (Long Strangle/Combination), Lower BEP = X_P - 30 = 390 - 30 = Rs 360 and Upper BEP = X_C + 30 = 400 + 30 = Rs 430!")

    story.append(PageBreak())
