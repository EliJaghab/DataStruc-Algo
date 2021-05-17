def productExceptSelf(nums):
    N = len(nums)
    answer = [0]*N
    answer[0] = 1
    for i in range(1, N):
        answer[i] = answer[i-1]*nums[i-1]

    R = 1
    for i in reversed(range(N)):
        answer[i] *= R
        R *= nums[i]
    return answer

# Time O(n)
# Space O(1)
