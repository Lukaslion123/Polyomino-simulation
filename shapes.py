import ast
import encoder
import sql


def generate_shapes(n):
    # dict = {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 35, 7: 108, 8: 369, 9: 1285, 10: 4655}
    final_x = 0

    def check_x(n):
        curr_n = n
        splice_string = str(n) + "|"
        with open("shapearrs.txt", "r") as shapearrs:
            overview = shapearrs.read()
            if splice_string in overview:
                return True
            else:
                curr_n -= 1
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

        def check_directions(grid_space, overlay_shape):
            free_arr = []
            for b in range(4):
                modifier = encoder.encode(b, 2)
                coords = []
                for a in range(2):
                    curr_coord = grid_space[a]
                    curr_modifier = modifier[a]
                    if a == 0:
                        if curr_modifier:
                            curr_coord += 1
                    else:
                        if curr_modifier:
                            curr_coord -= 1
                    coords.append(curr_coord)
                if not tuple(coords) in overlay_shape:
                    free_arr.append(coords)
            return free_arr

        print(res)
        for i in range(len(res)):
            curr_overlay_shape = res[i].copy()
            for g in range(len(curr_overlay_shape)):
                curr_grid_space = curr_overlay_shape[g]
                free = check_directions(curr_grid_space, curr_overlay_shape)
                lenghth = len(free)
                for f in range(lenghth):
                    special = res[i].copy()
                    special.append(tuple(free[f]))
                    sql.shape_add(special)
        sql.shape_tier(y)

    final_x = check_x(n)
    if final_x == True:
        final_x = n
        print(final_x)
        rescomp = get_prev_shapes(final_x - 1)
        print(rescomp)
        generate(final_x, rescomp)
    else:
        generate_shapes(final_x)


generate_shapes(2)
