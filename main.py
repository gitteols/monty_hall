
# main.py
import random

def Input_to_index(input:str):
    if input == '왼쪽': 
        return int(0)
    elif input == '가운데': 
        return int(1)
    elif input == '오른쪽': 
        return int(2)
    else:
        print('잘못입력하셨습니다.')
        Input_to_index()


def test_game(participant_choice:str, y_n:str):
    car_door = random.randint(0,2)
    select_door_index = Input_to_index(participant_choice)
    print(car_door, select_door_index)
    door_index = [0,1,2]
    new_doors = [0,1,2] # 새 문 리스트
    new_doors.remove(car_door) # 새 문리스트에서 차 카드 빼기
    if select_door_index in new_doors:
        new_doors.remove(select_door_index) # 새 문리스트에서 선택한 카드 있으면 빼기
    print(new_doors[0])
    
    door_index.remove(new_doors[0]) # 남은 염소문 열기
    print(door_index, new_doors)
    # print(new_doors[0]+'제거')
    new_choice = -1
    
    if y_n == 'y':
         # 선택한 문 이외의 문 선택
         door_index.remove(select_door_index)
         new_choice = door_index[0]
         if new_choice == car_door:
             print('문 뒤에 있는 것은 차 였습니다!')
             return 1
         else:
             print('문 뒤에 있는 것은 염소 였습니다!')
             return 0
    elif y_n == 'n':
        if select_door_index == car_door:
            print('문 뒤에 있는 것은 차 였습니다!')
            return 1
        else:
            print('문 뒤에 있는 것은 염소 였습니다!')
            return 0
    else:
        print('error')


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
    isWon = test_game('왼쪽', 'y')

    if isWon == 1:
        wonCount +=1

    print(f'{i+1}번째 게임 현재까지의 승률은 {round(wonCount/(i+1), 2)}입니다.')


