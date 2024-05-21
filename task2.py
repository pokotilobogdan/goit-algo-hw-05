import random

def generate_sorted_list(length):
    sorted_list = []
    last_element = 0
    for _ in range(length):
        last_element += random.randint(0, 100)/100
        sorted_list.append(last_element)
    return sorted_list

def binary_search(searched_value, current_list, index_left, index_right, counter=0):
    
    middle_index = (index_right + index_left)//2
    
    # Якщо елемент зі списку дорівнює шуканому     АБО              ми маємо лише один елемент,                   який при цьому є верхньою межою:
    if current_list[middle_index] == searched_value or (len(current_list[index_left : index_right+1]) == 1 and current_list[middle_index] >= searched_value):
        counter += 1
        return counter, current_list[middle_index]
    
    # Або якщо маємо лише один елемент,                      І при цьому він не є верхньою межою:
    elif len(current_list[index_left : index_right+1]) == 1 and current_list[middle_index] < searched_value:
        counter += 1
        return None
    
    # Або якщо елемент більше шуканого:
    elif current_list[middle_index] > searched_value:
        counter += 1
        # продовжуємо пошук на зрізі           від index_left до middle_index ВКЛЮЧНО (враховуємо шанс верхньої межі)
        return binary_search(searched_value, current_list, index_left, middle_index, counter)
        
    # Або якщо елемент менше шуканого:
    elif current_list[middle_index] < searched_value:
        counter += 1
        # продовжуємо пошук на зрізі      від middle_index НЕВКЛЮЧНО   до index_right
        return binary_search(searched_value, current_list, middle_index + 1, index_right, counter)


if __name__ == "__main__":
    
    new_list = generate_sorted_list(int(input("How many numbers do you want to generate? ")))
    print()
    # print([number for number in map(lambda number: round(number, 2), new_list)])
    print(new_list)
    print()

    searched_number = float(input("Which number do you wanna search for? "))
    print()

    print(binary_search(searched_number, new_list, 0, len(new_list)-1))
