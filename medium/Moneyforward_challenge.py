import random

def main(lines):
    guests = []
    initial_map = {}
    for i, v in enumerate(lines):
        if i == 0:
            continue
        guest = [int(num) for num in v.split(" ")]
        guests.append(guest)
        # map all the guests by their second initial:
        if guest[1] not in initial_map:
            initial_map[guest[1]] = {}
        if guest[0] not in initial_map[guest[1]]:
            initial_map[guest[1]][guest[0]] = []
        initial_map[guest[1]][guest[0]].append(i - 1)
    
    # and not we can traverse all the guests and search their pair in the initial_map
    # searching a map index that the same as the first initial of the current guest.
    # we have to store already taken guests for not making duplicates
    taken = []
    res = 0
    for guest_num, guest in enumerate(guests):
        # if this guest already taken - skip
        if guest_num in taken:
            continue
        # if no pair for this guest = continue
        if guest[0] not in initial_map:
            continue
        if guest[1] not in initial_map[guest[0]]:
            continue
        # check all the pairs and take one that matches
        for i, pair_num in enumerate(initial_map[guest[0]][guest[1]]):
            # don't take the same quest:
            if pair_num == guest_num:
                continue
            # if this guest already taken - skip
            if pair_num in taken:
                continue

            res += 1
            taken.append(guest_num)
            taken.append(pair_num)
            break

    print(res)


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
