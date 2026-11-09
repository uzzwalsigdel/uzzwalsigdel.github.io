# Paper 3 — BNK 202: Financial Derivatives

Tribhuvan University · Faculty of Management · BBA 8th Semester · Model Question 2026 · Full Marks 100 · Pass Marks 50 · Time 3 Hrs

## Group A — Brief-answer Questions (10 × 2 = 20)

### Q1. Why is a derivative instrument known as a zero-sum game?

**Solution:**

A derivative is called a zero-sum game because **whatever one party gains, the counterparty loses by exactly the same amount** (ignoring transaction costs).

- Every derivative contract has two sides — a long (buyer) and a short (seller/writer). It is a side-bet on the price of the underlying asset; no new wealth is created.
- Example: if a futures price rises by Rs 10, the long gains Rs 10 and the short loses Rs 10; the sum of gains and losses is zero.
- In options, the premium received by the writer equals the premium paid by the buyer, and the buyer's payoff at expiry is the writer's loss.
- After commissions and taxes it becomes slightly negative-sum for traders, but the derivative itself only transfers risk and wealth between parties.

### Q2. Why do investors pay more for an American option than similar European option?

**Solution:**

Investors pay more for an American option because it gives **everything a European option gives plus the right of early exercise** at any time up to expiry.

- A European option can be exercised only on the expiration date; an American option can be exercised on or before that date.
- Extra rights never reduce value, so American option price ≥ European option price (same S, X, T, σ, r).
- Early exercise can be valuable — e.g., a deep in-the-money American put (receive X now and earn interest on it) or an American call just before a large dividend.
- The difference (early-exercise premium) is the price of this flexibility; for a call on a non-dividend-paying stock it is zero, so both are equal.

### Q3. An investor who wants to achieve maximum gain and accept a higher maximum loss selects a call option with a lower exercise price. Justify.

**Solution:**

The statement is correct: a lower-strike call costs more (higher maximum loss) but pays more at every expiry price (higher gain).

- A call with a lower exercise price is more in-the-money, so its premium is higher. Since the maximum loss of a long call = premium paid, the **maximum loss is higher**.
- Profit at expiry = max(0, S_T − X) − C. For any S_T above the strikes, a lower X gives a larger payoff (S_T − X), and the extra payoff exceeds the extra premium when the price rises strongly.
- The lower-strike call also starts paying off at a lower stock price, so the chance of gain is higher.
- Hence an aggressive investor who wants the larger possible gain and can bear a larger premium loss selects the lower exercise price (e.g., X = 100, C = 12 vs X = 110, C = 6: at S_T = 140 profit is 28 vs 24; max loss is 12 vs 6).

### Q4. A longer-lived option has a higher price. Do you agree? Give reasons.

**Solution:**

Yes, generally a longer-lived option is worth more because it has **more time value**.

- More time means a greater chance that the stock price moves favourably (higher probability of ending deep in-the-money), while the loss is still limited to the premium.
- For **American options** (calls and puts) it is always true: a longer option has all the exercise opportunities of the shorter one plus more, so it can never be worth less.
- For **European calls** on non-dividend stocks it is also true, as longer time lowers the PV of the exercise price.
- Exception: a **European put** (deep in-the-money, where receiving X later lowers its PV) or a European call on a stock paying a large dividend before the longer expiry may be worth less.

### Q5. Define future contract.

**Solution:**

A futures contract is a **standardised, exchange-traded agreement between two parties to buy or sell a specified quantity of an asset at a price fixed today (the futures price) for delivery on a specified future date**.

- **Standardised**: quantity, quality, delivery date and place are fixed by the exchange.
- **Clearinghouse**: it becomes buyer to every seller and seller to every buyer, eliminating default risk.
- **Margin and marking-to-market**: initial and maintenance margins are required and gains/losses are settled daily.
- **Liquidity/offsetting**: most positions are closed by an opposite trade before delivery. Unlike a forward, it is not customised or private.

### Q6. What do you mean by upside capture in portfolio insurance?

**Solution:**

Upside capture is the **percentage of the uninsured portfolio's value (or gain) that the insured portfolio retains when the market rises**.

- Upside capture = Value of insured portfolio ÷ Value of uninsured portfolio (in a rising market) × 100.
- In portfolio insurance with protective puts, part of the funds is spent on put premiums, so fewer shares are held. When prices rise, the puts expire worthless and the insured portfolio is worth less than the uninsured one.
- Therefore upside capture is always less than 100%; the shortfall is the cost of insurance.
- Example: insured value Rs 92,300 vs uninsured Rs 100,000 → upside capture = 92.3%.

### Q7. Under what conditions is a long hedge using futures suitable?

**Solution:**

A long hedge (buying futures) is suitable when a firm **plans to buy an asset in the future and fears that its price will rise** (i.e., it is effectively short in the spot market).

- Example: a flour mill that must buy wheat in three months, an airline that must buy jet fuel, or an importer who must pay in dollars later.
- Buying futures today locks in the purchase price: if the spot price rises, the gain on futures offsets the higher cost of buying the asset.
- It is also used by someone who has short-sold an asset and must buy it back later (anticipatory hedge).
- Suitable when futures on the same or a highly correlated asset are available, so basis risk is small.

### Q8. Write the meaning of synthetic instruments.

**Solution:**

Synthetic instruments are **combinations of other securities/derivatives that replicate the payoff of a given instrument** exactly, so they should have the same price (law of one price).

- They are based mainly on put–call parity: S + P = C + X/(1 + r)^T.
- Synthetic call = long stock + long put − borrow PV(X); synthetic put = long call − long stock + lend PV(X).
- Synthetic stock = long call − long put + lend PV(X); synthetic forward/futures = long call + short put (same strike).
- Uses: to create a position when the actual one is unavailable or expensive, and to exploit arbitrage when actual and synthetic prices differ.

### Q9. Why do investors prefer bull spreads from call options over those from put options?

**Solution:**

Both spreads profit from a moderate price rise, but a call bull spread (buy low-strike call, sell high-strike call) is often preferred because:

- **Net debit, known risk**: the investor pays a net premium upfront; the maximum loss equals this premium and is known in advance. A put bull spread (buy low-strike put, sell high-strike put) produces a net credit but requires the writer to post **margin**.
- **Less early-assignment risk**: the short high-strike put in a put spread is in-the-money when prices fall and can be exercised early (American puts); the short out-of-the-money call in a call spread is rarely exercised early.
- **Simpler and intuitive**: buying calls to gain from a rise is easier to understand and has lower margin/cash-management problems.
- The put version is chosen only when it offers a better net premium.

### Q10. If you want to change the fixed-rate liability in to foliating-rate liability using a swap, how would you do it?

**Solution:**

Enter a plain-vanilla interest rate swap as the **fixed-rate receiver and floating-rate payer** (a pay-floating, receive-fixed swap).

