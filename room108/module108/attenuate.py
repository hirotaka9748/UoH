import socket

def attenuateABS(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.32', 10001))
    
        a="ABS8S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        print(repr(data))
    ##100%の時6832で5.3mW
    ##13580で4mW
    ##20350で3mW
    
def attenuateREL(numnum):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.32', 10001))
    
        a="REL8S" + str(numnum)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        print(repr(data))
    ##100%の時6832で5.3mW
    ##13580で4mW
    ##20350で3mW