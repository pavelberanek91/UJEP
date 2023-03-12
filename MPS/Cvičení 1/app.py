from petrinet import PetriNet
from place import Place
from token import Token
from transition import Transition
from arc import Arc

def testrunner():
    ...

def main():
    #udelat do trid tridni metody pro generovani vetsiho mnozstvi
    
    s1 = Place(name='s1', tokens=[Token(f't{Token.max_token_id}') for i in range(3)])
    s2 = Place(name='s2', tokens=[Token(f't{Token.max_token_id}') for i in range(5)])
    s3 = Place(name='s3', tokens=[Token(f't{Token.max_token_id}') for i in range(1)])
    s4 = Place(name='s4', tokens=[Token(f't{Token.max_token_id}') for i in range(2)])

    t1 = Transition('t1')
    t1.add_arc(Arc(name='a1', place=s1, edge_direction="input", weight=3))
    t1.add_arc(Arc(name='a2', place=s2, edge_direction="input", weight=2))
    t1.add_arc(Arc(name='a3', place=s3, edge_direction="output", weight=1))
    t1.add_arc(Arc(name='a4', place=s4, edge_direction="output", weight=3))

    print(s1)
    print(s2)
    print(s3)
    print(s4)
    t1.fire()
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(t1)

if __name__ == "__main__":
    testrunner()
    main()