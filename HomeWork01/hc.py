from random import random, randint
def neighbor(p, step = 0.01):
    nv = p.copy()       # 參數 v 為解答的資料結構
    i = randint(0, len(nv)-1) # 隨機選取一個變數
    if(random() > 0.5):
        nv[i] += step
    else:
        nv[i] -= step
    return nv

def optimize(f, p, maxGens, maxFails):   # 爬山演算法的主體函數
    falis = 0
    for i in range(maxGens):
        pnew = neighbor(p)
        if(pnew >= p):
            p = pnew
            falis = 0
        else:
            falis = falis + 1
        if (falis >= maxFails):
            break
    return p
