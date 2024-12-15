"""AoC 2024 Day 15 Task 1"""
import re
from dataclasses import dataclass


#File handling
def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

def clean_data(filename:str) -> list[list[str]]:
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
    return board, moves

def parse_move(move:chr) -> tuple:
    """Return move tuple"""
    match move:
        case '^':
            print('Up')
            return((-1,0))
        case 'v':
            print('Down')
            return((1,0))
        case '>':
            print('Right')
            return((0,1))
        case '<':
            print('Left')
            return((0,-1))

def look_ahead(location:tuple, move_mask:tuple):
    #TODO
    return None

def move_boxes():
    #TODO
    return None

def score_it():
    #TODO
    return None