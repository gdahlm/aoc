"""AoC 2024 Day 15 Task 1"""
import re
from dataclasses import dataclass


#File handling
def fread_line(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]
