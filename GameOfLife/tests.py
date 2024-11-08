import main
import numpy as np
def testThing():
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    actual_next_state1 = main.next_board_state(init_state1)

    if np.array_equal(expected_next_state1, actual_next_state1):
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print("Expected:") 
        print(expected_next_state1) 
        print("Actual:") 
        print(actual_next_state1) 

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = main.next_board_state(init_state2)

    if np.array_equal(expected_next_state2, actual_next_state2):
        print("PASSED 2") 
    else:
        print("FAILED 2!") 
        print("Expected:") 
        print(expected_next_state2) 
        print("Actual:") 
        print(actual_next_state2) 
    # TEST 3: Toad test
    # should come alive.
    init_state3 = [
        [0,0,0,0],
        [0,1,1,1],
        [1,1,1,0],
        [0,0,0,0]
    ]
    expected_next_state3 = [
        [0,0,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,0,0]
    ]
    actual_next_state3 = main.next_board_state(init_state3)

    if np.array_equal(expected_next_state3, actual_next_state3):
        print("PASSED 3") 
    else:
        print("FAILED 3!") 
        print("Expected:") 
        print(expected_next_state3) 
        print("\n")
        print("Actual:") 
        print(actual_next_state3) 
