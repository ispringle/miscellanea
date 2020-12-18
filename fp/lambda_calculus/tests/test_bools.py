import lambda_calculus.combinators as c
import lambda_calculus.bools as b


def test_true():
    assert b.true(1)(2) == 1
    assert b.true(1)(2) == c.K(1)(2)
    assert b.true(1)(2) != b.false(1)(2)
