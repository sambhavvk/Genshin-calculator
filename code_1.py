import math

def binomial_coefficient(n, k):
    return math.comb(n, k)

def probability_of_getting_b_things(a, b):
    p = 0.007  # 0.7% probability
    q = 1 - p
    odds = 0

    def guaranteed_success_probability(a, b):
        total_odds = 0
        blocks = a // 11
        remaining_tries = a % 11

        for i in range(blocks + 1):
            success_odds = binomial_coefficient(blocks, i) * (q ** (10 * i))
            remaining_odds = binomial_coefficient(10 * (i + 1) + remaining_tries - 1, b - i - 1) * (p ** (b - i - 1)) * (q ** (10 * (i + 1) + remaining_tries - b))
            total_odds += success_odds * remaining_odds
        return total_odds

    if a < 10:
        for i in range(b, a + 1):
            odds += binomial_coefficient(a, i) * (p ** i) * (q ** (a - i))
    else:
        odds = guaranteed_success_probability(a, b)

    return odds

# Example usage:
a = 200
b = 2
print(f"The odds of getting {b} things in {a} number of tries is {probability_of_getting_b_things(a, b)}")
