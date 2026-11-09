import math
from scipy.stats import norm

print("================ PAPER 1: BNK 221 ================")
# Q9: 3/10 net 50, paid on day 60, 360 days/yr
apc_q9 = (0.03 / 0.97) * (360 / (60 - 10))
ear_q9 = (1 + 0.03 / 0.97) ** (360 / 50) - 1
print(f"Q9: APC = {apc_q9*100:.4f}%, EAR = {ear_q9*100:.4f}%")

# Q10: 500,000 shares, 9 directors, 1 director
shares_q10 = int((500000 * 1) / (9 + 1)) + 1
print(f"Q10: Min shares = {shares_q10}")

# Q16: Mega Company warrants: N=2, E=150
# a) P0=140, W=10
tv_a_raw = (140 - 150) * 2
tv_a = max(tv_a_raw, 0)
prem_a_floor = 10 - tv_a
prem_a_raw = 10 - tv_a_raw
# b) P0=160, W=40
tv_b = (160 - 150) * 2
prem_b = 40 - tv_b
print(f"Q16a: TV_raw={tv_a_raw}, TV_floor={tv_a}, Prem_floor={prem_a_floor}, Prem_raw={prem_a_raw}")
print(f"Q16b: TV={tv_b}, Prem={prem_b}")

# Q17: AFC expansion Rs 200,000
# Bank: 12% discount interest
ear_bank_q17 = 0.12 / (1 - 0.12)
# Trade credit: 3/10 net 40, delayed 20 days -> day 60
apc_tc_360 = (0.03 / 0.97) * (360 / (60 - 10))
ear_tc_360 = (1 + 0.03 / 0.97) ** (360 / 50) - 1
apc_tc_365 = (0.03 / 0.97) * (365 / (60 - 10))
ear_tc_365 = (1 + 0.03 / 0.97) ** (365 / 50) - 1
print(f"Q17: Bank EAR={ear_bank_q17*100:.4f}%, TC_360 APC={apc_tc_360*100:.4f}% EAR={ear_tc_360*100:.4f}%, TC_365 APC={apc_tc_365*100:.4f}% EAR={ear_tc_365*100:.4f}%")

# Q19: Nepal Energy Company
# Funds = 600M, P0 = 600, Old shares = 4.8M, Par = 100, Ps = 500
new_shares = 600_000_000 / 500
rights_per_share = 4_800_000 / new_shares
vr = (600 - 500) / (rights_per_share + 1)
pe = 600 - vr
print(f"Q19: new_shares={new_shares:,.0f}, N={rights_per_share}, Vr={vr}, Pe={pe}")

# Q20: KEC borrow 800,000
alt1 = 0.15 / (1 - 0.15)
alt2 = 0.14 / (1 - 0.15)
alt3_unused = (800000 * 0.12 + (1000000 - 800000) * 0.01) / 800000
alt3_total = (800000 * 0.12 + 1000000 * 0.01) / 800000
print(f"Q20: Alt1={alt1*100:.4f}%, Alt2={alt2*100:.4f}%, Alt3(unused)={alt3_unused*100:.4f}%, Alt3(total)={alt3_total*100:.4f}%")

# Q21: Himalaya Company Lease vs Buy
# Lease = 150,000/yr for 3 yrs, Buy = 300,000, Salvage = 60,000, kd = 10%, T = 40%, kdt = 6%
kdt = 0.10 * (1 - 0.40)
pvifa_6_3 = (1 - (1 + kdt) ** -3) / kdt
pvif_6_3 = (1 + kdt) ** -3
after_tax_lease = 150000 * (1 - 0.40)
pv_leasing = after_tax_lease * pvifa_6_3
dep = (300000 - 60000) / 3
dep_tax_shield = dep * 0.40
pv_purchasing = 300000 - dep_tax_shield * pvifa_6_3 - 60000 * pvif_6_3
print(f"Q21: PVIFA={pvifa_6_3:.4f}, PVIF={pvif_6_3:.4f}, PV_Lease={pv_leasing:,.2f}, PV_Buy={pv_purchasing:,.2f}, NAL={pv_purchasing - pv_leasing:,.2f}")

