#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                if b == 0:
                    raise ZeroDivisionError
                result.append(a / b)
            else:
                raise TypeError
        except ZeroDivisionError as e:
            print("division by 0")
            result.append(0)
        except TypeError as e:
            print("wrong type")
            result.append(0)
        except IndexError as e:
            print("out of range")
            result.append(0)
        finally:
            pass
        return result
