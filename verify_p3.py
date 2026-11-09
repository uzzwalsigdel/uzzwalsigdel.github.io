# In Don M. Chance (An Introduction to Derivatives and Risk Management):
# How is a basis swap (or fixed-rate equivalent of SOFR vs T-bill) priced?
# Method A: Fixed-rate equivalent difference!
# Fixed rate on SOFR plain vanilla swap: R_sofr = (1 - B4_sofr) / sum(B_sofr) * (360/90)
# Fixed rate on T-bill plain vanilla swap: R_tbill = (1 - B4_tbill) / sum(B_tbill) * (360/90)
# Spread = R_sofr - R_tbill!
days_init = [90, 180, 270, 360]
sofr_init = [0.0750, 0.0795, 0.0852, 0.0900]
tbill_init = [0.0550, 0.0587, 0.0630, 0.0690]

B_sofr = [1 / (1 + r * (d / 360)) for r, d in zip(sofr_init, days_init)]
B_tbill = [1 / (1 + r * (d / 360)) for r, d in zip(tbill_init, days_init)]

R_sofr_q = (1 - B_sofr[-1]) / sum(B_sofr)
R_sofr_ann = R_sofr_q * (360 / 90)

R_tbill_q = (1 - B_tbill[-1]) / sum(B_tbill)
R_tbill_ann = R_tbill_q * (360 / 90)

spread_ann = R_sofr_ann - R_tbill_ann
spread_q = R_sofr_q - R_tbill_q
print(f"Method A (Chance Fixed-Rate Equivalent):")
print(f"  B_sofr = {[round(x, 4) for x in B_sofr]}, sum={sum(B_sofr):.4f}")
print(f"  B_tbill = {[round(x, 4) for x in B_tbill]}, sum={sum(B_tbill):.4f}")
print(f"  R_sofr (annualized) = {R_sofr_ann*100:.4f}% (quarterly {R_sofr_q*100:.4f}%)")
print(f"  R_tbill (annualized) = {R_tbill_ann*100:.4f}% (quarterly {R_tbill_q*100:.4f}%)")
print(f"  Spread (annualized) = {spread_ann*100:.4f}% (quarterly {spread_q*100:.4f}%)")

# What about Part b (60 days into the life of the swap)?
# Remaining days: 30, 120, 210, 300
days_60 = [30, 120, 210, 300]
sofr_60 = [0.0800, 0.0845, 0.0900, 0.0955]
tbill_60 = [0.0600, 0.0647, 0.0695, 0.0740]

B_sofr_60 = [1 / (1 + r * (d / 360)) for r, d in zip(sofr_60, days_60)]
B_tbill_60 = [1 / (1 + r * (d / 360)) for r, d in zip(tbill_60, days_60)]
print(f"At t=60:")
print(f"  B_sofr_60 = {[round(x, 4) for x in B_sofr_60]}, sum={sum(B_sofr_60):.4f}")
print(f"  B_tbill_60 = {[round(x, 4) for x in B_tbill_60]}, sum={sum(B_tbill_60):.4f}")

# First payment at day 90 (in 30 days) was set at day 0:
# T-bill payment at day 90 (per Rs 1 notional): 0.0550 * (90/360) = 0.01375
# SOFR payment at day 90 (before spread): 0.0750 * (90/360) = 0.01875
# Value of floating T-bill leg at t=60 (discounted at T-bill or SOFR):
val_tbill_leg_own = (1 + 0.0550 * (90/360)) * B_tbill_60[0]
val_sofr_leg_own = (1 + 0.0750 * (90/360)) * B_sofr_60[0]
# Value of spread payments (spread_q paid each quarter) discounted at SOFR:
pv_spread_sofr = spread_q * sum(B_sofr_60)
# Wait: what if T-bill leg is discounted using SOFR discount factors, or its own T-bill discount factors?
# If each floating leg is valued using its own discount factors:
# Value of SOFR - spread leg = val_sofr_leg_own - pv_spread_sofr
# Value of swap to CIT (pays T-bill, receives SOFR - spread):
val_cit_1 = 100_000_000 * ((val_sofr_leg_own - pv_spread_sofr) - val_tbill_leg_own)
print(f"  val_tbill_leg_own = {val_tbill_leg_own:.6f}")
print(f"  val_sofr_leg_own = {val_sofr_leg_own:.6f}")
print(f"  pv_spread_sofr = {pv_spread_sofr:.6f}")
print(f"  Value to CIT (Method 1) = Rs {val_cit_1:,.2f}")

# What if valued as difference between two fixed-rate legs or without subtracting spread from future reset?
# Wait: if Global Bank pays (SOFR - spread) and we only discount the known next net payment or if we value it via new fixed rates:
R_sofr_60_q = (1 - B_sofr_60[-1]) / sum(B_sofr_60)
R_tbill_60_q = (1 - B_tbill_60[-1]) / sum(B_tbill_60)
print(f"  New quarterly fixed rates at t=60: R_sofr={R_sofr_60_q*100:.4f}%, R_tbill={R_tbill_60_q*100:.4f}%")

