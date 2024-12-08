
from typing import List, Dict, Tuple
from itertools import combinations

def get_antennas_coordinates(text_matrix: List) -> Dict[str, List[Tuple[int, int]]]:
    """
    Parse antennas frequency an coordinates from text file.

    Args:
        text (str): text inpt

        Example :   ............
                    ........0...
                    .....0......
                    .......0....
                    ....0.......

    Returns:
        Dict[str, List[Tuple[int, int]]]:
            key : Antenna frequency
            value : List of coordinates of antennas for a given frequency

        Example : {'0': [(1, 8), (2, 5), (3, 7), (4, 4)]}
    """

    antennas_coordinates = {}
    
    for row in range(len(text_matrix)) :
        for column in range(len(text_matrix[row])) :
            char = text_matrix[row][column]
            if(char != '.') :
                if (char in antennas_coordinates) :
                    antennas_coordinates[char].append((row,column))
                else :
                    antennas_coordinates[char] = [(row,column)]
    
    return antennas_coordinates

def get_antennas_couples(antennas_coordinates: Dict[str, List[Tuple[int, int]]]) -> Dict[str, List[Tuple[Tuple[int, int], Tuple[int, int]]]]:
    """
    Generate all possible couples of antennas for each frequency.

    Args:
        antennas_coordinates (Dict[str, List[Tuple[int, int]]]):
            key : Antenna frequency
            value : List of coordinates of antennas for a given frequency

        Example:
            {'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'A': [(5, 6), (8, 8)] }
    Returns:
        Dict[str, List[Tuple[Tuple[int, int], Tuple[int, int]]]]: 
            key : Antenna frequency
            value : List of tuples of couples of antennas coordinates combinations for a given frequency

        Example:
            { '0': [((1, 8), (2, 5)), ((1, 8), (3, 7)), ...], 'A': [((5, 6), (8, 8))] }
    """
    
    antennas_couples = {}

    for frequency, coordinates in antennas_coordinates.items():
        #Warning : We get COMBINATIONS not PERMUTATIONS
        antennas_couples[frequency] = list(combinations(coordinates, 2)) # combinations(antennas_coordinates[frequency] return an iterator

    return antennas_couples

def get_antinodes_from_couple(antennas_couple: Tuple[Tuple[int, int], Tuple[int, int]], map: List[str]) -> List[Tuple[int, int]]:
    """
    Calculate the coordinates of antinodes created by a pair of antennas.

    Args:
        antennas_couple (Tuple[Tuple[int, int], Tuple[int, int]]): A tuple containing 
        the coordinates of two antennas.

        Example: ((1, 8), (2, 5))

    Returns:
        List[Tuple[int, int]]: A list containing the coordinates of the antinodes.

        Example: [(1, 8), (0, 11), (2, 5), (3, 2)]
    """

    (x_1, y_1), (x_2, y_2) = antennas_couple # TO REMEMBER: Unpack tuple

    vector_1_to_2 = (x_2 - x_1, y_2 - y_1)

    antinodes = []

    cpt = 0 # DO NOT FORGET TO START FROM 0
    while True  :
        antinode_1 = (x_1 - cpt * vector_1_to_2[0], y_1 - cpt * vector_1_to_2[1])
        if point_is_in_map(antinode_1, map) :
            antinodes.append(antinode_1)
            cpt += 1
        else :
            break

    cpt = 0
    while True :
        antinode_2 = (x_2 + cpt * vector_1_to_2[0], y_2 + cpt * vector_1_to_2[1])
        if point_is_in_map(antinode_2, map):
            antinodes.append(antinode_2)
            cpt += 1
        else :
            break


    return antinodes

def point_is_in_map(point : Tuple, map: List[str]) -> bool :
    """Check if a point is in map

    Args:
        point (Tuple): Point to check
        map (Dict[str]): Map

    Returns:
        bool: True if point is in map, False otherwise
    """    
    return (point[0] >= 0 and point[0] < len(map)) and (point[1] >= 0 and point[1] < len(map[0])) # DO NOT INCLUDE len(...) in accepted values

def print_antinodes(antinodes: List, map: List[str]) -> None :
    """
    Debug purpose
    """

    for row in range(len(map)) :
        for col in range(len(map[0])) :
            if (row,col) in antinodes:
                print('#', end = '')
            else :
                print('.', end = '')
        print('\n')

def get_antinodes_total_number(file_name: str) -> int:
    """Get the total number of antinodes in the map.

    Args:
        file_name (str): File name

    Returns:
        int: Total number of antinodes in the map
    """

    with open(file_name) as file : 
        map_text = file.read()

    map = map_text.split()
    
    antennas_coordinates = get_antennas_coordinates(map)
    antennas_couples = get_antennas_couples(antennas_coordinates)

    antinodes = []

    for frequency in antennas_couples :
        for couple in antennas_couples[frequency] :
            antinodes_from_couple = get_antinodes_from_couple(couple, map)
            antinodes += antinodes_from_couple.copy()

    return len(set(antinodes)) # WARNING: We need to remove duplicates

print(get_antinodes_total_number('input.txt'))

