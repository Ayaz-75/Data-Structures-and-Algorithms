my_array = [7, 12, 9, 4, 11]

lowest_el = my_array[0]

for current_element in my_array:
    if lowest_el > current_element:
        lowest_el = current_element

print(lowest_el)