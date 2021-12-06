import typing

from utils.task import print_result

LIFECYCLE = 8
SPAWNED_LIFE = 8
REBORN_LIFE = 6

def parse_input(input_file) -> typing.List[int]:
    with open(input_file) as f:
        return [int(x) for x in f.read().split(',')]

def simulate(genesis, days):
    baskets = dict(zip(range(LIFECYCLE+1),[0]*(LIFECYCLE+1)))

    for fish in genesis:
        baskets[fish] += 1
    
    for _ in range(0,days):
        to_spawn = baskets[0]
        
        for i in range(1,LIFECYCLE+1):
            baskets[i-1] = baskets[i]

        baskets[REBORN_LIFE] += to_spawn
        baskets[SPAWNED_LIFE] = to_spawn

    return sum(baskets.values())

if __name__ == "__main__":
    genesis = parse_input('day6/input.txt')
    print_result(1,simulate(genesis, 80))
    print_result(2,simulate(genesis, 256))