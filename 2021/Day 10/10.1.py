#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
with open("test_input_close.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)
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
#print(opening)
#print(closing)

def corrupt(chunk, opener = '', close = '',opened = [], closed = [], predict_close = []):
    pass
    if chunk == []:
        return "not_corrupt" 
    elif close != '' and  expected_delim[opener] != close:
        return [opened, closed, predict_close]
    else:
        if chunk[0] in opening:
            opener = chunk[0]
            opened.append(opener)
            predict_close.insert(0, expected_delim[opener])

        if chunk[0] in closing:
            close = chunk[0]
            closed.insert(0, close)
        return corrupt(chunk[1:], opener, close, opened, closed, predict_close)


score = 0
for chunk in lines:
    opened , closed, predicted = corrupt(chunk)
    print("Chunk: ", chunk)
    print("Opened: ", opened)
    print("Closed: ", closed)
    print("Predicted: ", predicted)
    #print("")

    ##score += scores[corrupt(chunk)]
    #print(score)

#print(score)



            

