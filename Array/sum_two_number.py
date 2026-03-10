def Sum_two_number(nums, target):

    result = {}

    for i, num in enumerate(nums):
        total = target - num
        
        if total in result:
            return [result[total], i]
        
        result[num] = i


print(Sum_two_number([2,7,11,15], 9))