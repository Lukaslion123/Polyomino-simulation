"""used to store and retrieve data from txt databases for different scripts"""

import ast


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


def search_shape(n, shape_id):
    """searches for a shape in shapearrs.txt and returns the shape array"""
    spliced = shape_search_tier(n)
    for line in spliced:
        id_string = line.find("]")
        id_string = line[id_string + 1 :].strip()
        if str(shape_id) == id_string:
            line = line.strip()
            line = line.split("]")[0] + "]"
            return ast.literal_eval(line)


def shape_search_tier(n):
    """searches for all shapes in a tier of n"""
    splice_string = str(n) + "|"
    linelist = shape_linelist()
    f1 = 0
    for i, line in enumerate(linelist):
        if splice_string in line and f1 == 0:
            tier_start = i + 1
            f1 = 1
        elif splice_string in line and f1 == 1:
            tier_end = i
            break
    return linelist[tier_start:tier_end]


def sim_init_section(tier, shape_id):
    """initializes a shape section in outcomes.txt"""
    with open("outcomes.txt", "a", encoding="UTF-8") as sim:
        sim.write(str(tier) + "-" + str(shape_id) + "\n")


def sim_write_result(arr1, arr2):
    """writes a simulation result to outcomes.txt"""
    with open("outcomes.txt", "a", encoding="UTF-8") as sim:
        sim.write(str(arr1) + "\n")
        sim.write(str(arr2) + "\n")


def sim_init_comb_dict(dictionary, r_ange):
    """writes a quick dictionary for the combinations"""
    for i in range(r_ange):
        with open("outcomes.txt", "a", encoding="UTF-8") as sim:
            sim.write(str(i) + ": " + str(dictionary[i]) + "\n")
