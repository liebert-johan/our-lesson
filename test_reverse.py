# hello
import pytest
from yandex_testing_lesson import reverse


def test_empty():
    assert reverse('') == ''


def test_one_symbol():
    assert reverse('a') == 'a'


def test_polindrome_word():
    assert reverse('asa') == 'asa'


def test_polindrome_stroke():
    assert reverse('asa asa asa') == 'asa asa asa'


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)


def test_list():
    with pytest.raises(TypeError):
        reverse(reverse(['1', '2', '1']))