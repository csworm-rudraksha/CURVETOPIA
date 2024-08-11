import numpy as np

def is_straight_line(points):
    if len(points) < 2:
        return False
    direction = points[1] - points[0]
    for i in range(2, len(points)):
        if not np.allclose(points[i] - points[i - 1], direction):
            return False
    return True

def is_circle(points):
    if len(points) < 3:
        return False
    center = np.mean(points, axis=0)
    radius = np.linalg.norm(points[0] - center)
    for point in points:
        if not np.isclose(np.linalg.norm(point - center), radius):
            return False
    return True

def is_rectangle(points):
    if len(points) != 4:
        return False
    distances = [np.linalg.norm(points[i] - points[(i + 1) % 4]) for i in range(4)]
    if not np.isclose(distances[0], distances[2]) or not np.isclose(distances[1], distances[3]):
        return False
    diag1 = np.linalg.norm(points[0] - points[2])
    diag2 = np.linalg.norm(points[1] - points[3])
    return np.isclose(diag1, diag2)

def is_regular_polygon(points):
    num_points = len(points)
    if num_points < 3:
        return False
    center = np.mean(points, axis=0)
    radius = np.linalg.norm(points[0] - center)
    angles = [np.arctan2(point[1] - center[1], point[0] - center[0]) for point in points]
    angles.sort()
    angle_diffs = [(angles[i] - angles[i - 1]) % (2 * np.pi) for i in range(num_points)]
    return np.allclose(angle_diffs, angle_diffs[0])

def regularize_paths(paths):
    regularized_paths = []
    for path in paths:
        points = np.array(path).reshape(-1, 2)
        if is_straight_line(points):
            regularized_paths.append(('line', points))
        elif is_circle(points):
            regularized_paths.append(('circle', points))
        elif is_rectangle(points):
            regularized_paths.append(('rectangle', points))
        elif is_regular_polygon(points):
            regularized_paths.append(('polygon', points))
        else:
            regularized_paths.append(('unknown', points))
    return regularized_paths
