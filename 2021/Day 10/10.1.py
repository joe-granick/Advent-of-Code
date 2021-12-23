#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

delimiters = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">") ]
opening = []
closing = []
expected_delim = {}
for delim in delimiters:
    open_delim, close_delim = delim[0], delim[1]
    opening.append(open_delim)
    closing.append(close_delim)
    expected_delim[open_delim] = close_delim
scores = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137, "not_corrupt" : 0}

def corrupt(chunk, opened = [], closed = [],  error = False):
    pass
    if not chunk or error == True:
        closing_delimiter = closed.pop(0)
        return [opened, closed,  error, closing_delimiter]
    else:
        if chunk[0] in opening:
            opener = chunk[0]
            opened.insert(0, opener)
        if chunk[0] in closing:
            close = chunk[0]
            opener = opened.pop(0)
            if close != expected_delim[opener]:
                error = True
            closed.insert(0, close)
        return corrupt(chunk[1:], opened, closed, error)

score = 0
for chunk in lines:
    opened , closed,  error, closing_delim = corrupt(chunk)
    print("Chunk: ", chunk.strip())
    print("Opened: ", opened)
    print("Closed: ", closed)
    print("Delimiter wrong: ", error)
    print("Delimeter used : ", closing_delim)
    if error == True:
        score += scores[closing_delim]
print(score)



            

