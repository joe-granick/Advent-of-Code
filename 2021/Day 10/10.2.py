#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
import math
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
syntax_scores = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137, "not_corrupt" : 0}
auto_complete_scores = {")" : 1, "]" : 2, "}" : 3, ">" : 4, "not_corrupt" : 0}

def corrupt(chunk, opened, closed,  error):
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
completion_scores = []
for chunk in lines:
    opened , closed,  error, closing_delim = corrupt(chunk, opened = [], closed = [],  error = False,)
    print("Chunk: ", chunk.strip())
    delim_score = 0
    if error == True:
        score += syntax_scores[closing_delim]
        print("Syntax error score: ", score)
        print("Delim error: ", closing_delim)
    if error == False:
        expected = []
        for delim in opened:
            expected.append(expected_delim[delim])
            new_points = auto_complete_scores[expected_delim[delim]]
            new_delim = delim_score*5
            delim_score = (new_delim + new_points)
        print("Autocomplete score: ", delim_score)
        print("Missing delimiters: ", expected)
        completion_scores.append(delim_score)
    print("\n")

print("Syntax error score: ",score)
completion_scores.sort()
mid = math.ceil(len(completion_scores)/2)
print(completion_scores)
print("Autocomplete score: ",completion_scores[mid-1])


            

