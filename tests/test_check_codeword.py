from lib.check_codeword import *

def test_if_codeword_is_correct():
    result = check_codeword('horse')
    assert  result == 'Correct! Come in.'

def test_check_if_codeword_is_close():
    result = check_codeword('holse')
    assert result == 'Close, but nope'

def test_check_if_codeword_is_wrong():
    result = check_codeword('lololo')
    assert result == 'WRONG!'


# def check_codeword(codeword):
#     if codeword =='horse':
#         return 'Correct! Come in.'
#     elif codeword[0] == 'h' and codeword[-1] == 'e':
#         return 'Close, but nope'
#     else:
#         return 'WRONG!'


