import numpy as np


def sliding_window(nums, window_size):
    window = list()
    res = list()
    for i in range(window_size):
        while len(window) > 0  and nums[i] >= nums[window[0]]:
            window.pop(-1)
        window.append(i)

    for i in range(window_size, len(nums)):
        res.append(nums[window[0]])
        while len(window) > 0 and nums[i] >= nums[window[-1]]:
            window.pop(-1)
        if len(window) > 0 and window[0] <= i-window_size:
            window.pop(0)
        window.append(i)

    res.append(nums[window[0]])
    return res

if __name__ == "__main__":
    #nums = np.random.randint(10, 100, 20)
    nums = [6,1,1,2,0,5]
    print(nums)
    res = sliding_window(nums, 3)
    print(res)
    
    
