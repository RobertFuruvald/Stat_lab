import numpy as np

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

# Bootstrapping to determine the interval for my
bootstrap_samples = np.random.choice(X, size=(m, n))
# Calculate the means for each sample
bootstrap_means = bootstrap_samples.mean(axis=1)

# Calculate the means - X_mean
bootstrap_calculated = X_mean - bootstrap_means

# Extract the proportion that falls within (a, b)
centered_means = bootstrap_means[(bootstrap_calculated > a) & (bootstrap_calculated < b)]
# Get the number of μ that fits within a,b
bounds = len(centered_means)
# Calculate the reasonable μ from the filtered means
reasonable_mu = np.mean(centered_means)

# estimate the probability
p = bounds / m
print("X_bar for the sample : ", X_mean)
print("Most probable estimator of μ: ", reasonable_mu)
print("Estimated probability with bootstrapping: ", p)