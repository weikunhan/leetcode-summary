"""
Given two 2D polygons write a function that calculates the IoU of their areas,
defined as the area of their intersection divided by the area of their union.
The vertices of the polygons are constrained to lie on the unit circle and you
can assume that each polygon has at least 3 vertices, given and in sorted order.

- You are free to use basic math functions/libraries (sin, cos, atan2, numpy etc)
  but not geometry-specific libraries (such as shapely).
- You are free to look up geometry-related formulas, optionally copy paste in
  short code snippets and adapt them to your needs.
- We do care and evaluate your general code quality, structure and readability
  but you do not have to go crazy on docstrings.
"""


import math
import numpy as np


def check_exist_value(point, value_list, d=1e-8):
    
    for n in value_list:
        if np.linalg.norm(np.asarray(point) - np.asarray(n)) < d:
            
            return True
        
    return False

def remove_duplicated_points(value_list):
    
    res = []
    
    for n in value_list:
        if not check_exist_value(n, res):
            res.append(n)
            
    return res

def compute_slope_and_y_intercept_value(point_value_list):
    
    x_value = point_value_list[0][0] - point_value_list[1][0]
    y_value = point_value_list[0][1] - point_value_list[1][1]
    slope_value = y_value / x_value
    y_intercept_value = (point_value_list[0][0] * point_value_list[1][1] - point_value_list[1][0] * point_value_list[0][1]) / x_value
    
    return slope_value, y_intercept_value

def check_same_value(distance_value, d=1e-8):
    if abs(distance_value) < d:
        
        return True
    else:
        
        return False

def get_intersection_point_list(a_point_value_list, b_point_value_list):
    
    res = []
    a_distance_value = a_point_value_list[0][0] - a_point_value_list[1][0]
    b_distance_value = b_point_value_list[0][0] - b_point_value_list[1][0]

    if check_same_value(a_distance_value) and check_same_value(b_distance_value):
        
        return res
    
    if check_same_value(a_distance_value):
        x_intercept_value = (a_point_value_list[0][0] + a_point_value_list[1][0]) / 2
        slope_value, y_intercept_value = compute_slope_and_y_intercept_value(b_point_value_list)
        res.append(x_intercept_value)
        res.append(slope_value * x_intercept_value + y_intercept_value)
        
        return res
        
    if check_same_value(b_distance_value):
        x_intercept_value = (b_point_value_list[0][0] + b_point_value_list[1][0]) / 2
        slope_value, y_intercept_value = compute_slope_and_y_intercept_value(a_point_value_list)
        res.append(x_intercept_value)
        res.append(slope_value * x_intercept_value + y_intercept_value)
        
        return res
    
    a_slope_value, a_y_intercept_value = compute_slope_and_y_intercept_value(a_point_value_list)
    b_slope_value, b_y_intercept_value = compute_slope_and_y_intercept_value(b_point_value_list)
    slope_distance_value = a_slope_value - b_slope_value
    
    if check_same_value(slope_distance_value):
        
        return res
    
    res.append((b_y_intercept_value - a_y_intercept_value) / slope_distance_value)
    res.append((a_slope_value * b_y_intercept_value - b_slope_value * a_y_intercept_value) / slope_distance_value) 
    
    return res
        

def get_poly_intersection_list(poly1, poly2):
    
    intersection_value_list = []
    orientation_value_list = []
    res = []
    
    for i in range(len(poly1)):
        a_point_value_list = [poly1[i], poly1[(i + len(poly1) - 1) % len(poly1)]] 
        x_max_value = max(a_point_value_list[0][0], a_point_value_list[1][0])
        x_min_value = min(a_point_value_list[0][0], a_point_value_list[1][0])
        y_max_value = max(a_point_value_list[0][1], a_point_value_list[1][1])
        y_min_value = min(a_point_value_list[0][1], a_point_value_list[1][1])
        
        for j in range(len(poly2)):
            b_point_value_list = [poly2[j], poly2[(j + len(poly2) - 1) % len(poly2)]]
            temp_point = get_intersection_point_list(
                a_point_value_list, b_point_value_list)
            
            if temp_point and x_min_value <= temp_point[0] and temp_point[0] <= x_max_value \
               and y_min_value <= temp_point[1] and temp_point[1] <= y_max_value \
               and not check_exist_value(temp_point, intersection_value_list):
                intersection_value_list.append(temp_point)
                orientation_value_list.append(math.atan2(temp_point[0], temp_point[1]))         
        
    if len(intersection_value_list) < 3:
        
        return res
    
    for a, b in sorted(zip(orientation_value_list, intersection_value_list)):
        res.append(tuple(b))
        
    return res

