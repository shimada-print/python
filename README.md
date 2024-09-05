# Python  
## インストール 
### anacondaをインストール
anaconda（アナコンダ）とはPythonで高度な開発をするツールですが、　　
容量が約４GBほど必要に対し、以下のPython.exeという単体なら、  
数十MBやanacondaだとPython.exeの最新バージョンを使用できない  
可能性があるので、下記のように単体でもインストールするのがお勧めです。  

また環境変数はanacondaでは設定せずに、下記のPython.exeの最新バージョン 
では設定するのがお勧めです。anacondaではJupyter Notebookなどを使うのを  
主とし、Python.exeの最新バージョンでは最新トレンドの把握などと考えています。

### Python.exeの最新バージョンをインストール
Python.exeをインストールする直前に環境変数を自分で設定するのは、  
慣れていても面倒なので、レ点にチェックの同時インストールがお勧めです。
## pipインストール
Python.exeをインストール直後だとpip installでsetuptoolsなどが  
インストールされていない状態なので、以下のようにインストール  
しましょう。

```
pip install setuptools
```
上記のコマンドをWindowsPowerShellなどでコピー＆ペーストをすると、  
下記のようになればインストールは成功です。  
![PowerShallで実行する](./image/cmd_pip-install-setuptools.jpg)  