- The firm continues to pay the fixed coupon on its existing loan/bond.
- Under the swap, it receives a fixed rate (which offsets the fixed coupon) and pays a floating rate (e.g., SOFR + spread).
- Net cost = Fixed paid on loan − Fixed received in swap + Floating paid ≈ Floating rate (± spread).
- Example: loan at 10% fixed; swap: receive 9.5% fixed, pay SOFR → net cost = SOFR + 0.5%, i.e., a floating-rate liability. Useful when rates are expected to fall.

## Group B — Short-answer Questions (Any six, 6 × 5 = 30)

### Q11. Describe the role of the derivative market.

**Solution:**

Derivative markets (options, forwards, futures and swaps) play an important role in modern financial systems. Their main roles are:

1. **Risk management (hedging):** The most important role. Derivatives allow firms and investors to transfer unwanted price risk to those willing to bear it. Exporters hedge currency risk with forwards, farmers hedge crop prices with futures, banks hedge interest rate risk with swaps, and investors insure portfolios with puts.

2. **Price discovery:** Futures and options prices reflect the market's collective expectations of future spot prices and volatility. Because trading is cheap and fast, new information is reflected first in derivative prices, which helps producers and consumers plan production and inventory.

3. **Operational advantages:** Derivatives have lower transaction costs than the spot market, higher liquidity, and make short selling easy (sell a futures or buy a put instead of borrowing shares). Large positions can be taken or reversed quickly.

4. **Market efficiency:** Arbitrage between spot and derivative markets (e.g., cash-and-carry, put–call parity) keeps prices of related assets in line, so mispricing is quickly eliminated and markets become more efficient.

5. **Speculation and leverage:** Speculators can take positions with a small initial outlay (margin or premium). They add liquidity and are the counterparties who absorb hedgers' risk.

6. **Completing the market:** Derivatives create payoff patterns (e.g., limited loss, insured portfolios, synthetic positions) that cannot be obtained easily with stocks and bonds alone, widening investors' choices.

**Criticism/caution:** Misuse (excessive speculation, poor understanding) can create large losses (e.g., Barings, 2008 crisis), so proper regulation and risk management are required. In Nepal, a formal derivative exchange is still developing, but forward contracts in foreign exchange and commodity markets are used.

### Q12. An investor purchased a June put option with an exercise price of Rs 600 by paying a premium of Rs 50 and is holding it until June. Under what circumstances will the option be exercised? Under what circumstances will the holder of the option make a profit? With the help of a diagram, explain how the profit from a long position in the option depends on the stock price at the maturity of the option.

**Solution:**

**Given:** Long put; exercise price X = Rs 600; premium P = Rs 50; held till expiry (June).

**Formula:**

- Payoff of long put at expiry = max(0, X − S_T)
- Profit = max(0, X − S_T) − P
- Breakeven S_T = X − P

**Step-by-step calculation:**

1. **When exercised:** The put gives the right to sell at Rs 600. It is exercised only if S_T < 600 (in-the-money). If S_T ≥ 600 it expires worthless.
2. **When profitable:** Profit > 0 when X − S_T > P, i.e., 600 − S_T > 50 → **S_T < 550**.
   - Breakeven = 600 − 50 = **Rs 550**.
   - Between Rs 550 and Rs 600 the put is exercised (to recover part of the premium) but there is still a net loss.
3. **Maximum profit** = X − P = 600 − 50 = **Rs 550** (if S_T = 0).
4. **Maximum loss** = premium = **Rs 50** (if S_T ≥ 600).

**Profit table:**

| S_T (Rs) | Exercise? | Payoff = max(0, 600 − S_T) | Premium | Profit (Rs) |
|---|---|---|---|---|
| 450 | Yes | 150 | 50 | +100 |
| 500 | Yes | 100 | 50 | +50 |
| 550 | Yes | 50 | 50 | 0 (breakeven) |
| 600 | Indifferent | 0 | 50 | −50 |
| 650 | No | 0 | 50 | −50 |
| 700 | No | 0 | 50 | −50 |

**Diagram (profit of long put vs stock price at maturity):** The profit line starts at +550 on the vertical axis (S_T = 0), slopes downward at 45° (each Rs 1 rise in S_T reduces profit by Rs 1), crosses the horizontal axis at the breakeven price Rs 550, reaches −50 at the exercise price Rs 600 and then stays flat at −50 for all higher prices.

```
Profit (Rs)
 +550 |\
      | \
 +100 |   \
      |    \
    0 |-----\-------------------------> S_T
      |   550\  600
  -50 |        \__________________________
      |
       (max loss = 50 for S_T >= 600)
```

**Answer / Interpretation:** The put is exercised when S_T < Rs 600 and gives a profit when S_T < Rs 550. Profit rises by Rs 1 for each Rs 1 fall in the stock price below 600, with maximum profit Rs 550 and maximum loss Rs 50. A long put is a bearish strategy with limited loss and large (but limited) gain.

> 💡 **Exam Hint (remember):** Long put profit = max(0, X − S_T) − P; Breakeven = X − P; Max profit = X − P; Max loss = P. **Trap:** "exercised" (S_T < X) and "profit" (S_T < X − P) are different conditions — between 550 and 600 you exercise but still lose. **Shortcut:** for a put, everything is "X minus": BE = X − P, max gain = X − P.

### Q13. An equity swap between the Employee Provident Fund (EPF) and Nabil Dealer is entered into. EPF pays floating interest payments based on SOFR, and Nabil pays a return on the NEPSE index. The payments are made quarterly, assuming a 30-day month and a 360-day year. The NEPSE index at the time of swap initiation was 2745.63, and the 90-day SOFR was 8 percent. Now, assume it is 50 days into the life of the swap. The NEPSE is now 2825.02, and the 40-day SOFR rate is 7.8 percent. Find the value of the swap today. Assume a notional principal of Rs 50,000,000.

**Solution:**

**Given:** NP = Rs 50,000,000; S_0 = 2745.63; S_t = 2825.02; initial 90-day SOFR L_0 = 8%; now day 50, so next payment in 40 days; 40-day SOFR = 7.8%. EPF pays floating (SOFR), receives NEPSE return. Nabil pays NEPSE return, receives SOFR.

**Formula:**

- Value of equity leg (per Re 1 notional) = S_t / S_0
- Value of floating leg (per Re 1) = (1 + L_0 × 90/360) × B_t(next payment)
- Discount factor B(40) = 1 / (1 + 0.078 × 40/360)
- Value to equity receiver (EPF) = NP × [S_t/S_0 − (1 + L_0 × 90/360) × B(40)]

Logic: Adding a notional to both legs does not change the value. The equity leg with notional is like holding NP rupees of the index, now worth NP × S_t/S_0. The floating leg resets to par (Re 1) right after the next payment, so today it is worth the PV of the already-known next payment plus notional.

**Step-by-step calculation:**

