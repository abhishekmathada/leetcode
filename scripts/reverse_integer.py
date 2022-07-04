class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        if x[0] == '-':
            x = '-' + x[:0:-1]
        else:
            x = x[::-1]

        if int(x) not in range(-2 ** 31, 2 ** 31):
            return 0
        else:
            return int(x)
