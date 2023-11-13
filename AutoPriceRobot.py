import pyautogui
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 创建一个Tkinter根窗口
root = Tk()
root.withdraw()  # 隐藏根窗口

# 打开文件对话框，选择文件路径
file_path = askopenfilename()

# 打印所选文件的路径
# print("选择的文件路径：", file_path)


# 定位所有元素
# 使用元素的截图定位元素
element_positions = pyautogui.locateAllOnScreen(file_path)

# 循环点击每个元素
for element_position in element_positions:
    element_center = pyautogui.center(element_position)
    pyautogui.click(element_center)
