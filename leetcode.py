class Solution():
    def addDigits(self, num):
        num = 38
        sum = num // 10 + num % 10
        result = sum // 10 + sum % 10

        print(result)
