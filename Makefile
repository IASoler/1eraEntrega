p20: multiAgents.py
	python2.7 pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
p21: multiAgents.py
	python2.7 pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
p22: multiAgents.py
	python2.7 pacman.py -p MinimaxAgent -l smallClassic -a depth=3
p2: multiAgents.py
	python2.7 autograder.py -q q2
p2n: multiAgents.py
	python2.7 autograder.py -q q2 --no-graphics
