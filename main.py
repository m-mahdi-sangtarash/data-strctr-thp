import numpy as np
import project3_functions as p3f

index = None
num_array = np.array([0 for _ in range(50)])
loop_status = 'open'
sort = 0

while loop_status == 'open':
    print('''\t===========================================
    |  enter numbers :                     e  |
    |  remove a number:                    r  |
    |  insert a number in special index :  i  |
    |  sort number:                        s  |
    |  show numbers list:                  v  |
    |  show biggest number in list:        b  |
    |  find a number in list:              f  |
    |  exit:                               q  |
    ===========================================''')

    work = input('\n\tenter your task: ')

    if work == 'e':
        if index is None or index < 49:
            num_array, index, sort = p3f.numbers_receiver_func(num_array, index)
        else:
            print('Your list is currently full. To add a number, you must remove a number first.\nOur suggestion: '
                  'enter <r>')

    elif work == 'r':
        if index is None:
            print(
                'Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                'the letter <e>.')
        else:
            num_array, index = p3f.remove_num_func(num_array, index)
            continue

    elif work == 'i':
        try:
            if index < 49:
                num_array, index, sort = p3f.insert_num(num_array, index)
                continue
            elif index == 49:
                print('Your list is currently full. To add a number, you must remove a number first.\nOur suggestion: '
                      'enter <r>')
                continue
        except TypeError:
            print('Your list is empty now! suggestion: enter <e>')

    elif work == 's':
        if index is None:
            print('Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                  'the letter <e>.')
            continue
        else:
            num_array, index, sort = p3f.sort_lst_func(num_array, index)
            continue

    elif work == 'v':
        if index is None:
            print('Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                  'the letter <e>.')
        else:
            print(num_array[0:index + 1])
            continue

    elif work == 'q':
        print('Goodbye...!')
        break

    elif work == 'b':
        if index is None:
            print('Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                  'the letter <e>.')
        else:
            p3f.find_biggest(num_array,array)
            continue

    elif work == 'f':
        if sort == 1:
            p3f.binary_search_func(num_array, index)
        else:
            sort = p3f.is_sorted_func(num_array, index)
            if sort == 1:
                p3f.binary_search_func(num_array, index)
            else:
                p3f.linear_search_func(num_array, index)

    else:
        print('invalid value ! Pay attention to the list of operations.')
        continue
