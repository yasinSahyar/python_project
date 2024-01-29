##
def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                         ## initializes a list called
evens = remove_odd_numbers(numbers)
print(f"The original list is: {numbers}")
print(f"The cut-down list is: {evens}")


"""
Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
 the same as the original list except that all uneven numbers have been removed. For testing, write a main program
  where you create a list, call the function, and then print out both the original as well as the cut-down list.
"""

"""

3.Inside the function, it uses a list comprehension to create a new list containing only the even numbers from the original list. The condition  checks if a number is even 
6.The result is assigned to the variable evens, which now holds a new list containing only the even numbers from the original list.
7.8.These lines print out the original list (numbers) and the cut-down list (evens) using formatted strings

"""