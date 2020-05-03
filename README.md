# Vocab-Scheduler 0.2

[中文版](README.zh-cn.md)

## Getting Started

In Scheduler 0.2, I redesigned and rewrote the whole program from scratch by writing much less code and adding extra functionalities. The scheduler 0.2 reads the command arguments as input (detail below) and creates your schedule (based on Ebbinghaus forgetting curve) in a `.csv` file (open with Microsoft Excel).

Note: The schedule will make you go through all vocabularies for 6 passes, but also remember to review a particular list (unit of task) twice on the first day. So when you finally accomplished everything on the scheduler, you did it 8 passes.  

## Prerequisite

```
❯ pip3 install pandas
```

## Usage

```
❯ python scheduler2.py \
    --units=31 \
    --year=2020 \
    --month=5 \
    --date=3 \
    --name="Unit"
```
