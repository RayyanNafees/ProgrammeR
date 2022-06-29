from functools import wraps

condition = True

decor = lambda func: lambda *args,**kwargs: func(*args,**kwargs) if condition else print('err')

@decor
def foo():
	print('SUCCESS')
	
foo()