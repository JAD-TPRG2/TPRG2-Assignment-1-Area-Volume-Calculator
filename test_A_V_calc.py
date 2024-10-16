'''Test file for Area and Volume Calculator'''
# Jeremy Domino (100919249)
# test_A_V_calc.py -- Tests the Area and Volume Calculator.
# TPRG2131 Section 02
# October 10, 2024
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).
# This Tests the calculatinons of Area and Volume of Square, Rectangle, Sphere, Cylinder, and Pyramid.

import pytest
from A_V_calc import area, area_sphere, area_cylinder, area_cone, area_pyramid, volume, volume_sphere, volume_cylinder, volume_cone, volume_pyramid


def test_area() -> float:
    '''Test rectangle area function'''
    #test 1
    assert area('v', 5.0, 5.0) == (25.0, f"{5.0} \u00d7 {5.0} = {25.0}\u339d\u00b2")
    assert area('d', 5.0, 5.0) == 25
    #test 2
    assert area('v', 3.0, 5.0) == (15.0, f"{3.0} \u00d7 {5.0} = {15.0}\u339d\u00b2")
    assert area('d', 3.0, 5.0) == 15.0
    #test 3
    assert area('v', 6.0, 7.0) == (42.0, f"{6.0} \u00d7 {7.0} = {42.0}\u339d\u00b2")
    assert area('d', 6.0, 7.0) == 42.0

def test_area_sphere() -> float:
    '''Test sphere area function'''
    #test 1
    assert area_sphere('v', 5.0) == (314.2, f"4 \u00d7 \u03c0 \u00d7 {5.0}\u00b2 = {314.2}\u339d\u00b2")
    assert area_sphere('d', 5.0) == 314.2
    #test 2
    assert area_sphere('v', 8.0) == (804.2, f"4 \u00d7 \u03c0 \u00d7 {8.0}\u00b2 = {804.2}\u339d\u00b2")
    assert area_sphere('d', 8.0) == 804.2
    #test 3
    assert area_sphere('v', 7.5) == (706.9, f"4 \u00d7 \u03c0 \u00d7 {7.5}\u00b2 = {706.9}\u339d\u00b2")
    assert area_sphere('d', 7.5) == 706.9

def test_area_cylinder() -> float:
    '''Test cylinder area function'''
    #test 1
    assert area_cylinder('v', 5.0, 5.0) == (314.2, f"2 \u00d7 \u03c0 \u00d7 {5.0} \u00d7 {5.0} + 2 \u00d7 \u03c0 \u00d7 {5.0}\u00b2 = {314.2} \u339d\u00b2")
    assert area_cylinder('d', 5.0, 5.0) == 314.2
    #test 2
    assert area_cylinder('v', 6.5, 7.5) == (571.8, f"2 \u00d7 \u03c0 \u00d7 {6.5} \u00d7 {7.5} + 2 \u00d7 \u03c0 \u00d7 {6.5}\u00b2 = {571.8} \u339d\u00b2")
    assert area_cylinder('d', 6.5, 7.5) == 571.8
    #test 3
    assert area_cylinder('v', 9.0, 10.0) == (1074.4, f"2 \u00d7 \u03c0 \u00d7 {9.0} \u00d7 {10.0} + 2 \u00d7 \u03c0 \u00d7 {9.0}\u00b2 = {1074.4} \u339d\u00b2")
    assert area_cylinder('d', 9.0, 10.0) == 1074.4
def test_area_cone() -> float:
    '''Test cone area function'''
    #test 1
    assert area_cone('v', 5.0, 5.0) == (189.6, f"(\u03c0 \u00d7 {5.0}) \u00d7 ({5.0} + \u221a({5.0}\u00b2 + {5.0}\u00b2)) = {189.6} \u339d\u00b2")
    assert area_cone('d', 5.0, 5.0) == 189.6
    #test 2
    assert area_cone('v', 6.2, 7.25) == (306.6, f"(\u03c0 \u00d7 {6.2}) \u00d7 ({6.2} + \u221a({7.25}\u00b2 + {6.2}\u00b2)) = {306.6} \u339d\u00b2")
    assert area_cone('d', 6.2, 7.25) == 306.6
    #test 3
    assert area_cone('v', 4.7, 3.0) == (151.7, f"(\u03c0 \u00d7 {4.7}) \u00d7 ({4.7} + \u221a({3.0}\u00b2 + {4.7}\u00b2)) = {151.7} \u339d\u00b2")
    assert area_cone('d', 4.7, 3.0) == 151.7

def test_area_pyramid() -> float:
    '''Test pyramid area function'''
    #test 1
    assert area_pyramid('v', 5.0, 5.0, 5.0) == (80.9, f"{5.0} \u00d7 {5.0} + {5.0} \u00d7 \u221a{5.0}/2\u00b2 + {5.0}\u00b2 + {5.0} \u00d7 \u221a{5.0}/2\u00b2 + {5.0}\u00b2 = {80.9} \u339d\u00b2")
    assert area_pyramid('d', 5.0, 5.0, 5.0) == 80.9
    #test 2
    assert area_pyramid('v', 2.0, 3.2, 5.0) == (33.2, f"{3.2} \u00d7 {2.0} + {3.2} \u00d7 \u221a{2.0}/2\u00b2 + {5.0}\u00b2 + {2.0} \u00d7 \u221a{3.2}/2\u00b2 + {5.0}\u00b2 = {33.2} \u339d\u00b2")
    assert area_pyramid('d', 2.0, 3.2, 5.0) == 33.2
    #test 3
    assert area_pyramid('v', 4.0, 6.6, 7.0) == (105.4, f"{6.6} \u00d7 {4.0} + {6.6} \u00d7 \u221a{4.0}/2\u00b2 + {7.0}\u00b2 + {4.0} \u00d7 \u221a{6.6}/2\u00b2 + {7.0}\u00b2 = {105.4} \u339d\u00b2")
    assert area_pyramid('d', 4.0, 6.6, 7.0) == 105.4