1. Index ratio: S_t / S_0 = 2825.02 / 2745.63 = **1.028915**
2. Discount factor: B(40) = 1 / (1 + 0.078 × 40/360) = 1 / (1 + 0.008667) = 1 / 1.008667 = **0.991408**
3. Next floating payment + notional (per Re 1) = 1 + 0.08 × 90/360 = 1 + 0.02 = 1.02
4. Floating leg value (per Re 1) = 1.02 × 0.991408 = **1.011236**
5. Equity leg value = 50,000,000 × 1.028915 = **Rs 51,445,752**
6. Floating leg value = 50,000,000 × 1.011236 = **Rs 50,561,798**
7. Value to EPF (receive equity, pay floating) = 51,445,752 − 50,561,798 = **+Rs 883,954**
8. Value to Nabil (receive floating, pay equity) = **−Rs 883,954**

| Leg | Per Re 1 | Value (Rs) |
|---|---|---|
| NEPSE (equity) leg | 1.028915 | 51,445,752 |
| SOFR (floating) leg | 1.011236 | 50,561,798 |
| Net to EPF | 0.017679 | +883,954 |

**Answer / Interpretation:** The swap is worth **Rs 883,954 to EPF** (an asset) and **−Rs 883,954 to Nabil Dealer** (a liability). The NEPSE has risen 2.89% in 50 days, more than the PV of the floating payment, so the equity receiver gains.

> 💡 **Exam Hint (remember):** V(equity receiver) = NP × [S_t/S_0 − (1 + L_0 × m/360) × B(days to next payment)]. **Trap:** use the OLD rate L_0 (8%, already fixed) for the next payment and the NEW rate (7.8%, 40 days) only for discounting; don't use 90 days for discounting. **Shortcut:** floating leg = "next payment + 1, discounted once" because it resets to par.

### Q14. People's Power Company (PCC), a Nepalese hydro-power company, purchased equipment from Baltimore Heavy Industry, a U. S. firm, for $5 million payable in one year. The current spot rate is Rs 140 per dollar, and the one-year forward rate is 130 yen per dollar. The annual interest rate is 5% in Nepal, and 8% in the U.S. PCC can also buy a one-year call option on the dollar at the strike price of Rs 125 per dollar for a premium of Rs 14 per dollar.
a. Assuming that the forward exchange rate is the best predictor of the future spot rate, compute the expected future rupee cost of meeting this obligation when the option hedge is used.
b. At what future spot rate do you think PCC may be indifferent between the option and forward hedge?

**Solution:**

(The "130 yen per dollar" in the question is a typo for **Rs 130 per dollar**.)

**Given:** Payable = $5,000,000 in 1 year; spot S_0 = Rs 140/$; forward F = Rs 130/$; i(Nepal) = 5%; i(US) = 8%; call on $: X = Rs 125/$, premium c = Rs 14/$ (paid today).

**Formula:**

- Expected future spot E(S_T) = F (forward is unbiased predictor)
- Option hedge cost per $ at T = min(S_T, X) + c × (1 + i_Nepal)
- Forward hedge cost per $ = F
- Indifference: S_T + c(1 + i_Nepal) = F (for S_T ≤ X)

**Step-by-step calculation:**

(a) Expected cost with option hedge

1. E(S_T) = Rs 130/$ > X = Rs 125 → the call will be exercised; PCC buys dollars at Rs 125.
2. Premium paid today, carried to year-end at the Nepalese rate: 14 × 1.05 = **Rs 14.70/$**
3. Expected cost per $ = 125 + 14.70 = **Rs 139.70/$**
4. Total expected rupee cost = 5,000,000 × 139.70 = **Rs 698,500,000**

Comparison:

| Strategy | Cost per $ (Rs) | Total cost (Rs) |
|---|---|---|
| Option hedge (expected) | 139.70 | 698,500,000 |
| Forward hedge (certain) | 130.00 | 650,000,000 |
| Unhedged (expected, S_T = 130) | 130.00 | 650,000,000 |

(b) Indifference rate

- If S_T ≥ 125: option is exercised, cost = 125 + 14.70 = 139.70 > 130 → forward is always cheaper.
- If S_T < 125: option lapses, PCC buys at spot; cost = S_T + 14.70.
- Set equal to forward: S_T + 14.70 = 130 → **S_T = Rs 115.30/$**

| Future spot S_T | Option hedge cost/$ | Forward cost/$ | Better |
|---|---|---|---|
| 110 | 110 + 14.70 = 124.70 | 130 | Option |
| 115.30 | 130.00 | 130 | Indifferent |
| 120 | 134.70 | 130 | Forward |
| 125 and above | 139.70 (capped) | 130 | Forward |

**Answer / Interpretation:** (a) Expected rupee cost with the option hedge = **Rs 139.70/$ = Rs 698.5 million**. (b) PCC is indifferent at a future spot rate of **Rs 115.30/$**; if the dollar falls below Rs 115.30, the option hedge is cheaper; above it, the forward hedge is cheaper. If the forward is an unbiased predictor, the forward hedge (Rs 650 million, with no uncertainty) is the best choice.

> 💡 **Exam Hint (remember):** Option hedge cost (payable) = min(S_T, X) + premium × (1 + home rate). Indifference: S_T* = F − premium × (1 + r_home). **Trap:** don't forget to compound the premium (it is paid today, the obligation is paid in a year), and use the HOME (Nepal) rate because the premium is in rupees. **Shortcut:** Indifference = 130 − 14.70 = 115.30.

### Q15. HDL stock is currently selling at Rs 900. A put option on HDL has an exercise price of Rs 1000 and matures in one year. The annually compounded interest rate is 8 percent. The quoted price of the put option is Rs 60. Identify the appropriate arbitrage opportunity and show the arbitrage profit for the stock price of Rs 800 and Rs 1200 after one year.

**Solution:**

**Given:** S_0 = Rs 900; X = Rs 1,000; T = 1 year; r = 8% (annual compounding); quoted put price P = Rs 60.

**Formula:**

- Lower bound of an American put: P ≥ max(0, X − S_0)
- Lower bound of a European put: P ≥ max(0, X/(1 + r)^T − S_0)

**Step-by-step calculation:**

1. Intrinsic value = X − S_0 = 1,000 − 900 = **Rs 100**
2. Lower bound (American put) = max(0, 100) = Rs 100
3. Quoted price Rs 60 < Rs 100 → **the put is underpriced** → arbitrage: **buy the put and buy the stock**.
4. Outlay today = 60 + 900 = **Rs 960**
5. Immediate exercise: deliver the stock at X = Rs 1,000 → riskless profit today = 1,000 − 960 = **Rs 40**.

If the position is instead held to expiry (protective put):

| Action today | Cash flow today | S_T = 800 | S_T = 1,200 |
|---|---|---|---|
| Buy put | −60 | Exercise: +(1,000 − 800) = +200 | Expires: 0 |
| Buy stock | −900 | Stock worth +800 | Sell stock +1,200 |
| **Total** | **−960** | **+1,000** | **+1,200** |
| **Arbitrage profit (vs outlay 960)** | | **1,000 − 960 = Rs 40** | **1,200 − 960 = Rs 240** |

At S_T = 800 the investor exercises the put and receives Rs 1,000 → profit Rs 40. At S_T = 1,200 the put lapses and the stock is sold for Rs 1,200 → profit Rs 240. A minimum of Rs 40 is guaranteed in all cases, with extra upside.

