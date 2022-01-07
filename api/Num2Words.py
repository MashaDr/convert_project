import sys

"""
Input: number = 1354789
Result: One Million Three Hundred Fifty Four Thousand Seven Hundred Eighty Nine

Above thousand, process in chunks of three
Under thousand:
    Case 1: Under twenty
    Case 2: Tens + Case 1
    Case 3: Digits + Hundred + Case 2
"""


class Num2Words:
    underTwenty = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                   "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    bigs = [[], "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion"]

    @staticmethod
    def to_words(num: int) -> list:
        """
         A helper recursion function that takes a number less than 1000 and convert to a list of words.
         @param num: A number less than 1000
         @return: A list of words.
        """
        if num == 0:
            return []
        elif num < 20:
            return [Num2Words.underTwenty[num - 1]]
        elif num < 100:
            return [Num2Words.tens[num // 10 - 2]] + Num2Words.to_words(num % 10)
        else:
            return [Num2Words.underTwenty[num // 100 - 1]] + ['Hundred'] + Num2Words.to_words(num % 100)

    @staticmethod
    def convert(num: int) -> str:
        """
        Convert a non-negative integer num to its English words representation.
        @param num: A non-negative integer. Max number = 9223372036854775807
        @return: A string with English words representing a number
        """
        if type(num) is not int:
            return f"Error: 'Number' can only be integer not {type(num)}"
        if num == 0:
            return "Zero"
        if num < 0:
            return "Error: a number can be positive"
        if num > sys.maxsize:
            return f"Error: Max size of int can be {sys.maxsize}"

        result = list()
        for i in range(len(Num2Words.bigs)):
            if num % 1000 != 0:
                tmp = [Num2Words.bigs[i]] + result if i != 0 else result
                result = Num2Words.to_words(num % 1000) + tmp
            num //= 1000
        return ' '.join(result)


if __name__ == "__main__":
    try:
        print(Num2Words.convert(11451))
        print(Num2Words.convert(100001102))
        print(Num2Words.convert(0))
    except Exception as e:
        print(e)
