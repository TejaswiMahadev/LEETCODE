class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        merged_dict = {}
        for id_, val in nums1:
            merged_dict[id_] = merged_dict.get(id_, 0) + val
        for id_, val in nums2:
            merged_dict[id_] = merged_dict.get(id_, 0) + val
        return sorted(merged_dict.items())

        