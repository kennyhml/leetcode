"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""



def checkStraightLine(coordinates: list[list[int]]) -> bool:
    last_slope = None

    for idx, p in enumerate(coordinates):
        if not idx:
            continue
            
        prior = coordinates[idx - 1]
        dy = p[1] - prior[1]
        dx = p[0] - prior[0]
        
        if dx == 0:
            return all(point[0] == p[0] for point in coordinates)

        m = dy / dx
        if last_slope and last_slope != m:
            return False

        last_slope = m

    return True