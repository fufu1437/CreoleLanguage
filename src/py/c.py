import re
# import sys
f = open("main/creole.crl","r")

class TokenType:
    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    EOF = "EOF"
    LCurly = "LCurly"  # {
    RCurly = "RCurly"  # }

class Token:
    def __init__(self, text, value = None) -> None:
        self.text = text
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.text}, {self.value})"
    
    def __repr__(self) -> str:
        return self.__str__()

class Lexer:
    def __init__(self,text) -> None:
        self.Token = Token
        self.Tokens = [
            (re.search(r"\s+",text), None),
            (re.search(r"\{",text), TokenType.LCurly),
            (re.search(r"\}",text), TokenType.RCurly),
            (re.search(r"\(",text), TokenType.LPAREN),
            (re.search(r"\)",text), TokenType.RPAREN),
            (re.search(r"\+",text), TokenType.PLUS),
            (re.search(r"-",text), TokenType.MINUS),
            (re.search(r"\*",text), TokenType.MULTIPLY),
            (re.search(r"/",text), TokenType.DIVIDE),
            (re.search(r"\d+\.\d+",text), TokenType.FLOAT),
            (re.search(r"\d+",text), TokenType.INTEGER),
            (re.search(r"[a-zA-Z_][a-zA-Z0-9_]*",text), TokenType.STRING)
            ]

a = Lexer("print da").Tokens
print(a)
f.close()