'''
Given two strings, determine the longest sequence of shared characters with respect to order

establish an empty subsequence

for each

Start a pointer
Evaluate the character at this pointer
    Check for first occurrence of the character
        if no occurrence, return length of subsequence
        if it occurs, add the character to the subsequence


'''



def longest_common_subsequence(text1: str, text2:str):
    src = min(text1, text2)

    if src == text1:
        ref = text2
    else:
        ref = text1

    ptr = 0

    subsequence = []

    for idx, char in enumerate(src):
        if char in ref[ptr:]:
            subsequence.append(char)
            ptr = idx

    return len(subsequence)

if __name__ == '__main__':
    print(longest_common_subsequence('55 glue', 'glorilla'))