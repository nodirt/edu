import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def tsp1(points):
    result = [points[0]]

    while points:
        cur = points[-1]
        closest = 0
        closestDist = float('inf')
        for i in range(0, len(points)):
            d = math.sqrt((cur.x - points[closest].x) ** 2 + (cur.y - points[closest].y))
            if d < closestDist:
                closest = i
                closestDir = d

        result.append(points.pop(closest))

    return result
