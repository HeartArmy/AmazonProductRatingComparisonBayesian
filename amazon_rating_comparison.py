import math

# -----------------------------
# SETTINGS (you can adjust these)
# -----------------------------

C = 4.2     # Global average rating across marketplace (estimate)
m = 50     # Minimum reviews to be fully trusted

# -----------------------------
# MANUALLY ADD PRODUCTS HERE
# Format: ("Product Name", average_rating, number_of_ratings)
# -----------------------------

products = [
    ("Product A", 4.6, 1052),
    ("Product B", 4.5, 10553),
    ("Product C", 4.5, 233),
    ("Product D", 4.6, 427),
    ("Product D", 4.6, 28245),
]

# -----------------------------
# CALCULATIONS
# -----------------------------

results = []

for name, R, v in products:
    # Bayesian Weighted Rating
    weighted_rating = (v / (v + m)) * R + (m / (v + m)) * C
    
    # Log-adjusted score (simple alternative)
    log_score = R * math.log(v + 1)
    
    results.append({
        "name": name,
        "avg_rating": R,
        "num_ratings": v,
        "weighted_rating": weighted_rating,
        "log_score": log_score
    })

# -----------------------------
# SORT BY WEIGHTED RATING
# -----------------------------

results_sorted = sorted(results, key=lambda x: x["weighted_rating"], reverse=True)

# -----------------------------
# PRINT RESULTS
# -----------------------------

print("\nRanked by Bayesian Weighted Rating:\n")

for i, product in enumerate(results_sorted, 1):
    print(f"{i}. {product['name']}")
    print(f"   Avg Rating: {product['avg_rating']}")
    print(f"   Number of Ratings: {product['num_ratings']}")
    print(f"   Weighted Rating: {product['weighted_rating']:.4f}")
    print(f"   Log Score: {product['log_score']:.4f}")
    print()