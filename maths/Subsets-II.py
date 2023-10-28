from collections import defaultdict

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1
        counts = [(k, v) for k, v in counts.items()]
        print(counts)

        res = []
        n = len(counts)
        curr_res = []

        def subsetInner(i: int, curr_res: List[int]):
            if i == n:
                res.append(curr_res[:])
                return

            initialLen = len(curr_res)
            subsetInner(i+1, curr_res)
            curr_res = curr_res[:initialLen]
            for j in range(counts[i][1]):
                curr_res.append(counts[i][0])
                subsetInner(i+1, curr_res)
            curr_res = curr_res[:initialLen]

        subsetInner(0, curr_res)

        return res


        
