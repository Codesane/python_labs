# lab4D.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 4D from: http://www.ida.liu.se/~TDDD64/python/la/la4.shtml

################################################
def is_empty_tree(tree):
	return isinstance(tree, list) and not tree

def is_leaf(tree):
	return isinstance(tree, int)

def create_tree(left, key, right):
	return [left, key, right]

def left_subtree(tree):
	return tree[0]

def right_subtree(tree):
	return tree[2]

def get_key(tree):
	return tree[1]
###


def traverse(tree, fn_inner, fn_leaf, fn_empty):
	if is_empty_tree(tree):
		return fn_empty()
	elif is_leaf(tree):
		return fn_leaf(tree)
	else:
		return fn_inner(get_key(tree), traverse(left_subtree(tree), fn_inner, fn_leaf, fn_empty),
			traverse(right_subtree(tree), fn_inner, fn_leaf, fn_empty))



def implode_all(key, lv, rv):
	return [key] + lv + rv

def implode_greatest(key, lv, rv):
	#@return since we come from the very bottom of the tree, we can simply see
	# which of the trees is the greater, hence we return the tree which has the longest "root"
	# and we continue doing so till we reach the top of the tree.
	return [key] + lv if len(lv) > len(rv) else [key] + rv

def null_fn():
	return []

def leaf_return(x):
	return [x]

def key_exists(key, tree):
	return key in traverse(tree, implode_all, leaf_return, null_fn)

def tree_size(tree):
	return len(traverse(tree, implode_all, leaf_return, null_fn))

def get_depth(tree):
	return len(traverse(tree, implode_greatest, leaf_return, null_fn))

print("-- Key Exist Case --")
print(key_exists(6, [6, 7, 8]))
print(key_exists(2, [6, 7, [[2, 3, 4], 0, []]]))
# ----------------

print("-- Tree Size Case --")
print(tree_size([2, 7, []]))
print(tree_size([]))
print(tree_size([[1, 2, []], 4, [[], 5, 6]]))
# ----------------

print("-- Depth Case --")
print(get_depth(9))
print(get_depth([1, 5, [10, 7, 14]]))

print("End Test Cases")

