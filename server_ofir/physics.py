import math

R = 6371009
ERRORMARGIN = 4 / 100


def main():
    print(getLocationAndRadius(0, 0, 1000, 1000, 90, 1))


def getLocationAndRadius(latitude, longitude, speed, deltaTime, bearing, currentRadius):
    x1 = math.radians(latitude)
    y1 = math.radians(longitude)
    brng = math.radians(bearing)

    d = speed * deltaTime
    radius = d * ERRORMARGIN + currentRadius

    # where x is latitude,
    # y is longitude,
    # brng is the bearing (clockwise from north),
    # d/R is the angular distance; d being the distance travelled, R the earth’s radius
    x2 = math.asin(math.sin(x1) * math.cos(d / R) + math.cos(x1) * math.sin(d / R) * math.cos(brng))
    y2 = y1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(x1), math.cos(d / R) - math.sin(x1) * math.sin(x2))

    res = {}

    res["latitude"] = math.degrees(x2)
    res["longitude"] = math.degrees(y2)
    res["radius"] = 1

    return res


if __name__ == "__main__":
    main()
