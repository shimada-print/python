#############################################################################
# 「日時も保存するメモ帳 ver.1」 Webスクリプトでは無くアプリ
#############################################################################

# 標準ライブラリのみ
import tkinter as tk
# AIが以下のfiledialogを出力しない場合もあり無いと起動しない
from tkinter import filedialog
# 書類名に保存日時を表示させるための標準ライブラリ
import datetime

# 検索と置換
def search_and_replace():
    search_text = tk.simpledialog.askstring("検索", "検索文字列を入力してください")
    if search_text:
        replace_text = tk.simpledialog.askstring("置換", "置換文字列を入力してください")
        pos = '1.0'
        while True:
            pos = text_area.search(search_text, pos, tk.END)
            if not pos:
                break
            last_pos = '%s+%sc' % (pos, len(search_text))
            text_area.delete(pos, last_pos)
            text_area.insert(pos, replace_text)
            pos = last_pos

# メインウィンドウの作成
root = tk.Tk()
root.title("日時も保存するメモ帳 ver.1")

# テキスト入力エリアの作成
text_area = tk.Text(root, font=("メイリオ", 12))
text_area.pack(fill="both", expand=True)

# メニューバーの作成
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# ファイルメニューの作成
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="新規作成", command=lambda: text_area.delete("1.0", tk.END))
file_menu.add_command(label="開く", command=lambda: open_file())
file_menu.add_command(label="保存", command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label="終了", command=root.quit)

# 編集メニューの作成
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="編集", menu=edit_menu)
edit_menu.add_command(label="検索と置換", command=search_and_replace)

# ファイルを開く関数
def open_file():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", f.read())


# ファイルを保存する関数
def save_file():
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", initialfile=f"新規テキスト書類_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    if file_path:
        encoding = tk.simpledialog.askstring("エンコーディング選択", "エンコーディングを選択してください (ANSI: 0, UTF-8: 1)", initialvalue="1")
        if encoding == "0":
            encoding = "ansi"
        elif encoding == "1":
            encoding = "utf-8"
        else:
            encoding = "utf-8"  # デフォルトはUTF-8
        with open(file_path, "w", encoding=encoding) as f:
            f.write(text_area.get("1.0", tk.END))

# メインループ
root.mainloop()
