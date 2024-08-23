import random
while True :
    user_input = input("ジャンケン、ポン！（グー・チョキ・パーから選びましょう）：")
    if user_input in ["グー","チョキ","パー"]:
        result_random = random.choice(["勝った！","あいこでしょう！","負けちゃった！"])
        print(result_random)
        if result_random != "あいこでしょう！":
            break

