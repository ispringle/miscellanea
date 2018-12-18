from input import initial
from train import ChooChoo

testA = """/->-⧵        
|   |  /----⧵
| /-+--+-⧵  |
| | |  | v  |
⧵-+-/  ⧵-+--/
  ⧵------/   """

testB = """/>-<⧵  
|   |  
| /<+-⧵
| | | v
⧵>+</ |
  |   ^
  ⧵<->/"""

def parseTracks(initial):
    tracks = [[char for char in line] for line in initial.splitlines()]
    master = [[char for char in line] for line in initial.splitlines()]
    y = 0
    trains = []
    for row in master:
        x = 0
        for element in row:
            if element in ['^', 'v', '<', '>']:
                trains.append(ChooChoo(x, y, element))
                if element in ['^', 'v']:
                    master[y][x] = '|'
                elif element in ['<', '>']:
                    master[y][x] = '-'
            x += 1
        y += 1
    return tracks, trains, tuple(master)

def printMap(tracks):
    for row in tracks:
        print(''.join(row))

def tick(trains, tracks, master):
    current_pos = []
    for t in trains:
        cx, cy = t.x, t.y
        nx, ny = t.step()
        tracks[ny][nx] = tracks[cy][cx]
        tracks[cy][cx] = master[cy][cx]
        if master[ny][nx] in ['/','⧵', '+']:
            t.turn(master[ny][nx])
        current_pos.append(','.join([str(nx),str(ny)]))
    return current_pos, tracks

def detectCrash(current_pos):
    c_loc = []
    if len(current_pos) != len(set(current_pos)):
        seen = []
        for loc in current_pos:
            if loc not in seen:
                seen.append(loc)
            else:
                c_loc.append(loc)
    return c_loc

def removeCollisions(trains, tracks, collisions):
    crashed_trained = []
    for crash in collisions:
        for t in trains:
            if t.status()[0] == crash:
                crashed_trained.append(t)
    remaining_trains = [t for t in trains if t not in crashed_trained]
    return remaining_trains, tracks

def partOne(tracks, trains, master):
    collission = False
    while not collission:
        current_pos, tracks = tick(trains, tracks, master)
        crashes = detectCrash(current_pos)
        if len(crashes) != 0:
            collission = True
    return crashes[0]

def partTwo(tracks, trains, master):
    while len(trains) > 2:
        current_pos, tracks = tick(trains, tracks, master)
        crashes = detectCrash(current_pos)
        if len(crashes) != 0:
            trains, tracks = removeCollisions(trains, tracks, 
                            [[int(i) for i in loc.split(',')] for loc in crashes])
    return trains[0].status()[0] 

    #return trains[0].x, trains[0].y

tracks, trains, master = parseTracks(initial)
print("The first collision is located at "
        + partOne(tracks, trains, master)
        + ".")
print("The last cart, after all others have collided is located at "
        + ','.join(str(i) for i in partTwo(tracks, trains, master))
        + ".")
