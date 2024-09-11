def solution(spell, dic):
    for word in dic:
        if sorted(word) == sorted(spell):
            return 1
    return 2