import socket
import time
import linecache

def pico1(path):
    path1 = path
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバを指定
        s.connect(('150.12.71.36', 5025))
        # サーバにメッセージを送る
        s.sendall(b":MEAS?\n")
        # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
        #
        b=repr(data).strip('b')
        bb=b.replace("'","")
        print(bb)
    with open(path1, 'a') as f:
        print(bb, file=f)
    time.sleep(0.1)    
    
def pico2(path):
    path2 = path
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバを指定
        s.connect(('150.12.71.38', 5025))
        # サーバにメッセージを送る
        s.sendall(b":MEAS?\n")
        # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
        #
        b=repr(data).strip('b')
        bb=b.replace("'","")
        print(bb)
    with open(path2, 'a') as f:
        print(bb, file=f)
    time.sleep(0.1)    
    
def pico3():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバを指定
        s.connect(('150.12.70.132', 5025))
        # サーバにメッセージを送る
        s.sendall(b":MEAS?\n")
        # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
        data = s.recv(1024)
        #
        volt=repr(data).strip('b')
        volt2=volt[1:-3]
        print(volt2)
        tesla = float(volt2)/0.00065
        tesla_2 = round(tesla,2)
        print(tesla_2)
    time.sleep(0.1)    
    

def diffpico(path1,path2,path3):
    i = 1
    while i < 1 + sum([1 for _ in open(path1)]):
        data1 = linecache.getline(path1, i).strip()
        data11 = data1[:-1]
        data111 = data11.replace("'","")
        data1111 = data111.replace("\\","")
        data2 = linecache.getline(path2, i).strip()
        data22 = data2[:-1]
        data222 = data22.replace("'","")
        data2222 = data222.replace("\\","")
        data333 = float(data1111) - float(data2222)
        print(data333)
        with open(path3, 'a') as f:
            print(data333, file=f)
        i += 1
        
def numpico(pico_path,pico_num_path):
    i = 1
    while i < 1 + sum([1 for _ in open(pico_path)]):
        data4 = linecache.getline(pico_path, i).strip()
        data44 = data4[:-1]
        data444 = data44.replace("'","")
        data4444 = data444.replace("\\","")
        with open(pico_num_path, 'a') as f:
                print(data4444, file=f)
        i+=1