# Now let's check Q22 (Krishna Pauroti Company):
# Stock price S0 = 240, X = 240, T = 3 months (0.25 yr), Call C = 40, Put P = 20, r = 6%, Investment = Rs 240,000
# a) Verdict favors company -> bullish -> buy Call options!
# Number of calls with Rs 240,000 = 240,000 / 40 = 6,000 calls.
# If S_T = 350 after 3 months:
# Profit per call = max(350 - 240, 0) - 40 = 110 - 40 = Rs 70.
# Total profit = 6,000 * 70 = Rs 420,000.
# 3-month HPR = 70 / 40 = 175%.
# Annualized return (simple) = 175% * (12/3) = 700% (or compound: (1 + 1.75)^4 - 1 = 5618.75%).
print("\nQ22 Part a: 6,000 calls, Profit = Rs 420,000, 3m return = 175%, simple annual = 700%")

# b) Verdict against company -> bearish -> buy Put options!
# Number of puts with Rs 240,000 = 240,000 / 20 = 12,000 puts.
# Wait! Look at the wording of part b:
# "How much will you earn/lose if the stock price after three months decreases to Rs 250?"
# Wait: S0 = 240, and it says "decreases to Rs 250" (or maybe typo in question for Rs 150, or literally Rs 250!).
# Let's calculate BOTH:
# Case 1 (Literally Rs 250): Since S_T = 250 > X = 240, the put option is out-of-the-money and expires worthless!
# Loss per put = Rs 20; Total loss = Rs 240,000 (100% loss in 3 months, or -400% simple annualized).
# Meanwhile, if invested in 1,000 shares of stock at Rs 240, at S_T = 250, stock gains Rs 10/share = Rs 10,000 (+4.17% in 3 months, +16.67% p.a.).
# Case 2 (If "decreases to Rs 250" was a printing typo for "decreases to Rs 150"):
# At S_T = 150, payoff per put = 240 - 150 = Rs 90, profit per put = 90 - 20 = Rs 70, Total profit = 12,000 * 70 = Rs 840,000 (+350% in 3m, +1400% p.a.), whereas stock loses Rs 90,000 (-37.5% in 3m, -150% p.a.).
# Showing BOTH Rs 250 (as printed) and Rs 150 (in case of printing typo) is super helpful for the exam!

# c) Long straddle: buy 1 call (C=40) + 1 put (P=20) at X=240 -> cost per straddle = 40 + 20 = Rs 60.
# With Rs 240,000, number of straddles = 240,000 / 60 = 4,000 straddles.
# Expiration stock prices: 160, 180, 200, 220, 240, 260, 280, 300, 320.
# Breakeven stock prices: X - (C+P) = 240 - 60 = Rs 180, and X + (C+P) = 240 + 60 = Rs 300.
# Max possible loss = Rs 60 per straddle (Rs 240,000 total) at S_T = 240.
# Max possible gain = Unlimited (on upside; on downside max gain is X - 60 = Rs 180 per straddle or Rs 720,000 if S_T = 0).

# d) Protective put (Portfolio insurance):
# Investment = Rs 240,000, S0 = 240, Put P = 20 (X = 240).
# Cost of 1 share + 1 put = 240 + 20 = Rs 260.
# Number of shares and puts = 240,000 / 260 = 923.0769 shares & puts (or 923 shares & puts, or for 1,000 shares cost is Rs 260,000; let's show both 923.08 units for Rs 240,000 budget AND per-share / 1,000-share basis!).
# Floor (ensured) value: 923.0769 * 240 = Rs 221,538.46 (or 923 * 240 = Rs 221,520; or Rs 240,000 on 1,000 shares).
# If S_T = 350:
# Value of insured portfolio = 923.0769 * 350 = Rs 323,076.92 (since put expires worthless).
# Uninsured stock portfolio (1,000 shares for Rs 240,000) at S_T = 350:
# Value of uninsured portfolio = 1,000 * 350 = Rs 350,000.
# Cost of insurance:
# Method 1 (Dollar/Percentage reduction in initial shares or premium): Rs 20 per share (or 20/260 = 7.69% of portfolio, or Rs 18,461.54 for 923.08 puts, or Rs 20,000 for 1,000 puts).
# Upside capture:
# Gain on insured portfolio = 323,076.92 - 240,000 = Rs 83,076.92 (Return = 34.62%)
# Gain on uninsured portfolio = 350,000 - 240,000 = Rs 110,000 (Return = 45.83%)
# Upside capture ratio = 323,076.92 / 350,000 = 92.31% (or in terms of gain/return: 83,076.92 / 110,000 = 75.52%)!
print("Q22 Part d verified!")
