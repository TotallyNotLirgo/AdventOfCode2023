import regex as re

async def run_part_one(input_data: list[str]) -> int:
    max_red = 12
    max_green = 13
    max_blue = 14
    impossible_id_sum = 0
    for line in input_data:
        game_id = re.findall(r"Game (\d+):", line)[0]
        reveals_string = line.split(":")[1].strip()
        reveals = reveals_string.split(";")
        for reveal in reveals:
            red = re.findall(r"(\d+) red", reveal)
            red = int(red[0]) if red else 0
            green = re.findall(r"(\d+) green", reveal)
            green = int(green[0]) if green else 0
            blue = re.findall(r"(\d+) blue", reveal)
            blue = int(blue[0]) if blue else 0
            if red > max_red or green > max_green or blue > max_blue:
                impossible_id_sum += int(game_id)
    return impossible_id_sum


async def run_part_two(input_data: list[str]) -> int:
    return 0