**Note (European bound and financing):** European lower bound = 1,000/1.08 − 900 = 925.93 − 900 = **Rs 25.93**; the price 60 does not violate it. If the Rs 960 were borrowed at 8% (repay 960 × 1.08 = 1,036.80), the hold-to-maturity strategy would lose 1,000 − 1,036.80 = −36.80 in the Rs 800 case. Hence the pure riskless arbitrage relies on **immediate exercise of the American put** (profit Rs 40 now); without borrowing, the Rs 40 minimum profit is locked in either way.

**Answer / Interpretation:** The put is underpriced (60 < intrinsic value 100). Buy the put and the stock for Rs 960. Arbitrage profit = **Rs 40 at S_T = 800** and **Rs 240 at S_T = 1,200** (or Rs 40 immediately by early exercise).

> 💡 **Exam Hint (remember):** American put ≥ X − S; European put ≥ X/(1 + r)^T − S. If P < bound → BUY put + BUY stock (cheap insurance). **Trap:** check WHICH bound applies — the American bound (100) is violated, the European bound (25.93) is not. **Shortcut:** riskless profit = bound − price = 100 − 60 = 40.

### Q16. The stock of Birat Company is currently selling for Rs 650. A 6-month call option on the stock has an exercise price of Rs 660. The standard deviation of returns on Birat stock has been estimated to be 50 percent. Currently, the 6-month T-bill rate is 10 percent. Using the BSM model, calculate the price of the call option on Birat.

**Solution:**

**Given:** S = Rs 650; X = Rs 660; σ = 0.50; r = 10% (continuously compounded); T = 6/12 = 0.5 year.

**Formula:**

- C = S × N(d1) − X × e^(−rT) × N(d2)
- d1 = [ln(S/X) + (r + σ²/2)T] / (σ√T)
- d2 = d1 − σ√T

**Step-by-step calculation:**

1. ln(S/X) = ln(650/660) = ln(0.984848) = **−0.015267**
2. σ²/2 = 0.25/2 = 0.125; (r + σ²/2)T = (0.10 + 0.125) × 0.5 = **0.1125**
3. σ√T = 0.5 × √0.5 = 0.5 × 0.707107 = **0.353553**
4. d1 = (−0.015267 + 0.1125) / 0.353553 = 0.097233 / 0.353553 = **0.2750**
5. d2 = 0.2750 − 0.3536 = **−0.0785**
6. N(d1) = N(0.2750) = **0.6083**
   - From the normal table: N(0.27) = 0.6064, N(0.28) = 0.6103 → N(0.275) = 0.6064 + 0.5 × (0.6103 − 0.6064) = 0.6083
7. N(d2) = N(−0.0785) = 1 − N(0.0785) = 1 − 0.5313 = **0.4687**
   - N(0.07) = 0.5279, N(0.08) = 0.5319 → N(0.0785) = 0.5279 + 0.85 × 0.0040 = 0.5313
8. e^(−rT) = e^(−0.10 × 0.5) = e^(−0.05) = **0.951229**
9. S × N(d1) = 650 × 0.6083 = **395.43**
10. X × e^(−rT) × N(d2) = 660 × 0.951229 × 0.4687 = 627.81 × 0.4687 = **294.26**
11. C = 395.43 − 294.26 = **Rs 101.17**

**Answer / Interpretation:** The BSM value of the Birat call is **≈ Rs 101.17 (≈ Rs 101)**. The option is slightly out-of-the-money (650 < 660), so its entire value is time value, which is high because volatility (50%) is high.

> 💡 **Exam Hint (remember):** C = S·N(d1) − X·e^(−rT)·N(d2); d1 = [ln(S/X) + (r + σ²/2)T]/(σ√T); d2 = d1 − σ√T. **Trap:** T in years (6 months = 0.5), σ² not σ in d1, and N(−d) = 1 − N(d). **Shortcut:** compute σ√T once (0.3536) and reuse it for both d1 and d2.

### Q17. An investor enters into two long futures contracts on orange. Each contract has a contract size of 10,000 pounds. The current futures price is Rs 100 per pound. The initial margin is Rs 3,00,000 per contract, and the maintenance margin is Rs 1,50,000.
a. What price change would lead to a margin call?
b. What happens if the margin call money is not deposited?
c. Under what circumstances could Rs 1,00,000 be withdrawn from the margin account?

**Solution:**

**Given:** Long 2 contracts × 10,000 lb = 20,000 lb; F_0 = Rs 100/lb; initial margin = 3,00,000 × 2 = Rs 6,00,000; maintenance margin = 1,50,000 × 2 = Rs 3,00,000.

**Formula:**

- Gain/loss on margin account = (F_t − F_0) × total quantity
- Margin call when balance < maintenance margin → loss > Initial − Maintenance
- Withdrawable amount = Balance − Initial margin

**Step-by-step calculation:**

(a) Margin call

1. Loss that triggers a call = 6,00,000 − 3,00,000 = **Rs 3,00,000**
2. Price fall = 3,00,000 / 20,000 = **Rs 15 per lb**
3. Futures price at which call occurs = 100 − 15 = **Rs 85 per lb** — a margin call is received if the price falls by more than Rs 15 (below Rs 85). The investor must then deposit variation margin to bring the balance back to the initial margin (Rs 6,00,000).

| Futures price (Rs/lb) | Gain/Loss (Rs) | Balance (Rs) | Status |
|---|---|---|---|
| 100 | 0 | 6,00,000 | Initial |
| 90 | −2,00,000 | 4,00,000 | No call |
| 85 | −3,00,000 | 3,00,000 | At maintenance level (call if below) |
| 80 | −4,00,000 | 2,00,000 | Margin call: deposit 4,00,000 |

(b) If the margin call is not met: the broker/clearinghouse **closes out (liquidates) the position** by taking an offsetting short position in the futures. The loss is realised and charged to the margin account; any remaining balance is returned to the investor (any deficit must be paid by the investor).

(c) Withdrawal of Rs 1,00,000

1. Any balance above the initial margin can be withdrawn. Need balance = 6,00,000 + 1,00,000 = 7,00,000 → gain = Rs 1,00,000
2. Price rise = 1,00,000 / 20,000 = **Rs 5 per lb**
3. Futures price = 100 + 5 = **Rs 105 per lb** — Rs 1,00,000 can be withdrawn when the futures price rises to Rs 105 or more.

**Answer / Interpretation:** (a) A fall of Rs 15/lb (price below Rs 85) triggers a margin call. (b) The position is closed out. (c) Rs 1,00,000 can be withdrawn if the futures price rises to Rs 105 (gain of Rs 5/lb).

> 💡 **Exam Hint (remember):** Price change for margin call = (Initial − Maintenance) ÷ total units; withdrawal price change = Amount ÷ total units. **Trap:** multiply margins and units by the NUMBER of contracts (2), and after a call you top up to the INITIAL margin, not the maintenance margin. **Shortcut:** per contract: 1,50,000/10,000 = Rs 15 — the number of contracts cancels out.

