# def is short for define
def hello(to="world"): # world is default value here,  simple parameter used name to
	print ("Hello, ", to)

hello() # uses the default parameter of hello func

name = input("What's your name?")
hello(name) # name will copied and passed to hello(HERE)

