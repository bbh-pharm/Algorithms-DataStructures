import random
map_dict = {1: '가위', 2: '바위', 3: '보'}
win = 0
lose = 0

while win != 3 and lose != 3:
  user = int(input("가위바위보를 선택하세요 (1.가위, 2.바위, 3.보) :"))
  com = random.randint(1, 3)
  print("===============================================")

  # 사용자 선택값 출력
  print(f"당신의 선택은 ({map_dict[user]})입니다.")
  # 컴퓨터 선택값 출력
  print(f"컴퓨터 선택은 ({map_dict[com]})입니다.")
  # 승자계산 및 결과 출력 ("이겼습니다!", "졌습니다!", "비겼습니다." 중 하나)
  if user == com:
    print("비겼습니다.", f"현재 스코어 {win}승 {lose}패")
  elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
    win += 1
    print("이겼습니다!", f"현재 스코어 {win}승 {lose}패")
  else:
    lose += 1
    print("졌습니다!", f"현재 스코어 {win}승 {lose}패")
  
  print("===============================================")
  if win == 3:
    print("먼저 3승을 했네요 최종 승리!")
