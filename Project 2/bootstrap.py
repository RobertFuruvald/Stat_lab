import numpy as np
from matplotlib import pyplot as plt

# Task is to calculate p = P(a < X_bar - μ < b)

# Sample from assignment
X = np.array([56, 101, 78, 67, 93, 87, 64, 72, 80, 69])
a = -4
b = 6
n = len(X)

# Compute the mean of X
X_mean = np.mean(X)
# number of resampling
m = 10000

# Bootstrapping to determine the probability
# Generate the resamples as vectors
bootstrap_samples = np.random.choice(X, size=(m, n))
# Calculate the means for each sample
bootstrap_means = bootstrap_samples.mean(axis=1)

# Calculate the X_mean - bootstrap_means
bootstrap_calculated = X_mean - bootstrap_means

# Extract the proportion that falls within (a, b)
centered_means = bootstrap_means[(bootstrap_calculated > a) & (bootstrap_calculated < b)]
# Get the number of μ that fits within a,b
within_bounds = len(centered_means)
# Calculate the reasonable μ from the filtered means
reasonable_mu = np.mean(centered_means)

# estimate the probability
p = within_bounds / m

# Calculate probability p = P(a < X_bar - μ < b)
p2 = np.mean((bootstrap_calculated > a) & (bootstrap_calculated < b))
# Compute the 2.5th and 97.5th percentiles for the bootstrap calculated
lower_ci = np.percentile(bootstrap_calculated, 2.5)
upper_ci = np.percentile(bootstrap_calculated, 97.5)

# Visualization
plt.figure(figsize=(10, 6))
plt.hist(bootstrap_calculated, bins=30, alpha=0.7, color='skyblue', edgecolor='black', density=True)
plt.axvline(lower_ci, color='red', linestyle='--', label='Lower CI')
plt.axvline(upper_ci, color='green', linestyle='--', label='Upper CI')
plt.axvline(X_mean - reasonable_mu, color='orange', linestyle='-', label='Sample Mean (X̄)')

# Highlight the interval (a, b)
plt.fill_betweenx([0, 0.02], a, b, color='grey', alpha=0.5, label='Interval (a, b)')

plt.title('Distribution of Bootstrap Calculated Values (X̄ - μ)')
plt.xlabel('Bootstrap Calculated (X̄ - μ)')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()

print(f"95% Confidence Interval for (X̄ - μ): [{lower_ci: .2f}, {upper_ci: .2f}]")
print("X_bar for the sample : ", X_mean)
print(f"Most probable estimator of μ: {reasonable_mu:.2f}")
print("Estimated probability with bootstrapping: ", p)