print "Hello World"
print "first python program"
print "This example is for the new book which i'm going to read this weekend"

#function example
# def fun_ex(arg1, arg2='world', *args, *kwargs):
# 	print arg1, arg2, *args, *kwargs

def fun_1(*args):
	print args, type(args)

fun_1(123)
fun_1("123")
fun_1((1, 2, 3))
fun_1([1, 2, 3])
fun_1({1, 2, 3})