# Q22: Himalayan Herbal Company (HHC)
# Existing: Common stock (par 5) = 5,000,000 -> 1,000,000 shares
# APIC = 10,000,000, RE = 15,000,000, Total = 30,000,000
# Raise Rs 10,000,000:
# Alt a: 20-yr 8% convertible debenture, conversion price Rs 50, face value Rs 1,000
# Number of debentures = 10,000,000 / 1,000 = 10,000; conversion ratio = 1000/50 = 20 shares/bond -> 200,000 new shares
# Alt b: 20-yr 10% straight bond with detachable warrant: each Rs 1,000 bond has 4 warrants at Rs 50/share
# Number of bonds = 10,000 -> total warrants = 40,000 warrants -> 40,000 * 4? Wait: "a detachable warrant to purchase four shares for Rs 50 a share" -> 10,000 bonds * 4 shares = 40,000 shares at Rs 50 = Rs 2,000,000 additional cash!
# Wait: Let's check EBIT = 20% of total capitalization!
print("Q22 HHC:")
# Current: Cap = 30M, EBIT = 20% of 30M = 6,000,000, Int = 0, EBT = 6M, Tax (50%) = 3M, NI = 3M, Shares = 1M, EPS = 3.00
# Convertible Before conversion: Cap = 40M, EBIT = 20% of 40M = 8,000,000, Int = 8% of 10M = 800,000, EBT = 7,200,000, NI = 3,600,000, Shares = 1M, EPS = 3.60
# Convertible After conversion: Cap = 40M, EBIT = 8,000,000, Int = 0, EBT = 8,000,000, NI = 4,000,000, Shares = 1,200,000, EPS = 4,000,000 / 1,200,000 = 3.3333
# Warrant Before exercise: Cap = 40M, EBIT = 8,000,000, Int = 10% of 10M = 1,000,000, EBT = 7,000,000, NI = 3,500,000, Shares = 1,000,000, EPS = 3.50
# Warrant After exercise: 40,000 shares * Rs 50 = Rs 2,000,000 inflow -> Total Cap = 42,000,000!
# EBIT = 20% of 42,000,000 = 8,400,000, Int = 1,000,000 (bonds remain!), EBT = 7,400,000, NI = 3,700,000, Shares = 1,040,000, EPS = 3,700,000 / 1,040,000 = 3.5577
print(f"EPS After Conv = {4000000/1200000:.4f}, EPS After Warrant = {3700000/1040000:.4f}")

print("\n================ PAPER 2: BNK 209 ================")
# Q15: HLV
hlv = (600000 - 30000) * 11.4699
print(f"Q15: HLV = {hlv:,.2f}")

print("\n================ PAPER 3: BNK 202 ================")
# Q13: Equity swap EPF (pays floating SOFR) vs Nabil (pays NEPSE return)
# Notional = 50,000,000, Quarterly (90 days), 30/360
# Initiation: NEPSE_0 = 2745.63, 90-day SOFR = 8%
# Now: t = 50 days into life (40 days remaining until day 90), NEPSE_t = 2825.02, 40-day SOFR = 7.8%
# Value of equity leg (per Rs 1 notional) at t=50: S_t / S_0 = 2825.02 / 2745.63
# Value of floating leg (per Rs 1 notional) at t=50: (1 + 0.08 * (90/360)) / (1 + 0.078 * (40/360))
eq_leg = 2825.02 / 2745.63
flt_leg = (1 + 0.08 * (90 / 360)) / (1 + 0.078 * (40 / 360))
val_epf = 50_000_000 * (eq_leg - flt_leg)
print(f"Q13: eq_leg={eq_leg:.6f}, flt_leg={flt_leg:.6f}, Value to EPF = Rs {val_epf:,.2f}, Value to Nabil = Rs {-val_epf:,.2f}")

