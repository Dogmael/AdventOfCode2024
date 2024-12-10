def disk_map_to_blocks(disk_map: str) -> str:
    blocks = []
    file_ID_number = 0
    file = True  # We are on file block

    for i in range(len(disk_map)):

        if disk_map[i] == "0":
            continue

        if file:
            blocks += [file_ID_number] * int(disk_map[i])
            file_ID_number += 1
        else:
            if disk_map[i] != "0":
                blocks += [-1] * int(disk_map[i])

        if disk_map[min(i + 1, len(disk_map) - 1)] != "0":
            file = not file

    return blocks


def remove_gap_between_blocks(blocks):
    i, j = 0, len(blocks) - 1

    while i < j:
        if blocks[i] != -1:
            i += 1
        elif blocks[j] == -1:
            j -= 1
        else:
            blocks[i] = blocks[j]
            blocks[j] = -1

    return blocks


def calculate_checksum(block_without_gap: str) -> int:
    checksum = 0

    for i, file_ID_number in enumerate(block_without_gap):
        if file_ID_number == -1:
            return checksum
        checksum += i * file_ID_number

    return checksum


with open("input.txt") as file:
    input = file.read().split("\n")[0]

print(input)

blocks_with_gaps = disk_map_to_blocks(input)
print("".join([str(i) if i != -1 else "." for i in blocks_with_gaps]))

block_without_gaps = remove_gap_between_blocks(blocks_with_gaps)
print("".join([str(i) if i != -1 else "." for i in block_without_gaps]))

checksum = calculate_checksum(block_without_gaps)
print(checksum)

# 91235952521 too low

# right answer : 6415184586041
