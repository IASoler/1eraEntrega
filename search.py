# -*- coding: utf-8 -*-
#
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class Node:
    def __init__ (self, stat, father, action, cost):
        self.stat   = stat      # Posicio.
        self.father = father    # D'on prove.
        self.action = action    # Accio o accions per arrivar del pare a aqui.
        self.cost   = cost      # El cost acomulatiu.

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "inici:", problem.getStartState ()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    Inicialitzant les variables necessaries
     - stat         Per saber on començem
     - node         Inicialitzar en un node
     - path         Per evitar repetir els passos ja fets
     - nextNode     Saber quin es el seguent element que hem de visitar
    """
    stat = problem.getStartState ()             # Saber on començem.
    if problem.isGoalState (stat): return []    # Assegurar-se que no es la solució
    path = set ( [stat] )                       # Stack, per saber el seguent pas.
    node = Node ( stat, False, [], 0 )          # Generem el primer node.

    # generant els fills
    nextNode = [ Node ( nStat, node, [nAction], nCost ) for nStat, nAction, nCost in problem.getSuccessors (stat)]  # Cami.

    """
    Inicialitzem la busqueda a la casella a trobar
    """
    # Buscarem mentres no haguem trobat el cami i tinguem per on explorar.
    while not problem.isGoalState ( stat ) and nextNode:
        # inicialitzem les variables necessaries
        node = nextNode.pop ()  # el node "seguent"
        stat = node.stat        # l'estat del node en questio

        # nomes li farem cas si no esta registrat
        if not stat in path:
                path.add (stat) # el registrem  per evitar repeticions

                # ja que el fem anar en 2 llocs
                successors = problem.getSuccessors (stat)

                if len (successors) == 2:
                    nextNode += [ Node ( nStat, node.father, node.action + [nAction], node.cost + nCost ) for nStat, nAction, nCost in successors if nStat not in path ]
                else:
                    nextNode += [ Node ( nStat, node, [nAction], node.cost + nCost ) for nStat, nAction, nCost in successors if nStat not in path ]




    # Assegurar-se que estem al final.
    if problem.isGoalState (stat):
        sol = []
        while node:
            #print node.stat, node.action
            sol = node.action + sol
            node = node.father
        return sol
    else:
        print "No ha trobat cap solucio"

    # Afegim el primer element al cami. Per evitar elements repetits.
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
