from math import exp, log, sqrt
from statistics import NormalDist
N = NormalDist().cdf
print("Q13 equity swap")
NP = 50e6; eq = 2825.02/2745.63; B = 1/(1+0.078*40/360); fl = (1+0.08*90/360)*B
print(eq, B, fl, NP*eq, NP*fl, NP*(eq-fl))
print("Q14"); print(125+14*1.05, (125+14*1.05)*5e6, 130*5e6, 130-14*1.05)
print("Q15 put bound", 1000/1.08-900)
print("Q16 BSM")
S, X, s, r, T = 650, 660, 0.5, 0.10, 0.5
d1 = (log(S/X)+(r+s*s/2)*T)/(s*sqrt(T)); d2 = d1-s*sqrt(T)
C = S*N(d1)-X*exp(-r*T)*N(d2); print(log(S/X), d1, d2, N(d1), N(d2), exp(-r*T), C)
print("Q18 binomial")
S = 1200; u = 1.25; d = 0.8; R = 1.04; p = (R-d)/(u-d); Cu = 300; Cd = 0; C = p*Cu/R; h = (Cu-Cd)/(S*u-S*d)
print(p, C, h, h*S-140, (h*S-140)*1.04, h*S*u-Cu, (h*S-140)*1.04-(h*S*u-Cu), ((h*S-140)*1.04-(h*S*u-Cu))/(h*S-140))
print("Q19 swap")
def Bs(rates, days): return [1/(1+r*d/360) for r, d in zip(rates, days)]
days = [90, 180, 270, 360]
Bsof = Bs([.075, .0795, .0852, .09], days); Btb = Bs([.055, .0587, .063, .069], days)
fs = (1-Bsof[-1])/sum(Bsof); ft = (1-Btb[-1])/sum(Btb)
print(Bsof, sum(Bsof), fs, fs*4); print(Btb, sum(Btb), ft, ft*4); spread = fs*4-ft*4; print("spread", spread)
days2 = [30, 120, 210, 300]
Bsof2 = Bs([.08, .0845, .09, .0955], days2); Btb2 = Bs([.06, .0647, .0695, .074], days2)
NP = 100e6
vsof = NP*(1+.075*.25)*Bsof2[0]; vtb = NP*(1+.055*.25)*Btb2[0]; vspread = NP*spread*0.25*sum(Bsof2)
print(Bsof2, sum(Bsof2), Btb2); print(vsof, vtb, vspread, vsof-vspread-vtb)
print("alt spread", NP*spread*0.25*sum(Btb2), vsof-NP*spread*0.25*sum(Btb2)-vtb)
print("Q20 forward")
I = 10*exp(-.08*2/12)+10*exp(-.08*5/12); F0 = (500-I)*exp(.04); print(I, F0)
FVd = 10*exp(.08*4/12)+10*exp(.08/12); print(FVd, 500*exp(.04), 515+FVd-500*exp(.04), (515-F0)*exp(.04))
I2 = 10*exp(-.08*2/12); F1 = (480-I2)*exp(.08*.25); print(I2, F1, (F0-F1)*exp(-.02), F0*exp(-.02)-(480-I2))
print("Q22")
print(240000/40, 6000*110, 6000*110-240000, (6000*110-240000)/240000, (6000*110-240000)/240000*4)
print(240000/20, 12000*90-240000, (12000*90-240000)/240000*4)
for ST in range(160, 321, 20): print(ST, (abs(ST-240)-60)*4000)
print(240000/260, 923*260, 923*240, 923*350, 923*20, 923*350/350000)
