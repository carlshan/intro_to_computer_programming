test_case2 = [1]
print(flatten(test_case2))
# This should print
# [1]

def flatten(S):
    if S == []:
        ## Your code here
    if isinstance(S[0], list):
        ## Your code here
    else:
        ## Your code here

test_case1 = []
print(flatten(test_case1))
# This should print
# []

test_case2 = [1]
print(flatten(test_case2))
# This should print
# [1]

test_case3 = [1, [2, 3, 4], [5, [6, [7]]]]
print(flatten(test_case3))
# This should print
# [1, 2, 3, 4, 5, 6, 7]


