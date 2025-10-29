# Binomial Distribution Formula:
# P(X=k) = C(n, k) * (p^k) * ((1-p)^(n-k))
# where C(n, k) = n! / (k! * (n-k)!)
import math

def binomial_distribution(n, k, p):
    """
    Calculates the probability of k successes in n trials for a binomial distribution.

    Args:
        n (int): The number of independent trials.
        k (int): The number of successes in the n trials.
        p (float): The probability of success on a single trial. Value must be between 0 and 1 (0 <= p <= 1).

    Returns:
        float: The probability of exactly k successes.
    """
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")
    if not (0 <= k <= n):
        raise ValueError("Number of successes k must be between 0 and n.")

    # Calculate the binomial coefficient (nCk)
    # This calculates the number of ways to choose k successes from n trials, without regard to order of the successes. 
    # For example, if you have 3 trials and want 2 successes, math.comb(3, 2) would be 3 (SSN, SNS, NSS).
    combinations = math.comb(n, k)

    # Calculate the probability
    # p ** k: The probability of getting k successes.
    # (1 - p) ** (n - k): The probability of getting n - k failures.
    probability = combinations * (p ** k) * ((1 - p) ** (n - k))

    return probability

if __name__ == "__main__":
    # Example Usage
    n_trials = 3
    k_successes = 2
    p_probability = 0.7

    prob = binomial_distribution(n_trials, k_successes, p_probability)
    print(f"Probability of {k_successes} successes in {n_trials} trials with p={p_probability}: {prob:.4f}")

    # n_trials_2 = 5
    # k_successes_2 = 4
    # p_probability_2 = 0.3

    # prob_2 = binomial_distribution(n_trials_2, k_successes_2, p_probability_2)
    # print(f"Probability of {k_successes_2} successes in {n_trials_2} trials with p={p_probability_2}: {prob_2:.4f}")

    # Edge cases
    try:
        binomial_distribution(10, 5, 1.2)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        binomial_distribution(10, 12, 0.5)
    except ValueError as e:
        print(f"Error: {e}")
