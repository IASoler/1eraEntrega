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
        maxValue, bestAction = self.maxValueT (gameState, self.depth)
        return bestAction

    # Retorna el valor i l'accio mes faborables minMax
    def maxValueT (self, state, depth):

        # Comprovem si estem al final.
        if (depth == 0) or state.isWin () or state.isLose():
            return self.evaluationFunction (state), None

        # Inicialitzem els valors, per tal de poder treballar amb ells.
        arr = state.getLegalActions ()

        bestAction = arr.pop ()
        maxValue = self.minValueT (state.generateSuccessor (0, bestAction), depth)

        # Entrem dins del bucle.
        for action in arr:

            # Valor que te un pas en concret.
            value = self.minValueT (state.generateSuccessor (0, action), depth)

            # Comprovem si el resultat es millor.
            if value > maxValue:
                maxValue = value
                bestAction = action

        # Retornem el valor i accio millors.
        return maxValue, bestAction

    # Funcio que retorna els moviments mes defavorables.
    def minValueT (self, state, depth):

        # Comprovem si estem al final.
        if (depth == 0) or state.isWin () or state.isLose():
            return self.evaluationFunction (state)

        # En cas contrari, restem depth i calculem quants fantasmes hi ha.
        depth -= 1
        numTotalGhosts = state.getNumAgents () -1

        # Fem les convinacions per descobrir el minim.
        return self.ghostNumber (state, numTotalGhosts, depth)

    # Funcio especialitzada pels fantasmes.
    def ghostNumber (self, state, numGhost, depth):

        # No cal comprovar final, ja que s'ha fet a minValueT.
        # Tot i que cal comprovar si queden fantasmes.
        if not numGhost:
            value, nUse = self.maxValueT (state, depth)
            return value

        # Inicialitzem els valors, per tal de poder treballar amb ells.
        arr = state.getLegalActions (numGhost)

        if not arr:
            return self.ghostNumber (state, numGhost -1, depth)

        bestAction = arr.pop ()
        minValue = self.ghostNumber (state.generateSuccessor (numGhost, bestAction), numGhost -1, depth)

        for action in arr:

            value = self.ghostNumber (state.generateSuccessor (numGhost, action), numGhost -1, depth)
            minValue = min (minValue, value)

        # Retornem el valor desitjat.
        return minValue


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

