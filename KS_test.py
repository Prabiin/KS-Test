from scipy.stats import ksone


def critical_value(lev_of_sig, df):
    return ksone.ppf(1-lev_of_sig/2, df)


inputs = []
rank = []
rank_calc = []
D_plus = []
D_minus = []
D_calc = []
N = int(input("Enter the number of inputs to be tested: "))

print(f"Enter {N} numbers between 0 and 1:")
# creates sample list
for i in range(N):
    number = float(input("Enter sample numbers: "))
    inputs.append(number)
inputs.sort()           # sorting in ascending order
for i in range(N):      # giving ranks
    rank.append(i + 1)
# calculates i/N
for i in range(N):
    rank_calc.append(round((rank[i] / N), 3))
# Calculates D+ and D-
for i in range(N):
    D_plus.append(round((rank_calc[i] - inputs[i]), 3))
    D_minus.append(round(inputs[i] - ((i+1-1)/N), 3))
# displaying the outcomes
print(f"Inputs      : {inputs}")
print(f"i(rank)     : {rank}")
print(f"i/N         : {rank_calc}")
print(f"D+          : {D_plus}")
print(f"D-          : {D_minus}")
D_calc.append(max(D_plus))
D_calc.append(max(D_minus))
print(f"Max(D+,D-)  : {D_calc}")
print("\nThe calculated value of D is " + str(max(D_calc)))
alpha = float(input("\nPlease enter the level of significance: "))
deg_of_freedom = N
D_tabulated = round(critical_value(alpha, deg_of_freedom), 3)
print(f"\nThe tabulated value at level of significance {alpha} and degree of freedom {deg_of_freedom} is {D_tabulated}")
if D_tabulated > D_calc[0]:
    print("\nHere D_tabulated > D_calculated.")
    print("The null hypothesis is accepted. Hence the random numbers are uniformly distributed.")
else:
    print("\nHere D_tabulated < D_calculated.")
    print("The null hypothesis is rejected. Hence the random numbers are not uniformly distributed.")
