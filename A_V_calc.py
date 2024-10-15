'''Area & Volume Calculator'''
# Jeremy Domino (100919249)
# A_V_calc.py -- Area and Volume Calculator.
# TPRG2131 Section 02
# October 10, 2024
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).
# All formulas are from: Google Calculators.
# This program calulates Area and Volume of Square, Rectangle, Sphere, Cylinder, and Pyramid.

import math
import sys

def user_input(message) -> float:
    '''Get user input and validate it.'''    
    user_in = float(input(message))
    while user_in <= 0.0:
        user_in = float(input('Please enter a number greater than 0.0: '))
    return user_in

def area(length, wid) -> float:
    '''Calculate the area of a rectangle or square.'''
    r_area = float(length * wid)
    equation = f"({length} \u00d7 {wid}) = {round(r_area,1)}\u339d\u00b2"
    return round(r_area, 1), equation

def volume(length, wid, hei) -> float:
    '''Calculate the volume of rectangle or cube.'''
    r_volume = float(length * wid * hei)
    equation = f"({length} \u00d7 {wid} \u00d7 {hei}) = {round(r_volume,1)}\u339d\u00b3"
    return round(r_volume, 1), equation

def area_sphere(rad) -> float:
    '''Calculate the area of a sphere.'''
    s_area = float(4 * math.pi * rad**2)
    equation = f"(4 \u00d7 \u03c0 \u00d7 {rad}\u00b2) = {round(s_area,1)}\u339d\u00b2"
    return round(s_area, 1), equation

def volume_sphere(rad) -> float:
    '''Calculate the volume of a sphere.'''
    s_volume = float((4/3) * math.pi * rad**3)
    equation = f"(4/3 \u00d7 \u03c0 \u00d7 {rad}\u00b3) = {round(s_volume,1)}\u339d\u00b3"
    return round(s_volume, 1), equation

def area_cylinder(rad, hei) -> float:
    '''Calculate the area of a cylinder.'''
    c_area = float((2 * math.pi * rad * hei) + (2 * math.pi * rad**2))
    equation = f"(2 \u00d7 \u03c0 \u00d7 {rad} \u00d7 {hei} + 2 \u00d7 \u03c0 \u00d7 {rad}\u00b2) = {round(c_area,1)} \u339d\u00b2"
    return round(c_area, 1), equation

def volume_cylinder(rad, hei) -> float:
    '''Calculate the volume of a cylinder.'''
    c_volume = float(math.pi * rad**2 * hei)
    equation = f"(\u03c0 \u00d7 {rad}\u00b2 \u00d7 {hei}) = {round(c_volume,1)} \u339d\u00b3"
    return round(c_volume, 1), equation

def area_pyramid(wid, length, hei) -> float:
    '''Calculate the area of a pyramid.'''
    p_area = float((length * wid) + (length * (math.sqrt((wid / 2)**2 + hei**2))) + (wid * (math.sqrt((length / 2)**2 + hei**2))))
    equation = f"({length} \u00d7 {wid} + {length} \u00d7 \u221a{wid}/2\u00b2 + {hei}\u00b2 + {wid} \u00d7 \u221a{length}/2\u00b2 + {hei}\u00b2) = {round(p_area,1)} \u339d\u00b2"
    return round(p_area, 1), equation

def volume_pyramid(wid, length, hei) -> float:
    '''Calculate the volume of a pyramid.'''
    p_volume = float((wid * length * hei) / 3)
    equation = f"({wid} \u00d7 {length} \u00d7 {hei} / 3) = {round(p_volume,1)} \u339d\u00b3"
    return round(p_volume, 1), equation

def area_cone(rad, hei) -> float:
    '''Calculate the area of a cone.'''
    co_area = float((math.pi * rad) * (rad + (math.sqrt((hei**2 + rad**2)))))
    equation = f"(\u03c0 \u00d7 {rad} \u00d7 {rad} + \u221a {hei}\u00b2 + {rad}\u00b2) = {round(co_area,1)} \u339d\u00b2"
    return round(co_area, 1), equation

def volume_cone(rad, hei) -> float:
    '''Calculate the volume of a cone.'''
    co_volume = float(math.pi * rad**2 * (hei / 3))
    equation = f"(\u03c0 \u00d7 {rad}\u00b2 \u00d7 {hei}/3) = {round(co_volume,1)} \u339d\u00b3"
    return round(co_volume, 1), equation

