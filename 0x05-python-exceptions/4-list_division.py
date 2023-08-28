#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    k = 0
    new = [0 for k in range(list_length)]
    while k < list_length:
        try:
            new[k] = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            k += 1
    return new
