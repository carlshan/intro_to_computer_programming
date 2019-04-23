
def recursive_max(nums):
    if len(nums) == 1: # base case - only one thing in the list
        return nums[0]
    else:
        max_of_rest = recursive_max(nums[1:])
        if nums[0] > max_of_rest:
            return nums[0]
        else:
            return max_of_rest

print(recursive_max([88, 2, 100, 2, 1, 5, 1000]))


def reverse_list(L):
    if len(L) == 1: # base case - only one thing in the list
        return L
    else:
        return [L[-1]] + reverse_list(L[:-1])

print(reverse_list([1, 5, 100, 12]))

def flatten(S):
    if len(S) == 0:
        return S
    elif isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    else:
        return [S[0]] + flatten(S[1:])

print(flatten([1,2,3, [4, 5, [6, 7, 8, [100, 2, [123123]]]]]))
