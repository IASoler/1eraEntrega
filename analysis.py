#!/usr/bin/env python
# -*- coding: utf-8 -*-

# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

"""
1 sol cop a destí
(1/4)^5 (∑_{n=0}^{∞} (1/4)^{2n}) = 1/960

Per arribar M cops
1/960^M

Probabilitat per N intents
1 - (1 - 1/960^M)^N

Amb 50 iteracions hauriem d'arribar 5 cops mínim
1 - (1 - 1/960^5)^50 ≈ 6.132165100348645475611080182211467617907813930083333 × 10^-14

Resultat exageradament petit per a ser possible.
Si desitgem que sigui un 99% amb 5 cops arribar a desti:
N = log (1 - Prob) / log (1 - 1/960^M)
N = log (1 - 0.99) / log (1 - 1/960^5) ≈ 3.75493 × 10^15

Valor que és molt llunya als 50.
Entre una cosa i l'altre, direm que és impossible arribar al resultat desitjat.
"""

def question3():
    answerEpsilon = None
    answerLearningRate = None
    # If not possible, return 'NOT POSSIBLE'
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
