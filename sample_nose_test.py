from nose.tools import assert_equals
from nose.tools import ok_, eq_
from nose.tools import raises


def test_sample_nosetest():
    assert 'HELLO' == 'hello'.upper()

def test_sample_nose1test():
      assert_equals('HELLO','hello'.upper())

def test_using_ok():
    ok_(2+3==5)

def test_using_eq():
    eq_(2+3, 5)

@raises(TypeError)
def test_using_raises():
    eq_(2+'3', 5)