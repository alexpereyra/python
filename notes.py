Data & Operations

Data types - numbers, strings, lists
Operations with data types
strings - numbers/letters
can use single quote ' or double quote "
start on more than one line ' ' ' or '" " "
\n new line
'A single\\backslash
ctrl+a beginning of a line or ctrl+e end of line
lists = ["string", "string"] or lists = ["num", "num"]
variable names must start with a letter, numbers or _
variables can be any data type and can change (dynamic typing)
each data type have constructers  used for changing data type to another
cannot concatenate string and number
str() int() float(3.5) 
operators manipulate data   + - * /   **
"na " * 3 + "batman    'na na na batman'
[ "na" ] * 3 + [ "batman"]    [ 'na', 'na', 'na', 'batman' ] 

Comparing & Deciding

boolean (data type) - true false
string/num comparison ==  <  >  !=   >=   <=
comparisons follow dictionary order
in operator "pine" in "pineapple"    5 in [  1, 2, 3, 4, 5 ]
strings/lists are "iterable" therefore in cannot use "int" data type
# comment
if statement decision
block several lines of code by using :
if/elif/else
boolean operaters - and, or, not

Slicing, Splitting, Joining, & Iterating

Slicing [ 4:9 ]   [ 4: ]   
start at beginning to end and take every other [ ::2 ]
start at 4 and to the end and get every other [ 4 : -1 : 2 ]
list_colors = [ 'red', 'blue', 'green', 'white']  lists = [ 0 ] = red
list_colors [ 1 : ] = 'black'   list_colors = [ 'red', 'b' , 'l' , 'a' , 'c' , 'k'  ]
list_colors [ 1 : ] = [ 'black' ]   list_colors = [ 'red' , 'black' ]
list_colors [ 1 : ] = [ 'black' ] * 2   list_colors = [ 'red' , 'black' , 'black' ]
list_colors [ 1 : 2 ] = [ 'black' ]   list_colors = c
list_colors [ 1 : 2 ] = [ 'black'] * 2   list_colors = [ 'red' , 'black' , 'black' , 'green' , 'white' ]
sentence  = 'the rabbit ran past the turtle'
python strings are immutable and can't be changed directly
sentence [ 4 : 10 ] = 'rabbit'
sentence [ 0 : 4 ] + 'dog' + sentence [ 10 : ]  sentence = 'the dog ran past the turtle'
output is changed here, but sentence variable never changes
printing out sentence is still sentence = 'the rabbit ran past the turtle'

sentence.split( ' ' )
sentence = ['the', 'rabbit', 'ran', 'past', 'the', 'turtle']
sentence.split( 'r' )
sentence = ['the ', 'abbit ', 'an past the tu', 'tle']
ran_num = "15:24:89:1:500:12"
ran_num.split(':')
['15', '24', '89', '1', '500', '12']
ctrl+r searched history commands

joining is the inverse of splitting
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
" - ".join(colors)
'Red - Orange - Yellow - Green - Blue - Purple'
" - ".join(colors).split(' - ')
['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']

for & while are loops

for color in colors: print("is " + color + " your favorite?")
is Red your favorite?
is Orange your favorite?
is Yellow your favorite?
is Green your favorite?
is Blue your favorite?
is Purple your favorite?

for number in [ 1, 2, 3, 4, 5 ]:
    double = number * 2
	print("Twice " + str(number) + " is " + str(double))
	
Twice 1 is 2
Twice 2 is 4
Twice 3 is 6
Twice 4 is 8
Twice 5 is 10

loops can iterate over lists
modifiers = ["Dark", "Light", "Brown"]
for c in colors:
     ...:     for m in modifiers:
     ...:         print(m + " " + c)

Dark Red
Light Red
Brown Red
Dark Orange
Light Orange
Brown Orange
Dark Yellow
Light Yellow
Brown Yellow
Dark Green
Light Green
Brown Green
Dark Blue
Light Blue
Brown Blue
Dark Purple
Light Purple
Brown Purple

loops can iterate over strings
for v in "aeiou":
    print("My favorite vowel is " + v)

My favorite vowel is a
My favorite vowel is e
My favorite vowel is i
My favorite vowel is o
My favorite vowel is u

while use test to make decisions

while countdown >= 0:
    print(str(countdown))
    countdown -= 1
	
10
9
8
7
6
5
4
3
2
1
0

countdown is now = -1

empty lists count as false, meaning... name [] is false name = ['alex'] = true
function that comes with lists .pop which removes last element
names = ["Daniel", "James", "Peter", "Sean"]
names.pop()
'Sean'
['Daniel', 'James', 'Peter']
names.pop()
'Peter'
['Daniel', 'James']

while names:
    print("welcome, Mr. " + names.pop())

welcome, Mr. Sean
welcome, Mr. Peter
welcome, Mr. James
welcome, Mr. Daniel

opposite of .pop is .append for adding to a list and/or strings
names.append("Albert")
['Daniel', 'James', 'Peter', 'Sean', 'Albert']

