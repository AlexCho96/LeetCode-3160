from typing import List

'''
Time Limit Exceeded in this case
'''

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball, color, count, output = {}, {}, 0, []

        for key,value in queries:
            if key in ball:
                color[ball[key]] -= 1
                if color[ball[key]] == 0:
                    del color[ball[key]]
                    count -= 1
            ball[key] = value
            color[value] = color.get(value, 0) + 1
            if color[value] == 1:
                count += 1
            output.append(count)
        return output