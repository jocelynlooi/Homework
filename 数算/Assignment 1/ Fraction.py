import math
def n(a1, b1, a2, b2):
    numerator = a1 * b2 + a2 * b1
    denominator = b1 * b2
    common_divisor = math.gcd(numerator, denominator)
    return f"{numerator // common_divisor}/{denominator // common_divisor}"
a1, b1, a2, b2 = map(int, input().split())
print(n(a1, b1, a2, b2))