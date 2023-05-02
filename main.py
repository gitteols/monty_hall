
# main.py
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
    
    participant_choice = input("문을 선택하세요 (왼쪽, 가운데, 오른쪽 중에서 선택): ")
    
    select_door_index = Input_to_index(participant_choice)
    
    
    door_index = [0,1,2]

    new_choice = -1
    # print(door_index)
    change_choice = input(f'문을 바꾸시겠습니까? y/n')
    
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



# main

import random

def monte_carlo_simulation(change_choice, num_trials):
    num_wins = 0
    
    for i in range(num_trials):
        # 게임 시뮬레이션
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        choice = random.randint(0, 2)
        
        if change_choice:
            # 선택을 변경한 경우
            new_choice = [i for i in range(3) if i != choice and doors[i] == 'goat'][0]
            # 염소가 아닌 다른 문 중에서 선택 가능한 문을 선택합니다.
            new_choice = [i for i in range(3) if i != choice and i != new_choice][0]
            if doors[new_choice] == 'car':
                num_wins += 1
        else:
            # 선택을 유지한 경우
            if doors.count('car') == 1 and doors[choice] == 'car':
                num_wins += 1
    
    win_rate = num_wins / num_trials
    return win_rate



def game_intro():
    print("안녕하세요 플레이어님! 몬티홀 문제(Monty Hall problem) 게임에 참가해 주셔서 감사드립니다.")
    print("여기 세 개의 문이 있습니다. 하나의 문 뒤에는 자동차가, 나머지 두 개의 문 뒤에는 염소가 있습니다.")
    print("플레이어님은 지금부터 다음 세 개의 문 중 마음에 드는 문 하나를 선택합니다.")
    print("마음에 드는 문을 고르셨나요?")
    print("그럼 제가 플레이어님이 선택하지 않은 두 문중 하나의 문을 열겠습니다.")
    print("이 문 뒤에 있는 것은 염소였습니다!")
    print("자 이제 자동차는 플레이어님이 고르신 문과, 선택하지 않은 문. 두 곳중 한곳에 있습니다.")
    print("처음 고르신 문에서 다른 문으로 변경하실 기회를 드리겠습니다. 다른 문으로 선택을 변경하시겠습니까?")



wonCount = 0
game_intro()
gameCount = int(input("게임 몇번 할래? :"))
for i in range(gameCount):
    isWon = play_game()

    if isWon == 1:
        wonCount +=1 