## Group C — Long-answer Questions (Any three, 3 × 10 = 30)

### Q18. NRIC stock is currently trading at Rs 1200 per share. At-the-money options on MRIC with 180 days to expiration are actively traded in the option exchange. You want to use the binomial model to value this option and expect that either the stock price increases by 25 percent or it decreases by 20 percent at the end of six months. You can borrow money at 8 percent per annum. Assume a 360-day year.
a. Calculate the fair price of the call option today.
b. Calculate the arbitrage return in percentage if the actual price of this call option in the market is Rs 140.

**Solution:**

**Given:** S = Rs 1,200; X = Rs 1,200 (at-the-money); u = 1.25; d = 0.80; r = 8% p.a. → per period (180 days) r = 0.08 × 180/360 = 4% → (1 + r) = 1.04; market call price = Rs 140.

**Formula:**

- Su = S × u; Sd = S × d; Cu = max(0, Su − X); Cd = max(0, Sd − X)
- Risk-neutral probability p = [(1 + r) − d] / (u − d)
- C = [p × Cu + (1 − p) × Cd] / (1 + r)
- Hedge ratio h = (Cu − Cd) / (Su − Sd)

**Step-by-step calculation:**

(a) Fair price

1. Su = 1,200 × 1.25 = **Rs 1,500**; Sd = 1,200 × 0.80 = **Rs 960**
2. Cu = max(0, 1,500 − 1,200) = **Rs 300**; Cd = max(0, 960 − 1,200) = **0**
3. p = (1.04 − 0.80) / (1.25 − 0.80) = 0.24 / 0.45 = **0.5333**; 1 − p = 0.4667
4. C = (0.5333 × 300 + 0.4667 × 0) / 1.04 = 160 / 1.04 = **Rs 153.85**
5. Hedge ratio h = (300 − 0) / (1,500 − 960) = 300 / 540 = **0.5556 shares per call**

Check (replication): Hedge portfolio = buy 0.5556 shares, write 1 call. Value at T: up = 0.5556 × 1,500 − 300 = 533.33; down = 0.5556 × 960 − 0 = 533.33 (riskless). PV = 533.33/1.04 = 512.82. So 0.5556 × 1,200 − C = 512.82 → C = 666.67 − 512.82 = 153.85 ✓

(b) Arbitrage with market price Rs 140

Market price 140 < fair value 153.85 → **call is underpriced → buy the call and short h = 0.5556 shares**, lend the proceeds at 4%.

Per call:

| Action | Today | Up (S_T = 1,500) | Down (S_T = 960) |
|---|---|---|---|
| Short 0.5556 shares | +666.67 | −833.33 | −533.33 |
| Buy 1 call | −140.00 | +300.00 | 0 |
| Lend net proceeds at 4% | −526.67 | +547.73 | +547.73 |
| **Net** | **0** | **+14.40** | **+14.40** |

1. Net inflow today = 666.67 − 140 = **526.67**
2. Invested at 4%: 526.67 × 1.04 = **547.73**
3. Net outflow at expiry (either state) = **533.33** (up: 833.33 − 300; down: 533.33 − 0)
4. Riskless profit = 547.73 − 533.33 = **Rs 14.40 per call**
5. Arbitrage return = 14.40 / 526.67 = **2.73% per six months ≈ 5.47% per annum** (over and above the risk-free return).

Alternative view: shorting the hedge portfolio means effectively borrowing 526.67 today and repaying 533.33 later, i.e., borrowing at 533.33/526.67 − 1 = **1.27% per half year (2.53% p.a.)** versus the market rate of 4% (8% p.a.) — a saving of 2.73% per period.

Scaled example (1,000 calls, 556 shares):

| Action | Today (Rs) | Up (Rs) | Down (Rs) |
|---|---|---|---|
| Short 556 shares | +667,200 | −834,000 | −533,760 |
| Buy 1,000 calls | −140,000 | +300,000 | 0 |
| Lend 527,200 at 4% | −527,200 | +548,288 | +548,288 |
| **Net** | **0** | **+14,288** | **+14,528** |

**Answer / Interpretation:** (a) Fair call price = **Rs 153.85** (hedge ratio 0.5556). (b) At Rs 140 the call is underpriced; buying calls and shorting 0.5556 shares per call earns a riskless **Rs 14.40 per call = 2.73% per six months (≈ 5.47% p.a.) excess return**. Arbitrage buying will push the call price up toward Rs 153.85.

> 💡 **Exam Hint (remember):** p = (1 + r − d)/(u − d); C = [pCu + (1 − p)Cd]/(1 + r); h = (Cu − Cd)/(Su − Sd). **Trap:** r must be for the period (8% × 180/360 = 4%), NOT 8%; and if C(market) < C(fair) you BUY the call and SHORT h shares (reverse if overpriced). **Shortcut:** arbitrage profit per call at T = (C_fair − C_market) × (1 + r) = 13.85 × 1.04 = 14.40.

### Q19. A one-year swap with quarterly payment and notional principal of Rs 100 million is entered between Citizen Investment Trust (CIT) and Global Bank. Payments will be based on a 30-day month and a 360-day year. The CIT agreed to make interest payments based on the 90-day T-bill rate, and Global Bank agreed to make interest payments based on the 90-day SOFR minus a spread.
a. Find the spread that should be deducted from the SOFR rate on each payment date.
The term structures of interest rates are given below.

| Term | SOFR rate | T-bill rate |
|---|---|---|
| 90 days | 7.50% | 5.50% |
| 180 days | 7.95% | 5.87% |
| 270 days | 8.52% | 6.30% |
| 360 days | 9.00% | 6.90% |

b. Assume it is 60 days into the life of the swap. The new term structures of interest rates are as follows. Find the value of the swap for both counterparties.

| Term | SOFR rate | T-bill rate |
|---|---|---|
| 30 days | 8.00% | 6.00% |
| 120 days | 8.45% | 6.47% |
| 210 days | 9.00% | 6.95% |
| 300 days | 9.55% | 7.40% |

**Solution:**

**Given:** NP = Rs 100 million; quarterly payments (90 days); 30/360. CIT pays T-bill, receives SOFR − spread; Global Bank pays SOFR − spread, receives T-bill.

**Formula:**

- Discount factor B(t) = 1 / (1 + r × t/360)
- Fixed rate of a plain-vanilla swap (per quarter) = [1 − B(360)] / ΣB; annual = × 360/90
- Basis swap spread = Fixed rate (SOFR swap) − Fixed rate (T-bill swap)
- Value of floating leg (with notional) = (1 + L_0 × 90/360) × B(days to next payment)
- Value of spread leg = NP × spread × 90/360 × ΣB (remaining)

Logic: A basis swap = (pay T-bill, receive fixed) + (pay fixed, receive SOFR). For zero initial value, the spread must equal the difference between the fixed rates of the two plain-vanilla swaps.

**Step-by-step calculation:**

(a) Spread

SOFR discount factors:

