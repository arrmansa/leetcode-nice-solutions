from math import gcd


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Preprocessing
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        intpart, numerator = divmod(numerator, denominator)
        if numerator == 0:
            return sign + str(intpart)

        com = gcd(numerator, denominator)
        numerator //= com
        denominator //= com

        twopow = 0
        while denominator % 2 == 0:
            twopow += 1
            denominator //= 2
        fivepow = 0
        while denominator % 5 == 0:
            fivepow += 1
            denominator //= 5
        zerocount = max(twopow, fivepow)
        numerator *= (2 ** (zerocount - twopow)) * (5 ** (zerocount - fivepow))

        if denominator == 1:
            nonrepeating = str(numerator)
            nonrepeating = "0" * (zerocount - len(nonrepeating)) + nonrepeating
            return sign + str(intpart) + "." + nonrepeating

        # Attempting to solve for x in A^x mod B = 1, where A = 10 and B = denominator
        ninesneeded = 10 ** len(str(denominator)) - 1
        while ninesneeded % denominator != 0:
            ninesneeded = ninesneeded * 10 + 9

        numerator *= ninesneeded // denominator
        nonrepeating = str(numerator // ninesneeded) if zerocount else ""
        repeating = str(numerator % ninesneeded)
        nonrepeating = "0" * (zerocount - len(nonrepeating)) + nonrepeating
        repeating = "0" * (len(str(ninesneeded)) - len(repeating)) + repeating
        return sign + str(intpart) + "." + nonrepeating + "(" + repeating + ")"
