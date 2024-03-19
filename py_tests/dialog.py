"""
simpledialog
ダイアログ表示テスト
"""
from tkinter import simpledialog as sd

# 文字列受付
a = sd.askstring("", "askstring")
# 整数受付
b = sd.askinteger("", "askinteger")
# 浮動小数点受付
c = sd.askfloat("", "askfloat")

# 出力
print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")