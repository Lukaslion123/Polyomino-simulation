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
        return new_comb

    fill_shapes()
    grid_dict_prep()
    for c in range(r_ange):
        combination = dict_combinations[c]
        transformed_combination = night_cycle(combination)
        print([combination, transformed_combination])
