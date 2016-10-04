"""
((5, 11), ((1, 1), (28, 1)))
((5, 11), ((1, 1), (28, 1)))
((6, 12), ((1, 1), (28, 1)))
((5, 7), ((1, 12), (28, 1)))
((6, 6), ((1, 12), (28, 1)))
((1, 7), ((1, 12), (28, 1)))
((8, 4), ((1, 12), (28, 1)))
((15, 9), ((1, 1), (28, 12)))
((18, 12), ((1, 1),))
((16, 2), ((1, 1), (28, 12)))
((11, 11), ((1, 1), (28, 1)))
((11, 9), ((1, 1), (28, 1)))
((10, 10), ((1, 1), (28, 1)))
((24, 6), ((1, 1),))
((22, 4), ((1, 1),))
((18, 6), ((1, 1), (28, 1)))
((24, 12), ((28, 12),))
((28, 12), ())
((24, 8), ((28, 12),))
((22, 6), ((28, 12),))
((22, 2), ((28, 12),))
((18, 12), ((28, 1),))
((28, 2), ((28, 1),))
((26, 4), ((28, 1),))
((12, 6), ((1, 12), (28, 12)))
((10, 6), ((1, 12), (28, 12)))
((16, 10), ((1, 12),))
https://technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/
"""

def manhatan ( x, y ): return abs ( x[0] - y[0] ) + abs ( x[1] - y[1] )

def memorize (fn, *args):
	memo = dict ()
	if not memo.has_key ( args ):
		t = fn ( args )
		memo[args] = t
		return t
	return memo[args]
	

#@memo
def cost ( stat, descobrir ):
	if not descobrir: return 0
"""
	minim = 0

	previ = descobrir.pop ()
	val = heu
"""

def fibR ( n ):
	if n!=1 and n!=2:
		return fibR ( n-1 ) + fibR ( n-2 )
	return 1

#
#fibM = memorize ( fibR, 5 )
#

class Memoize:
	def __init__ (self, fn):
		self.fn = fn
		self.memo = dict ()

	def __call__ (self, *args):
		args = args[0]
		if not self.memo.has_key ( args ):
			print self.memo, self.memo.has_key ( args )
			t = self.fn ( args )
			self.memo[args] = t
			return t
		print "yupi"
		return self.memo[args]

@Memoize
def fibR2 ( n ):
	if n!=1 and n!=2:
		return fibR ( n-1 ) + fibR ( n-2 )
	return 1
