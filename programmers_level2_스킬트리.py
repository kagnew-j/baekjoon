def solution(skill, skill_trees):
    target = list(skill)
    target_list = [skill[:i+1] for i in range(len(skill))]
    sol = 0
    for ele in skill_trees:
        temp = list(ele)
        temp_ans = ""
        for word in temp:
            if word in target:
                temp_ans += word
        if temp_ans in target_list or temp_ans == "":
            sol += 1
    return sol