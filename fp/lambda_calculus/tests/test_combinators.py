import lambda_calculus.combinators as f


def test_I():
    assert f.I(f.I) == f.I
    assert f.I(1) == 1
    assert f.I(1) != 2


def test_M():
    assert f.M(f.I) == f.I
    assert f.M(f.I) != f.K


def test_K():
    assert f.K(1)(2) == 1
    assert f.K(1)(2) != 2
    assert f.K(f.I)(1)(2) == 2


def test_KI():
    assert f.KI(1)(2) == 2
    assert f.KI(1)(2) != 1


def test_C():
    assert f.C(f.K)(1)(2) == 2
    assert f.C(f.K)(1)(2) != 1
