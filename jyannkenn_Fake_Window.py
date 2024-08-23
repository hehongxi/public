import random
import tkinter as tk
from tkinter import messagebox

# 初始化感叹号计数器
exclamation_count = 0


def play_game(user_choice):
    global exclamation_count
    result = ["勝った！", "あいこでしょう！", "負けちゃった！"]
    choice = ["グー", "チョキ", "パー"]

    result_random = random.choice(result)

    if result_random == "あいこでしょう！":
        result_random += "！" * exclamation_count
        exclamation_count += 1
    else:
        exclamation_count = 1

    result_label.config(text=result_random)

    if "あいこでしょう！" in result_random:
        return
    else:
        disable_buttons()


def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")


def reset_game():
    global exclamation_count
    result_label.config(text="")
    exclamation_count = 1
    for btn in buttons:
        btn.config(state="normal")


# 创建主窗口
root = tk.Tk()
root.title("ジャンケンゲーム")

# 创建结果标签
result_label = tk.Label(root, text="", font=("Arial", 24))
result_label.pack(pady=20)

# 创建按钮
buttons = []
choices = ["グー", "チョキ", "パー"]
for choice in choices:
    btn = tk.Button(root, text=choice, font=("Arial", 18), command=lambda c=choice: play_game(c))
    btn.pack(side=tk.LEFT, padx=10)
    buttons.append(btn)

# 创建重置按钮
reset_button = tk.Button(root, text="リセット", font=("Arial", 18), command=reset_game)
reset_button.pack(pady=20)

# 运行主循环
root.mainloop()
