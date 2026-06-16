def top_three(lst):
    lst.sort(reverse=True)
    return lst[:3]


def word_count(x):
    words = x.split(" ")
    return {word: words.count(word) for word in set(words)}


def common_skills(person1_skills, person2_skills):
    return list(set(person1_skills) & set(person2_skills))
