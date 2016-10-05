# m = memoria
# boll, per a saber quan sortir
# t[nv], valor temporal, fet anar per saber amb qui comparar-se
def possible ( v ):
	boll = True
	lenv = len ( v ) -2
	while boll:
		boll = False # Cutrada per evitar fer anar goto...
		m = v[-1]
		tv = m
		for i in xrange ( lenv, -1, -1 ):
			tn = v[i]
			if tn < tv:
				boll = True
			print i
		boll = False


