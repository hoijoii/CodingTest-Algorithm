"""

"""

def solution(word):
    answer = len(word)
    vowels = "AEIOU"
    diff = [781, 156, 31, 6, 1];

    for i in range(len(word)):
        idx = vowels.index(word[i])
        answer += idx * diff[i]

    return answer