# Q14: PCC $5M payable in 1 year.
# Spot = Rs 140/$, 1-yr Forward = Rs 130/$ (note typo "130 yen per dollar" in question, obviously Rs 130 per dollar).
# r_Nepal = 5%, r_US = 8%, Call option strike X = Rs 125/$, premium = Rs 14/$
# a) Future value of option premium per dollar = 14 * (1 + 0.05) = Rs 14.70 (or uncompounded Rs 14; let's show both!)
# Since expected future spot = forward rate = Rs 130/$ > strike Rs 125/$, call option WILL be exercised at Rs 125/$.
# With interest on premium (5%): total cost per $ = 125 + 14*(1.05) = Rs 139.70 -> for $5M = Rs 698,500,000.
# Without interest on premium: total cost per $ = 125 + 14 = Rs 139.00 -> for $5M = Rs 695,000,000.
# b) Indifference between option hedge and forward hedge (Rs 130/$):
# Notice that even if the option expires worthless (S_T <= 125), cost is S_T + 14.70 (or S_T + 14).
# Wait: if S_T + 14.70 = 130 => S_T = Rs 115.30/$ (or without interest on premium: S_T + 14 = 130 => S_T = Rs 116/$)!
# Let's check: at S_T = 115.30 (with interest) or 116.00 (without interest), the option is NOT exercised (since S_T < 125), so PCC buys dollars in the spot market at S_T and adds the option premium cost (14.70 or 14.00) to equal the forward rate of Rs 130/$!
print("Q14 verified")

# Q15: HDL stock S0 = 900, Put X = 1000, T = 1 yr, r = 8% (annual compounding), P_mkt = 60
# Lower bound for European put: P_min = X/(1+r)^T - S0 = 1000/1.08 - 900 = 925.93 - 900 = Rs 25.93 (or continuous: 1000*e^-0.08 - 900 = 923.12 - 900 = 23.12)
# Wait! Market price of Put is Rs 60, which is GREATER than 25.93! Wait why would there be arbitrage at P=60?
# Wait: could it be a CALL option or is Rs 60 a typo in their question or is X - S0 = 1000 - 900 = 100 (intrinsic value / American put lower bound)?
#Wait! Let's check BOTH!
# In many Nepalese finance textbooks (e.g., Paudel et al. / Manandhar et al. based on Chance/Hull), how do they compute the lower bound of a put option or put-call parity?
# Wait: if someone compares P = 60 with X/(1+r) - S0 = 1000/1.08 - 900 = 25.93, or what if they didn't discount X (X - S0 = 1000 - 900 = 100 > 60), OR what if they used P_min = X/(1+r) - S0? Wait: let's check what happens at ST = 800 and ST = 1200 if you buy stock (900) + buy put (60) = 960 and borrow 960 at 8%!
# Wait: if you buy stock (900) + buy put (60) = Rs 960 today, at T=1 your payoff is AT LEAST X = Rs 1,000!
# What is the future value of Rs 960 borrowed at 8%?
# 960 * 1.08 = Rs 1,036.80 > 1,000! Wait: why is 960 * 1.08 = 1036.80 > 1000? Because P = 60 > 25.93!
# Wait why did the question ask: "Identify the appropriate arbitrage opportunity and show the arbitrage profit for the stock price of Rs 800 and Rs 1200 after one year"?
# Let's check! If a textbook author wrote:
# Intrinsic value (or undiscounted lower bound) = X - S0 = 1000 - 900 = 100 > 60, OR did the author think:
# Buy stock (900) + Buy put (60) = 960, and forgot interest or thought 925.93? No, wait: if you buy stock (900) + buy put (60) = 960, and borrow 960 at 8%, you owe 1036.80, which loses 36.80 at ST=800!
# What if you SHORT stock (+900), SELL put (+60) = +960, invest 960 at 8% -> grows to 1,036.80! Then at ST=800, put is exercised against you -> you buy stock at 1,000 to close short stock, net profit = 1036.80 - 1000 = +36.80! What about at ST=1200? Put expires worthless, you have to buy stock at 1200, net = 1036.80 - 1200 = -163.20 (not riskless!).
# WAIT A SECOND! Why did the question author think there is an arbitrage with ST=800 and ST=1200?
# Let's check how Nepalese BBA textbooks (Asmita / Buddha Publication for BNK 202 Financial Derivatives) solve this exact problem!
print("Checking Q15:")
print("PV(X) = 1000/1.08 =", 1000/1.08)

