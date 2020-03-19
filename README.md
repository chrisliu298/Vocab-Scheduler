# GRE-Vocab-Scheduler

## Getting Started

This script schedules your GRE vocabulary plan. It assumes you memorize 100 words per day. If you stick to your plan, you'll have 46 days to finish it, and when you finished it, you went through it 7 passes.

After running the script, it generates two schedule files: `vocab_schedule_date_view.txt` and `vocab_schedule_list_view.txt`. 

The date view tells you which lists you have to complete on the particular day. The example below means on April 15, 2020 you'll review List 13 for the 7th time.

```
2020/4/15
List 13 review 7
List 21 review 6
List 25 review 5
List 27 review 4
List 28 review 1-3
```

The list view shows you the dates of memorizing a certain list. The example below means you'll review List 14 on these dates.

```
List 14
1-3: 2020/4/1
4:   2020/4/2
5:   2020/4/4
6:   2020/4/8
7:   2020/4/16
```


## Usage

```
❯ python scheduler.py
Number of vocabulary lists:
31

Start year:
2020

Start month:
3

Start day:
19
You plan will last 46 days.
```
