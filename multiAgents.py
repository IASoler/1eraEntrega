# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Per entendrem, heightNumber es un valor gran.
        width, height = newFood.width, newFood.height
        heightNumber = width * height

        # Iniciem el valor que retornarem.
        score = 0

        # L'accio parats no ens agrada.
        if action == 'Stop':
            score -= 100

        # Afaborim el menjar mes proper.
        nF = newFood.asList()
        minFood = 10 * heightNumber
        for i in nF:
            a = util.manhattanDistance ( newPos, i)
            if a < minFood: minFood = a

        # Tot i que si no ha trobat menjar (finalitzat), puntuarem molt a fabor.
        if minFood == 10 * heightNumber: minFood = - 10 * heightNumber

        # Tenim en compte el menjar i el cas especial del final.
        score -= minFood

        n = util.manhattanDistance (newPos, newGhostStates[0].getPosition () )
        # Vigilem la distancia del fantasma.
        if n < 5:
            score += 10* util.manhattanDistance (newPos, newGhostStates[0].getPosition () ) - 1000*heightNumber
        # Sino, tindrem en compte el nombre restant de menjar.
        else:
            score += heightNumber - 100*len (nF)

        # Retornem el score.
        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # Descobrim la profunditat.
        depth = self.depth

        # Primer de tot, comprovem si es coherent la pregunta.
        if gameState.isLose () or gameState.isWin() or depth == 0:
            return None

        print gameState, depth
        maxValue, bestAction = self.maxValue (gameState, depth)
        return bestAction

    def maxValue (self, state, depth):
        # Comprovem el final del joc.
        if depth == 0 or state.isWin () or state.isLose(): return self.evaluationFunction (state)

        # Inicialitzem bestAction, minValue i arr(ay).
        arr = state.getLegalActions ()
        bestAction = arr.pop ()
        maxValue = self.minValue (state.generateSuccessor (0, bestAction), depth -1)

        # Entrem dins del bucle.
        for action in arr:

            # Valor que te un pas en concret.
            value = self.minValue (gameState.generateSuccessor (0, action), depth -1)

            # Comprovem si el resultat es millor.
            if value > maxValue:
                maxValue = value
                bestAction = action

        return maxValue, bestAction

    # Funcio que retornara accio i valor.
    def minValue (self, state, depth):
        # Comprovem el final del joc.
        if depth == 0 or state.isWin () or state.isLose(): return self.evaluationFunction (state)

        # Inicialitzem bestAction, minValue i arr(ay).
        arr = state.getLegalActions (1) # Fantasma.
        bestAction = arr.pop ()
        minValue, nUse = self.maxValue (state.generateSuccessor (1, bestAction), depth -1)

        # Entrem dins del bucle.
        for action in arr:

            # Valor que te un pas en concret.
            value, nUse = self.maxValue (state.generateSuccessor (1, action), depth -1)

            # Comprovem si el resultat es el pitjor.
            minValue = min (minValue, value)

        return mixValue



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

#        for action in gameState.getLegalActions():
#            value = self.minValue ( gameState.generateSuccessor (
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

