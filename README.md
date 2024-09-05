# Python  
## インストール 
### anacondaをインストール
anaconda（アナコンダ）とはPythonで高度な開発をするツールですが、anaconda（アナコンダ）とはPythonで高度な開発をするツールですが、容量が約４GBほど必要に対し、以下のPython.exeという単体なら、数十MBやanacondaだとPython.exeの最新バージョンを使用できない可能性があるので、下記のように単体でもインストールするのがお勧めです。  

また簡略化されたコマンドを入力できるパスはanacondaでは設定せずに、下記のPython.exeの最新バージョンでは設定するのがお勧めです。anacondaではJupyter Notebookなどを使うのを主とし、Python.exeの最新バージョンでは最新トレンドの把握などと考えています。

### Python.exeの最新バージョンをインストール
Python.exeをインストールする時に、Pytthonがインストールされたか確認できるバージョン表示のコマンド「python –version」などが表示できるパスを、自分で設定するのは慣れていても面倒なので、Python.exeをインストールする時にパスの同時インストールがお勧めです。パスが設定されていないや、インストールされていない状態ですと、ターミナルでは「Python」と表示されるだけなようです。
```
pip install setuptools
```
上記のコマンドをWindowsPowerShellなどで入力すると、下記のようになればインストールは成功です。  
![PowerShallで実行する](./image/cmd_pip-install-setuptools.jpg)  

### 起動には開発・デプロイ・クライアントOSが違うので書類の変更が必要です
Windowsのターミナルでは初期設定で書類読み込みは、uft-8（ユニコード）ではなくANSI（ShiftJIS）になっているのに対し、githubではuft-8のの改行コードがLF（UnixやMac）になっているので、ダウンロードしWindowsで起動する場合は、ダブルクリックで起動する書類だけは、ANSIのCR+LF（Windowsの改行コード）でメモ帳などで保存（変更）してください。  

あるいはWindowsのターミナルでuft-8で読み込む方法もありますが、少し複雑なのと、昔からの業務スクリプトなどがANSIが多い点からして、上記の書類を変更が無難です。
