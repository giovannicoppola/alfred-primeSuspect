#!/usr/bin/python3
import json
import sys
import random

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_closest_primes(x):
    """Find the closest prime numbers less than and greater than x."""
    smaller_prime = None
    larger_prime = None

    # Find smaller prime
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            smaller_prime = i
            break

    # Find larger prime
    i = x + 1
    while True:
        if is_prime(i):
            larger_prime = i
            break
        i += 1

    return smaller_prime, larger_prime

def prime_factorization(n):
    """Return the prime factorization of n as a list of (factor, exponent) tuples."""
    factors = []
    d = 2
    while d * d <= n:
        exp = 0
        while n % d == 0:
            n //= d
            exp += 1
        if exp > 0:
            factors.append((d, exp))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors

def format_factorization(factors):
    """Format prime factorization using superscript characters."""
    superscripts = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    parts = []
    for base, exp in factors:
        if exp == 1:
            parts.append(str(base))
        else:
            parts.append(f"{base}{str(exp).translate(superscripts)}")
    return " × ".join(parts)

FUN_FACTS = [
    # Basics
    "2 is the smallest prime and the only even prime number.",
    "The number 1 is not prime — by definition, a prime has exactly two distinct divisors.",
    "A prime ≥ 5 always ends in 1, 3, 7, or 9.",
    "3 is the only prime that is also a triangular number (1 + 2 = 3).",
    "There are exactly 25 prime numbers below 100.",
    "Every prime > 3 can be written as 6n ± 1 for some positive integer n.",

    # History & proofs
    "There are infinitely many primes — proven by Euclid over 2,000 years ago.",
    "The Sieve of Eratosthenes (circa 240 BC) is one of the oldest algorithms still in use today.",
    "Wilson's theorem: p is prime if and only if (p − 1)! + 1 is divisible by p.",
    "For any prime p ≥ 5, p² − 1 is always a multiple of 24.",
    "Bertrand's postulate: for any n > 1, there is always a prime between n and 2n.",

    # Famous conjectures & open problems
    "Goldbach's Conjecture: every even number > 2 is the sum of two primes. Still unproven!",
    "The Riemann Hypothesis, one of math's greatest unsolved problems, concerns prime distribution.",
    "Twin primes (like 11 & 13) differ by 2. It's unknown if there are infinitely many.",
    "Legendre's conjecture: there's always a prime between n² and (n+1)². Still unproven!",
    "The Green–Tao theorem (2004): the primes contain arithmetic progressions of any length.",

    # Special types of primes
    "A Sophie Germain prime p means 2p + 1 is also prime (e.g., 11 → 23).",
    "\"Emirp\" primes are prime when reversed too: 13 ↔ 31, 37 ↔ 73.",
    "Palindromic primes read the same backward: 131, 757, 11311…",
    "Happy primes reach 1 when you keep summing the squares of their digits.",
    "Mersenne primes have the form 2ᵖ − 1. Every even perfect number is linked to one.",
    "A repunit prime is made entirely of 1s — like 1111111111111111111 (19 ones).",
    "Fibonacci primes are Fibonacci numbers that are also prime: 2, 3, 5, 13, 89, 233…",
    "A Wieferich prime p satisfies 2ᵖ⁻¹ ≡ 1 (mod p²). Only two are known: 1093 and 3511.",
    "Chen primes p have the property that p + 2 is either prime or a product of two primes.",
    "Cuban primes are differences of consecutive cubes: 7 = 2³ − 1³, 19 = 3³ − 2³…",

    # Large primes & records
    "The largest known primes are Mersenne primes with millions of digits!",
    "2³¹ − 1 = 2,147,483,647 is a Mersenne prime — the largest ever found by hand (Euler, 1772).",
    "GIMPS (Great Internet Mersenne Prime Search) uses distributed computing to hunt for record primes.",

    # Patterns & curiosities
    "Arrange numbers in a spiral and highlight primes — diagonal patterns emerge (Ulam spiral).",
    "Prime deserts: gaps between consecutive primes can be arbitrarily large.",
    "The sum of the reciprocals of all primes diverges — it grows without bound.",
    "Consecutive primes tend to avoid sharing their last digit — known as the 'prime conspiracy' (2016).",
    "73 is the 21st prime, 7 × 3 = 21, and both 73 and 21 are palindromes in binary.",
    "The number 41 generates primes: n² + n + 41 is prime for every n from 0 to 39.",
    "The digit sum of any prime > 3 is never divisible by 3.",
    "Every even perfect number (6, 28, 496…) can be written as 2ᵖ⁻¹ × (2ᵖ − 1) where 2ᵖ − 1 is prime.",

    # Real-world applications
    "RSA encryption relies on the difficulty of factoring large primes.",
    "Primes are used in hashing algorithms for efficient data storage and retrieval.",
    "Cicadas have 13- or 17-year life cycles — both prime — to avoid predators.",
    "Some composers use primes to structure rhythm and melody for unique patterns.",
    "Scientists included primes in messages to outer space — a potential universal language.",
    "In the movie Contact, aliens send a sequence of prime numbers as first contact.",
    "Credit card numbers use prime-based modular arithmetic for error detection (Luhn algorithm).",
    "Prime numbers help generate pseudorandom numbers used in simulations and cryptography.",
]

items = []

try:
    myQuery = int(sys.argv[1])

    if is_prime(myQuery):
        myTitle = f"💫 {myQuery:,} is a prime number!"
        mySubtitle = "✨ No factors — indivisible! 😎"
        items.append({
            "title": myTitle,
            "subtitle": mySubtitle,
            "valid": True,
            "arg": f"{myQuery} is a prime number"
        })

        # Add a random fun fact as a second row
        fact = random.choice(FUN_FACTS)
        items.append({
            "title": "💡 " + fact,
            "subtitle": "🧠 Fun fact about prime numbers — ⏎ to copy",
            "valid": True,
            "arg": fact,
            "icon": {"path": "icon.png"}
        })

    else:
        if myQuery < 2:
            items.append({
                "title": f"❌ {myQuery:,} is not a prime number",
                "subtitle": "☝️ Prime numbers must be greater than 1",
                "valid": True,
                "arg": f"{myQuery} is not a prime number"
            })
        else:
            smaller, larger = find_closest_primes(myQuery)
            closest_parts = []
            if smaller is not None:
                closest_parts.append(f"⬇️ {smaller:,} (-{myQuery - smaller})")
            if larger is not None:
                closest_parts.append(f"⬆️ {larger:,} (+{larger - myQuery})")

            items.append({
                "title": f"❌ {myQuery:,} is not a prime number",
                "subtitle": f"🔎 Closest primes: {', '.join(closest_parts)}",
                "valid": True,
                "arg": f"{myQuery} is not a prime number"
            })

            # Prime factorization + all factors as second row
            pf = prime_factorization(myQuery)
            pf_str = format_factorization(pf)
            myFactors = [x for x in range(2, int(myQuery / 2) + 1) if myQuery % x == 0]
            myFactorsString = ", ".join(str(n) for n in myFactors)
            items.append({
                "title": f"🧮 {myQuery:,} = {pf_str}  ({myFactorsString})",
                "subtitle": "📋 Prime factorization & factors — ⏎ to copy",
                "valid": True,
                "arg": f"{myQuery} = {pf_str} ({myFactorsString})",
                "icon": {"path": "icon.png"}
            })

except (ValueError, IndexError):
    items.append({
        "title": "🚨 This is not an integer…",
        "subtitle": "… enter a valid number 🔢",
        "valid": False
    })

result = {"items": items}
print(json.dumps(result))
