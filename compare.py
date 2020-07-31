def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(max_num(300, 301, 302))


def equal_num(num4, num5, num6):
    if num4 == num5 and num4 == num6 and num5 == num6:
        return num4
    else:
        return False


print(equal_num(4, 4, 90))


def not_equal_num(num7, num8, num9):
    if num7 != num8 and num7 != num9 and num8 != num9:
        return True
    else:
        return num7, num8, num9


print(not_equal_num(4, 4, 4))
