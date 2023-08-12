import random
from collections import defaultdict

def main(lines):
    pairs = 0

    # let's make a map of guests by their SECOND initials
    initial_map = defaultdict(dict)
    for i, v in enumerate(lines):
        # first element in the input is a number of lines so skip it
        if i == 0:
            continue

        guest = v.split(" ")

        if guest[1] in initial_map and guest[0] in initial_map[guest[1]] and initial_map[guest[1]][guest[0]] > 0:
            pairs += 1
            initial_map[guest[1]][guest[0]] -= 1
        elif guest[0] in initial_map and guest[1] in initial_map[guest[0]]:
            initial_map[guest[0]][guest[1]] += 1
        else:
            initial_map[guest[0]][guest[1]] = 1

    print(pairs)

if __name__ == '__main__':
    n = 10

    lines = []
    lines.append("00")
    pairs = 0
    for i in range(1, n + 1):
        for j in range(10 * n + 1, 11 * n + 1):
            lines.append(str(i) + " " + str(j))
            if random.random() >= 0.5:
                lines.append(str(j) + " " + str(i))
                pairs += 1

    print(lines)
    print("pairs:", pairs)


    main(lines)
