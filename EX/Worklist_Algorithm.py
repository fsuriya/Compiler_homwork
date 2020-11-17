# Python cann't union first set is empty set
def newUnion(A, B):
    setA = A.copy()
    setB = B.copy()
    if setA != {}:
        return setA.union(setB)
    elif setB != {}:
        return setB.union(setA)
    else:
        return {}

def newMinus(A, B):
    setA = A.copy()
    setB = B.copy()
    if (setA != {}) and (setB != {}):
        return setA - setB
    elif (setA != {}) and (setB == {}):
        return setA
    elif (setA == {}):
        return {}
    
# Initialize CFG
next = [[2], [3, 4], [5], -1, [6], [7, 8], [2], [2]]
use = [{}, {"x"}, {"e"}, {"x"}, {"e", "x"}, {"x"}, {"z"}, {"y"}]
deff = [{"e"}, {}, {"z"}, {}, {"y"}, {}, {"e"}, {"e"}]

# Check number of input
if (len(next) == len(use)) and (len(next) == len(deff)):
    n = len(next)
else:
    print("Wrong input!!!")

# 1. Initialize worklist to all CFG node
worklist = list(range(n))

# 2. Initialize in[n] = {} ; for all n
inn = [{}] * n

# 3. While worklist != {}
while(len(worklist) != 0):
    # remove node n from worklist
    work = worklist.pop(0)
    # assign in[n] = use[n] U (U of success(n) of in[n'] - def[n])
    succIn = {}
    if next[work] != -1:
        for j in next[work]:
            succIn = newUnion(succIn, inn[j])
    inTemp = inn.copy()
    inn[work] = newUnion(use[work], newMinus(succIn, deff[work]))
    # if in[n] change, add all predecessors of n to worklist
    if inn != inTemp:
