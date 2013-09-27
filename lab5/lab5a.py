# lab5A.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 5A from: http://www.ida.liu.se/~TDDD64/python/la/la5.shtml

variables = {}

def isassignment(p):
	return isinstance(p, list) and len(p) == 3 and p[0] == 'set'

def assignment_variable(p):
	return p[1]

def assignment_expression(p):
	return p[2]

def assign_var(exp):
	variables[assignment_variable(exp)] = get_expression(assignment_expression(exp))


# @returns the Value as an Integer of the expression. Will evaluate the answer recursively.
# Supported operations are "+", "*", "/" and "-"
def get_expression(exp):
	if not isinstance(exp, list):
		return exp if not exp in variables.keys() else variables[exp]
	elif exp[1] == '+':
		return int(get_expression(exp[0])) + int(get_expression(exp[2]))
	elif exp[1] == '*':
		return int(get_expression(exp[0])) * int(get_expression(exp[2]))
	elif exp[1] == '-':
		return int(get_expression(exp[0])) - int(get_expression(exp[2]))
	elif exp[1] == '/':
		return int(get_expression(exp[0])) / int(get_expression(exp[2]))

def read_var(p):
	if isinstance(p, list) and len(p) == 2 and p[0] == 'read':
		variables[p[1]] = input("Enter value for " + p[1] + ": ")

def get_logic(exp):
	if isinstance(exp, list):
		if exp[1] == '<':
			return (int(get_expression(exp[0])) < int(get_expression(exp[2])))
		elif exp[1] == '>':
			return (int(get_expression(exp[0])) > int(get_expression(exp[2])))
		elif exp[1] == '=':
			return (int(get_expression(exp[0])) == int(get_expression(exp[2]))) # I seriously hadto conver them again...

def eval_calc(lang):
	variables['k'] = 0
	if isinstance(lang, list) and lang[0] == 'calc':
		execute(lang[1:])

def execwhile(logic, statements):
	if get_logic(logic):
		execute(statements)
		execwhile(logic, statements)

def print_var(var):
	if isinstance(var, int):
		print(var)
	elif var in variables.keys():
		print(var + " = " + str(variables[var]))
	else:
		print(var)

def execute(statements):
	st = statements[0]
	if st[0] == 'read':
		read_var(st)
	elif st[0] == 'print':
		print_var(st[1])
	elif st[0] == 'set':
		assign_var(st)
	elif st[0] == 'while':
		execwhile(st[1], st[2:])
	elif st[0] == 'read':
		read_var(st[1])
	if len(statements) > 1:
		execute(statements[1:])

calc1 = ['calc', ['set', 'a', '5'], ['print', 'a']]

calc2 = ['calc', ['set', 'x', 7],
		 ['set', 'y', 12],
		 ['set', 'z', ['x', '+', 'y']],
		 ['print', 'z']]

calc3 = ['calc', ['read', 'p1'],
		 ['set', 'p2', 47],
		 ['set', 'p3', 179],
		 ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']],
		 ['print', 'result']]
calc4 = ['calc', ['read', 'n'],
		 ['set', 'sum', 0],
		 ['while', ['n', '>', 0],
		 	['set', 'sum', ['sum', '+', 'n']],
			['set', 'n', ['n', '-', 1]]],
		 ['print', 'sum']]

calc_progs = (calc1, calc2, calc3, calc4)

if __name__ == "__main__":
	k = 1
	for c in calc_progs:
		print("Running Test", k)
		eval_calc(c)
		k += 1
		print("\n")
