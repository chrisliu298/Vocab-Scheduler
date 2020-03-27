# GRE-Vocab-Scheduler

[中文版](README_CN.md)

## Getting Started

In Scheduler 0.2, I redesigned and rewrote the whole program from scratch by writing much less code and adding extra functionalities. The scheduler 0.2 reads the command arguments as input (detail below) and creates your schedule (based on Ebbinghaus forgetting curve) in a `.csv` file (open with Microsoft Excel).

## Usage

```
❯ python3 scheduler2.py 6 2020 3 26 Unit
```

Arguments: `python3 scheduler2.py units_of_vocabularies start_year start_month start_day customized_task_name`