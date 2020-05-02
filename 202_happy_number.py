def isHappy(n: int) -> bool:
        def cal(n):
            res = 0
            while n:
                tmp = n % 10
                res += tmp * tmp
                n = n // 10
            return res
        
        slow = n
        fast = cal(n)
        while slow != fast:
        #while True:
            slow = cal(slow)
            fast = cal(fast)
            fast = cal(fast)
            #if slow == fast:
            #    break
        
        return slow == 1

if __name__ == "__main__":
    print(isHappy(19))
