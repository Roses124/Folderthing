import school_scores
scores_list = school_scores.get_all()
index = 0
print(scores_list[0])
test_takers = []
for row in scores_list:
    #gets out state and yr
    print(row["State"]["Name"], row["Year"])

for row in scores_list:
    test_takers.append(row["Total"]["Test-takers"])
