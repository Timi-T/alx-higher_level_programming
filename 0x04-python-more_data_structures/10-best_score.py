#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sco = list(map(lambda x: x, (a_dictionary[key] for key in a_dictionary)))
    for i in range(1, len(sco)):
        if sco[i - 1] > sco[i]:
            a = sco[i - 1]
        elif sco[i] > sco[i - 1]:
            a = sco[i]
        else:
            a = None
    for key in a_dictionary:
        if a_dictionary[key] == a:
            return key
    return None
