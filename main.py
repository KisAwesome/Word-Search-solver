import zono.workers
import zono.colorlogger
import english_words
import time
import collections


st = time.time()
worker = zono.workers.Workload(zono.workers.AutoThreads)

board = [
    ['-','-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-','-'],
    ['-','-','s','u','p','e','r','-'],
    ['-','-','i','d','o','l','-','-'],
    ['-','-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-','-']

] 




stringBoard = ''
for i in board:
    stringBoard+=str(i)
    for j in i:
        print(j,end=' ')
    print()

print('\n')



querys = list(english_words.web2_lower)



def get_diagonals(L):
    h, w = len(L), len(L[0])
    return [[L[h - p + q - 1][q]
             for q in range(max(p-h+1, 0), min(p+1, w))]
            for p in range(h + w - 1)]


def antidiagonals(L):
    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p-h+1,0), min(p+1, w))]
            for p in range(h + w - 1)]


def rough_check(query):
    for i in query:
        if not i in stringBoard:
            return False
    return True

def check_(query):
    for c,o in collections.Counter(query).items():
        if stringBoard.count(c)<o:
            return False
    return True
    



def find_word(query,board):   
    if not rough_check(query): return
    if not check_(query):return
    query = query.lower()
    state = False
    if len(query) == 1:
        return False
    for ycord,y in enumerate(board):
        x = ''.join(y).lower()
        if query in x:
            ind = x.index(query)
            start = ind
            end = len(query)-1+ind
            print(f'word {query} found at y cord {ycord} starts at x {start} and ends at {end}')
            state = True

        rev = x[::-1]
        if query in rev:
            ind = rev.index(query)
            start = ind
            end = len(query)-1+ind
            print(f'word {query} found at y cord {ycord} starts at x {end} and ends at {start} (the word is reversed)')
            state = True




    diagonals = []


    diagonals = get_diagonals(board)+antidiagonals(board)



    for i in diagonals:
        x = ''.join(i).lower()
        if query in x:
            print(f'found {query} diagonally')
            state = True

        rev = x[::-1]
        if query in rev:
            print(f'found {query} diagonally')
    HORIZONTALS = []
    for i,_ in enumerate(board[0]):
        l = []
        for j in board:
            l.append(j[i])

        HORIZONTALS.append(l)

    for ycord,x in enumerate(HORIZONTALS):
        x = ''.join(x).lower()
        if query in x:
            ind = x.index(query)
            start = ind
            end = len(query)-1+ind
            print(f'word {query} found at y cord {ycord} starts at x {start} and ends at {end} (word found horizontaly)')
            state = True

        rev = x[::-1]
        if query in rev:
            ind = rev.index(query)
            start = ind
            end = len(query)-1+ind
            print(f'word {query} found at y cord {ycord} starts at x {end} and ends at {start} (the word is horizontal+ reversed)')
            state = True
    return state


    




found = worker.run(querys,find_word,board).count(True)
zono.colorlogger.major_log(f'Searched for {len(querys)} words in {round(time.time()-st,1)}s, found {found} words')