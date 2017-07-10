def grid():

	a = '+' + ' -' * 4
	b = '+'
	c = '/' + " " * 8
	d = '/'
  
	def print_1():
		print(a, a, b)
    
	def print_2():
		print(c, c, d)
    
	def do_twice(f):
		f()
		f()
    
	def do_four(f):
		do_twice(f)
		do_twice(f)
    
	def print_grid():
		print_1()
		do_four(print_2)
    
	do_twice(print_grid)
	print_1()
