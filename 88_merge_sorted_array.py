def merge(nums1: list, m: int, nums2: list, n: int) -> None:

    i = m
    j = n
    k = m + n
    while i > 0 and j > 0:
        if nums1[i-1] >= nums2[j-1]:
            nums1[k-1] = nums1[i-1]
            i -= 1
            k -= 1
        else:
            nums1[k-1] = nums2[j-1]
            j -= 1
            k -= 1
    if j > 0:
        nums1[:k] = nums2[:k]


if __name__ == "__main__":
    nums1 = [2, 0]
    nums2 = [1]
    merge(nums1, 1, nums2, len(nums2))
    print(nums1)
