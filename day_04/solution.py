import regex as re

async def run_part_one(input_data: list[str]) -> int:
    total_score = 0
    for line in input_data:
        winning, mine = re.findall(r": ([0-9 ]+) \| ([0-9 ]+)", line)[0]
        winning_numbers = re.findall(r"\d+", winning)
        my_numbers = re.findall(r"\d+", mine)
        score = 0
        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                score += 1
        if score > 0:
            total_score += 1 << (score - 1)
    return total_score

async def run_part_two(input_data: list[str]) -> int:
    card_counts = [1 for _ in input_data]
    for i, line in enumerate(input_data):
        winning, mine = re.findall(r": ([0-9 ]+) \| ([0-9 ]+)", line)[0]
        winning_numbers = re.findall(r"\d+", winning)
        my_numbers = re.findall(r"\d+", mine)
        score = 0
        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                score += 1
        for j in range(score):
            card_counts[i + j + 1] += card_counts[i]
    return sum(card_counts)