Functions reusable block of code that can be assigned a name and used when needed
built in functions examples  
bool(alex) is true bool() is false print() len('alex') is 4 str() float(6.23) abs() - absolute value bin() binary representation of number
round() sum() max() min() range() sorted() reverse()
function(arguments) = return value(s)

function_practice = ("jsdfkjhanwuencrauwyeruyweryaluwylcusdcmliu")
''.join(reversed(sorted(function_practice)))
'yyyywwwwuuuuuussrrrnnmlllkjjihfeeeddcccaaa'

''.join(reversed(sorted([ "this", "is", "feaking", "awesome"])))
'thisisfeakingawesome'
'thisisfeakingawesome'.split(" ")

a_string = "apples, oranges, and bananas"
a_string.find('an')
10
a_string[10:]
'anges, and bananas'

format nice way of concatenating strings
"hello, {0}, and welcome to {1}".format("Alex", "Greg")
'hello, Alex, and welcome to Greg'
"there are " + str(5) + " items in your carts.".format(5) or "there are {0} items in your carts.".format(5)
'there are 5 items in your carts.'

In [9]: a_list = "this is a long string".split(" ")

In [10]: a_list
Out[10]: ['this', 'is', 'a', 'long', 'string']

In [11]: a_list.sort()

In [12]: a_list
Out[12]: ['a', 'is', 'long', 'string', 'this']

In [13]: a_list.reverse()

In [14]: a_list
Out[14]: ['this', 'string', 'long', 'is', 'a']

In [15]: a_list.remove('long')

In [16]: a_list
Out[16]: ['this', 'string', 'is', 'a']

In [17]: b_list = a_list

In [18]: a_list
Out[18]: ['this', 'string', 'is', 'a']

In [19]: b_list
Out[19]: ['this', 'string', 'is', 'a']

In [20]: b_list.pop()
Out[20]: 'a'

In [21]: a_list
Out[21]: ['this', 'string', 'is']

#example above is b_list pointing to data in a_list so modifications are made to both lists functions
#use copy function to modify without affecting other functions

In [26]: c_list = a_list.copy()

In [27]: c_list.append('randoms words')

In [28]: a_list
Out[28]: ['this', 'string']

In [29]: b_list
Out[29]: ['this', 'string']

In [30]: c_list
Out[30]: ['this', 'string', 'randoms words']


#parameters are when variables are inside the function definition and arguments on the outside
In [33]: def greet(name): print("hello, {0}".format(name))  <---parameter
In [34]: greet("Greg") <---argument
hello, Greg

In [39]: def product(numbers):
    ...:     p = 1
    ...:     for n in numbers:
    ...:         p *= n
    ...:     return p
    ...:
    ...:

In [40]: product([1, 2, 3, 4])
Out[40]: 24

In [44]: def combine_and_sort(first, second):
    ...:     return sorted((first + second))
    ...:
    ...:

In [45]: combine_and_sort([1, 3, 5,], [2, 4, 6])
Out[45]: [1, 2, 3, 4, 5, 6]

In [49]: def combine_and_sort(first, second, third):
    ...:     return sorted((first + second + third))
    ...:
    ...:

In [50]: combine_and_sort([1, 3, 5,], [2, 4, 6], [7, 9, 11])
Out[50]: [1, 2, 3, 4, 5, 6, 7, 9, 11]

In [51]: def combine_and_sort(first, second, third):
    ...:     return sorted((first + second))
    ...:
    ...:

In [52]: combine_and_sort([1, 3, 5,], [2, 4, 6], [7, 9, 11])
Out[52]: [1, 2, 3, 4, 5, 6]

In [53]: def combine_and_sort(first, second, third):
    ...:     return sorted((first + third))
    ...:
    ...:

In [54]: combine_and_sort([1, 3, 5,], [2, 4, 6], [7, 9, 11])
Out[54]: [1, 3, 5, 7, 9, 11]

#some data types are mutable...lists being the only mutable type worked on so far
#remember when you point function to function...you are just pointing to data

In [55]: def naughty_product(numbers):
    ...:     p = 1
    ...:     while numbers:
    ...:         p *= numbers.pop()
    ...:     return p
    ...:
    ...:

In [56]: naughty_product([1, 2, 3, 4])
Out[56]: 24

In [57]: nums = [1, 2, 3, 4]
In [59]: naughty_product(nums)
Out[59]: 24

In [60]: nums
Out[60]: []

#nums list is empty because of .pop function
sorted() vs sort()

In [61]: sorted([ 5, 8, 4, -2])
Out[61]: [-2, 4, 5, 8]

In [62]: nums = [ 5, 8, 4, -2]

In [63]: sorted(nums)
Out[63]: [-2, 4, 5, 8]

In [64]: nums
Out[64]: [5, 8, 4, -2]

In [65]: nums.sort()

In [66]: nums
Out[66]: [-2, 4, 5, 8]























