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
    

# Create dataflow
# -1 is empty
next = [[2], [3, 4], [5], -1, [6], [7, 8], [2], [2]]
use = [{}, {"x"}, {"e"}, {"x"}, {"e", "x"}, {"x"}, {"z"}, {"y"}]
deff = [{"e"}, {}, {"z"}, {}, {"y"}, {}, {"e"}, {"e"}]

if (len(next) == len(use)) and (len(next) == len(deff)):
    n = len(next)
else:
    print("Wrong input!!!")

# Start with in[n] = out[n] = empty
inn = [{}] * n
out = [{}] * n

# Init temp inOld and outOld
inOld = []
outOld = []

counter = 1
while not((inn == inOld) and (out == outOld)):
    # Temp for store in_Old and out_Old
    inOld = inn.copy()
    outOld = out.copy()

    for i in range(n):
        # out[n] = allConnect in[n']
        out[i] = {}
        if next[i] != -1:
            for j in next[i]:
                out[i] = newUnion(out[i], inn[j-1])
        
        # in[n] = use [n] U (out[n] - def[n])
        inn[i] = newUnion(use[i], newMinus(out[i], deff[i]))
    
    print(str(counter) + " : ")
    print("Out")
    print(out)
    print("In")
    print(inn)
    counter = counter + 1