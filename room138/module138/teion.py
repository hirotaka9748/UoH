import socket
import time


def status_m1(path1):
    path = path1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.113', 7777))
    # サーバにメッセージを送る
        s.sendall(b"PS?5\n")
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        b=repr(data[:-2]).strip('b')
        bb=b.replace("'","")
        print(bb)
    with open(path1, 'a') as f:
        print(bb, file=f)
        
        
def move_m1(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.113', 7777))
    
        a="ABS5S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        print("MOVE")
    time.sleep(5)
    
    
def move0_m1(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.113', 7777))
    
        a="ABS5S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        print("MOVE")
    time.sleep(20)
    
def status_m2(path1):
    path = path1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.113', 7777))
    # サーバにメッセージを送る
        s.sendall(b"PS?2\n")
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
    #
        b=repr(data[:-2]).strip('b')
        bb=b.replace("'","")
        print(bb)
    with open(path1, 'a') as f:
        print(bb, file=f)
        
        
def move_m2(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.113', 7777))
    
        a="ABS2S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        print("MOVE")
    time.sleep(5)
    
    
def move0_m2(num):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
        s.connect(('150.12.70.113', 7777))
    
        a="ABS2S" + str(num)+ "\n"
        
    # サーバにメッセージを送る
        s.sendall(a.encode())
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        print("MOVE")
    time.sleep(20)

