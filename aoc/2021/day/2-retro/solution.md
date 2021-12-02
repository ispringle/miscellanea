So each line in today's input is a word, either "forward", "up" or "down"
followed by a an integer.

~~~
:parse-file
~~~

Retroforth has a way of opening a file as a stream
and iterating over the lines of the file, so we will use that. To do so we have
to create a word (function) because the stream won't accept an anonymous
function definition in the input (I tried...).

~~~
  ASCII:SPACE s:tokenize [ ] a:for-each
~~~

To parse each line we need to create pairs of `(str int)`. Retroforth has a
cool string utility in the `s:` namespace that will create an array of strings.
So we need to split on the whitespace. The string part of the line goes onto
the stack followed by the string that needs to be a number (this happens in
push-tokens).

```
"123"
"forward"
```

A note: `s:tokenize` takes a string and a char `( sc -- a)`, the string is
getting applied to the stack by `file:for-each-line` further down.

~~~
s:to-number swap
~~~

We then call `s:to-number` and convert the `"123"` into an integer and then we
swap the two items at the top of the stack, because later when we match our
values we want to read the kind of value (forward, up, down) before we read the
actual value.

```
"forward"
#123
```

~~~
  'forward [ + ] s:case
~~~

Next we figure out what the string really means to us. "forward" means we just
add to the value on the stack for "forward" (did I mention that we also are
keeping the bottom two values on the stack as our two forward and depth values?
:) ).

~~~
  'down    [ swap [ + ] dip ] s:case
  'up      [ swap [ - ] dip ] s:case
  drop-pair ;
~~~

If it's "up" or "down" we need to `swap` `(nm -- mn)` the values because
this is the stack

```
"string" <--- this just got popped so it's not on the stack, adding for clarity only
#new-value
#forward-value
#depth-value
```

After we bring up the right value we add or subtract (add for "down" and
subtract for "up") as a quotation (like a lambda sorta). Then we call `dip`
which pops a value, runs the quotation and then pushes the value back to the
stack; `(nq -- n)`)

~~~
#0 #0 'input.txt [ parse-file ] file:for-each-line
~~~

Initialize the stack with two zeros -- the first for depth and the second for
forward-ness? -- push the file name to the stack along with the previously
created word as a quotation. Both the string and quotation are then consumed by
`file:for-each-line`.

~~~
* n:put nl
~~~

Finally, we  multiple the two values on the stack by each other and then pop
them off the stack, and add a newline for neatness!

The second part is almost the same as the first, we just have to change what we
do with the keywords. I'll only highlight the differences.

~~~
:o [ swap [ [ dup ] dip swap ] dip swap ] dip swap ;
~~~

First, I wrote a little utility word to reorder the stack. This takes:

```
a
b
c
d
```

And arranges it thusly:


```
a
c
b
d
a
```

~~~
:parse-file
  ASCII:SPACE s:tokenize [ ] a:for-each s:to-number swap
  'forward [ [ + ] [ o * + swap ] bi ] s:case
~~~

When we see "forward" we now do something a little different. Instead of just adding, we have to add the forward value to our forward position as well as updating our depth by multiplying the forward value by the new _aim_ value. To do this we need to get the "aim" value, which is the bottom of the stack, bring it to the top and multiply it by the current forward value. Then we need to add that new value to our depth. Finally we swap our depth back to the second value on the stack. To do both things -- adding forward's value to our forward on the stack and multiply it by our depth -- we have to use the `bi` word which takes `x` and runs it against tqo quotations `( xqq -- ? )`.

~~~
  'down [ [ rot ] dip + rot rot ] s:case
  'up [ [ rot ] dip - rot rot ] s:case
  drop-pair ;
~~~

Same idea as before, but the depth value now changes our "aim" and we also have to shuffle the stack around to get at our aim element.

~~~
#0 #0 #0 'input.txt [ parse-file ] file:for-each-line
* n:put nl
~~~

Nothing new here either!
