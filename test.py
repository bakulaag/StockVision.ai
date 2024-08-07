list = [1,2,3,4]
list1 = [4,5,5,6]
i = 0
j = 0
list2 = []
while i<len(list) and j<len(list1):
    if list[i]< list1[j]:
        list2.append(list[i])
        i = i+1
    else:
        list2.append(list1[j])
        j = j+1
list2.extend(list[i:])
list2.extend(list1[j:])

print(list2)

def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3
