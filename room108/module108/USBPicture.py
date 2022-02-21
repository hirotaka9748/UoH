import cv2
from datetime import datetime
import os

def picture(num):
    new_dir_path = num
    
    if not os.path.exists(new_dir_path):
    # ディレクトリが存在しない場合、ディレクトリを作成する
        os.makedirs(new_dir_path)

    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = num + "/" + date + ".png"
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(path, frame)
    cap.release()
    print("OK!")