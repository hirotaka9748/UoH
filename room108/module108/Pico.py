import socket

def pico(num):
    path = num + ".txt"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバを指定
        s.connect(('150.12.71.38', 5025))
        # サーバにメッセージを送る
        s.sendall(b":MEAS?\n")
        # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
        #
        b=repr(data[:-2]).strip('b')
        bb=b.replace("'","")
        print(bb)
    with open(path, 'a') as f:
        print(bb, file=f)