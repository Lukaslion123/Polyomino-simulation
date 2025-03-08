import ast
import encoder
import sql

start_n = 0
set_n = False
iteration_n = 0


def generate_shapes(n):
    global start_n
    global set_n
    global iteration_n
    # dict = {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 35, 7: 108, 8: 369, 9: 1285, 10: 4655}
    final_x = 0
    curr_n = 0
    iteration_n = n
    if set_n == False:
        start_n = n
        set_n = True

    def check_x(z):
        global curr_n
        global iteration_n
        curr_n = z
        splice_string = str(z) + "|"
        with open("shapearrs.txt", "r") as shapearrs:
            overview = shapearrs.read()
            if splice_string in overview:
                return True
            else:
                curr_n -= 1
                iteration_n -= 1
                check_x(curr_n)
                return curr_n

    def get_prev_shapes(x):
        splice_string = str(x) + "|"
        result = []
        with open("shapearrs.txt", "r") as shapearrs:
            lines = shapearrs.readlines()
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
        sql.shape_tier(y)

        def check_directions(overlay_shape):
            free_arr = []
            for g in range(len(overlay_shape)):
                for b in range(4):
                    coords = encoder.shape_movement_dir(overlay_shape[g], b)
                    if not coords in overlay_shape:
                        free_arr.append(coords)
            return free_arr

        for i in range(len(res)):
            curr_overlay_shape = res[i].copy()
            free = check_directions(curr_overlay_shape)
            print(free)
            for f in range(len(free)):
                special = curr_overlay_shape.copy()
                print(special)
                print(free[f])
                special.append(tuple(free[f]))
                sql.shape_add(special)
        sql.shape_tier(y)

    final_x = check_x(n - 1)
    if final_x == True:
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


generate_shapes(6)
