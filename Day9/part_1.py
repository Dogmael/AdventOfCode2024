from typing import List


def disk_map_to_blocks(disk_map: str) -> List[int]:
    """Convert disk map to blocks (free or with data)

    Args:
        disk_map (str): Disk map. The digits alternate between indicating the length of a file and the length of free space.
            A disk map like 90909 would represent three nine-block files in a row (with no free space between them).

        Example : '12345'

    Returns:
        List[int]: List of blocks (free or with data).
        The disk map 12345 has three files: a one-block file with ID 0, a three-block file with ID 1, and a five-block file with ID 2.

        Example :  '0..111....22222' but format in a list of string (check 'part_1_wrong_with_string.py' to undersand why) ->
        [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9]
    """
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


def remove_gap_between_blocks(blocks: List[int]) -> List[int]:
    """Move file blocks one at a time from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks).

    Args:
        blocks (List[int]): List of blocks (free or with data).

        Example : [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9]

    Returns:
        List[int]: List of blocks (free or with data) without gap between blocks of data. All empty blocks are at the end of the list.

        Example : [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    """
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


def calculate_checksum(block_without_gap: List[int]) -> int:
    """Calculate the checksum of the blocks

    Example : 00998 -> 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32 -> 77

    Args:
        block_without_gap (List[int]): List of blocks (free or with data) without gap between blocks of data. All empty blocks are at the end of the list.

        Example : [0, 0, 9, 9, 8]

    Returns:
        int: Checksum of the blocks.

        Example : 77
    """
    checksum = 0

    for i, file_ID_number in enumerate(block_without_gap):
        if file_ID_number == -1:
            return checksum
        checksum += i * file_ID_number

    return checksum


def disk_map_to_checksum(file_name: str) -> int:
    """Calculate the checksum of the disk map

    Args:
        file_name (str): File name containing the disk map.

    Returns:
        int: Checksum of the disk map.
    """
    with open(file_name) as file:
        disk_map = file.read()
    # print(disk_map)

    blocks_with_gaps = disk_map_to_blocks(disk_map)
    # print(blocks_with_gaps)
    # print("".join([str(i) if i != -1 else "." for i in blocks_with_gaps]))

    block_without_gaps = remove_gap_between_blocks(blocks_with_gaps)
    # print(block_without_gaps)
    # print("".join([str(i) if i != -1 else "." for i in block_without_gaps]))

    checksum = calculate_checksum(block_without_gaps)
    return checksum


print(disk_map_to_checksum("input.txt"))