def main():
    '''Main program calculates area and volume of different shapes'''
    while True: # Loop until user quits
        try:
            # First Menu ask user how they want calculation displayed
            menu_input = input('\nSelect calculation style:\n(V) Calculated view\n(D) Default view\n(Q) to Quit\n')
            if menu_input.lower() == 'q':
                print('\nGood Bye')
                sys.exit(0)

            # Second Menu ask user what they want to calculate
            user = int(input('\n(1) Calculate the Area & Volume of a Square/Rectangle\n(2) Calculate the Area & Volume of a Sphere\n(3) Calculate the Area & Volume of a Cylinder\n(4) Calculate the Area & Volume of Pyramid\n(5) Calculate the Area & Volume of Cone\nEnter your choice: '))
            # Calculate the area and volume of rectangle or square
            if user == 1:
                rec_len = user_input('What is the length of the base in \u339d: ')
                rec_wid = user_input('What is the width of the base in \u339d: ')
                rec_hei = user_input('What is the height of the Rectangle in \u339d: ')
                rec_area = area(rec_len, rec_wid)
                rec_volume = volume(rec_len, rec_wid, rec_hei)
                if menu_input.lower() == 'v':
                    print(f'\nArea:{rec_area[0]}\u339d\u00b2, {rec_area[1]}\nVolume:{rec_volume[0]}\u339d\u00b3, {rec_volume[1]}')
                else:
                    print(f'\nThe Area of the Rectangle is {rec_area[0]}\u339d\u00b2\nThe Volume of the Rectangle is {rec_volume[0]}\u339d\u00b3')
            # Calculate the area and volume of sphere
            elif user == 2:
                sphere_rad = user_input('What is the radius of the Sphere in \u339d: ')
                sphere_area = area_sphere(sphere_rad)
                sphere_volume = volume_sphere(sphere_rad)
                if menu_input.lower() == 'v':
                    print(f'\nArea: {sphere_area[0]}\u339d\u00b2, {sphere_area[1]}\nVolume: {sphere_volume[0]}\u339d\u00b3, {sphere_volume[1]}')
                else:
                    print(f'\nThe Area of the Sphere is {sphere_area[0]} \u339d\u00b2\nThe Volume of the Sphere is {sphere_volume[0]} \u339d\u00b3')
            # Calculate the area and volume of cylinder
            elif user == 3:
                cyl_rad = user_input('What is the radius of the Cylinder in \u339d: ')
                cyl_hei = user_input('What is the height of the Cylinder in \u339d: ')
                cyl_area = area_cylinder(cyl_rad, cyl_hei)
                cyl_volume = volume_cylinder(cyl_rad, cyl_hei)
                if menu_input.lower() == 'v':
                    print(f'\nArea: {cyl_area[0]}\u339d\u00b2, {cyl_area[1]}\nVolume: {cyl_volume[0]}\u339d\u00b3, ({cyl_volume[1]})')
                else:
                    print(f'\nThe Area of the Cylinder is {cyl_area[0]} \u339d\u00b2\nThe Volume of the Cylinder is {cyl_volume[0]} \u339d\u00b3')
            # Calculate the area and volume of pyramid
            elif user == 4:
                pyr_len = user_input('What is the length of the base in \u339d: ')
                pyr_wid = user_input('What is the width of the base in \u339d: ')
                pyr_hei = user_input('What is the height of the Pyramid in \u339d: ')
                pyr_area = area_pyramid(pyr_wid, pyr_len, pyr_hei)
                pyr_volume = volume_pyramid(pyr_wid, pyr_len, pyr_hei)
                if menu_input.lower() == 'v':
                    print(f'\nArea: {pyr_area[0]}\u339d\u00b2, {pyr_area[1]}\nVolume: {pyr_volume[0]}\u339d\u00b3, {pyr_volume[1]}')
                else:
                    print(f'\nThe Area of the Pyramid is {pyr_area[0]} \u339d\u00b2\nThe Volume of the Pyramid is {pyr_volume[0]} \u339d\u00b3')
            # Calculate the area and volume of cone
            elif user == 5:
                cone_rad = user_input('What is the radius of the base in \u339d: ')
                cone_hei = user_input('What is the height of the Cone in \u339d: ')
                cone_area = area_cone(cone_rad, cone_hei)
                cone_volume = volume_cone(cone_rad, cone_hei)
                if menu_input.lower() == 'v':
                    print(f'\nArea: {cone_area[0]}\u339d\u00b2, {cone_area[1]}\nVolume: {cone_volume[0]}\u339d\u00b3, {cone_volume[1]}')
                else:
                    print(f'\nThe Area of the Pyramid is {cone_area[0]} \u339d\u00b2\nThe Volume of the Pyramid is {cone_volume[0]} \u339d\u00b3')
        # Error handling for invalid input
        except(ValueError, TypeError):
            print('\nInvalid Input\n')

if __name__ == "__main__":
    main()
