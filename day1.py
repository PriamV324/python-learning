def describe_list(lst):
    total = sum(lst)
    average = total / len(lst)
    odds = [x for x in lst if x % 2 != 0]
    evens = [x for x in lst if x % 2 == 0]
    return {"total": total, "average": average, "odds": odds, "evens": evens}


print(describe_list([1, 2, 3, 4, 5, 6]))
