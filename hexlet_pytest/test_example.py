# from hexlet_pytest.example import reverse
#
# def test_reverse():
#     print(111111)
#     assert reverse('hexlet') == 'telxeH'
#
# # def test_reverse_for_empty_string():
# #     assert reverse('') == ''

from functions import get_function

without = get_function()


# BEGIN (write your solution here)
assert without([2, 1, 2, 3, 4], 2, 3) == [1, 4]
assert without([], 2) == []