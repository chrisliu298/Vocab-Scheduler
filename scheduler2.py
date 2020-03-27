import sys
import os
import pandas as pd
from datetime import datetime, timedelta

# 8 memory cycles (with the first three in the same day)
mem_cyc = [0, 1, 2, 4, 7, 15]


def get_unit_dates(start_date):
    """
    Returns the dates of memorizing a certain unit
    """
    global mem_cyc
    return [(start_date + timedelta(days=i)).strftime("%x") for i in mem_cyc]


def make_unit_view(num_units, start):
    """
    """
    unit_view = {}
    for unit in range(num_units):
        unit_view[unit + 1] = get_unit_dates(start + timedelta(unit))
    return unit_view


def get_unique_dates(unit_view):
    unique_dates = []
    for unit in unit_view.items():
        unique_dates += unit[1]
    return sorted(set(unique_dates))


def auto_populate(full_len, date_view_dict):
    """
    """
    return


def switch_date_view(unit_view, naming):
    """
    Switch to the date view
    """
    unique_dates = get_unique_dates(unit_view)
    ind_dates_pairs = []
    for index, dates in unit_view.items():
        for date in dates:
            ind_dates_pairs.append((index, dates.index(date) + 1, date))
    date_view_dict = {}
    for date in unique_dates:
        date_view_dict[date] = []
    for date in unique_dates:
        for pair in ind_dates_pairs:
            if pair[2] == date:
                date_view_dict[date].append(f"{naming[4]} {pair[0]} (Review {pair[1]})")
                ind_dates_pairs.remove(pair)
    # date_view_dict = auto_populate(6, date_view_dict)
    filename = f"date_view_{naming[0]}units_{naming[2]}_{naming[3]}_{naming[1]}"
    with open(filename + ".csv", "w+") as file:
        for date, units in date_view_dict.items():
            units.sort(key=lambda x: x[-2])
            file.write(f"{date} ")
            for unit in units:
                if units.index(unit) == len(units) - 1:
                    file.write(f"{unit}")
                else:
                    file.write(f"{unit} ")
            file.write("\n")
    file.close()
    # pd.read_csv(filename + ".csv").to_excel(filename + "xlsx", index=None, header=False)
    return date_view_dict


def beautify_csv(filename, full_len):
    file = open(filename, "r").readlines()
    lines = [i.split() for i in file]
    for i in lines:
        while len(i) <= full_len:
            i.append(" ")
        print(i)
    new_file = open(filename, "w+")
    for i in lines:
        for j in i:
            new_file.write(f"{j}, ")
        new_file.write("\n")
    new_file.close()

if __name__ == "__main__":
    # Prompts
    num_units = int(sys.argv[1])
    start_date = datetime(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    naming = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]

    # Make a dictionary of unit:dates pair
    unit_view = make_unit_view(num_units, start_date)
    # Make a dictionary of date:units pair
    date_view = switch_date_view(unit_view, naming)
    beautify_csv("date_view_31units_3_26_2020.csv", 6)