| Days | Rate | Calculation | B |
|---|---|---|---|
| 90 | 7.50% | 1/(1 + 0.075 × 90/360) = 1/1.01875 | 0.98160 |
| 180 | 7.95% | 1/(1 + 0.0795 × 180/360) = 1/1.03975 | 0.96177 |
| 270 | 8.52% | 1/(1 + 0.0852 × 270/360) = 1/1.06390 | 0.93994 |
| 360 | 9.00% | 1/(1 + 0.09 × 360/360) = 1/1.09000 | 0.91743 |
| | | **Σ** | **3.80073** |

Fixed rate (SOFR swap) = (1 − 0.91743)/3.80073 = 0.021724 per quarter → × 4 = **8.69% p.a.**

T-bill discount factors:

| Days | Rate | Calculation | B |
|---|---|---|---|
| 90 | 5.50% | 1/(1 + 0.055 × 90/360) = 1/1.01375 | 0.98644 |
| 180 | 5.87% | 1/(1 + 0.0587 × 180/360) = 1/1.02935 | 0.97149 |
| 270 | 6.30% | 1/(1 + 0.063 × 270/360) = 1/1.04725 | 0.95488 |
| 360 | 6.90% | 1/(1 + 0.069 × 360/360) = 1/1.06900 | 0.93545 |
| | | **Σ** | **3.84826** |

Fixed rate (T-bill swap) = (1 − 0.93545)/3.84826 = 0.016773 per quarter → × 4 = **6.71% p.a.**

Spread = 8.69% − 6.71% = **1.98% p.a. (≈ 198 basis points)**, deducted from SOFR on each payment date. So Global Bank pays (SOFR − 1.98%) and CIT pays T-bill.

(b) Value 60 days into the swap (next payment in 30 days, then 120, 210, 300 days)

New discount factors:

| Days | SOFR B | T-bill B |
|---|---|---|
| 30 | 1/(1 + 0.08 × 30/360) = 0.99338 | 1/(1 + 0.06 × 30/360) = 0.99502 |
| 120 | 1/(1 + 0.0845 × 120/360) = 0.97260 | 1/(1 + 0.0647 × 120/360) = 0.97889 |
| 210 | 1/(1 + 0.09 × 210/360) = 0.95012 | 1/(1 + 0.0695 × 210/360) = 0.96104 |
| 300 | 1/(1 + 0.0955 × 300/360) = 0.92628 | 1/(1 + 0.074 × 300/360) = 0.94192 |
| Σ | 3.84238 | — |

1. **SOFR floating leg** (next payment fixed at initial 90-day SOFR 7.5%): 100,000,000 × (1 + 0.075 × 90/360) × 0.99338 = 100,000,000 × 1.01875 × 0.99338 = **Rs 101,200,331**
2. **Spread leg** (fixed payment each quarter): 100,000,000 × 0.0198063 × 90/360 = **Rs 495,158** per quarter; PV = 495,158 × 3.84238 = **Rs 1,902,587**
3. Net value of SOFR − spread leg = 101,200,331 − 1,902,587 = **Rs 99,297,744**
4. **T-bill leg** (next payment fixed at initial 90-day T-bill 5.5%): 100,000,000 × (1 + 0.055 × 90/360) × 0.99502 = 100,000,000 × 1.01375 × 0.99502 = **Rs 100,870,647**
5. Value to CIT (receives SOFR − spread, pays T-bill) = 99,297,744 − 100,870,647 = **−Rs 1,572,903**
6. Value to Global Bank (receives T-bill, pays SOFR − spread) = **+Rs 1,572,903**

**Answer / Interpretation:** (a) Spread = **1.98% (≈ 198 bp)** deducted from SOFR. (b) After 60 days, the swap is worth **−Rs 1,572,903 to CIT** and **+Rs 1,572,903 to Global Bank**. Both floating legs reset to par at each payment date, so each is valued as the PV of the next known payment plus notional; the spread payments are a fixed annuity discounted at the SOFR factors.

> 💡 **Exam Hint (remember):** Swap fixed rate = (1 − B_last)/ΣB × (360/90); Basis spread = Fixed(SOFR) − Fixed(T-bill); Floating leg value = (1 + L_0 × 90/360) × B(next). **Trap:** the next payment uses the OLD (initial) 90-day rates (7.5% and 5.5%), not the new 30-day rates; days to discount are 30, 120, 210, 300 (not 90, 180…). **Shortcut:** compute both columns of discount factors in one table and reuse ΣB.

### Q20. A stock is expected to pay a dividend of Rs 10 per share in two months and five months from today. The stock price is Rs 500, and the risk-free interest rate is 8% p.a. with continuous compounding for all maturities. An investor has just taken a short position in a six-month forward contract on the stock.
a. What are the forward price and the initial value of the forward contract?
b. Show the arbitrage process if the market price of the forward is Rs 515.
b. Three months later, the stock price is Rs 480, and the risk-free rate of interest is still 8% p.a. What are the forward price and the value of the short position in the forward contract?

**Solution:**

**Given:** S_0 = Rs 500; D = Rs 10 at t = 2/12 and 5/12; r = 8% (continuous); T = 6/12 = 0.5; market forward = Rs 515; after 3 months S = Rs 480.

**Formula:**

- PV of dividends I = Σ D × e^(−r t)
- F_0 = (S_0 − I) × e^(rT)
- Value of short forward at time t = (K − F_t) × e^(−r(T − t)) = K e^(−r(T−t)) − (S_t − I_t)

**Step-by-step calculation:**

(a) Forward price and initial value

1. I = 10e^(−0.08 × 2/12) + 10e^(−0.08 × 5/12) = 10e^(−0.013333) + 10e^(−0.033333) = 9.8676 + 9.6722 = **19.5397**
2. S_0 − I = 500 − 19.5397 = 480.4603
3. e^(0.08 × 0.5) = e^(0.04) = 1.040811
4. F_0 = 480.4603 × 1.040811 = **Rs 500.07**
5. Initial value of the forward = **0** (delivery price is set equal to the forward price, so no money changes hands).

(b) Arbitrage at market forward Rs 515

Market forward 515 > fair 500.07 → forward is overpriced → **cash-and-carry arbitrage: sell the forward, borrow, buy the stock**.

| Time | Action | Cash flow (Rs) |
|---|---|---|
| Today | Short forward at 515 | 0 |
| Today | Borrow 500 for 6 months at 8% cc | +500.00 |
| Today | Buy 1 share | −500.00 |
| 2 months | Receive dividend 10, invest for 4 months: 10e^(0.08 × 4/12) | → 10.2702 at T |
| 5 months | Receive dividend 10, invest for 1 month: 10e^(0.08 × 1/12) | → 10.0669 at T |
| 6 months | Deliver share under forward | +515.00 |
| 6 months | Receive invested dividends | +20.34 |
| 6 months | Repay loan 500e^(0.04) | −520.41 |
| | **Arbitrage profit at T** | **+14.93** |

Profit = 515 + 20.34 − 520.41 = **Rs 14.93** (= 515 − 500.07). Selling forwards and buying stock will push the forward price down toward Rs 500.07.

(c) After 3 months (T − t = 3 months = 0.25 year)

