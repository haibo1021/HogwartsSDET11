import allure
import pytest

from unit.test_demo import TestDemo


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def setup_module():
    print("setup module")


def setup_function():
    print("setup function")


@pytest.mark.abc
def test_a():
    print(eval("1+2"))
    assert 123 == 123
    allure.attach.file(r'C:\Users\Jason\Desktop\sc_20200313.png', attachment_type=allure.attachment_type.PNG)


class TestClass:
    def setup(self):
        print("setup")

    @classmethod
    def setup_class(cls):
        print("setup class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    # def test_x(self):
    #     demo = TestDemo()
    #     demo.fun_2()

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
