"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: describe what this function computes. -> the function goes through each character of a string and returns the total number of vowels
    # TODO: Input(s): explain each parameter. -> text: takes a string
    # TODO: Output: explain what the function returns. -> an integer which represents the total number of vowels found in the input
    # TODO: Replace this exception with your implementation.
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
        else:
            continue
    return count



# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes. -> checks through a list of lists and returns the lists that contain two elements
    # TODO: Input(s): explain each parameter. -> items is one list comprised of lists of different lengths.
    # TODO: Output: explain what the function returns. -> the function returns a new list that is comprised of the input's lists with only two elements
    # TODO: Replace this exception with your implementation.
    new = []
    for l in items:
        if len(l) == 2:
            new.append(l)
        else:
            continue
    return new


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes. -> makes a new list with the original item elements, but every list with a pair is sorted within itself.
    # TODO: Input(s): explain each parameter. -> items is a list of lists
    # TODO: Output: explain what the function returns. -> it returns a copy of the original list execpt any lists of pairs are sorted
    # TODO: Replace this exception with your implementation.
    new = []
    for l in items:
        if len(l) == 2 and l[0] > l[1]:
            new.append([l[1], l[0]])
        else:
            new.append(l)
    return new
        


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: describe what this function computes. -> this function computes the sum between two Price objects
    # TODO: Input(s): explain each parameter. -> it takes two Price objects as parameter, which have dollar and cent attributes
    # TODO: Output: explain what the function returns. -> it returns the sum of the two Prices, while carrying over cents
    # TODO: Replace this exception with your implementation.
    dollars_sum = first.dollars + second.dollars
    cents_sum = first.cents + second.cents
    if cents_sum > 99:
        dollars_sum += cents_sum // 100
        cents_sum -= 100
    return data.Price(dollars_sum, cents_sum)


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes. -> this function computes the area of a rectangle object using its attributes
    # TODO: Input(s): explain each parameter. -> one Rectangle object, which has top_left and bottom_right attributes
    # TODO: Output: explain what the function returns. -> the function returns the area of the rectangle
    # TODO: Replace this exception with your implementation.
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes. -> the function computes list of Book objects depending on the supplied author
    # TODO: Input(s): explain each parameter. -> author is a string, books is a list of Book objects
    # TODO: Output: explain what the function returns. -> the function returns a list of books with an author attribute that matches the author string input
    # TODO: Replace this exception with your implementation.
    l = []
    for book in books:
        if author in book.authors:
            l.append(book)
        else:
            continue
    return l


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes. -> the function computes a new Circle object based on attributes of a given Rectangle
    # TODO: Input(s): explain each parameter. -> one Rectangle object with attributes of a top_left and bottom_right, which are Points.
    # TODO: Output: explain what the function returns. -> a new Circle object
    # TODO: Replace this exception with your implementation.

    x_distance = (rectangle.bottom_right.x - rectangle.top_left.x) / 2
    y_distance = (rectangle.top_left.y - rectangle.bottom_right.y) / 2

    x_center = rectangle.top_left.x + x_distance
    y_center = rectangle.top_left.y - y_distance

    center = data.Point(x_center, y_center)

    if x_distance > y_distance:
        return data.Circle(center, x_distance)
    else:
        return data.Circle(center, y_distance)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes. -> the function calculates the average of all the pay_rate attributes, then returns a list of employees whose individual rates fall below that average
    # TODO: Input(s): explain each parameter. -> employess is a list of Employee objects
    # TODO: Output: explain what the function returns. -> it returns a list of Employees that fall below the average pay rate
    # TODO: Replace this exception with your implementation.
    sum = 0
    for employee in employees:
        sum += employee.pay_rate
    if len(employees) > 0:
        average = sum / len(employees)
    else:
        return []
    under = []
    for employee in employees:
        if employee.pay_rate < average:
            under.append(employee)
        else:
            continue
    return under
