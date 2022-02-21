import socket

def move(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.32', 10001))
    
        a="REL2S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        print(repr(data))
        
def back(numnum):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.32', 10001))
    
        a="ABS2S" + str(numnum)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        print(repr(data))
        