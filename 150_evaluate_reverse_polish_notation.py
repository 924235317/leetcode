def evalRPN(tokens):
    def is_number(num):
        try:
            float(num)
        except ValueError:
            return False

        return True

    nums = list()

    for t in tokens:
        if is_number(t):
            nums.append(int(t))
        else:
            nums1 = nums.pop()
            nums2 = nums.pop()

            if t == "+":
                nums.append(nums1 + nums2)
            elif t == "-":
                nums.append(nums1 - nums2)
            elif t == "*":
                nums.append(nums1 * nums2)
            elif t == "/":
                if (nums1 > 0 and nums2 > 0) or (nums1 < 0 and nums2 < 0):
                    flag = 1
                else:
                    flag = -1

                num = abs(nums2) // abs(nums1)
                
                nums.append(num * flag)

    return nums.pop()


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens))

            
