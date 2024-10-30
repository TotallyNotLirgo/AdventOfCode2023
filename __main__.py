import asyncio
from day_01 import solution as day_01_solution

async def main():
    print(f"{' Day 1 ':-^80}")
    with open("day_01/input.txt") as f:
        data = f.read().splitlines()
    print(await day_01_solution.run_part_one(data))
    print(await day_01_solution.run_part_two(data))


if __name__ == "__main__":
    asyncio.run(main())
