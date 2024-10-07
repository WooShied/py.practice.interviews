#remove duplicates


# Write a function that would just return a length of an array
# that does not contains any duplicates.
# For example: if [1 1 2] is passed then output should be 2
# [0 0 1 1 1 2 2 3 3 4] output should be 5
# [0 1 2 3 4]

# Note: array passed in would already be sorted

def remove_doups(arr):
    unique_val = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            unique_val.append(arr[i])

    return unique_val

arr = [1, 1, 2, 2, 3, 4, 5, 6 ,6]
print(remove_doups(arr))