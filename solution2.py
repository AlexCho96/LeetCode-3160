from typing import List

'''
Time Limit Exceeded in this case
'''

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result, output = {}, []

        for i in range(len(queries)):
            result[queries[i][0]] = queries[i][1]
            output.append(len(set(list(result.values()))))
        return output      