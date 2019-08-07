import math

R = 6371009
ERRORMARGIN = 4/100

def main():
    direction_d = 144
    bearing = math.radians(direction_d)
    speed_ms = 472.05
    deltaTime = 1
    position = (32.583128426179705,35.17730425957495)
    d = speed_ms*deltaTime
    print("distance: " + d)
    radius = d * ERRORMARGIN
    print("radius: " + radius)
    print("output: " + getLocation(math.radians(position[0]), math.radians(position[1]), d, bearing))

def getLocation(x1, y1, d, brng):
    # where x is latitude,
    # y is longitude,
    # brng is the bearing (clockwise from north),
    # d/R is the angular distance; d being the distance travelled, R the earth’s radius
    x2 = math.asin( math.sin(x1)*math.cos(d/R) + math.cos(x1)*math.sin(d/R)*math.cos(brng) )
    y2 = y1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(x1), math.cos(d/R)-math.sin(x1)*math.sin(x2))

    returnPos = (math.degrees(x2), math.degrees(y2))
    
    return returnPos


if __name__ == "__main__":
    main()
