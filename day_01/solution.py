import regex as re

digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


async def run_part_one(input_data: list[str]) -> int:
    sum = 0
    for line in input_data:
        numbers = re.findall(r"\d", line)
        assert len(numbers) > 0, "Invalid input data"
        first_number = numbers[0]
        last_number = numbers[-1]
        sum += int(first_number + last_number)
    return sum


async def run_part_two(input_data: list[str]) -> int:
    sum = 0
    numbers_regex = "|".join([f"{digit}" for digit in digits])
    numbers_regex = "[0-9]|" + numbers_regex
    for line in input_data:
        numbers = re.findall(numbers_regex, line, overlapped=True)
        assert len(numbers) > 0, "Invalid input data"
        first_number = numbers[0]
        last_number = numbers[-1]
        if first_number in digits:
            first_number = str(digits.index(first_number))
        if last_number in digits:
            last_number = str(digits.index(last_number))
        sum += int(first_number + last_number)
    return sum
