import math

''' Locker Problem '''
class Door:
    doorStatus = 0 # 0 for closed, 1 for open

def lockerProblem(n):
    listDoors = [Door() for k in range(n)] # initialize n doors

    for i in range(0, n): # You make n passes by the lockers
        count = 0
        for j in range(i, n): # on the ith pass...
            # print("on pass: ", i, "j: ", j, "on locker: ", j+count) // debugging
            if j + count < n: # if we won't exceed the list, toggle every ith locker door
                if listDoors[j+count].doorStatus == 0: # if the door is closed
                    listDoors[j+count].doorStatus = 1 # open door
                elif listDoors[j+count].doorStatus == 1: # if the door is open
                    listDoors[j+count].doorStatus = 0 # close door
            count += i
    print("After passing through ", n, " lockers...")
    for h in range(n):
        if listDoors[h].doorStatus == 1:
            print(" OL ", end="")
        elif listDoors[h].doorStatus == 0:
            print(" CL ", end="")
    print("\n", int(math.sqrt(n)), " lockers are open.")
    print("\n")

lockerProblem(10) # run program with 10 lockers    
lockerProblem(50) # run program with 50 lockers
lockerProblem(100) # run program with 100 lockers