def test_volume() -> float:
    '''Test rectangle volume function'''
    #test 1
    assert volume('v', 5.0, 5.0, 5.0) == (125.0, f"{5.0} \u00d7 {5.0} \u00d7 {5.0} = {125.0}\u339d\u00b3")
    assert volume('d', 5.0, 5.0, 5.0) == 125.0
    #test 2
    assert volume('v', 3.0, 8.5, 9.25) == (235.9, f"{3.0} \u00d7 {8.5} \u00d7 {9.25} = {235.9}\u339d\u00b3")
    assert volume('d', 3.0, 8.5, 9.25) == 235.9
    #test 3
    assert volume('v', 6.0, 7.3, 11.0) == (481.8, f"{6.0} \u00d7 {7.3} \u00d7 {11.0} = {481.8}\u339d\u00b3")
    assert volume('d', 6.0, 7.3, 11.0) == 481.8

def test_volume_sphere() -> float:
    '''Test sphere volume function'''
    #test 1
    assert volume_sphere('v', 5.0) == (523.6, f"(4/3) \u00d7 \u03c0 \u00d7 {5.0}\u00b3 = {523.6}\u339d\u00b3")
    assert volume_sphere('d', 5.0) == 523.6
    #test 2
    assert volume_sphere('v', 9.2) == (3261.8, f"(4/3) \u00d7 \u03c0 \u00d7 {9.2}\u00b3 = {3261.8}\u339d\u00b3")
    assert volume_sphere('d', 9.2) == 3261.8
    #test 1
    assert volume_sphere('v', 4.35) == (344.8, f"(4/3) \u00d7 \u03c0 \u00d7 {4.35}\u00b3 = {344.8}\u339d\u00b3")
    assert volume_sphere('d', 4.35) == 344.8

def test_volume_cylinder() -> float:
    '''Test cylinder volume function'''
    #test 1
    assert volume_cylinder('v', 5.0, 5.0) == (392.7, f"\u03c0 \u00d7 {5.0}\u00b2 \u00d7 {5.0} = {392.7} \u339d\u00b3")
    assert volume_cylinder('d', 5.0, 5.0) == 392.7
    #test 2
    assert volume_cylinder('v', 2.2, 15.0) == (228.1, f"\u03c0 \u00d7 {2.2}\u00b2 \u00d7 {15.0} = {228.1} \u339d\u00b3")
    assert volume_cylinder('d', 2.2, 15.0) == 228.1
    #test 1
    assert volume_cylinder('v', 10.0, 42.0) == (13194.7, f"\u03c0 \u00d7 {10.0}\u00b2 \u00d7 {42.0} = {13194.7} \u339d\u00b3")
    assert volume_cylinder('d', 10.0, 42.0) == 13194.7

def test_volume_cone() -> float:
    '''Test cone volume function'''
    #test 1
    assert volume_cone('v', 5.0, 5.0) == (130.9, f"(\u03c0 \u00d7 {5.0}\u00b2) \u00d7 ({5.0}/3) = {130.9} \u339d\u00b3")
    assert volume_cone('d', 5.0, 5.0) == 130.9
    #test 2
    assert volume_cone('v', 9.0, 10.0) == (848.2, f"(\u03c0 \u00d7 {9.0}\u00b2) \u00d7 ({10.0}/3) = {848.2} \u339d\u00b3")
    assert volume_cone('d', 9.0 , 10.0) == 848.2
    #test 3
    assert volume_cone('v', 2.9, 4.6) == (40.5, f"(\u03c0 \u00d7 {2.9}\u00b2) \u00d7 ({4.6}/3) = {40.5} \u339d\u00b3")
    assert volume_cone('d', 2.9, 4.6) == 40.5

def test_volume_pyramid() -> float:
    '''Test pyramid volume function'''
    #test 1
    assert volume_pyramid('v', 5.0, 5.0, 5.0) == (41.7, f"({5.0} \u00d7 {5.0} \u00d7 {5.0}) / 3 = {41.7} \u339d\u00b3")
    assert volume_pyramid('d', 5.0, 5.0, 5.0) == 41.7
    #test 2
    assert volume_pyramid('v', 1.9, 3.2, 6.5) == (13.2, f"({1.9} \u00d7 {3.2} \u00d7 {6.5}) / 3 = {13.2} \u339d\u00b3")
    assert volume_pyramid('d', 1.9, 3.2, 6.5) == 13.2
    #test 3
    assert volume_pyramid('v', 4.3, 7.6, 12.6) == (137.3, f"({4.3} \u00d7 {7.6} \u00d7 {12.6}) / 3 = {137.3} \u339d\u00b3")
    assert volume_pyramid('d', 4.3, 7.6, 12.6) == 137.3
