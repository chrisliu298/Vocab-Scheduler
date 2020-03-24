import datetime
from datetime import datetime
from datetime import timedelta


def compute_dates():
    """
    Return a set of review dates grouped by review dates
    e.g. review_dates_4 refers to the 4th review dates for all # lists
    """

    # Create empty lists for all review dates
    review_dates_1_3 = []
    review_dates_4 = []
    review_dates_5 = []
    review_dates_6 = []
    review_dates_7 = []

    # A loop to append the review date for each pass
    for i in range(LIST_NUM):
        review_dates_1_3.append(START_DATE + timedelta(days=i))
        review_dates_4.append(START_DATE + timedelta(days=i + INTERVALS[1]))
        review_dates_5.append(START_DATE + timedelta(days=i + INTERVALS[2]))
        review_dates_6.append(START_DATE + timedelta(days=i + INTERVALS[3]))
        review_dates_7.append(START_DATE + timedelta(days=i + INTERVALS[4]))

    return (
        review_dates_1_3,
        review_dates_4,
        review_dates_5,
        review_dates_6,
        review_dates_7,
    )


def combine(
    list_num,
    review_dates_1_3,
    review_dates_4,
    review_dates_5,
    review_dates_6,
    review_dates_7,
):
    """
    Return a 2d array of all lists and corresponding review dates
    """
    total = []
    for i in range(list_num):
        total.append([f"List {i + 1}"])
    for i in range(LIST_NUM):
        total[i].append(review_dates_1_3[i].strftime("%Y/%-m/%-d"))
        total[i].append(review_dates_4[i].strftime("%Y/%-m/%-d"))
        total[i].append(review_dates_5[i].strftime("%Y/%-m/%-d"))
        total[i].append(review_dates_6[i].strftime("%Y/%-m/%-d"))
        total[i].append(review_dates_7[i].strftime("%Y/%-m/%-d"))

    return total


def make_list_view(
    review_dates_1_3, review_dates_4, review_dates_5, review_dates_6, review_dates_7,
):
    """
    Generate a text file of review dates in list view
    """

    # Write the date information to a file
    file = open("vocab_schedule_list_view.txt", "w+")
    for i in range(LIST_NUM):
        file.write(f"List {i + 1}" + "\n")
        file.write(
            INTERVAL_NAME[0] + ": " + review_dates_1_3[i].strftime("%Y/%-m/%-d") + "\n"
        )
        file.write(
            INTERVAL_NAME[1] + ":   " + review_dates_4[i].strftime("%Y/%-m/%-d") + "\n"
        )
        file.write(
            INTERVAL_NAME[2] + ":   " + review_dates_5[i].strftime("%Y/%-m/%-d") + "\n"
        )
        file.write(
            INTERVAL_NAME[3] + ":   " + review_dates_6[i].strftime("%Y/%-m/%-d") + "\n"
        )
        file.write(
            INTERVAL_NAME[4] + ":   " + review_dates_7[i].strftime("%Y/%-m/%-d") + "\n"
        )
        file.write("\n")
    file.close()


def make_date_view(total):
    """
    Generate a text file of review dates in date view
    """
    learn_count = 0
    review_count = 0

    file = open("vocab_schedule_date_view.txt", "w+")
    start = total[0][1]
    end = total[-1][-1]
    start_year, start_mon, start_day = start.split("/")
    end_year, end_mon, end_day = end.split("/")

    current_date = datetime(int(start_year), int(start_mon), int(start_day))
    end_date = datetime(int(end_year), int(end_mon), int(end_day))

    delta = end_date - current_date
    days_num = delta.days + 1
    print(f"You plan will last {days_num} days.")

    while current_date != (end_date + timedelta(days=1)):  # loop the range of all dates
        day = current_date.strftime("%Y/%-m/%-d")  # current date
        file.write(day + "\n")
        for i in total:  # loop the total
            if day in i:
                ind = i.index(day)
                if ind == 1:
                    learn_count += 100
                    file.write(f"List {total.index(i) + 1}" + " review 1\n")
                else:
                    review_count += 100
                    file.write(f"List {total.index(i) + 1}" + f" review {ind}\n")

        current_date += timedelta(days=1)
        file.write("\n")


def plan(list_num):
    """
    Make new review plan
    """
    (review_1_3, review_4, review_5, review_6, review_7) = compute_dates()
    make_list_view(review_1_3, review_4, review_5, review_6, review_7)
    schedule = combine(list_num, review_1_3, review_4, review_5, review_6, review_7)
    make_date_view(schedule)


if __name__ == "__main__":
    # Prompts
    input_list_num = int(input("Number of vocabulary lists:\n"))
    print()
    input_start_year = int(input("Start year:\n"))
    print()
    input_start_mon = int(input("Start month:\n"))
    print()
    input_start_day = int(input("Start day:\n"))

    # Constants
    LIST_NUM = input_list_num  # number of all vocabulary lists
    START_DATE = datetime(
        input_start_year, input_start_mon, input_start_day
    )  # my start date is July 2nd 2019
    INTERVALS = [0, 1, 3, 7, 15]
    INTERVAL_NAME = ["1-3", "4", "5", "6", "7"]

    # Make new plan
    plan(LIST_NUM)
