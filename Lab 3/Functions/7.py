def has_33(nums):
    c= False
    for i in range(1, len(nums)):
        num = nums[i]*10+nums[i-1]
        if num == 33:
            c=True
            break
    return c
nums=list(map(int,input().split()))
print(has_33(nums))