1. Only one dividend remains (at month 5, i.e., 2 months from now): I = 10e^(−0.08 × 2/12) = **9.8676**
2. S − I = 480 − 9.8676 = 470.1324
3. e^(0.08 × 0.25) = e^(0.02) = 1.020201
4. New forward price F_t = 470.1324 × 1.020201 = **Rs 479.63**
5. Value of short forward = (K − F_t) × e^(−0.08 × 0.25) = (500.07 − 479.63) × 0.980199 = 20.44 × 0.980199 = **Rs 20.03**
   - Check: K e^(−r(T−t)) − (S − I) = 500.07 × 0.980199 − 470.13 = 490.17 − 470.13 = 20.03 ✓

**Answer / Interpretation:** (a) F_0 = **Rs 500.07**; initial value = 0. (b) Forward at 515 is overpriced; cash-and-carry gives a riskless profit of **Rs 14.93** per share. (c) After 3 months, forward price = **Rs 479.63**; value of the short position = **+Rs 20.03** (the short gains because the stock price fell).

> 💡 **Exam Hint (remember):** F_0 = (S_0 − PV of dividends) × e^(rT); value of short = (K − F_t)e^(−r(T−t)); value of long = (F_t − K)e^(−r(T−t)). **Trap:** after 3 months, the 2-month dividend has ALREADY been paid — include only the remaining one, discounted for 2 months (not 5). **Shortcut:** arbitrage profit = market forward − fair forward (515 − 500.07 = 14.93).

### Q21. Explain the margin rule and the margin operation process by a clearinghouse in option trading.

**Solution:**

**Meaning of margin in options**

Margin is a performance bond (good-faith deposit) that a trader must keep with the broker/clearinghouse to ensure that contractual obligations will be met. In options, the right belongs to the buyer and the obligation to the writer, so margin rules differ for buyers and writers.

**Margin rules**

1. **Option buyers:** The buyer has a right but no obligation. Therefore, the buyer pays the **full premium** upfront (no buying on margin for short-term options; long-term options may be partly margined). The maximum loss is the premium, so no further margin is needed.

2. **Covered call writers:** A writer who owns the underlying stock (covered call) needs **no additional margin**; the shares are deposited/held with the broker and can be delivered if exercised.

3. **Uncovered (naked) call writers:** Because the potential loss is unlimited, the writer must deposit:
   - Margin = 100% of the premium received + 20% of the underlying stock value − amount by which the option is out-of-the-money,
   - subject to a minimum of premium + 10% of the stock value.
   - Example: S = 100, X = 105, premium = 4 for 100 shares: 400 + 0.20 × 10,000 − 500 = 1,900; minimum = 400 + 1,000 = 1,400 → margin = Rs 1,900.

4. **Uncovered put writers:** Margin = premium + 20% of stock value − out-of-the-money amount, minimum premium + 10% of the exercise price. A cash-secured put (cash equal to the strike deposited) needs no additional margin.

5. **Spreads and combinations:** For spreads, the margin is based on the maximum possible loss (difference between strikes minus net premium), since the long leg protects the short leg.

6. Margins are **recomputed daily** as prices change; if the margin is insufficient, a margin call is issued.

**Margin operation process by the clearinghouse**

1. **Novation / guarantee:** The clearinghouse (e.g., OCC in the USA) becomes the buyer to every seller and the seller to every buyer. It guarantees the performance of every contract, eliminating counterparty default risk.
2. **Clearing members:** Only clearing members deal directly with the clearinghouse. Brokers who are not members clear through members. Customers post margin with brokers, brokers with clearing members, and clearing members with the clearinghouse.
3. **Daily collection and marking-to-market:** The clearinghouse values all short positions daily and collects additional margin from clearing members whose positions have lost value; members in turn collect from customers.
4. **Margin calls and liquidation:** If a member or customer fails to meet a call, the position is closed out and the margin used to cover losses.
5. **Exercise and assignment:** When a buyer exercises, the clearinghouse assigns the exercise **randomly** to a clearing member with a short position, who then assigns it to one of its customer writers (random or FIFO).
6. **Clearing/guarantee fund and default waterfall:** If a member defaults, losses are met first from the defaulter's margin, then its clearing fund contribution, then the clearinghouse's own capital and the contributions of other members.

**Nepalese context:** NEPSE does not yet have an organised options exchange; SEBON has issued commodity/derivative regulations and the market is at an early stage, so these margin practices are drawn from international exchanges.

**Conclusion:** Margin rules protect the system from writers' default, while the clearinghouse's daily margining, guarantee and assignment process makes option markets safe and liquid.

## Group D — Comprehensive / Case Analysis (20)

### Q22. Krishna Pauroti Company is an exchange-listed company that produces and sells different brands of bread throughout Nepal. The company's products gained popularity in a short period. The company's earnings and stock price are growing rapidly. Since its stock is actively traded on the stock exchange, it is also listed on the options exchange. Call and put options on Krishna stock, which is also actively trading. The company has announced that it is planning to expand its capacity by 100 percent within six months to meet the increased demand. Yesterday, a case against the Company was filed in court, stating that a popular brand of the Company's bread is unhealthy and the company is knowingly ignoring public health. The court had issued a stay order to the company to stop the production and sale of that particular brand of bread until the court gave a final verdict. Today's trade volume of Krishna stock has become very low. The stock closed at Rs 240 per share today. Call and put options on Krishna with an exercise price of Rs 240 and three months to expiration closed at Rs 40 and Rs 20, respectively. Stock traders in the market are waiting for the court verdict. Special courts handle such cases, and usually, the verdict comes within three months. The risk-free rate of interest is currently 6 percent per annum. You are considering investing Rs 240,000 in Krishna stock, an option on Krishna stock, or a combination of both.
a. If you believe the court verdict will favor the company and want to speculate on the option, which option do you buy? Why? How much will you earn/lose if the stock price after three months increases to Rs 350? What will be your annual rate of return?
b. If you believe that the court verdict will come against the company and want to speculate on the option, which option do you buy? Why? How much will you earn/lose if the stock price after three months decreases to Rs 250? What will be your annual rate of return? Compare the risk and return of your investment with that of your stock investment.
c. Assume you cannot guess whether the court verdict may come in favor of or against the company. Is a long straddle beneficial in such conditions? Why? Calculate gain/loss from long straddle for expiration stock prices of Rs 160, Rs 180, … Rs 320. After three months, calculate the maximum possible gain, maximum possible loss, and breakeven stock price(s) for your strategy.
d. Considering the uncertainty of the verdict, you want to ensure your portfolio of stocks using put options. How many stocks and put options do you need to hold? What will be the ensured value of your portfolio? What will be the value of the ensured portfolio if the verdict came in favor of the company, and the stock price increased to Rs 350? Also, calculate the cost of insurance and the upside capture. [4+4+6+6]

**Solution:**

**Given:** S_0 = Rs 240; call (X = 240) C = Rs 40; put (X = 240) P = Rs 20; T = 3 months; r_f = 6% p.a.; investment = Rs 240,000.

