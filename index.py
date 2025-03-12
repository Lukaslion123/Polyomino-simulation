"""hub for the program, where the user can choose to run the simulation or generate shapes"""

import sim
import sql
import shapes


def main():
    """interactive function for the program"""
    side_prompt = input("enter sub process(n for none)(c): ")
    if side_prompt == "c":
        with open("shapearrs.txt", "w", encoding="UTF-8") as shapearrs:
            shapearrs.write("")
        with open("outcomes.txt", "w", encoding="UTF-8") as outcomes:
            outcomes.write("")
        sql.shape_tier(1)
        sql.shape_add([(0, 0)], 0)
        sql.shape_tier(1)
    input_n = int(input("Enter the value of n: "))
    instruction = input("Sim/Shapes: ")
    if instruction == "sim":
        shape_id = int(input("Enter the shape id: "))
        sim.main(input_n, shape_id)
    elif instruction == "shapes":
        shapes.generate_shapes(input_n)
    else:
        print("Invalid input")


def bypass(side_p, inp_n, inst, shpe_id=None):
    """quickly repeat instruction for testing"""
    if side_p == "c":
        with open("outcomes.txt", "w", encoding="UTF-8") as shapearr:
            shapearr.write("")
        # sql.shape_tier(1)
        # sql.shape_add([(0, 0)], 0)
        # sql.shape_tier(1)
    if inst == "sim":
        sim.main(inp_n, shpe_id)
    elif inst == "shapes":
        shapes.generate_shapes(inp_n)
    else:
        print("Invalid input")


# main()
for i in range(35):
    bypass("c", 6, "sim", shpe_id=i + 1)
