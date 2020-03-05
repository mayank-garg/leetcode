"""
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_digit(val1):
            try:
                int(val1)
            except Exception as e:
                return False
            return True
        def perform_operation(val1, val2, op):
            val1 = int(val1)
            val2 = int(val2)
            if op == "+":
                return val1+val2
            if op == "-":
                return val1-val2
            if op == "*":
                return val1*val2
            if op == "/":
                return int(val1/val2)
        stack = []
        pos = len(tokens)-1
        for i in range(pos, -1, -1):
            token = tokens[i]
            if not stack:
                stack.append(token)
            elif not is_digit(token):
                stack.append(token)
            elif is_digit(stack[-1]):
                stack.append(token)
                while len(stack) > 2 and is_digit(stack[-2]):
                    val1 = stack.pop()
                    val2 = stack.pop()
                    operator = stack.pop()
                    result = perform_operation(val1, val2, operator)
                    stack.append(str(result))
            else:
                stack.append(token)
        if len(stack) == 1:
            return stack[-1]
        val1 = stack.pop()
        val2 = stack.pop()
        operator = stack.pop()
        return perform_operation(val1, val2, operator)