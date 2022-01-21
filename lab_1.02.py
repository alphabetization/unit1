'''
Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2               9                                  n
b   2/3                     0.6                                 n
c   2.0 * 1.5               3.0                                n
d   (2 + 3) * 10            50                                  n
e   5.0 // 2                2.0                                n
f   5.0 % 2                 1.0                                 n

Section 2
    Input                   Output                          Did it do something unexpected?
a   a                       error                           y
b   'a'                     'a'                              y

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'                 'a + b'                             n
b   'a' + 'b'               'ab'                               n

Section 4
    Input                   Output                          Did it do something unexpected?
a   'a' * 'b'               error                               y
b   'a' * 2                 aa                                 y

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                  20
b   .5 * 2                      float                       1
c   10/2                        integer                     5
d   10%2                        float                       5?
e   2 ** 3                      integer                     6 or 12
f   (2+5)*3                     integer                     21
g   2 + 5 * 3                   integer                     17
h   'ab' + '12' + '3'           string                      'ab123'
i   x                           string
j   "ab" + "cd"
k   'abc' * 2
l   '1'*2 + '2' * 3
m   1 * 2 + '3' * 2
n   'A' ** 2
o   'bc' % 2
p   'bc' / 2

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''