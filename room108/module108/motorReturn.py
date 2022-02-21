import socket

def back():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.32', 10001))
    
        a="REL1S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        print(repr(data))
        
