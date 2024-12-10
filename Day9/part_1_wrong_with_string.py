def disk_map_to_blocks(disk_map: str) -> str:
    blocks = ""  # DO NOT USE STRING. file_ID_number > 9 we can't split it easy. E.G : '999899989998..999999999999' -> [9998,9998,9998,-1,-1,9999,9999,9999]
    file_ID_number = 0
    file = True  # We are on file block

    for i in range(len(disk_map)):

        if disk_map[i] == "0":
            continue

        if file:
            blocks += str(file_ID_number) * int(disk_map[i])
            file_ID_number += 1
        else:
            if disk_map[i] != "0":
                blocks += "." * int(disk_map[i])

        if disk_map[min(i + 1, len(disk_map) - 1)] != "0":
            file = not file

    return blocks


def remove_gap_between_blocks(blocks):
    # blocks = list(blocks) -> WARNING DO NOT DO THIS : '99999999'-> '9','9','9','9','9','9','9','9' event if it is '9999', '9999'
    i, j = 0, len(blocks) - 1

    while i < j:
        if blocks[i] != ".":
            i += 1
        elif blocks[j] == ".":
            j -= 1
        else:
            blocks[i] = blocks[j]
            blocks[j] = "."

    return "".join(blocks)


def calculate_checksum(block_without_gap: str) -> int:
    checksum = 0

    for i, char in enumerate(block_without_gap):
        if char == ".":
            return checksum
        checksum += i * int(char)

    return checksum


with open("input.txt") as file:
    input = file.read().split("\n")[0]

print(input)

blocks_with_gaps = disk_map_to_blocks(input)
print(blocks_with_gaps)

block_without_gaps = remove_gap_between_blocks(blocks_with_gaps)
print(block_without_gaps)

checksum = calculate_checksum(block_without_gaps)
print(checksum)

# 91235952521 too low

# right answer : 6415184586041
