# Hyungchol Jun  # 2014-03-31
# P 8.11

"""
P_8.11 (as .py) use input to get input file name.  Output is printed

write a program that reads in a text file, converts all words to lowercase,
and prints out all words in the file that contain the letter a, the letter b, and so on.
Build a dictionary whose keys are the lowercase letters, and whose values are sets of words containing the given letter

텍스트 파일을 읽어서 모두 소문자로 바꾸는 프로그램을 작성하라.
그리고 a 가 들어가는 단어, b가 들어가는 단어, c가 들어가는 단어 등등을 프린트하라
a가 들어가는 단어는 a키에 b가 들어가는 단어는 b키에 c가 들어가는 단어는 c키에 저장하는 딕셔너리를 만들어라.
"""


def func0401():
	dic = {}

	aset = set()
	bset = set()
	cset = set()
	dset = set()
	eset = set()
	fset = set()
	gset = set()
	hset = set()
	iset = set()
	jset = set()
	kset = set()
	lset = set()
	mset = set()
	nset = set()
	oset = set()
	pset = set()
	qset = set()
	rset = set()
	sset = set()
	tset = set()
	uset = set()
	vset = set()
	wset = set()
	xset = set()
	yset = set()
	zset = set()

	fileName = input("Input file name including file format :")
	file = open("%s" % fileName, "r")

	for i in range(len(file.readlines()) + 1):
		if i == 1:
			file.seek(0)
		fileLine = file.readline()
		fileLine = fileLine.rstrip()
		fileLine = fileLine.lower()
		if "a" in fileLine:
			aset.add(fileLine)
		if "b" in fileLine:
			bset.add(fileLine)
		if "c" in fileLine:
			cset.add(fileLine)
		if "d" in fileLine:
			dset.add(fileLine)
		if "e" in fileLine:
			eset.add(fileLine)
		if "f" in fileLine:
			fset.add(fileLine)
		if "g" in fileLine:
			gset.add(fileLine)
		if "h" in fileLine:
			hset.add(fileLine)
		if "i" in fileLine:
			iset.add(fileLine)
		if "j" in fileLine:
			jset.add(fileLine)
		if "k" in fileLine:
			kset.add(fileLine)
		if "l" in fileLine:
			lset.add(fileLine)
		if "m" in fileLine:
			mset.add(fileLine)
		if "n" in fileLine:
			nset.add(fileLine)
		if "o" in fileLine:
			oset.add(fileLine)
		if "p" in fileLine:
			pset.add(fileLine)
		if "q" in fileLine:
			qset.add(fileLine)
		if "r" in fileLine:
			rset.add(fileLine)
		if "s" in fileLine:
			sset.add(fileLine)
		if "t" in fileLine:
			tset.add(fileLine)
		if "u" in fileLine:
			uset.add(fileLine)
		if "v" in fileLine:
			vset.add(fileLine)
		if "w" in fileLine:
			wset.add(fileLine)
		if "x" in fileLine:
			xset.add(fileLine)
		if "y" in fileLine:
			yset.add(fileLine)
		if "z" in fileLine:
			zset.add(fileLine)
	if aset != set():
		dic["a"] = aset
	if bset != set():
		dic["b"] = bset
	if cset != set():
		dic["c"] = cset
	if dset != set():
		dic["d"] = dset
	if eset != set():
		dic["e"] = eset
	if fset != set():
		dic["f"] = fset
	if gset != set():
		dic["g"] = gset
	if hset != set():
		dic["h"] = hset
	if iset != set():
		dic["i"] = iset
	if jset != set():
		dic["j"] = jset
	if kset != set():
		dic["k"] = kset
	if lset != set():
		dic["l"] = lset
	if mset != set():
		dic["m"] = mset
	if nset != set():
		dic["n"] = nset
	if oset != set():
		dic["o"] = oset
	if pset != set():
		dic["p"] = pset
	if qset != set():
		dic["q"] = qset
	if rset != set():
		dic["r"] = rset
	if sset != set():
		dic["s"] = sset
	if tset != set():
		dic["t"] = tset
	if uset != set():
		dic["u"] = uset
	if vset != set():
		dic["v"] = vset
	if wset != set():
		dic["w"] = wset
	if xset != set():
		dic["x"] = xset
	if yset != set():
		dic["y"] = yset
	if zset != set():
		dic["z"] = zset

	print(dic)
