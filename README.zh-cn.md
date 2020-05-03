# Vocab-Scheduler 0.2

[English](README.md)

## 开始

在 scheduler 0.2 中，我重新设计并重写了整个程序，它现在使用更少的代码，并增加了额外的功能。scheduler 0.2 会读取命令行参数并创建一个 `.csv` 文件，这个文件中包含了你的任务安排（基于 Ebbinghaus 遗忘曲线），并请使用 Microsoft Excel 打开它。

注意：这个安排表会让使用者背 6 遍所有的单词，但请记住一定要在背某个单元的时候，当天再额外复习两遍，所以当你完成这个安排表上的所有内容的时候，你总共背了 8 遍。

## 安装

```
❯ pip3 install pandas
```

## 使用方法

```
❯ python scheduler2.py \
    --units=31 \
    --year=2020 \
    --month=5 \
    --date=3 \
    --name="Unit"
```