# Q16: Birat Company BSM model
# S0 = 650, X = 660, T = 0.5, sigma = 0.50, r = 0.10
S0, X, T, sigma, r = 650, 660, 0.5, 0.50, 0.10
d1 = (math.log(S0 / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
d2 = d1 - sigma * math.sqrt(T)
Nd1 = norm.cdf(d1)
Nd2 = norm.cdf(d2)
C_bsm = S0 * Nd1 - X * math.exp(-r * T) * Nd2
print(f"Q16 BSM: d1={d1:.4f}, d2={d2:.4f}, N(d1)={Nd1:.4f}, N(d2)={Nd2:.4f}, C={C_bsm:.2f}")

# Q18: Binomial model
# S0 = 1200, X = 1200 (at-the-money), T = 180/360 = 0.5, u = 1.25, d = 0.80, r = 0.08
Su = 1200 * 1.25 # 1500
Sd = 1200 * 0.80 # 960
Cu = max(Su - 1200, 0) # 300
Cd = max(Sd - 1200, 0) # 0
# Periodic r for 180 days:
# Method 1: simple periodic r_p = 0.08 * (180/360) = 0.04 -> R = 1.04
p_simple = (1.04 - 0.80) / (1.25 - 0.80)
C_simple = (p_simple * Cu + (1 - p_simple) * Cd) / 1.04
# Method 2: annual compounding (1.08)^0.5 = 1.03923
R_comp = (1.08) ** 0.5
p_comp = (R_comp - 0.80) / (1.25 - 0.80)
C_comp = (p_comp * Cu + (1 - p_comp) * Cd) / R_comp
# Method 3: continuous e^(0.08*0.5) = 1.04081
R_cont = math.exp(0.08 * 0.5)
p_cont = (R_cont - 0.80) / (1.25 - 0.80)
C_cont = (p_cont * Cu + (1 - p_cont) * Cd) / R_cont
print(f"Q18 Binomial: Simple(R=1.04): p={p_simple:.4f}, C={C_simple:.2f}; Comp: p={p_comp:.4f}, C={C_comp:.2f}; Cont: p={p_cont:.4f}, C={C_cont:.2f}")

# Q19: Basis swap CIT (pays 90-day T-bill) vs Global Bank (pays 90-day SOFR - spread)
# Let's compute discount factors at initiation:
days_init = [90, 180, 270, 360]
sofr_init = [0.0750, 0.0795, 0.0852, 0.0900]
tbill_init = [0.0550, 0.0587, 0.0630, 0.0690]
B_sofr = [1 / (1 + r * (d / 360)) for r, d in zip(sofr_init, days_init)]
B_tbill = [1 / (1 + r * (d / 360)) for r, d in zip(tbill_init, days_init)]
print("Q19 B_sofr:", [round(b, 6) for b in B_sofr])
print("Q19 B_tbill:", [round(b, 6) for b in B_tbill])

# Q20: Forward on dividend-paying stock
# S0 = 500, D1 = 10 at t=2/12, D2 = 10 at t=5/12, r = 0.08 continuous, T = 6/12 = 0.5
I = 10 * math.exp(-0.08 * (2/12)) + 10 * math.exp(-0.08 * (5/12))
F0 = (500 - I) * math.exp(0.08 * 0.5)
# 3 months later (t = 3/12): D1 already paid! D2 is now in 2 months (5-3=2 months), remaining T-t = 3/12 = 0.25, St = 480
I_t = 10 * math.exp(-0.08 * (2/12))
Ft = (480 - I_t) * math.exp(0.08 * 0.25)
# Value of short forward: (F0 - Ft) * e^(-0.08 * 0.25)  or  F0 * e^(-0.08 * 0.25) - (480 - I_t)
V_short = (F0 - Ft) * math.exp(-0.08 * 0.25)
print(f"Q20: I={I:.4f}, F0={F0:.2f}, I_t={I_t:.4f}, Ft={Ft:.2f}, V_short={V_short:.2f}")
