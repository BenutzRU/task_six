import pytest
def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)

def testonetask():
    assert average_num([1, 2]) == 1.5
    assert average_num([0.5, 1.5, 2.5]) == 1.5
    assert average_num([1]) == 1.0
    assert average_num([-1]) == -1.0
    assert average_num([]) == "Error" # или assert average_num([]) == 0.0 ?
    assert average_num([1, 'b',2, 4]) == "Error"
    assert average_num(['a', 'b', 'c']) == "Error"