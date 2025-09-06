"""
# Probability Basics

- Conditional Probability
  The probability of an event A given that event B has occurred

  P(A|B) = P(A ∩ B) / P(B)

- Bayes' Theorem

  P(A|B) = P(B|A) * P(A) / P(B)

  - P(A): Prior probability
  - P(B|A): Likelihood

Python Implementation and Examples:
"""
def bayes_theorem(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

################################## Exercise 1  ##################################
"""
# Problem
# - A disease affects 1% of a population
# - A test is 95% accurate for diseased individuals and 90% accurate for non-diseased individuals
# - Find the probability of having the disease given a positive test result

This is a classic application of Bayes' Theorem in probability theory.
Let's break down the problem and solution step by step.
"""

def bayes_theorem(prior, sensitivity, specificity):
    """
    Calculate the posterior probability using Bayes' Theorem.
    
    Parameters:
    prior (float): Prior probability of having the disease (prevalence)
    sensitivity (float): True positive rate (probability of positive test if diseased)
    specificity (float): True negative rate (probability of negative test if not diseased)
    
    Returns:
    float: Posterior probability (probability of having the disease given a positive test)
    """
    # Calculate the evidence (total probability of a positive test)
    # P(Positive) = P(Positive|Disease)*P(Disease) + P(Positive|No Disease)*P(No Disease)
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    
    # Calculate the posterior probability using Bayes' Theorem
    # P(Disease|Positive) = [P(Positive|Disease) * P(Disease)] / P(Positive)
    posterior = (sensitivity * prior) / evidence
    
    return posterior

# Given values
prior = 0.01        # 1% prevalence (P(Disease))
sensitivity = 0.95  # 95% true positive rate (P(Positive|Disease))
specificity = 0.90  # 90% true negative rate (P(Negative|No Disease))

# Calculate the probability
posterior = bayes_theorem(prior, sensitivity, specificity)

# Print the result
print("Probability of Disease Given Positive Test: ", round(posterior, 4))

"""
Explanation:

1. Terminology:
   - Prior (0.01): The probability of having the disease before taking the test (1%)
   - Sensitivity (0.95): The probability that the test is positive if you have the disease (95%)
   - Specificity (0.90): The probability that the test is negative if you don't have the disease (90%)

2. Bayes' Theorem Formula:
   P(A|B) = [P(B|A) × P(A)] / P(B)
   
   In this case:
   P(Disease|Positive) = [P(Positive|Disease) × P(Disease)] / P(Positive)

3. Calculation Steps:
   a. Calculate P(Positive):
       = P(Positive|Disease)×P(Disease) + P(Positive|No Disease)×P(No Disease)
       = (0.95 × 0.01) + (0.10 × 0.99)  [Note: P(Positive|No Disease) = 1 - Specificity]
       = 0.0095 + 0.099 = 0.1085
   
   b. Calculate P(Disease|Positive):
       = (0.95 × 0.01) / 0.1085 ≈ 0.0876 or 8.76%

4. Interpretation:
   Even with a positive test result from a test that seems accurate (95% sensitivity, 90% specificity),
   the probability of actually having the disease is only about 8.76%. This counterintuitive result
   occurs because the disease is rare (only 1% prevalence), so there are many more false positives
   than true positives.

This demonstrates why it's important to consider base rates (prior probabilities) when interpreting
test results, especially for rare conditions.
"""

"""
Common Probability Distributions

Gaussian (Normal) Distribution
- Bell-shaped curve with mean (μ) and standard deviation (σ)
- Probability Density Function (PDF): 
  f(x) = (1 / (σ√(2π))) * e^(-(x-μ)²/(2σ²))

Bernoulli Distribution
- Describes outcomes of a binary experiment (success/failure)
- P(X=1) = p, P(X=0) = 1-p

Python Implementation and Visualization:
"""
"""
# Common Probability Distributions

- **Binomial Distribution**
  - Models the number of successes in n independent Bernoulli trials
  - Formula: P(X = k) = C(n,k) * p^k * (1-p)^(n-k)
    Where:
    - n: number of trials
    - k: number of successes
    - p: probability of success in each trial
    - C(n,k): binomial coefficient (n choose k)

- **Poisson Distribution**
  - Models the number of events in a fixed interval of time or space
  - Formula: P(X = k) = (λ^k * e^{-λ}) / k!
    Where:
    - λ: average rate of events (mean number of occurrences)
    - k: number of events
    - e: base of natural logarithm (~2.71828)

Python Implementation and Visualization:
"""
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
x = np.linspace(-4, 4, 100)

def gussian_func(x):
    return (1/(np.sqrt(2*np.pi*sigma**2))) * np.exp(-0.5*((x-mu)/sigma)**2)

y = [gussian_func(i) for i in x ]
print(y)

plt.plot(x,y)
plt.show()

def Bernoulli_Distributions(p):
    plt.bar([0,1],[1-p, p], color = "blue")
    plt.title("Bernoulli Distribution")
    plt.xticks([0, 1], labels=["0 (Failure)", "1 (Success)"])
    plt.show()
Bernoulli_Distributions(0.6)

def Binomial_Distribution(n,p):
    from scipy.stats import binom
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)
    plt.bar(x, y, color="blue")
    plt.title("Binomial Distribution")
    plt.show()

n, p = 10, 0.5
Binomial_Distribution(n,p)

def Poisson_Distribution(lam, k):
    from scipy.stats import poisson
    x = np.arange(0,k)
    y = poisson.pmf(x, lam)
    plt.bar(x, y, color="orange")
    plt.show()

Poisson_Distribution(lam = 3, k = 10)


################################## Exercise 2  ##################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson

x = np.linspace(-4, 4, 100)
y = norm.pdf(x, loc=0, scale = 1)
plt.plot(x, y, label = "Gaussian")
plt.title("Gaussian Distribution")
plt.show()


n, p = 10,0.5
y = binom.pmf(x,n,p)
plt.bar(x, y, label="Bionmial")
plt.title("Binomial Distribution")
plt.show()

