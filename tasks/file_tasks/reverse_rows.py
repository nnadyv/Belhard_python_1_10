"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""
from pathlib import Path


def revert_rows(text, new_text):

    with open(text, "r+") as t, open(new_text, "w") as t_new:
        for a in t:
            t_new.writelines(right_rows(a) + "\n")


def right_rows(line):
    line = line.split()
    new_dict = {}
    for idx, a in enumerate(line):
        if a[-1] in ",.":
            new_dict[idx] = a[-1]
        line[idx] = a.strip(",.")
    line.reverse()
    for i, l in new_dict.items():
        line[i] += l
    line = " ".join(line)
    return ". ".join(map(lambda v: v.strip().capitalize(), line.split(".")))


revert_rows(Path("text.txt"), Path("text1.txt"))
