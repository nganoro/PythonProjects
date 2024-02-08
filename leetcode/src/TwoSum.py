class TwoSum:

    def findSum(nums: list(), target: int) -> list():
        result = list()
        map = {}

        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp in map:
                result.insert(0, map.get(temp))
                result.insert(1, i)
                break
            else:
                map[nums[i]] = i

        return result

    nums = [2, 7, 11, 15]
    target = 9
    print(findSum(nums, target))
