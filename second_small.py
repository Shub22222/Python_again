nums = [45, 12, 78, 3, 90, 21]

small=nums[0]
Sec_small=nums[0]

for i in range(len(nums)):
    if small>nums[i]:
        Sec_small=small
        small=nums[i]

    print("this is small",small)
    print("this is sec small",Sec_small)
