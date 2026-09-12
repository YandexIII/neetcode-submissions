class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {
            '(' : '',
            '[' : '',
            '{' : '',
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        for symbol in s:
            if len(stack) == 0:
                stack.append(symbol)
            else:
                if stack[-1] == symbols[symbol]:
                    print("dwed")
                    stack.pop()
                    stack.append(symbol)
                    stack.pop()
                else:
                    stack.append(symbol)
            print(stack)
        
        if len(stack) == 0:
            return True
        
        return False
        


            
