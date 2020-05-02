from functools import cmp_to_key

def largestNumber(nums):
    def comp(str1, str2):
        if str1 + str2 > str2 + str1:
            return 1
        elif str1 + str2 == str2 + str1:
            return 0
        else:
            return -1
    
    nums_str = list(map(str, nums))
    nums_str = sorted(nums_str, key=cmp_to_key(comp), reverse=True)
    
    return str(int("".join(nums_str)))

if __name__ == "__main__":
    nums = [10, 2]
    print(largestNumber(nums))
