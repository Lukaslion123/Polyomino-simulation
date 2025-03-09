"""used to store and retrieve data from txt databases for different scripts"""


def shape_tier(n):
    """adds an n-tier symbol into shapearrs.txt"""
    with open("shapearrs.txt", "a", encoding="UTF-8") as shapearrs:
        shapearrs.write(str(n) + "|\n")


def shape_add(shape_arr):
    """adds an array containing a shape coord encode into shapearrs.txt"""
    with open("shapearrs.txt", "a", encoding="UTF-8") as shapearrs:
        shapearrs.write(str(shape_arr) + "\n")


def shape_stringify():
    """returns the contents of shapearrs.txt as a string"""
    with open("shapearrs.txt", "r", encoding="UTF-8") as shapearrs:
        return shapearrs.read()


def shape_linelist():
    """returns the contents of shapearrs.txt as a list of lines"""
    with open("shapearrs.txt", "r", encoding="UTF-8") as shapearrs:
        return shapearrs.readlines()
