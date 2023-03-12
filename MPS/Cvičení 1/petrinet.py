from typing import List
from place import Place
from token import Token
from transition import Transition
from arc import Arc


class PetriNet:
    '''
    Petri nets are models of parallel and distributed systems named after Carl Adam Petri.
        Petri net (PN) comprises of states that are changed through local events. Mathematical
        model is weighted bipartite directed multigraph represented as tuple N = (P, T, F, W).
        P = {p1, p2, ..., pi, ..., pn} is finite set of places, |P| = n
        T = {t1, t2, ..., tj, ..., tm} is finite set of transitions |T| = m
        F = set of arcs, F = (I, O) = (P x T) u (T x P)
        I = input functions, describes token flow from places to transition
        O = output functions, describes token flow from transition to places
        W = weight function: W: F -> N
        P, T elements are nodes of graph
        I, O elements are edges of graph
    '''

    def __init__(self, places: List[Place], transitions: List[Transition], arcs: List[Arc], initial_marking: List[Token]):
        self._places = places
        self._transitions = transitions
        self._arcs = arcs
        self._initial_marking = initial_marking

    def fire(self, transition_name: str) -> bool:
        '''
        Executes action that moves tokens from place to another place trought transition that fires.
        '''
        ...

class OrdinaryPetriNet(PetriNet):
    '''
    Ordinary Petri Net N = (P, T, I, O) is PN where all arcs are unity-weighted.
    P = places
    T = transitions

    '''

    def __init__(self, places: List[Place], transitions: List[Transition], arcs: List[Arc], initial_marking: List[Token]):
        super().__init__(places, transitions, arcs, initial_marking)
