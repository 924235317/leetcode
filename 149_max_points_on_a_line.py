def maxPoints(points):
    def gcd(num1, num2):
        max_val = max(num1, num2)
        min_val = min(num1, num2)
        num1 = max_val
        num2 = min_val
        if num2 == 0:
            return num1
        
        if num1 == num2:
            return num1
        
        if num1 > num2:
            return gcd(num2, num1 % num2)
        else:
            return gcd(num1, num2 % num1)

    if not points:
        return 0

    max_num = 1
    for i in range(len(points) - 1):
        h = dict()
        same_point = 1
        for j in range(i + 1, len(points)):
            xp1, yp1 = points[i]
            xp2, yp2 = points[j]

            if xp1 > xp2:
                x1, y1 = xp1, yp1
                x2, y2 = xp2, yp2
            else:
                x1, y1 = xp2, yp2
                x2, y2 = xp1, yp1
                
            if x1 == x2 and y1 == y2:
                same_point += 1
            else:
                if x1 == x2:
                    key = (None, None)
                else:
                    common_divisor = gcd(abs(y1 - y2), abs(x1 - x2))
                    k1 = (y1 - y2) / common_divisor
                    k2 = (x1 - x2) / common_divisor
                    
                    if k1 < 0:
                        k1, k2 = -k1, -k2
                    elif k1 == 0:
                        k1, k2 = 0, abs(k2)

                    key = (k1, k2)
                if key not in h:
                    h[key] = 0

                h[key] += 1
                      
        local_max = 0
        for hh in h.values():
            local_max = max(hh + same_point, local_max)

        local_max = max(local_max, same_point)
        
        max_num = max(max_num, local_max)
        
    return max_num


if __name__ == "__main__":
    points = [[1,1],[2,2],[3,3]]
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    points = [[0,0],[94911151,94911150],[94911152,94911151]]
    points = [[0, 0], [0, 0]]

    print(maxPoints(points))
