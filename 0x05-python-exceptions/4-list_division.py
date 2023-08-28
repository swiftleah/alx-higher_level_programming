#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("wrong type")

            division_result = 0
            if b != 0:
                division_result = a / b

            result.append(division_result)
        except ZeroDivisionError as zde:
            print(zde)
            result.append(0)
        except TypeError as te:
            print(te)
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
