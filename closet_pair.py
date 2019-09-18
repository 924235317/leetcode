from random import randint
import math
import time

def gen_random_points(length: int, min_val: int, max_val: int) -> list:
    res = list()
    for i in range(length):
        x = randint(min_val, max_val)
        y = randint(min_val, max_val)
        res.append([x, y])
    return res


def sort_by_x(array: list) -> list:
    return sorted(array, key=lambda x:x[0])

def sort_by_y(array: list) -> list:
    return sorted(array, key=lambda x:x[1])

def dist(point1: list, point2: list) -> int:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def closet_pair_core(array: list, l: int, r: int) -> float:
    if r - l == 1:
        return dist(array[l], array[r])

    if r - l == 2:
        dist1 = dist(array[l], array[l + 1])
        dist2 = dist(array[r], array[l + 1])
        dist3 = dist(array[l], array[r])
        return min(dist1, min(dist2, dist3))
    
    m = (l + r) // 2

    min_l = closet_pair_core(array, l, m)
    min_r = closet_pair_core(array, m + 1, r)
    
    min_dist = min(min_l, min_r)

    tmp = list()
    for i in range(l, r+1):
        if abs(array[i][0] - array[m][0]) < min_dist:
            tmp.append(array[i])

    tmp = sort_by_y(tmp)
    for i in range(len(tmp)):
        for j in range(i + 1, len(tmp)):
            tmp_dist = dist(tmp[i], tmp[j])
            if tmp_dist < min_dist:
                min_dist = tmp_dist
    return min_dist


def closet_pair(array: list) -> float:
    if len(array) < 2:
        return -1
    array = sort_by_x(array)
    return closet_pair_core(array, 0, len(array) - 1)

def closet_pair_fool(array: list) -> float:
    min_dist = None
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if min_dist is None:
                min_dist = dist(array[i], array[j])
            else:
                min_dist = min(dist(array[i], array[j]), min_dist)
    return min_dist

if __name__ == "__main__":
    length = 10
    array = gen_random_points(length, 10, 500)
    
    start = time.time()
    for i in range(10000):
        tmp = closet_pair_fool(array)
    print(tmp)
    print("time: ", time.time() - start)
    start = time.time()
    for i in range(10000):
        tmp = closet_pair(array)
    print(tmp)
    print("time2: ", time.time() - start)

    
