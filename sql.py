"""used to store and retrieve data from txt databases for different scripts"""


def shape_tier(n):
    """adds an n-tier symbol into shapearrs.txt"""
    with open("shapearrs.txt", "a", encoding="UTF-8") as shapearrs:
        shapearrs.write(str(n) + "|\n")


def shape_add(shape_arr, shape_id):
    """adds an array containg a shape coord encode into shapearrs.txt"""
    if shape_arr is False:
        return
    with open("shapearrs.txt", "a", encoding="UTF-8") as shapearrs:
        shapearrs.write(str(shape_arr) + str(shape_id) + "\n")


def shape_stringify():
    """returns the contents of shapearrs.txt as a string"""
    with open("shapearrs.txt", "r", encoding="UTF-8") as shapearrs:
        return shapearrs.read()


def shape_linelist():
    """returns the contents of shapearrs.txt as a list of lines"""
    with open("shapearrs.txt", "r", encoding="UTF-8") as shapearrs:
        return shapearrs.readlines()
