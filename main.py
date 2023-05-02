# main

import random

def Input_to_index(input:str):
    if input == '왼쪽': 
        return 0
    elif input == '가운데': 
        return 1
    elif input == '오른쪽': 
        return 2
    else:
        print('잘못입력하셨습니다.')
        Input_to_index()

def play_game():
    car_door = random.randint(0,2)
    print(car_door)
    participant_choice = input("문을 선택하세요 (왼쪽, 가운데, 오른쪽 중에서 선택): ")
    
    select_door_index = Input_to_index(participant_choice)
    print(select_door_index)
    
    door_index = [0,1,2]

    new_choice = -1
    # print(door_index)
    change_choice = input(f'문을 바꾸시겠습니까? y/n')
    print(change_choice)
    if change_choice == 'y':
         # 선택한 문 이외의 문 선택
         rand_choice =  random.randrange(0, 2)
         door_index.remove(select_door_index)
         new_choice = door_index[rand_choice]
         if new_choice == car_door:
             return 1
         else:
             return 0
    elif change_choice == 'n':
        if select_door_index == car_door:
            return 1
        else:
            return 0
    else:
        print('error')

print(play_game())
