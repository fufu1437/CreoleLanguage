from ast import For
import re
import sys
from tkinter import N, S

num=0

for i in sys.argv:
    num+=1
    if i=="-f":
        f = open(f"main/{sys.argv[num]}","r")


class Token_state():#state->状态
    def __init__(self) -> None:
        self.StringState  = None #StringState  -> 字符串状态
        self.IntegerState = None #IntegerState -> 整数状态
        self.SyntaxState  = None #SyntaxState  -> 语法状态
        self.FloatState   = None #FloatState   -> 浮点数状态

f.close()