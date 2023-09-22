# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [w,w, w, w, s, s, s, w]

def depthFirstSearch(problem:SearchProblem)->List[Direction]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:


    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    """

    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    '''
    from game import Directions,Configuration
    from util import Stack
    from time import sleep
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    s = problem.getStartState()
    fringe = Stack()
    memoire,results = [], [] #on met direct le state initial car different format
    fringe.push(s)


    while fringe.isEmpty() == False:

        s_ = fringe.pop() #nouveau etat
        pth = Configuration(s,s_) #chemin reliant l ancien etat au nouveau etat
        print(len(pth.getDirection()))
        if problem.isGoalState(s_) == True :
            return results #on return tous les états visités

        else :

            if len(pth.getDirection())==2: C = problem.getSuccessors(s_)
            else :
                C = problem.getSuccessors(pth.getDirection()[0]) #j'obtiens les successeurs tous sans exceptions

            for state in C: #on balaie l ensemble des successeurs
                path_state = Configuration(s_,state) #chemin d'états
                is_present0=False
                for Pth in memoire: # on balaie la mémoire
                    if Pth.__eq__(path_state):
                        is_present0=True
                if is_present0==False:
                    fringe.push(state) #L=LuC
                    #if no successeur don t save in stack s

            memoire.append(pth.getPosition())
            # is_present=False
            # if len(s_)==3 :
            #     for Pth in memoire:
            #         if Pth.__eq__(pth):
            #             is_present=True
            #     if is_present==False: #si le path n'est pas déjà présent dans la memoire apres avoir bouclé pour verifier que c'etait le cas
            #         memoire.append(pth) #il faut enregistrer non pas le noeud mais le path (on peut avoir plusieurs fois le meme noeud mais ne venant pas de la meme source)
    for state in memoire :
       results.append(state[1])
    return results #no solution



def depthFirstSearch(problem:SearchProblem)->List[Direction]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:


    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    """

    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    '''
    # from game import Directions,Configuration
    # from util import Stack
    # from time import sleep
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #
    # s = problem.getStartState()
    # fringe = Stack()
    # memoire,results = [], [] #on met direct le state initial car different format
    # fringe.push(s)
    #
    #
    # while fringe.isEmpty() == False:
    #
    #     s_ = fringe.pop() #nouveau etat
    #     pth = Configuration(s,s_) #chemin reliant l ancien etat au nouveau etat
    #
    #     if problem.isGoalState(s_) == True :
    #         return results #on return tous les états visités
    #
    #     else :
    #
    #         if len(pth.getDirection())==2: C = problem.getSuccessors(s_)
    #         else :
    #             C = problem.getSuccessors(pth.getDirection()[0]) #j'obtiens les successeurs tous sans exceptions
    #
    #         for state in C: #on balaie l ensemble des successeurs
    #             path_state = Configuration(s_,state) #chemin d'états
    #             is_present0=False
    #             for Pth in memoire: # on balaie la mémoire
    #                 if Pth.__eq__(path_state):
    #                     is_present0=True
    #             if is_present0==False:
    #                 fringe.push(state) #L=LuC
    #                 #if no successeur don t save in stack s
    #         memoire.append(pth)
    #     s=s_
    # for state in memoire[1:] :
    #    results.append(state.getDirection()[1])
    #
    #
    # return results #no solution
    from util import Stack
    from time import sleep
    fringe = Stack()
    fringe.push(problem.getStartState())
    memoire = []
    path = [] #final path to G
    stck_path = Stack() #append in the same order the pat to go to the state from S And the state (wth fringe)
    while fringe.isEmpty()==False:
        s = fringe.pop()
        if problem.isGoalState(s):
            return path
        elif s not in memoire:
            memoire.append(s)
            successors = problem.getSuccessors(s)
            for state in successors:
                fringe.push(state[0])
                state_path = path + [state[1]]
                stck_path.push(state_path) #on ajoute la direction pour aller a cet état en meme temps que l'on ajoute cet etat dans la fringe
        path = stck_path.pop()
    return path




def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    """Search the shallowest nodes in the search tree first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
    '''
    from util import Queue
    from time import sleep
    fringe = Queue()
    fringe.push(problem.getStartState())
    memoire = []
    path = []  # final path to G
    stck_path = Queue()  # append in the same order the pat to go to the state from S And the state (wth fringe)
    while fringe.isEmpty() == False:
        s = fringe.pop()
        if problem.isGoalState(s):
            return path
        elif s not in memoire:
            memoire.append(s)
            successors = problem.getSuccessors(s)
            for state in successors:
                fringe.push(state[0])
                state_path = path + [state[1]]
                stck_path.push(
                    state_path)  # on ajoute la direction pour aller a cet état en meme temps que l'on ajoute cet etat dans la fringe
        path = stck_path.pop()
    return path

def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    """Search the node of least total cost first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    '''

    from util import Queue
    from time import sleep
    fringe = Queue()
    fringe.push(problem.getStartState())
    memoire = []
    path = []  # final path to G
    stck_path = Queue()  # append in the same order the pat to go to the state from S And the state (wth fringe)
    while fringe.isEmpty() == False:
        s = fringe.pop()
        if problem.isGoalState(s):
            return path
        elif s not in memoire:
            memoire.append(s)
            successors = problem.getSuccessors(s)
            for state in successors:
                fringe.push(state[0])
                state_path = path + [state[1]]
                stck_path.push(
                    state_path)  # on ajoute la direction pour aller a cet état en meme temps que l'on ajoute cet etat dans la fringe
        path = stck_path.pop()
    return path


def nullHeuristic(state:GameState, problem:SearchProblem=None)->List[Direction]:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    """Search the node that has the lowest combined cost and heuristic first."""
    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 4 ICI
    '''

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
