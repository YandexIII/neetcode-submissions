class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # pair: (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = (i - index) * height
                maxArea = max(maxArea, area)
                start = index
            stack.append((start, h))
        
        while stack:
            start = stack[-1][0]
            height = stack[-1][1]
            end = len(heights)
            area = (end - start) * height
            stack.pop()
            maxArea = max(maxArea, area)
        
        return maxArea