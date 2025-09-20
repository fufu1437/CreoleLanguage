import re
# import sys
f = open("main/creole.crl","r")

# num = 0
# for i in sys.argv:
#     num+=1
#     if i=="-f":


# class Token_state():#state->状态
#     def __init__(self) -> None:
#         self.StringState  = None #StringState  -> 字符串状态
#         self.IntegerState = None #IntegerState -> 整数状态
#         self.SyntaxState  = None #SyntaxState  -> 语法状态
#         self.FloatState   = None #FloatState   -> 浮点数状态


def token(expression):
    token_pattern = r"\bprint\b"
    token = re.findall(token_pattern, expression)
    return token



str1 = "print('Hello, World!')"

tokens = token(str1)

print(tokens)

f.close()