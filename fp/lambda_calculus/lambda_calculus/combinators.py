# λa.a
def I(a): return a  # noqa: E741, E743


# λa.aa
def M(a): return a(a)


# λab.a
def K(a): return lambda b: a


# λab.b
# We can also do `KI = K(I)`
# We can also do `KI = C(K)`
def KI(a): return lambda b: b


# λfab.fba
def C(f): return lambda a: lambda b: f(b)(a)
