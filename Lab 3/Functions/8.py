def spy_game(nums):
    is7 = False
    for i in range(2, len(nums)):
        agent = nums[i-2] * 100 + nums[i-1] * 10 + nums[i]
        if agent == 7:
            is7 = True
            break
    return is7
nums = list(map(int, input().split()))
print(spy_game(nums))