**Formula:**

- Call profit = max(0, S_T − X) − C; Put profit = max(0, X − S_T) − P
- Straddle profit = |S_T − X| − (C + P); breakevens = X ± (C + P)
- Return = Profit / Investment; annual (simple) = 3-month return × 12/3
- Protective put: units = Investment / (S + P); floor = units × X; upside capture = insured value / uninsured value

**Step-by-step calculation:**

**(a) Favourable verdict → buy CALL options**

Why: a favourable verdict will push the price up. A call gives leveraged, unlimited upside with loss limited to the premium; a put would lose.

1. Number of calls = 240,000 / 40 = **6,000 calls**
2. Payoff at S_T = 350: (350 − 240) × 6,000 = 110 × 6,000 = **Rs 660,000**
3. Profit = 660,000 − 240,000 = **Rs 420,000**
4. 3-month return = 420,000 / 240,000 = **175%**
5. Annual rate of return = 175% × 12/3 = **700%** (simple); compounded = (1 + 1.75)^4 − 1 = (2.75)^4 − 1 ≈ 5,620%

Comparison: buying 1,000 shares (240,000/240) → profit = (350 − 240) × 1,000 = Rs 110,000 = 45.83% (183.3% annualised).

**(b) Unfavourable verdict → buy PUT options**

Why: an adverse verdict will push the price down. A put gains as the price falls, with loss limited to the premium (safer than short selling, which has unlimited loss and is not easy in Nepal).

1. Number of puts = 240,000 / 20 = **12,000 puts**

The question says the price "decreases to Rs 250", but Rs 250 is above Rs 240. Both readings are shown.

(i) As stated, S_T = Rs 250:

- Put payoff = max(0, 240 − 250) = 0 → puts expire worthless
- Loss = **−Rs 240,000** → return = −100% (−400% annualised, simple)
- Stock investment (1,000 shares): gain = (250 − 240) × 1,000 = +Rs 10,000 → +4.17% (16.67% annualised)

(ii) If the intended price is Rs 150:

- Put payoff = (240 − 150) × 12,000 = **Rs 1,080,000**
- Profit = 1,080,000 − 240,000 = **Rs 840,000** → return = 350% (**1,400% annualised**)
- Stock investment: loss = (150 − 240) × 1,000 = −Rs 90,000 → −37.5% (−150% annualised)

| Case | Puts (12,000) | Return | Stock (1,000 shares) | Return |
|---|---|---|---|---|
| S_T = 250 | −240,000 | −100% (−400% p.a.) | +10,000 | +4.17% (16.67% p.a.) |
| S_T = 150 | +840,000 | +350% (1,400% p.a.) | −90,000 | −37.5% (−150% p.a.) |

Risk–return comparison: options give much higher (leveraged) returns when the forecast is correct, but the whole investment (100%) can be lost if the price does not move as expected. The stock investment gives smaller returns, but losses are only partial — lower risk, lower return.

**(c) Long straddle (buy 1 call + 1 put, X = 240)**

Why: the verdict will cause a large price move but the direction is unknown. A long straddle profits from a big move in either direction; loss is limited to the total premium. So it is beneficial here.

1. Cost per straddle = 40 + 20 = Rs 60; number = 240,000 / 60 = **4,000 straddles**
2. Profit per straddle = |S_T − 240| − 60

| S_T (Rs) | Call payoff | Put payoff | Total payoff | Profit per straddle | Total profit (× 4,000) (Rs) |
|---|---|---|---|---|---|
| 160 | 0 | 80 | 80 | 20 | 80,000 |
| 180 | 0 | 60 | 60 | 0 | 0 |
| 200 | 0 | 40 | 40 | −20 | −80,000 |
| 220 | 0 | 20 | 20 | −40 | −160,000 |
| 240 | 0 | 0 | 0 | −60 | −240,000 |
| 260 | 20 | 0 | 20 | −40 | −160,000 |
| 280 | 40 | 0 | 40 | −20 | −80,000 |
| 300 | 60 | 0 | 60 | 0 | 0 |
| 320 | 80 | 0 | 80 | 20 | 80,000 |

3. Maximum loss = total premium = 60 × 4,000 = **Rs 240,000** (at S_T = 240)
4. Maximum gain = **unlimited** on the upside; on the downside maximum = (240 − 60) × 4,000 = **Rs 720,000** (if S_T = 0)
5. Breakeven prices = 240 − 60 = **Rs 180** and 240 + 60 = **Rs 300**

```
Total profit (Rs '000)
  +80 |\                                   /
      | \                                 /
    0 |--\-------------------------------/------> S_T
      |  180\                         /300
  -80 |      \                       /
 -160 |        \                   /
 -240 |          \_______V_______/
                        240
        (V-shape: max loss 240,000 at S_T = 240)
```

**(d) Portfolio insurance with protective puts**

1. One put per share; cost per unit = 240 + 20 = Rs 260
2. Units = 240,000 / 260 = 923.08 → **923 shares and 923 puts**; cost = 923 × 260 = Rs 239,980 (Rs 20 left as cash)
3. Ensured (floor) value = 923 × 240 = **Rs 221,520** (+ Rs 20 cash) — the minimum value whatever the verdict
4. If S_T = 350: puts expire worthless; value = 923 × 350 = **Rs 323,050**
5. Cost of insurance = 923 × 20 = **Rs 18,460** (= 20/240 = 8.33% of the stock value)
6. Uninsured portfolio (1,000 shares) at 350 = 1,000 × 350 = Rs 350,000
7. Upside capture = 323,050 / 350,000 = **92.3%**

Upside capture is the proportion of the uninsured portfolio's value that the insured portfolio retains in a rising market; it is below 100% because part of the money was spent on put premiums (fewer shares are held).

**Answer / Interpretation:**

- (a) Buy 6,000 calls; profit **Rs 420,000** (175% in 3 months; **700% p.a.**).
- (b) Buy 12,000 puts; at Rs 250 the puts expire worthless → loss **Rs 240,000** (−100%, −400% p.a.) vs stock gain Rs 10,000; if the price falls to Rs 150, profit Rs 840,000 (350%, 1,400% p.a.) vs stock loss Rs 90,000.
- (c) A long straddle suits the uncertain verdict: 4,000 straddles; max loss **Rs 240,000**, max gain unlimited (Rs 720,000 on the downside); breakevens **Rs 180 and Rs 300**.
- (d) Hold **923 shares + 923 puts**; floor **Rs 221,520**; value at 350 = **Rs 323,050**; insurance cost **Rs 18,460**; upside capture **92.3%**.

> 💡 **Exam Hint (remember):** Number of options = Investment ÷ premium; straddle BE = X ± (C + P); protective put units = Investment ÷ (S + P); floor = units × X; upside capture = insured ÷ uninsured value. **Trap:** annualise a 3-month return by × 4 (simple), and in (d) divide by (S + P), not by S. **Shortcut:** straddle profit changes Rs 20 × 4,000 = Rs 80,000 for every Rs 20 step in S_T — fill the table by adding/subtracting 80,000.
