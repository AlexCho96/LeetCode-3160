from typing import List

'''
Memory Limit Exceeded in this case
'''

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        results = [[x, 0] for x in range(0, limit + 1)]
        output = []
        for i in range(len(queries)):
            results[queries[i][0]][1] = queries[i][1]
            colored = list(map(lambda x: x[1], results))
            if 0 in colored:
                output.append(len(set(colored)) - 1)
            else:
                output.append(len(set(colored)))

        return output