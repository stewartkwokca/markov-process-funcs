import numpy as np

#M = np.array([[0.7, 0.2], [0.3, 0.8]])
#x_0 = np.array([[100], [100]])

def checkValidTransitionMatrix(T):
    if T.shape[0] != T.shape[1]:
        return False
    for i in range(len(T)):
        if sum(T[:, i]) != 1:
            return False
    return True


def iterateNTimes(n, T, s, out=False):
    if checkValidTransitionMatrix(T):
        for i in range(n):
            if out:
                print(f"{i}: {s}")
            s = np.matmul(T, s)
        if out:
            print(f"{n}: {s}")
        return s
    return None
def steady_state(T):
    if checkValidTransitionMatrix(T):
        eigen = np.linalg.eig(T)
        for i in range(len(eigen[0])):
            if eigen[0][i] == 1:
                s_s = (1/sum(eigen[1][:,i])) * eigen[1][:,i]
                return s_s
    return None

#print(checkValidTransitionMatrix(M))
#print(steady_state(M))
#print(iterateNTimes(2000, M, steady_state(M)))