def convert_numpy_array(value_list, type_value=np.float64):
    
    return np.array(value_list, dtype=type_value)

def compute_area_value(poly_array):
    
    x_array = poly_array[:, 0]
    y_array = poly_array[:, 1]
    
    return 0.5 * np.abs(np.dot(y_array, np.roll(x_array, 1)) - np.dot(x_array, np.roll(y_array, 1)))

def iou(poly1, poly2):
    
    res = 0.0
    poly1 = remove_duplicated_points(poly1)
    poly2 = remove_duplicated_points(poly2)
    poly = get_poly_intersection_list(poly1, poly2)
    
    if poly:
        poly1_array = convert_numpy_array(poly1)
        poly2_array = convert_numpy_array(poly2)
        poly_array = convert_numpy_array(poly)
        total_value = compute_area_value(poly1_array) + compute_area_value(poly2_array)
        intersection_value = compute_area_value(poly_array)
        res = intersection_value / (total_value - intersection_value)
        
        return res
    
    return res

# --------------------------------------------------------

if __name__ == "__main__":

    cases = []
    # Case 1: a vanilla case (see https://imgur.com/a/dSKXHPF for a diagram)
    poly1 = [
        (-0.7071067811865475, 0.7071067811865476),
        (0.30901699437494723, -0.9510565162951536),
        (0.5877852522924729, -0.8090169943749476),
    ]
    poly2 = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (0.7071067811865475, -0.7071067811865477),
    ]
    cases.append((poly1, poly2, "simple case", 0.12421351279682288))
    # Case 2: another simple case
    poly1 = [
        (1, 0),
        (0, 1),
        (-0.7071067811865476, -0.7071067811865476),
    ]
    poly2 = [
        (-0.1736481776669303, 0.984807753012208),
        (-1, 0),
        (0, -1),
    ]
    cases.append((poly1, poly2, "simple case 2", 0.1881047657147776))
    # Case 3: yet another simple case, note the duplicated point
    poly1 = [
        (0, -1),
        (-1, 0),
        (-1, 0),
        (0, 1),
    ]
    poly2 = [
        (0.7071067811865476, 0.7071067811865476),
        (-0.7071067811865476, 0.7071067811865476),
        (-0.7071067811865476, -0.7071067811865476),
        (0.7071067811865476, -0.7071067811865476),
        (0.7071067811865476, -0.7071067811865476),
    ]
    cases.append((poly1, poly2, "simple case 3", 0.38148713966109243))

    # Case 4: shared edge
    poly1 = [
        (-1, 0),
        (-0.7071067811865476, -0.7071067811865476),
        (0.7071067811865476, -0.7071067811865476),
        (1, 0),
    ]
    poly2 = [
        (0, 1),
        (-1, 0),
        (1, 0),
    ]
    cases.append((poly1, poly2, "shared edge", 0.0))

    # Case 5: same polygon
    poly1 = [
        (0, -1),
        (-1, 0),
        (1, 0),
    ]
    poly2 = [
        (0, -1),
        (-1, 0),
        (1, 0),
    ]
    cases.append((poly1, poly2, "same same", 1.0))

    # Case 6: polygons do not intersect
    poly1 = [
        (-0.7071067811865476, 0.7071067811865476),
        (-1, 0),
        (-0.7071067811865476, -0.7071067811865476),
    ]
    poly2 = [
        (0.7071067811865476, 0.7071067811865476),
        (1, 0),
        (0.7071067811865476, -0.7071067811865476),
    ]
    cases.append((poly1, poly2, "no intersection", 0.0))


    import time
    t0 = time.time()

    for poly1, poly2, description, expected in cases:
        computed = iou(poly1, poly2)
        print('-'*20)
        print(description)
        print("computed:", computed)
        print("expected:", expected)
        print("PASS" if abs(computed - expected) < 1e-8 else "FAIL")

    # details here don't matter too much, but this shouldn't be seconds
    dt = (time.time() - t0) * 1000
    print("done in %.4fms" % dt)
