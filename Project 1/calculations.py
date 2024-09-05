import numpy as np
import matplotlib.pyplot as plt

# probability functions for each dice
def p_dice(n):
    return np.ones(n)/n

tetra_pf = p_dice(4)
cube_pf = p_dice(6)
octa_pf = p_dice(8)
dodeca_pf = p_dice(12)
icosa_pf = p_dice(20)

# Task 1: Probability function of S
S = np.convolve(tetra_pf,cube_pf)
S = np.convolve(S,octa_pf)
S = np.convolve(S,dodeca_pf)
S = np.convolve(S,icosa_pf)


#Task 2: Probability of winning the game: S<=10 || S>=45
P_winning = sum(S[0:5]) + sum(S[40:])
print("Probability of winning: ", P_winning)


# Monte-Carlo
trials = [pow(10,i) for i in range(1,6)]

def rand_dice(n):
    return np.random.randint(1,n+1)


def monte(trial):
    win = 0
    for _ in range(trial):
        X = rand_dice(4) + rand_dice(6) + rand_dice(8) + rand_dice(12) + rand_dice(20)
        if X<=10 or X>=45:
            win = win + 1

    return win/trial



# task 4
for trial in trials:
    print(f'{trial} trials: ', monte(trial))

# task 5
not_winning = True
t = 2
i = 5
while not_winning:
    i = i+1
    tries = pow(t,i)
    print("tries: ", tries)
    prob = monte(tries)
    relative = abs(prob - P_winning)/P_winning
    #if P_winning*0.9 <= prob <= P_winning*1.1:
    if relative < 0.1:
             # p = prob
    #         # for _ in range(50):
    #         #     prob = monte(tries)
    #         #     p = p + prob
    #         # print("p/11: ", p/51)
    #         # if P_winning*0.9 < p/51 < P_winning*1.1:
        not_winning = False

    print("prob: ", prob)
    number_of_trials_needed = pow(t,i)
    print("Trials needed: ", number_of_trials_needed)


#Plots
# The sum S ranges from 5 to 50
possible_sums = np.arange(5, 51)
# data prep
table_data = [[s, f"{prob:.6f}"] for s, prob in zip(possible_sums, S)]

# Create the plot and add a table
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')  # Turn off the axis

# Create the table
table = ax.table(cellText=table_data, colLabels=["S", "P(S=s)"], cellLoc='center', loc='center')

# Adjust the table's style
table.auto_set_font_size(False)
table.set_fontsize(10)

# Display the table
plt.show()