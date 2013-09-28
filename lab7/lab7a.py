# Encoding: ISO-8859-1

db = [
 [['författare', ['john', 'zelle']], 
  ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], 
  ['år', 2010]], 
 [['författare', ['armen', 'asratian']], 
  ['titel', ['diskret', 'matematik']], 
  ['år', 2012]], 
 [['författare', ['j', 'glenn', 'brookshear']], 
  ['titel', ['computer', 'science', 'an', 'overview']], 
  ['år', 2011]], 
 [['författare', ['john', 'zelle']], 
  ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], 
  ['år', 2009]], 
 [['författare', ['anders', 'haraldsson']], 
  ['titel', ['programmering', 'i', 'lisp']], 
  ['år', 1993]]
]

		
def match(seq, pattern):
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False



def search(expr, pdb):
	if expr[0] == '--':
		pass
	elif isinstance(expr[0], list):
		


#search(['titel', ['&', '&']], '--'], db)

