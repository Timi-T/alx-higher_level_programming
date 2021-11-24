#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary) == False:
        return None
    score_list = list(map(lambda x: x, (a_dictionary[key] for key in a_dictionary)))
    for i in range(1, len(score_list)):
        if score_list[i - 1] > score_list[i]:
            a = score_list[i - 1]
        else:
            a = score_list[i]
    for key in a_dictionary:
        if a_dictionary[key] == a:
            return key
    return
