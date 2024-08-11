import numpy as np

def find_reflection_symmetry(points):
    # Check for reflection symmetry
    if len(points) < 2:
        return None
    center = np.mean(points, axis=0)
    for i in range(len(points)):
        if not np.any(np.all(points == 2 * center - points[i], axis=1)):
            return False
    return True

def find_rotational_symmetry(points):
    # Check for rotational symmetry
    center = np.mean(points, axis=0)
    centered_points = points - center
    angles = np.arctan2(centered_points[:, 1], centered_points[:, 0])
    angles = np.mod(angles, 2 * np.pi)
    angles = np.sort(angles)
    angle_diffs = np.diff(angles)
    return np.allclose(angle_diffs, angle_diffs[0])

def find_symmetries(paths):
    symmetric_paths = []
    for path in paths:
        for points in path:
            reflection_symmetry = find_reflection_symmetry(points)
            rotational_symmetry = find_rotational_symmetry(points)
            symmetric_paths.append((points, reflection_symmetry, rotational_symmetry))
    return symmetric_paths
