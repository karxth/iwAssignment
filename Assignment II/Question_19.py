"""Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid"""
class Validity(object):
    def __init__(self, str1):
        self.str1 = str1

    def check(self):
        stack = []
        parentheses_char = {"(": ")", "{": "}", "[": "]"}
        for p in self.str1:
            if p in parentheses_char:
                stack.append(p)
            elif len(stack) == 0 or parentheses_char[stack.pop()] != p:
                return f'{self.str1} are invalid'
        return f'{self.str1} are valid'


value1 = input("Enter: ")
obj1 = Validity(value1)
print(obj1.check())
