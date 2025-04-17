from operator import length_hint


def longest_substring(quest, K):
    windowStart, windowEnd = 0, 1
    result = 0
    substring = quest[0]
    count = 1
    while windowEnd < len(quest):
        if quest[windowEnd] not in substring and count < K:
            substring += quest[windowEnd]
            windowEnd += 1
            count += 1
        elif quest[windowEnd] in substring or len(substring) < 1:
            substring += quest[windowEnd]
            windowEnd += 1
        else:
            length = len(substring)
            substring = substring[windowStart:]
            windowStart += 1
            if length > result:
                result = length
    return result

# print(longest_substring("araaci", K=2))

#optimized code
def longest_substring_optimized(quest, K):
    windowStart = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(quest)):
        right_char = quest[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > K:
            left_char = quest[windowStart]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            windowStart += 1

        max_length = max(max_length, window_end - windowStart + 1)

    return max_length

print(longest_substring_optimized("araaci", K=2))