# Bug 2: Return the items that meet a minimum score
def passing_scores(scores, minimum=50):
    passed = []
    for score in scores:
        if score < minimum:
            passed.append(score)
    return passed

results = [35, 50, 67, 82, 49, 91]
print("Passing scores:", passing_scores(results))
