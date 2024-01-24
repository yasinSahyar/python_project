##

import random


def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        ## Check if the point is inside the unit circle 检查点是否在单位圆内
        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    ## Calculate the approximation of pi
    approx_pi = 4 * points_inside_circle / num_points

    return approx_pi


def main():
    try:
        num_points = int(input("Enter the number of random points to generate: "))

        if num_points <= 0:
            print("Please enter a positive integer.")
        else:
            result = approximate_pi(num_points)
            print(f"Approximation of pi with {num_points} random points: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")



main()




"""
Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle. 
A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around the
 unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), 
 and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle 
  A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. 
  This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number 
  of random points, such as one million, inside square B. Let N be the total number of random points. Each point inside 
  the square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A. 
  Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate, and 
  then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation
   of pi to the user. 
(Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
"""

"""
6.18. The approximate_pi function takes the number of random points (num_points) as an argument.
It initializes a counter (points_inside_circle) to keep track of how many points fall inside the unit circle.
It uses a loop to generate num_points random points within the square B.
For each point, it checks whether it falls inside the unit circle using the condition 

If the condition is met, the point is inside the circle, and the counter is incremented.
After processing all points, it calculates the approximation of pi using the formula 

points_inside_circle
num_points

num_points
points_inside_circle


23. 34 . The main function serves as the main entry point for the program.
It prompts the user to enter the number of random points to generate.
It uses a try-except block to handle potential errors, such as if the user enters a non-integer value.
It checks if the entered value is a positive integer. If not, it prints an error message. 
Otherwise, it calls the approximate_pi function and prints the result. 
"""