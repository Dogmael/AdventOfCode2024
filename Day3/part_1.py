import re


with open('input.txt', "r") as file :
    text = file.read()

# SOLUTION 1 WITH REGEX
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, text)

result = 0

if matches:
    print(matches)
    for match in matches:
        result += (int(match[0]) * int(match[1]))

print(result)