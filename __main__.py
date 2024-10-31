import asyncio
from types import ModuleType
from day_01 import solution as day_01_solution
from day_02 import solution as day_02_solution
from day_03 import solution as day_03_solution
from day_04 import solution as day_04_solution
from day_05 import solution as day_05_solution

async def run_day(day: int, solution: ModuleType):
    print(f"{f' Day {day} ':-^80}")
    with open(f"inputs/day_{day:02}") as f:
        data = f.read().splitlines()
    print(await solution.run_part_one(data))
    print(await solution.run_part_two(data))

async def main():
    # await run_day(1, day_01_solution)
    # await run_day(2, day_02_solution)
    # await run_day(3, day_03_solution)
    # await run_day(4, day_04_solution)
    await run_day(5, day_05_solution)


if __name__ == "__main__":
    asyncio.run(main())
