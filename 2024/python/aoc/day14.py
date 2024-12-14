"""AoC <YEAR> <DAY> <TASK>"""

# (Width (x), Height (y))
test_board_size = (11, 7)
input_board_size = (101, 103)

def fread_line(file_path: str):
    """Lazy read of file returning a generator"""
    with open(file_path, "r", encoding="utf-8") as file_in:
        yield from file_in

def movement(time_ticks: int,position: tuple, velocity: tuple, board_size:tuple) -> tuple:
    board_width, board_height = board_size
    x_vel, y_vel = velocity
    x, y = position
    x += time_ticks * x_vel
    y += time_ticks * y_vel
    x = x % board_width
    y = y % board_height
    return (x,y)

def parse_data(fname):
    finput = list(fread_line(fname))
    finput = [x.strip() for x in finput]
    data = [x.strip('p=').split(' v=') for x in finput]
    return data

def get_endpoints(data, board_size):
    points = []
    for item in data:
        loc, velocity = item
        cur_x, cur_y = loc.split(',')
        cur_x, cur_y = int(cur_x), int(cur_y)
        xvel, yvel = velocity.split(',')
        xvel, yvel = int(xvel), int(yvel)
        position = (cur_x,cur_y)
        velocity = (xvel,yvel)

        _ = movement(100, position, velocity, board_size)
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

def main(fname='data/input/14.txt') -> None:
    """Main function"""
    #board_size = (11, 7)

    board_size = (101, 103)
    #board_width, board_height = board_size

    data = parse_data(fname)
    endpoints = get_endpoints(data, board_size)
    sector_count = score_it(endpoints,board_size)

    return sector_count

if __name__ == "__main__":
    print(main())
