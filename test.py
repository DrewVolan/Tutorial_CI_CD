from function import is_even

def test(number, expected):
    res = is_even(number)
    assert res == expected

test(2, True)
test(3, False)
test(4, False) # Ошибка специально