inp = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
inp = inp.replace(" ", "").split(",")
x, y = 0, 0
heading = 0
locations = set()
revisited = False

for i in range(0, len(inp)):
    if inp[i][0] == "R":
        heading += 90
    else:
        heading -= 90

    if heading >= 360:
        heading = 0

    if heading < 0:
        heading = 270

    if heading == 0:
        y += int(inp[i][1:])
    elif heading == 90:
        x += int(inp[i][1:])
    elif heading == 180:
        y -= int(inp[i][1:])
    elif heading == 270:
        x -= int(inp[i][1:])

    current_location = (x, y)
    locations.add(current_location)
