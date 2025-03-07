def shape_tier(n):
    with open("shapearrs.txt", "a") as shapearrs:
        shapearrs.write(str(n) + "|\n")


def shape_add(shape_arr):
    with open("shapearrs.txt", "a") as shapearrs:
        shapearrs.write(str(shape_arr) + "\n")
