class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or time > (target - stack[-1][0]) / stack[-1][1]:
                stack.append(car)
        print(stack)
        return len(stack)



