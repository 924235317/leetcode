def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 > len2:
        return findMedianSortedArrays(nums2, nums1)

    if len2 == 0:
        raise ValueError

    l = 0
    r = len1
    half_len = (len1 + len2 + 1) // 2
    while l <= r:
        m1 = (l + r) // 2
        m2 = half_len - m1
        if m1 < len1 and nums1[m1] < nums2[m2-1]:
            l = m1 + 1
        elif m1 > 0 and nums1[m1-1] > nums2[m2]:
            r = m1 - 1
        else:
            max_left = -1
            if m1 == 0:
                max_left = nums2[m2-1]
            elif m2 == 0:
                max_left = nums1[m1-1]
            else:
                max_left = max(nums1[m1-1], nums2[m2-1])

            if (len1 + len2) % 2 == 1:
                return max_left

            min_right = 100000
            if m1 == len1:
                min_right = nums2[m2]
            elif m2 == len2:
                min_right = nums1[m1]
            else:
                min_right = min(nums1[m1], nums2[m2])

            return (max_left + min_right) / 2.0

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
   
