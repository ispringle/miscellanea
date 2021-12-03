i=:"."0>cutopen 1!:1<'input.txt' NB. Input into a 2D array of ints
C=:(+/>:#-+/) NB. The common fn, takes a list of binaries, returns one binary # w/ most common bits from each
I=:-. NB. Invert a binary number
T=:#. NB. Binary to Decimal
p1 =: (C i) *&T (I C i) NB. Convert both to decimal and get product

CI =: 1 : 0  NB. Create function Common-iterator which takes y and iterates over it
	v =. (#~ (u (>: (# y) - ]) x { +/ y) = x&{"1) y
	(>:x) (T@:]`(u CI)@.(1 < # v)) v
)

p2 =: 0 (] CI *I CI) i
p1;p2
