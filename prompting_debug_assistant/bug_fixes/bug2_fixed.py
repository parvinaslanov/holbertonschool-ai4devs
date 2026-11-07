def passing_scores(scores, minimum=50):
    return [score for score in scores if score >= minimum]

scores = [32, 50, 67, 49, 82, 91]
print(passing_scores(scores))
