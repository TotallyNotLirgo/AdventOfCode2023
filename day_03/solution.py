import regex as re

symbol_coords = []
number_coords = []

def find_cords(
    input_data: list[str],
) -> tuple[list[tuple[int, int]], list[tuple[int, int, int, str]]]:
    symbol_coords = []
    number_coords = []
    for y, line in enumerate(input_data):
        symbols = re.finditer(r"[^0-9\.a-z]", line)
        numbers = re.finditer(r"[0-9]+", line)
        for symbol in symbols:
            x = symbol.start()
            symbol_coords.append((x, y))
        for number in numbers:
            x = number.start()
            x_max = number.end() - 1
            number_coords.append((x, x_max, y, number.group()))
    return symbol_coords, number_coords


def is_adjacent(
    symbol: tuple[int, int], number: tuple[int, int, int, str]
) -> int:
    sx = symbol[0]
    sy = symbol[1]
    nx_min = number[0]
    nx_max = number[1]
    ny = number[2]
    num = int(number[3])
    if abs(ny - sy) > 1:
        return 0
    if nx_min <= sx - 1 <= nx_max:
        return num
    if nx_min <= sx - 0 <= nx_max:
        return num
    if nx_min <= sx + 1 <= nx_max:
        return num
    return 0


async def run_part_one(input_data: list[str]) -> int:
    symbol_coords, number_coords = find_cords(input_data)
    return sum(
        [
            is_adjacent(symbol, number)
            for symbol in symbol_coords
            for number in number_coords
        ]
    )


async def run_part_two(input_data: list[str]) -> int:
    symbol_coords, number_coords = find_cords(input_data)
    gear_ratio_sum = 0
    for symbol in symbol_coords:
        numbers = [is_adjacent(symbol, number) for number in number_coords]
        numbers.sort(reverse=True)
        index_1 = numbers.index(0)
        ratios = numbers[:index_1]
        if len(ratios) != 2:
            continue
        gear_ratio_sum += ratios[0] * ratios[1]
    return gear_ratio_sum
