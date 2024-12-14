"""AoC <YEAR> <DAY> <TASK>"""

# (Width (x), Height (y))
test_board_size = (11, 7)
input_board_size = (101, 103)

def fread_line(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

def movement(time_ticks: int,position: tuple, velocity: tuple, board_size:tuple) -> tuple:
    board_width, board_height = board_size
    x_vel, y_vel = velocity
    x, y = position
    x += time_ticks * x_vel
    y += time_ticks * y_vel
    x = x % board_width
    y = y % board_height
    return (x,y)

def parse_data(file_name):
    finput = fread_line(file_name)
    data = [x.strip('p=').split(' v=') for x in finput]
    return data

def get_endpoints(data, board_size, steps=100):
    points = []
    for item in data:
        loc, velocity = item
        cur_x, cur_y = loc.split(',')
        cur_x, cur_y = int(cur_x), int(cur_y)
        xvel, yvel = velocity.split(',')
        xvel, yvel = int(xvel), int(yvel)
        position = (cur_x,cur_y)
        velocity = (xvel,yvel)

        _ = movement(steps, position, velocity, board_size)
        #print(_)

        points.append(_)

    return points

def score_it(points, board_size)-> int:
    board_width, board_height = board_size
    total = 1
    res = {'NW':0, 'NE':0, 'SE':0, 'SW': 0}
    x_center = (board_width-1)//2
    y_center =  (board_height-1)//2
    for point in points:
        x, y = point
        if x == x_center  or y == y_center:
            pass
        elif x < x_center and y > y_center:
            res['NW'] +=1
        elif x > x_center and y > y_center:
            res['NE'] +=1
        elif x < x_center and y < y_center:
            res['SW'] +=1
        elif x > x_center and y < y_center:
            res['SE'] +=1

        #print((x,y))
    for item in res.items():
        _, value = item
        if value != 0:
            total *= value
    return total

def print_points(points, board_size):
    x_len, y_len = board_size
    cols, rows = x_len, y_len
    board = []
    for row in range(rows):
        board.append([['.'] for x in range(cols)])
    for point in set(points):
        col, row = point
        board[row][col] = ['#']

    for item in board:
        print(''.join([''.join(x) for x in item]))

def find_min(data, board_size, r_min=100, r_max=10000):
    min_score = None
    res = None
    for steps in range(r_min, r_max):
        endpoints = get_endpoints(data, board_size, steps)
        score = score_it(endpoints,board_size)
        if min_score is None:
            min_score = score
        if score < min_score:
            min_score = score
            res = steps

    return res

def main(fname='data/input/14.txt') -> int:
    """Main function"""
    #board_size = (11, 7)

    board_size = (101, 103)
    #board_width, board_height = board_size

    data = parse_data(fname)
    endpoints = get_endpoints(data, board_size)
    sector_count = score_it(endpoints,board_size)

    return sector_count


def main2(fname='data/input/14.txt') -> int:
    # Task 2
    board_size = (101, 103)

    data = parse_data(fname)
    min_score = find_min(data, board_size, r_min=2000, r_max=10000)

    return min_score

if __name__ == "__main__":
    print('Task 1:',main())
    print('Task 2:',main2())
