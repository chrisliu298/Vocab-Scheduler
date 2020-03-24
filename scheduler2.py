import sys
from datetime import datetime, timedelta

# 8 memory cycles (with the first three in the same day)
mem_cyc = [0, 0, 0, 1, 2, 4, 7, 15]


def get_unit_dates(start_date):
    global mem_cyc
    return [(start_date + timedelta(days=i)).strftime("%x") for i in mem_cyc]


if __name__ == "__main__":
    # Prompts
    num_units = int(sys.argv[1])
    start_date = datetime(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

    # Make a dictionary of unit:dates pair
    day_task_dict = dict()
    for unit in range(num_units):
        day_task_dict[unit + 1] = get_unit_dates(start_date + timedelta(unit + 1))

    for key, value in day_task_dict.items():
        print(key, value)
