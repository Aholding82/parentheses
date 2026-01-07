class Solution:
    def __init__(self,s):
        self.s = s

    def parentheses(self):
        stack = []
        for x in self.s:
            stack.append(x)
            if stack[0] == ')' or stack[0] == ']' or stack[0] == '}':
                break

            if x == ')' or x == ']' or x =='}':
                stack.pop()
                y = stack.pop()
                if y == '(' and x == ')':
                    continue
                elif y == '{' and x == '}':
                    continue
                elif y == '[' and x == ']':
                    continue

            else:
                continue

        # print(stack)
        if stack == []:
            result = 'valid'
            return result
        else:
            result = 'Invalid String'
            return result

input = '()()()()()((()))'
p = Solution(input)
validation = p.parentheses()
print(validation)