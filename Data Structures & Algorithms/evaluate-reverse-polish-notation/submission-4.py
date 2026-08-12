class Solution:
    def evalRPN(self, lis: List[str]) -> int:
        stack=[]     
        for i in lis:
            if i =='+':
                a=stack.pop()+stack.pop()
                stack.append(a)
            elif i=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif i=='*':
                a=int(stack.pop())*int(stack.pop())
                stack.append(a)
            elif i=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(i))
        return stack[0]