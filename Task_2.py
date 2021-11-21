"""
Create a function that takes a list of integers and returns
what the smallest number is in.

Do not use built-in functions.

eg for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5,
because the smallest element is found at this index in this list.
"""

if __name__ == '__main__':

    int_list = [42, 13, 56, 7, 12, 3, 85]
    print(int_list)

    min_num = int_list[0]
    min_index = 0
    for i in range(1, len(int_list)):
        # print(i, int_list[i])
        if min_num < int_list[i]:
            min_num = min_num
            min_index = min_index
        else:
            min_num = int_list[i]
            min_index = i

    print(f'Smallest element is {min_num}. \nIndex of the smallest element is {min_index}')
