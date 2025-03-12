"""This module contains the simulation functions for the project."""

import sql
import encoder


def main(n, shape_id):
    """bundles together the simulation functions"""
    shape = sql.search_shape(n, shape_id)
    dict_combinations = {}
    dict_comb_id = {}
    dict_grid_id = {}
    r_ange = 2**n

    sql.sim_init_section(n, shape_id)

    def fill_shapes():
        """makes a dictionary of combinations of bolleans on the board"""
        for i in range(r_ange):
            dict_combinations[i] = encoder.binary_encode(i, n)
            dict_comb_id[dict_combinations[i]] = i

    def grid_dict_prep():
        """prepares the grid index dictionary for the simulation"""
        temp_dict = {}
        for g, coord in enumerate(shape):
            temp_dict[coord] = g
        for s, coord in enumerate(shape):
            arr = []
            around = encoder.shape_check_directions(shape, shape[s], reverse=True)
            for _, coordinate in enumerate(around):
                appended = temp_dict[coordinate]
                arr.append(appended)
            dict_grid_id[s] = arr

    def night_cycle(combination):
        """runs a single step of the simulation"""
        new_comb = []
        for g, me in enumerate(combination):
            neigbours = dict_grid_id[g]
            neighbours_genders = []
            for n in neigbours:
                neighbours_genders.append(combination[n])
            my_type_cnt = neighbours_genders.count(me)
            not_my_type_cnt = neighbours_genders.count(not me)
            if not_my_type_cnt > my_type_cnt:
                new_comb.append(not me)
            else:
                new_comb.append(me)
        return tuple(new_comb)

    def handle_backend(c):
        """handles the backend of the simulation"""
        curr_c = None
        curr_sim_arr = []
        backup_arr = []
        stat_arr = []
        curr_sim_arr.append(c)
        while curr_c not in backup_arr:
            backup_arr = curr_sim_arr.copy()
            print(curr_sim_arr)
            print(curr_c)
            combination = dict_combinations[c]
            transformed_combination = night_cycle(combination)
            print(dict_comb_id)
            curr_c = dict_comb_id[transformed_combination]
            print(curr_c)
            curr_sim_arr.append(curr_c)
        index = curr_sim_arr.index(curr_c)
        cyclicity_result = len(set(curr_sim_arr[index + 1 :]))
        stat_arr.append("CYCLE:" + str(cyclicity_result))
        sql.sim_write_result(curr_sim_arr, stat_arr)

    fill_shapes()
    grid_dict_prep()
    sql.sim_init_comb_dict(dict_combinations, r_ange)
    for c in range(r_ange):
        handle_backend(c)
