from typing import Self

class HPfloat:
    def __init__(self, int1: int, decimal: int, *, digits: int = 0) -> None:
        """
        int : 整数位
        decimal : 小数位
        digits : 小数点后"0"的个数, 默认 0
        例 : HPfloat(1, 2, Digits = 2) -> 1.002
        """
        self.Int     = abs(int1)     #整数位
        self.Decimal = abs(decimal) #小数位
        self.Digits  = abs(digits)

    # def out(self)->str:
    #     """
    #     Returns the stored float, In the form of a string
    #     返回存储的浮点数，以字符串的形式
    #     """
    #     return f"{self.Int}.{self.Decimal}"





    def __add__(self,b:Self)-> 'HPfloat':
        """
        Add the two HPfloat numbers together and return the HPfloat\n
        将两个HPfloat数相加, 返回HPfloat
        """
        a_digits = self.Digits
        b_digits = b.Digits
        accuracy = 1 if max(b_digits,a_digits) == 0 else max(b_digits,a_digits)
        accuracy_len = len(str(accuracy))
        a_decimal = self.Decimal * 10 ** accuracy
        b_decimal = b.Decimal * 10 ** accuracy
        a_b_int_and = self.Int + b.Int
        a_len = len(str(a_decimal))
        b_len = len(str(b_decimal))
        a_b_decimal_and = (a_decimal * (10 ** (b_len - a_digits))) + (b_decimal * (10 ** (a_len - b_digits)))
        while True:
            if a_b_decimal_and % 10 ==0:
                a_b_decimal_and = int(str(a_b_decimal_and)[:-1])
            else:
                break
        a_b_decimal_and_len = len(str(a_b_decimal_and))
        if a_b_decimal_and_len >= (a_len-accuracy_len + b_len-accuracy_len) :
            a_b_int_and = a_b_int_and + 1
            a_b_decimal_and = str(a_b_decimal_and)[1:]
        
        digits=max(a_digits,b_digits)+max(len(str(self.Decimal)),len(str(b.Decimal)))
        return HPfloat(a_b_int_and, int(a_b_decimal_and),digits=digits-len(str(a_b_decimal_and)))



    def __sub__(self,b:Self)-> 'HPfloat':


        
        return HPfloat(0,0)
    

    def __str__(self) -> str:
        return f"{self.Int}.{self.Digits*"0"}{self.Decimal}"
    
    



if __name__ == "__main__":
    float1 = HPfloat(1,91,digits=2)
    float2 = HPfloat(3,1,digits=1)

    print(float1+float2)