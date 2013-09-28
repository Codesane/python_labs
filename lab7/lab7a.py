# lab7A.py
# @author Felix Ekdahl
# Student-ID: felno295
# http://www.ida.liu.se/~TDDD64/python/la/la7.shtml

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


def normalize_val(val):
	if isinstance(val, list) and len(val) > 1:
		return val[1] if isinstance(val[1], list) else [val[1]]
	else:
		if val == '--':
			return ['--']
		else:
			return [val]

def search(pattern, pdb):
	pA = normalize_val(pattern[0])
	pT = normalize_val(pattern[1])
	pY = normalize_val(pattern[2])

	res = []
	for segment in pdb:
		dA = normalize_val(segment[0])
		dT = normalize_val(segment[1])
		dY = normalize_val(segment[2][1])
		if match(dA, pA) and match(dT, pT) and match(dY, pY):
			res.append(segment)
		
	return res
	
	
print(search(['--', ['titel', ['&', '&']], '--'], db))

