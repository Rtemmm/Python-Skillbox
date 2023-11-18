with open("first_tour.txt") as f:
    candidates = [x for x in f.readlines()]
    total = int(candidates[0][:-1])
    winners = dict()

    for i_string in range(1, len(candidates)):
        candidate = candidates[i_string].split()
        if int(candidate[2]) > total:
            winners[(candidate[1][:1] + ".", candidate[0])] = int(candidate[2])

with open("second_tour.txt", "w") as f:
    winners = dict(sorted(winners.items(), reverse=True))
    for index, winner in enumerate(winners):
        f.write(f"{index+1}) {winner[0]}{winner[1]} {winners[winner]}\n")