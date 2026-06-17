def parse_survey_scores(raw: list) -> dict:
    valid = []
    invalid_count = 0

    for item in raw:
        try:
            valid.append(float(item))  # what goes here?
        except (ValueError, TypeError):
            invalid_count += 1  # what happens when it fails?

    average = round(sum(valid) / len(valid), 2)  # how do you calculate average?

    return {
        "valid": valid,
        "invalid_count": invalid_count,
        "average": average,
    }


def categorise_nps(score: list[int]) -> dict:
    categories = {"promoters": 0, "passives": 0, "detractors": 0}

    for s in score:
        if s >= 9:
            categories["promoters"] += 1
        elif s >= 7:
            categories["passives"] += 1
        else:
            categories["detractors"] += 1

    # Calculate NPS
    nps = ((categories["promoters"] - categories["detractors"]) / len(score)) * 100
    categories["nps_score"] = round(nps, 1)

    return categories


transactions = [
    {"product": "Cola", "category": "Beverage", "price": 45, "quantity": 3},
    {"product": "Chips", "category": "Snack", "price": 30, "quantity": 5},
    {"product": "Water", "category": "Beverage", "price": 20, "quantity": 8},
    {"product": "Biscuit", "category": "Snack", "price": 25, "quantity": 4},
    {"product": "Juice", "category": "Beverage", "price": 60, "quantity": 2},
    {"product": "Nuts", "category": "Snack", "price": 80, "quantity": 1},
    {"product": "Soda", "category": "Beverage", "price": 35, "quantity": 6},
]


# 1. Total revenue per category (price * quantity, summed by category)
revenue_by_category =

# 2. Names of products priced above 40
expensive_products = ???

# 3. Unique categories that appear more than 2 times
frequent_categories = ???

print(revenue_by_category)
print(expensive_products)
print(frequent_categories)
