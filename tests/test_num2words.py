import pytest
from api.Num2Words import Num2Words


def test_sanity():
    # should always pass
    assert True

@pytest.mark.parametrize("number, expected",
                         [
                             (1354789, 'One Million Three Hundred Fifty Four Thousand Seven Hundred Eighty Nine'),
                             (0, 'Zero'),
                             (111, 'One Hundred Eleven'),
                             (100001101, 'One Hundred Million One Thousand One Hundred One'),
                             (1354789, 'One Million Three Hundred Fifty Four Thousand Seven Hundred Eighty Nine'),
                             (485, 'Four Hundred Eighty Five'),
                             (-1, 'Error: a number can be positive'),
                             ('TEST', "Error: 'Number' can only be integer not <class 'str'>"),
                             (9223372036854775807, 'Nine Quintillion Two Hundred Twenty Three Quadrillion Three Hundred Seventy Two Trillion Thirty Six Billion Eight Hundred Fifty Four Million Seven Hundred Seventy Five Thousand Eight Hundred Seven'),
                             (9223372036854775899,'Error: Max size of int can be 9223372036854775807')
                         ])
def test_convert(number, expected):
    """Test the convert function
        Convert takes the following parameters:
        param: number [int]
        returns: str
    """
    assert Num2Words.convert(number) == expected
