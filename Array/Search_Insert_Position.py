class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        print("\nArray:", nums)
        print("Target:", target)
        
        while left <= right:
            mid = (left + right) // 2
            
            print(f"\nLeft: {left}, Right: {right}, Mid: {mid}")
            print(f"nums[{mid}] = {nums[mid]}")
            
            if nums[mid] == target:
                print(" Target found at index:", mid)
                return mid
            
            elif nums[mid] < target:
                print(" Going right")
                left = mid + 1
            else:
                print(" Going left")
                right = mid - 1
        
        print("\n Target not found.")
        print(" Insert position:", left)
        return left


nums = list(map(int, input("Enter sorted array (space separated): ").split()))
target = int(input("Enter target: "))

sol = Solution()
result = sol.searchInsert(nums, target)

print("\nFinal Answer:", result)