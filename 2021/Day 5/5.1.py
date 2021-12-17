with open('input.txt') as f:
    lines = f.readlines()


def line_segment(line):
    line_segment = {"x1": None, "x2": None, "y1": None, "y2": None}
    line = line.split()
    p1 = line[0].split(",")
    p2 = line[2].split(",")
    line_segment["x1"], line_segment["y1"] = int(p1[0]), int(p1[1])
    line_segment["x2"], line_segment["y2"] = int(p2[0]), int(p2[1])
    if int(p1[0]) == int(p2[0]):
        line_segment["Direction"] = "Vertical"
        line_segment["slope"] = float("inf")
    elif int(p1[1]) == int(p2[1]):
        line_segment["Direction"] = "Horizontal"
        line_segment["slope"] = 0
    else:
        line_segment["Direction"] = "Diagonal"
        slope = (int(p2[1]) - int(p1[1]))/(int(p2[0])-int(p1[0]))
        slope = int(slope)
        line_segment["slope"] = slope
        line_segment["intercept"] =  int(int(p1[1]) - slope * int(p1[0]))
    return line_segment

def create_segments(lines):
    line_segments = []
    for line in lines:
        line_segments.append(line_segment(line))
    return line_segments

segments = create_segments(lines)
#for segment in segments:
 #       print(segment)

def add_segments(segments):
    coord = {}
    for segment in segments:
        if segment["Direction"] == "Horizontal":
            for x in range(min(segment["x1"], segment["x2"]), max(segment["x1"], segment["x2"])+1):
                keyval = (x + 0 ,segment["y1"] + 0)
                key = str(keyval)
                if key not in coord:
                    coord[key] = 1
                else:
                    coord[key] += 1
        elif segment["Direction"] == "Vertical":
            for y in range(min(segment["y1"], segment["y2"]), max(segment["y1"], segment["y2"])+1):
                keyval = (segment["x1"] + 0,y + 0)
                key = str(keyval)
                if key not in coord:
                    coord[key] = 1
                else:
                    coord[key] += 1
        else:
            #print(segment)
            m = int(segment["slope"])
            b = int(segment["intercept"])
            xstart = min(segment["x1"], segment["x2"])
            xend = max(segment["x1"], segment["x2"])
            for x in range(xstart, xend+1):
                y =  x*m + b
                #print(x, y, m, b)
                val = (x, y)
                key = str(val)
                #print("Diagonal")
                #print(key)
                #x += 1
                if key not in coord:
                    coord[key] = 1
                else:
                    coord[key] += 1

    return coord
coord_count = add_segments(segments)
#print(coord_count)
def dangerous_points(coord):
    total = 0
    for k in coord:
        if coord[k] >=2:
            total += 1
    return total

print(dangerous_points(coord_count))





    
