他のサイトから来た方、閲覧ありがとうございます。READMME.md（本説明文.マークダウン書類）は本プロジェクトの原文作成コーナーになっており、省略無しの最新版となっております。  

しかし本文の以下で「:::message alert」（[ZennのMarkdown記法一覧](https://zenn.dev/zenn/articles/markdown-guide)を参照）などと誤表記されていますが、これは本サイトでは表示できないマークダウンの確認・情報収集のために、修正していません。Zenn版の本書類は[コレ)](https://zenn.dev/shimada_print/articles/6f6f1d91373384)です。  

では、以下が本プロジェクトの説明文となります。

## PythonとAIで「日時も保存するメモ帳（初心者が日報を混乱なく書き込めるシステム）」を1時間ほどで作ってみた
![Pythonアプリをプログラミングする少女](./image/python_memo-book_note.jpg)  
### 初心者が日報などの入力する仕事をしやすくするにはシンプルに
アプリなのでWindowsなどのOS上で動くメモ帳を、AIに数秒でプログラミングさせた。しかしその前の企画を考えたり、README.md（詳細を述べた説明文はAIだと生成しづらい）を作るのに1時間弱かかった。シンプルなのでユーザーのOSにPowerShellCoreがインストール済みなら、MacやLinux（Unix）でも動くかもしれない。 

### ツールとレガシーで使いやすくするためにコード書類名は「main.py」
ツールとは自作のC#の実行書類.exe（Pythonの実行書類.pycなどは…）などで本コードを連携させたり、AIが生成したapp.pyよりも、mainの方が本体ぽく、昔から馴染み（レガシー）があるのでmain.pyにしてみた。
```python
#############################################################################

# 「日時も保存するメモ帳 ver.1」 Webスクリプトではなくアプリ
# https://github.com/shimada-print/python/

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
```

AIにプログラミングをしてもらったが、タイトル・ヘッダとライブラリの説明コメントは人間が自作した。「標準ライブラリのみ」とはpipで追加インストールしなくても良いということだ。 

出力ファイル名を「新規テキスト書類+保存した日時.txt」という保存した日時も出るようにした。ANSI（シフトJIS）かuft-8（ユニコード）で保存させるアラートを出したのは、初心者だと他の形式で保存し、サーバーと合わない可能性があり、またANSIかuft-8のどちらか１つに置き換えて固定し方が良いが、今回はサーバー連携版ではなくスタンドアローン版と例としてこうした。他のアプリはこの機能が見受けられない。  

保存日時も命名されることにより、上書き保存はされづらくなり、オペ（操作）ミスによる情報の損失も減る。また長期のデータ管理もしやすい。命名する時も後で命名が出来るので、忙しい時にも便利。  

特に初心者だとアプリが多機能だと、誤操作（オペミス）もするのでシンプルなエディターを作ってみた。  

ソースコードを「新規テキスト書類」を「日報」と置き換えて、業務システムの定型機能としても良いと思う。  

1999年頃にはこういうプログラミングはVCなどで作成されたが、ビックデータやAIへの業務データの自動保存という点でも、現実的にAI利用の独占状態であるPythonで作成してみた。

なおこのプログラムはメモ帳というよりも、もっとユーザーを楽にするには、音声で文字入力が出来るWebページなどからコピペして、本スクリプトで保存や、「本スクリプトでそれらの機能を追加するというか、その機能はPythonよりも速度が早いC++やGo言語などで作成し、サーバーのPtyhonプログラミングで受取となるかな」と思う。

### この私的な素人プロジェクトは今までに無い初心者向けな試み
main.pyとは、一々プログラミングの本体の書類名を変えると混乱するので、他のプログラミング言語のようにメイン（主なプログラミング）とした。  

拡張子がpyだとWebスクリプトだと勘違いする人いるので、ソースコードのタイトルはに「Webスクリプトではなくアプリ」であると表記した。  

しかし今も多機能なメモ帳などのアプリが多くあるが、余計な情報となり仕事で集中が出来ないのでシンプルにした。   

2024年9月8日に1時間ほどでAIを使い作成。「AIでどこまでプログラミングが出来るか？」という試みでもある。 

現代は人手不足なので初心者向けにしないと仕事が成立しなくなる。人間が自分が生活していて不便な点を解消するアイディアを考えて、AIがそれを解消するプログラミングをするという流れに、今後もなるだろう。

## 上記の自作の文を大手のAIで「ですます調にして」とプロンプトしてみた
「ですます調」に置き換えるだけだと思ったら、文章の簡略化や整備までしてきた。また「PowerShell Coreがインストールされていれば、Windows、Mac、Linuxで動作します」とあるので、例えばWindows環境しか持っていなくても、目安にはなりえる。自分の企画の評価という点でもAIの利用は参考になる。  

自分の企画の評価という点でもAIの利用は参考になる。しかし題名なども以下のように、インパクトが無いキーワードに変更されてしまった。なお少し修正した文を再度ですます調にしてもらったら違う語調になったり、自分の気持ちまで勝手に述べられているのは可笑しいと思う。

:::message
以下「ですます調にして」とだけ言ったのに、AIが文章を私が思っていない感想を持ち出すような、強制的に内容を変更してしまった。たぶんAIを作っている人が、広告業や文系でなく理数系なので、こうなるのかもしれない。
:::
## PythonとAIで「日時も保存するメモ帳」を作ってみた話

### 初心者でも使いやすいシンプルなメモ帳アプリを作ってみたよ

AIの力を借りて、初心者でも簡単に使えるメモ帳アプリを1時間で作ってみました。このアプリは、日報などの入力作業を効率化し、ミスを減らすことを目的としています。

**どんなアプリなの？**

* **シンプル:** 初心者でも使いやすいように、余計な機能は省いてシンプルにしました。
* **日時自動保存:** ファイル名に保存日時が自動的に付くので、いつ保存したのかが一目で分かり、うっかり上書きしてしまう心配がありません。
* **エンコーディング選択:** 漢字などの文字化けを防ぐために、保存する際の文字コードを自分で選べるようにしました。
* **どこでも使える:** Windowsだけでなく、MacやLinuxでも使える可能性があります。

**作った背景**

* **AIでプログラミング:** AIにコードを生成してもらって、短時間でアプリを作ってみました。
* **初心者向け:** 初心者でも使いやすいように、シンプルな機能に絞って開発しました。
* **データ管理:** 日報などのデータを効率的に管理できるようにしました。

**作った時の苦労話**

AIにコードを作ってもらったけど、AIだけでは完璧なコードは作れないので、自分でコードを修正したり、コメントを追加したりする必要がありました。特に、README.mdのような説明文は、AIだけではうまく作れなかったので苦労しました。

**今後の展望**

* **音声入力:** マイクで話した言葉を文字に変えて、直接メモ帳に入力できるようにしたいです。
* **クラウド連携:** スマホや他のパソコンからも、同じメモ帳にアクセスできるようにしたいです。
* **もっとすごい機能:** C++やGo言語を使って、もっと高速で複雑な機能を追加したいです。

**まとめ**

今回の実験で、AIがプログラミングをサポートしてくれることで、誰でも簡単にアプリを作れるようになる可能性を感じました。これからもAIの進化とともに、もっとすごいものが作れるようになると思います。

**技術的なこと**

* **プログラミング言語:** Python
* **GUIライブラリ:** Tkinter
* **AI:** [AIツールの名称]（例：ChatGPT）
* **開発時間:** 約1時間

**最後に**

このメモ帳アプリは、まだまだ発展途上です。でも、自分なりに工夫して作ったので、愛着があります。
今後、もっとたくさんの人に使ってもらえるように、さらに機能を改善していきたいです。

:::message alert
以上が、AIが生成した（原文を一部省略している）ものだが、AIだと文章は個性的なものを、綺麗な定型的なものに置き換えてしまうらしい。これはデフォルトで「ですます調だけに置き換える」とし、「ビジネスで通用する文章にして」などとモード切替な機能にした方が良いと思う。
:::

## 本プロジェクトのデプロイ先
https://github.com/shimada-print/python/tree/main/memo-book

GitHubなどのクラウドで編集しながらデプロイ（格納）した方がデータ紛失は少ないが、社外秘の社内LAN内のデータの場合は、本スクリプトのようなシステムの方が良いかもしれない。
