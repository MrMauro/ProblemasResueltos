# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
# A subsequence of a string is a new string generated form the original string with some characteres (can be none)
# deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde"
#
# Example 1:
# 
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3

def countSubsequence(s,words):
    count = 0
    indexMap={}

    # Paso 1: Llenar el indexMap

    for i,char in enumerate(s):
        if char not in indexMap:
            indexMap[char] = [i]
        else:
            indexMap[char].append(i)

    # s = "abac"
    # Iteración:
    # i=0 -> 'a' → indexMap['a'] = [0]
    # i=1 -> 'b' → indexMap['b'] = [1]
    # i=2 -> 'a' → indexMap['a'] = [0, 2]
    # i=3 -> 'c' → indexMap['c'] = [3]

    # Paso 2: Verificar cada palabra

    for word in words:
        prev_index=-1
        is_subsequence=True

        for char in word:
            if char not in indexMap:
                is_subsequence=False
                break

            # busqueda secuencial del siguiente indice valido
            found = False
            for idx in indexMap[char]:
                if idx > prev_index:
                    prev_index = idx
                    found = True
                    break

            if not found:
                is_subsequence = False
            break

        if is_subsequence:
            count += 1

    return count

s = "abcde"
words = ["a","bb","acd","ace"]

print(countSubsequence(s,words))