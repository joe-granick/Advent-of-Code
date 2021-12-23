#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
with open("test_input_last.txt", "r", encoding="utf-8") as f:
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

def corrupt(chunk, opened, closed,  error, close_count, close_need):
    pass
    if not chunk or error == True:
        closing_delimiter = closed.pop(0)
        return [opened, closed,  error, closing_delimiter, close_count, close_need]
    else:
        if chunk[0] in opening:
            opener = chunk[0]
            opened.insert(0, opener)
            close_need[expected_delim[opener]] +=1
        if chunk[0] in closing:
            close = chunk[0]
            close_count[close] += 1 
            opener = opened.pop(0)
            if close != expected_delim[opener]:
                error = True
            closed.insert(0, close)
        return corrupt(chunk[1:], opened, closed, error, close_count, close_need)

score = 0
completion_score = 0
for chunk in lines:
    opened , closed,  error, closing_delim, delimiters_used, delimeters_needed = corrupt(chunk, opened = [], closed = [],  error = False, close_count  = defaultdict(lambda: 0), close_need = defaultdict(lambda: 0))
    print("Chunk: ", chunk)
    print("Opened: ", opened)
    #print("Closed: ", closed)
    print("Delimiter wrong: ", error)
    print("Delimeter used : ", closing_delim)
    if error == True:
        score += syntax_scores[closing_delim]
    if error == False:
        print("Delimeters used : ", delimiters_used)
        print("Delimeters Needed : ",  delimeters_needed)
        for delim, need in delimeters_needed.items():
            delim_score = 0
            delim_score = (need - delimiters_used[delim])*auto_complete_scores[delim]
            completion_score += delim_score
            print(completion_score)

print(score)
print(completion_score)


            

