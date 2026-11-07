# Bug 2: Return scores that meet the minimum passing score.
def passing_scores(scores, minimum=50):
    passed = []
    for score in scores:
        if score < minimum:
            passed.append(score)
    return passed

results = [35, 50, 67, 82, 49, 91]
passing = passing_scores(results)
print("Passing scores:", passing)
print("Number passing:", len(passing))
