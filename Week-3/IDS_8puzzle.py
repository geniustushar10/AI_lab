def iterative_deepening_search(src, target):

    depth_limit = 0

    while True:

        result = depth_limited_search(src, target, depth_limit, [])

        if result is not None:

            print("Success")

            return

        depth_limit += 1

        if depth_limit > 30:  # Set a reasonable depth limit to avoid an infinite loop

            print("Solution not found within depth limit.")

            return



def depth_limited_search(src, target, depth_limit, visited_states):

    if src == target:

        print_state(src)

        return src

    

    if depth_limit == 0:

        return None

    

    visited_states.append(src)

    poss_moves_to_do = possible_moves(src, visited_states)

    

    for move in poss_moves_to_do:

        if move not in visited_states:

            print_state(move)

            result = depth_limited_search(move, target, depth_limit - 1, visited_states)

            if result is not None:

                return result

    

    return None



def possible_moves(state, visited_states):

    b = state.index(0)

    d = []

    

    if b not in [0, 1, 2]: 

        d.append('u')

    if b not in [6, 7, 8]: 

        d.append('d')

    if b not in [0, 3, 6]: 

        d.append('l')

    if b not in [2, 5, 8]: 

        d.append('r')



    pos_moves_it_can = []

    

    for i in d:

        pos_moves_it_can.append(gen(state, i, b))

        

    return [move_it_can for move_it_can in pos_moves_it_can if move_it_can not in visited_states]



def gen(state, m, b):

    temp = state.copy()

    

    if m == 'd':

        temp[b + 3], temp[b] = temp[b], temp[b + 3]

    elif m == 'u':

        temp[b - 3], temp[b] = temp[b], temp[b - 3]

    elif m == 'l':

        temp[b - 1], temp[b] = temp[b], temp[b - 1]

    elif m == 'r':

        temp[b + 1], temp[b] = temp[b], temp[b + 1]



    return temp



def print_state(state):

    print(f"{state[0]} {state[1]} {state[2]}\n{state[3]} {state[4]} {state[5]}\n{state[6]} {state[7]} {state[8]}\n")

    

src = [1,2,3,0,4,5,6,7,8] 

target = [1,2,3,4,5,0,6,7,8] 



iterative_deepening_search(src, target)
