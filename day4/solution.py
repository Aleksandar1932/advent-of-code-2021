import numpy as np

from utils.task import print_result

REPLACEMENT_ELEMENT = -1

def parse_input(filename:str):

    with open(filename, 'r') as f:
        draws = f.readline().split(',')
        draws = list(map(lambda x: int(x), draws))

        current_ticket = []
        tickets = []
        for idx, line in enumerate(f.readlines()):
            tokens = line.split()
            if (len(tokens) > 0):
                current_ticket.append(list(map(lambda x: int(x), tokens)))
            else:
                tickets.append(np.array(current_ticket))
                current_ticket = []

    return draws, tickets[1:]


def task_1(draws, tickets):
    for draw in draws:
        for ticket in tickets:
            if draw in ticket:
                ticket[ticket == draw] = REPLACEMENT_ELEMENT
                if WON_ROL_COL_SUM in ticket.sum(axis = 1) or WON_ROL_COL_SUM in ticket.sum(axis = 0):
                    # winniing ticket
                    ticket[ticket == REPLACEMENT_ELEMENT] = 0
                    return ticket.sum() * draw

def task_2(draws, tickets):
    scores = []
    for draw in draws:
        for ticket in tickets:
            if draw in ticket:
                ticket[ticket == draw] = REPLACEMENT_ELEMENT
                if WON_ROL_COL_SUM in ticket.sum(axis = 1) or WON_ROL_COL_SUM in ticket.sum(axis = 0):
                    # winniing ticket
                    ticket[ticket == REPLACEMENT_ELEMENT] = 0
                    score = ticket.sum() * draw
                    if score != 0:
                        scores.append(score)

    return scores[-1]


if __name__ == '__main__':
    draws, tickets = parse_input('day4/input.txt')

    WON_ROL_COL_SUM = REPLACEMENT_ELEMENT * len(tickets[1][0])

    print_result(1,task_1(draws, tickets))
    print_result(1,task_2(draws, tickets))
