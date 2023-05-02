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




# 선택을 유지한 경우의 승률 계산
win_rate = monte_carlo_simulation(change_choice=False, num_trials=1000)
print(f"선택을 유지한 경우의 승률: {win_rate}")

# 선택을 변경한 경우의 승률 계산
win_rate = monte_carlo_simulation(change_choice=True, num_trials=5000)
print(f"선택을 변경한 경우의 승률: {win_rate}")