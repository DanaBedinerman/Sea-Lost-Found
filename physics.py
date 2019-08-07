import math

R = 6371009
ERRORMARGIN = 4/100

class Physics:
    def __init__(self, x1, y1, speed, deltaTime, brng, currentRadius):
        self.x1 = math.radians(x1)
        self.y1 = math.radians(y1)
        self.d = speed*deltaTime
        self.brng = math.radians(brng)
        self.currentRadius = currentRadius
    
    def getLocation(self, x1, y1, d, brng):
        # where x is latitude,
        # y is longitude,
        # brng is the bearing (clockwise from north),
        # d/R is the angular distance; d being the distance travelled, R the earth’s radius
        x2 = math.asin( math.sin(x1)*math.cos(d/R) + math.cos(x1)*math.sin(d/R)*math.cos(brng) )
        y2 = y1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(x1), math.cos(d/R)-math.sin(x1)*math.sin(x2))

        returnPos = [math.degrees(x2), math.degrees(y2)]
        
        return returnPos

    def getRadius(self, currentRadius, d):
        return d * ERRORMARGIN * currentRadius

    def getResults(self):
        res = {}
        res["position"] = self.getLocation(self.x1, self.y1, self.d, self.brng)
        res["radius"] = self.getRadius(self.currentRadius, self.d)
        return res

def main():

    
    direction_d = 144
    bearing = math.radians(direction_d)
    speed_ms = 472.05
    deltaTime = 1
    position = (32.583128426179705,35.17730425957495)
    p = Physics(position[0], position[1], speed_ms, deltaTime, direction_d, 0)
    print(p.getResults())


if __name__ == "__main__":
    main()
