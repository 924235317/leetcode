if num == 0:
            return False
        
        if num in [1, 2, 3, 5]:
            return True
        
        res = False
        if num % 2 == 0:
            res = res or self.isUgly(num // 2)
        if num % 3 == 0:
            res = res or self.isUgly(num // 3)    
        if num % 5 == 0:
            res = res or self.isUgly(num // 5)
        
        return res
