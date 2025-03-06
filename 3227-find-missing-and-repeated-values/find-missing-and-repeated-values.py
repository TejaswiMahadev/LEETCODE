class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        all_numbers = set(range(1, n * n + 1))
        seen = set()
        repeated = None
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)
                all_numbers.discard(num)
        
    
        missing = all_numbers.pop()
        
        return [repeated, missing]
