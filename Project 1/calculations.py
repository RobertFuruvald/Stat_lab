import numpy as np
import matplotlib.pyplot as plt


# probability functions for each dice
def p_dice(n):
    return np.ones(n) / n


# Create the different dices
tetra_pf = p_dice(4)
cube_pf = p_dice(6)
octa_pf = p_dice(8)
dodeca_pf = p_dice(12)
icosa_pf = p_dice(20)

# Task 1: Probability function of S
S = np.convolve(tetra_pf, cube_pf)
S = np.convolve(S, octa_pf)
S = np.convolve(S, dodeca_pf)
S = np.convolve(S, icosa_pf)

# Task 2: Probability of winning the game: S<=10 || S>=45
P_winning = sum(S[0:6]) + sum(S[40:])
print("Probability of winning: ", P_winning)

# Monte-Carlo
trials = [pow(10, i) for i in range(1, 6)]


def rand_dice(n):
    return np.random.randint(1, n + 1)


def monte(trial):
    win = 0
    for _ in range(trial):
        X = rand_dice(4) + rand_dice(6) + rand_dice(8) + rand_dice(12) + rand_dice(20)
        if X <= 10 or X >= 45:
            win = win + 1

    return win / trial


# task 3 1000 trials with the monte method
print("Task 3 1000 trials with the monte method: ", monte(1000))

# task 4 run different number of trials
task_4 = []
for trial in trials:
    task_4.append(monte(trial))


# task 5

# Function to simulate the Monte Carlo relative error
def monte_trials(n, max_trials=100000):
    end_result = []
    n_trials = []
    while n < max_trials:
        sim_prob = monte(n)
        relative_error = abs(sim_prob - P_winning) / P_winning
        end_result.append(relative_error)
        n_trials.append(n)
        n += 1000
    # Returns the number of trials
    return n_trials, end_result


task_5 = monte_trials(1000)


# Plots for the tasks
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

# Create a bar chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.bar(possible_sums, S, color='skyblue', edgecolor='black')

# Add labels and title
ax.set_xlabel('Sum (S)')
ax.set_ylabel('Probability P(S=s)')
ax.set_title('Probability Distribution of S (Sum of Five Platonic Dice)')

# Task 4 figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(trials, task_4, marker='o', linestyle='-', color='blue', label='Probability')
ax.axhline(y=P_winning, color='red', linestyle='--', label='Exact Probability')

# Label
ax.set_xlabel('Number of Trials')
ax.set_ylabel('Estimated Probability')
ax.set_title('Estimated Probability for n trials')
# Set the x-axis to logarithmic scale for better visualization
ax.set_xscale('log')
fig.legend()
# Task 5 figure
plt.figure(figsize=(8, 8))
plt.plot(task_5[0], task_5[1], label="Relative error")

plt.axhline(0.10, color="red", linestyle="--", label="10% Error Threshold")
plt.xlabel("Number of Trials")
plt.ylabel("Relative Error")
plt.title("Convergence of Relative Error")
plt.legend()

# Display the figures
plt.show()