def sort_lst_func(num_array, index):
    for turn in range(0, index):
        for num_checker in range(0, index):
            if num_array[num_checker] > num_array[num_checker + 1]:
                num_array[num_checker + 1] += num_array[num_checker]
                num_array[num_checker] = num_array[num_checker + 1] - num_array[num_checker]
                num_array[num_checker + 1] -= num_array[num_checker]
            else:
                continue
    sort = 1
    print('The list of numbers is sorted in ascending order.')
    return num_array, index, sort


def numbers_receiver_func(num_array, index):
    while 0 < 1:
        if index is None:
            try:
                num_array[0] = int(input('enter your number (If you want to end this operation, you can enter a '
                                         'letter.): '))
                index = 0
                sort = 0
            except ValueError:
                return num_array, index

        else:
            for i in range(index, 50):
                try:
                    num_array[index + 1] = int(input('enter your number (If you want to end this operation, you can '
                                                     'enter a letter.): '))
                    index += 1
                    sort = 0
                except ValueError:
                    break
            return num_array, index, sort


def remove_num_func(num_array, index):
    while 0 < 1:
        try:
            remove_ind = int(input(f'please select number place (between 0 - {index}:'))
            break
        except ValueError:
            print('\ninvalid value! please try again.')
            continue
    turn = remove_ind
    while turn < index:
        num_array[turn] = num_array[turn + 1]
        turn += 1

    index -= 1
    print('\n number removed!')
    return num_array, index


def insert_num(num_array, index):
    while 0 < 1:
        try:
            add_index = int(input(f'Choose the place to add the number you want.(between 0 - {index + 1}: )'))
            if add_index > (index + 1) or add_index < 0:
                print('invalid index!. try again.')
                continue
            else:
                break
        except ValueError:
            print('invalid value! try again!')
            continue

    while 0 < 1:
        try:
            add_number = int(input('enter your number: '))
            break
        except ValueError:
            print('\ninvalid Value! Try again.\n')
            continue

    if add_index == index + 1:
        index += 1
        num_array[index] = add_number

    else:
        replacer = index
        index += 1
        while replacer >= add_index:
            num_array[replacer + 1] = num_array[replacer]
            replacer -= 1
        num_array[add_index] = add_number
    sort = 0
    print(f'number {add_number} add to {add_index}th section.')
    return num_array, index, sort


def linear_search_func(num_array, index):
    while 0 < 1:
        try:
            item = int(input('enter your number ke mikhay peyda konam: '))
            break
        except ValueError:
            print('invalid value! please try again.')
            continue
    m = index
    while num_array[m] != item and m <= index:
        m += 1
    if num_array[m] == item:
        print(f'item {item} is in {m}th index.')
    else:
        print(f'item {item} not found!')


def binary_search_func(num_array, index):
    while 0 < 1:
        try:
            item = int(input('enter your number: '))
            break
        except ValueError:
            continue
    ub = index
    m = int(ub / 2)
    lb = 0
    while num_array[m] != item and ub >= lb:
        if item < num_array[m]:
            ub = m - 1
        else:
            lb = m + 1
        m = int((ub + lb) / 2)
    if item == num_array[m]:
        print(f'{item} in {m} index')
    else:
        print('item not found!')


def is_sorted_func(num_array, index):
    check_index = 0
    while num_array[check_index] < num_array[check_index] and check_index < index:
        check_index += 1
    if check_index == index:
        sort = 1
    else:
        sort = 0
    return sort


def find_biggest(num_array, index):
    big_index = 0
    big_number = num_array[big_index]
    while big_index < index:
        if big_number < num_array[big_index + 1]:
            big_number = num_array[big_index + 1]
            big_index += 1
        else:
            big_index += 1
            continue

    print(f'biggest number in list is: {big_number}')
