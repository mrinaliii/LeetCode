class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for i in nums1:
            found = False
            n = -1
            for j in range(len(nums2)):
                if nums2[j] == i:
                    found = True
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > i:
                            n = nums2[k]
                            break
                    break

            res.append(n)
        return res
        