import math

# Poisson Distribution Formula:
# P(X=k) = (lambda^k * e^(-lambda)) / k!
def poisson_distribution(k, lambda_val):
    """
    Calculates the probability of k occurrences in a fixed interval or region
    for a Poisson distribution.

    Args:
        k (int): The number of occurrences.
        lambda_val (float): The average number of occurrences in the interval/region. It must be a positive value (lambda > 0).

    Returns:
        float: The probability of exactly k occurrences.
    """
    if lambda_val <= 0:
        raise ValueError("Lambda (average rate) must be greater than 0.")
    if k < 0:
        raise ValueError("Number of occurrences k must be non-negative.")

    # P(X=k) = (lambda^k * e^(-lambda)) / k!
    # lambda_val ** k: Lambda raised to the power of k
    # math.exp (for calculating e to the power of a number) and math.factorial (for calculating factorials)
    # math.exp(-lambda_val): euler's number raised to the power of negative lambda
    probability = (lambda_val ** k * math.exp(-lambda_val)) / math.factorial(k)

    return probability

if __name__ == "__main__":
    # Example Usage
    k_occurrences = 2
    lambda_average = 3.0

    prob = poisson_distribution(k_occurrences, lambda_average)
    print(f"Probability of {k_occurrences} occurrences with lambda={lambda_average}: {prob:.4f}")

    # k_occurrences_2 = 5
    # lambda_average_2 = 1.5

    # prob_2 = poisson_distribution(k_occurrences_2, lambda_average_2)
    # print(f"Probability of {k_occurrences_2} occurrences with lambda={lambda_average_2}: {prob_2:.4f}")

    # Edge cases
    try:
        poisson_distribution(5, -1.0)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        poisson_distribution(-2, 3.0)
    except ValueError as e:
        print(f"Error: {e}")
