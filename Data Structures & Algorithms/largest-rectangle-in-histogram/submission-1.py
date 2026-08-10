class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i, height in enumerate(heights):
            latest_i = i
            if not stack:
                stack.append([i, height])
                continue
            
            while stack and height < stack[-1][1]:
                holder = stack.pop()
                area = (i - holder[0]) * holder[1]
                latest_i = holder[0]
                if area > max_area:
                    max_area = area

            stack.append([latest_i, height])

            

        while stack:
            holder = stack.pop()
            area = ((len(heights)) - holder[0]) * holder[1]

            if area > max_area:
                max_area = area

        return max_area