import socket
import platform
import psutil
import os
import logging
import netifaces  # 複数のネットワークインターフェースに対応

from flask import Flask, render_template, url_for

app = Flask(__name__)

# ロギングの設定
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/')
def index():
    try:
        # システム情報
        system = platform.system()
        node = platform.node()
        release = platform.release()
        version = platform.version()

        # CPU情報
        cpu_count = psutil.cpu_count(logical=True)
        cpu_percent = psutil.cpu_percent(interval=1)

        # メモリ情報
        mem = psutil.virtual_memory()
        mem_percent = mem.percent

        # ディスク情報
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent

        # IPアドレスの取得
        # 複数のネットワークインターフェースに対応
        ip_addresses = []
        for interface in netifaces.interfaces():
            if interface != 'lo':  # ローカルループバックインターフェースを除外
                addrs = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addrs:
                    ip_addresses.append(addrs[netifaces.AF_INET][0]['addr'])

        # 環境変数 (必要なものだけ)
        env_vars = {
            'USER': os.environ.get('USER'),
            'HOME': os.environ.get('HOME'),
        }

        return render_template('index.html',
                              system=system,
                              node=node,
                              release=release,
                              version=version,
                              cpu_count=cpu_count,
                              cpu_percent=cpu_percent,
                              mem_percent=mem_percent,
                              disk_percent=disk_percent,
                              ip_addresses=ip_addresses,
                              env_vars=env_vars)

    except Exception as e:
        logging.error(f"エラーが発生しました: {e}")
        return f"エラーが発生しました: {e}"

if __name__ == '__main__':
    # Debug mode: on
    # デバックモードがoffでもログは出力する
    # app.run(debug=True)

    # Debug mode: off
    # 「プライベートIP:5000」でLAN内の他のPCから閲覧できるようにする
    app.run(host='0.0.0.0', port=5000)
