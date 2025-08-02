import tkinter as tk

root = tk.Tk()
root.title("计算器")
root.geometry("260x230")
root.resizable(width=False, height=False)

number_entry = tk.Entry(
    root,
    font=("SimHei", 12),
    width=20,
    justify="right",
    bg="white",

)
number_entry.place(x=10, y=10, width=170, height=30)
tk.Button(root, text="计算",command=lambda: on_button_click("计算")).place(x=190, y=10, width=50, height=30)

operational_buttons = [
    ["7", "8", "9", "清除"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "-"],
    ["0", ".", "/", "*"],
]

# 创建按钮
for i in range(len(operational_buttons)):
    for j in range(len(operational_buttons[i])):
        text = operational_buttons[i][j]
        button = tk.Button(
            text=text,
            font=("SimHei", 12),
            width=5,
            height=2,
            command=lambda t=text: on_button_click(t)  # 绑定事件，传递当前按钮文本
        )
        button.place(x=10 + 60 * j, y=50 + 40 * i, width=50, height=30)
def on_button_click(text):
    if text == "清除":
        number_entry.delete(0, tk.END)
    elif text == "计算":
        try:
            result = eval(number_entry.get())
            number_entry.delete(0, tk.END)
            number_entry.insert(0, result)
        except:
            number_entry.delete(0, tk.END)
            number_entry.insert(0, "错误")
    else:
        number_entry.insert(tk.END, text)

root.mainloop()