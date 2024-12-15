"""AoC 2024 Day 15 Task 1"""
import re
from dataclasses import dataclass


#File handling
def read_file(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

def clean_data(filename):
    raw_input = read_file(filename)
    board = []
    moves = []
    for line in raw_input:
        match line:
            case "":
                pass
            case x if '#' in line:
                board.append(line)
            case _:
                moves.append(line)

