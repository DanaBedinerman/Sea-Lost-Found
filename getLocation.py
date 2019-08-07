import math

R = 6371009
ERRORMARGIN = 4/100

def main():
    direction_d = 144
    bearing = math.radians(direction_d)
    speed_ms = 472.05
    deltaTime = 1
    position = (32.583128426179705,35.17730425957495)
    
    print("distance: " + d)
    
    print("radius: " + radius)
    print("output: " + getLocation(math.radians(position[0]), math.radians(position[1]), d, bearing))

def getLocationAndRadius(latitude, longitude, speed, deltaTime, bearing, currentRadius):
    x1 = math.radians(x)
    y1 = math.radians(y)
    brng = math.radians(bearing)

    d = speed_ms*deltaTime
    radius = d * ERRORMARGIN + currentRadius
    
    # where x is latitude,
    # y is longitude,
    # brng is the bearing (clockwise from north),
    # d/R is the angular distance; d being the distance travelled, R the earth’s radius
    x2 = math.asin( math.sin(x1)*math.cos(d/R) + math.cos(x1)*math.sin(d/R)*math.cos(brng) )
    y2 = y1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(x1), math.cos(d/R)-math.sin(x1)*math.sin(x2))

    res = {}
    
    res["latitude"] = math.degrees(x2)
    res["longitude"] = math.degrees(y2)
    res["radius"] = radius
    
    return res


if __name__ == "__main__":
    main()
