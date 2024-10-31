import json

import regex as re


async def run_part_one(input_data: list[str]) -> int:
    seeds = [int(s) for s in re.findall(r"\d+", input_data[0])]
    mapping = {}
    for i, line in enumerate(input_data[1:]):
        if not line:
            continue
        title = re.findall(r"([a-z]+)\-to\-([a-z]+) map:", line)
        if len(title) == 1:
            source, destination = title[0]
            mapping[source] = {"destination": destination, "mapping": []}
            continue
        dstart, sstart, l = re.findall(f"([0-9]+) ([0-9]+) ([0-9]+)", line)[0]
        mapping[source]["mapping"].append((int(dstart), int(sstart), int(l)))

    for key in mapping:
        mapping[key]["mapping"].sort(key=lambda x: x[0])

    current_source = "seed"
    current_ids = seeds.copy()
    while current_source != "location":
        for i, id in enumerate(current_ids):
            for dstart, sstart, l in mapping[current_source]["mapping"]:
                if id >= sstart and id < sstart + l:
                    current_ids[i] = dstart + id - sstart
                    break
        current_source = mapping[current_source]["destination"]
    return min(current_ids)


async def run_part_two(input_data: list[str]) -> int:
    seeds = [
        [int(s), int(s) + int(l) - 1]
        for s, l in re.findall(r"(\d+) (\d+)", input_data[0])
    ]
    mapping = {}
    for i, line in enumerate(input_data[1:]):
        if not line:
            continue
        title = re.findall(r"([a-z]+)\-to\-([a-z]+) map:", line)
        if len(title) == 1:
            source, destination = title[0]
            mapping[source] = {
                "destination": destination,
                "mapping": [],
            }
            continue
        d, s, l = re.findall(f"([0-9]+) ([0-9]+) ([0-9]+)", line)[0]
        mapping[source]["mapping"].append(
            (int(s), int(s) + int(l) - 1, int(d), int(d) + int(l) - 1)
        )

    for key in mapping:
        mapping[key]["mapping"].sort(key=lambda x: x[0])

    current_source = "seed"
    current_ids = seeds.copy()
    while current_source != "location":
        new_ids = []
        current_ids.sort(key=lambda x: x[0])
        current_mapping = mapping[current_source]["mapping"]
        print(current_ids)
        print(current_mapping)
        left_bound = current_ids[0][0]
        right_bound = max(mapping[current_source]["mapping"][0][0], current_ids[0][0])
        print(left_bound, right_bound)
        left_bound = min(right_bound + 1, current_ids[0][1])
        right_bound = max(mapping[current_source]["mapping"][0][0], current_ids[0][0])
        print(left_bound, right_bound)
        # print(current_ids)
        # for i, id in enumerate(current_ids):
        #     for dstart, sstart, l in mapping[current_source]["mapping"]:
        #         if id >= sstart and id < sstart + l:
        #             current_ids[i] = dstart + id - sstart
        #             break
        current_source = mapping[current_source]["destination"]
    return 0
