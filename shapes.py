"""handles the generation of n-ominoes for n and values
under if they aren't already present in the database"""

import ast
import encoder
import sql

# pylint: disable=invalid-name
# pylint: disable=global-statement
# pylint: disable=redefined-outer-name

start_n = 0
set_n = False
iteration_n = 0
curr_n = 0


def generate_shapes(n):
    """handles generation and storage of n-ominoes for n and values
    under if they aren't already present in the database"""
    # dict = {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 35, 7: 108, 8: 369, 9: 1285, 10: 4655}
    global start_n
    global set_n
    global iteration_n
    final_x = 0
    iteration_n = n
    if not set_n:
        start_n = n
        set_n = True

    def check_x(z):
        """calculate the value of x for the get_prev_shapes
        function based on the current value of iteration_n"""
        global curr_n
        curr_n = z
        splice_string = str(z) + "|"
        overview = sql.shape_stringify()
        if splice_string in overview:
            return True
        else:
            curr_n -= 1
            iteration_n -= 1
            check_x(curr_n)
            return curr_n

    def get_prev_shapes(x):
        """gets the shapes of n-1 from the database for use in generating the shapes of n"""
        splice_string = str(x) + "|"
        result = []
        lines = sql.shape_linelist()
        f1 = 0
        for i, line in enumerate(lines):
            if splice_string in line and f1 == 0:
                cutstart = i + 1
                f1 = 1
            elif splice_string in line and f1 == 1:
                cutend = i
                break
        ls = lines[cutstart:cutend]
        for line in ls:
            l = line.strip()
            result.append(ast.literal_eval(l))
        return result

    def generate(y, res):
        """specifically handles the generation part of the script"""
        sql.shape_tier(y)

        def check_directions(overlay_shape):
            """checks for which squares are free around the current base
            shape of n-1 and returns them for further use"""
            free_arr = []
            for _, shape in enumerate(overlay_shape):
                for b in range(4):
                    coords = encoder.shape_movement_dir(shape, b)
                    if not coords in overlay_shape:
                        free_arr.append(coords)
            return free_arr

        for _, curr_overlay_shape in enumerate(res):
            curr_overlay_shape = curr_overlay_shape.copy()
            free = check_directions(curr_overlay_shape)
            print(free)
            for _, coord in enumerate(free):
                special = curr_overlay_shape.copy()
                print(special)
                print(coord)
                special.append(tuple(coord))
                sql.shape_add(special)
        sql.shape_tier(y)

    final_x = check_x(n - 1)
    if final_x:
        if iteration_n > start_n:
            iteration_n = start_n
        elif iteration_n == 1:
            iteration_n += 1
        final_x = iteration_n
        rescomp = get_prev_shapes(final_x - 1)
        generate(final_x, rescomp)
        if iteration_n < start_n:
            generate_shapes(iteration_n + 1)
            iteration_n += 1
    else:
        generate_shapes(final_x)


generate_shapes(3)
