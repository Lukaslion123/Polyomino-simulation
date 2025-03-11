"""this script is responsible for the generation of n-ominoes"""

import ast
import encoder
import sql

# pylint: disable=invalid-name
# pylint: disable=global-statement
# pylint: disable=redefined-outer-name

original_n = 0
recursed = False
iteration_n = 0
db_query = 0


def generate_shapes(n):
    """bundles together the functions for the generation of n-ominoes"""
    # dict = {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 35, 7: 108, 8: 369, 9: 1285, 10: 4655}
    global original_n
    global recursed
    global iteration_n
    final_y = 0
    iteration_n = n
    if not recursed:
        original_n = n
        recursed = True

    def check_x(z):
        """calculate the value of x for the get_prev_shapes
        function based on the current value of iteration_n"""
        global db_query
        global iteration_n
        db_query = z
        splice_string = str(db_query) + "|"
        overview = sql.shape_stringify()
        if splice_string in overview:
            return True
        else:
            db_query -= 1
            iteration_n -= 1
            check_x(db_query)
            return db_query

    def get_prev_shapes(x):
        """gets the shapes of n-1 from the database for use in generating the shapes of n"""
        prev_shapes = []
        extracted_content = sql.shape_search_tier(x)
        for line in extracted_content:
            shape_line = line.strip()
            shape_line = shape_line.split("]")[0] + "]"
            prev_shape = ast.literal_eval(shape_line)
            prev_shapes.append(prev_shape)
        return prev_shapes

    def generate(y, prev_shapes):
        """specifically handles the generation part of the script"""
        sql.shape_tier(y)
        shape_id = 0

        def filter_shapes(shape):
            """filters n-ominoes to remove duplicates and leave only free polyominoes"""
            nonlocal shape_id
            tl_reading = encoder.shape_overallcoords(shape)
            linelist = sql.shape_linelist()
            new_linelist = []
            for line in linelist:
                line = line.split("]")[0] + "]"
                new_linelist.append(line)
            candidate = tl_reading.copy()
            for _ in range(2):
                for _ in range(4):
                    if str(candidate) in new_linelist:
                        print("invalid")
                        return False
                    candidate = encoder.shape_rotate(candidate)
                candidate = encoder.shape_mirror(candidate)
            print("valid")
            shape_id += 1
            return candidate

        for _, curr_overlay_shape in enumerate(prev_shapes):
            curr_overlay_shape = curr_overlay_shape.copy()
            free_spaces = []
            for _, coord in enumerate(curr_overlay_shape):
                buffer_value = encoder.shape_check_directions(curr_overlay_shape, coord)
                for _ in range(len(buffer_value)):
                    single_space = buffer_value.pop()
                    free_spaces.append(single_space)
            for _, coord in enumerate(free_spaces):
                new_shape = curr_overlay_shape.copy()
                new_shape.append(tuple(coord))
                final_step = filter_shapes(new_shape)
                sql.shape_add(final_step, shape_id)
        sql.shape_tier(y)

    final_y = check_x(n - 1)
    if final_y:
        if iteration_n > original_n:
            iteration_n = original_n
        elif iteration_n == 1:
            iteration_n += 1
        final_y = iteration_n
        previous_shapes = get_prev_shapes(final_y - 1)
        generate(final_y, previous_shapes)
        if iteration_n < original_n:
            iteration_n += 1
            generate_shapes(iteration_n)
    else:
        generate_shapes(final_y)
