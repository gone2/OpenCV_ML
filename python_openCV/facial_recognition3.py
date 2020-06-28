import cv2
import numpy as np
import pymysql
import sys
from os import listdir
from os.path import isdir, isfile, join
from datetime import datetime
import time

# 얼국 인식용 xml 파일
face_classifier = cv2.CascadeClassifier(r'C:\Users\jeonjiwon\Desktop\machine_learning\haarcascade_frontalface_default.xml') 
folderUrl = r'C:\Users\jeonjiwon\Desktop\machine_learning\faces_learning'
# 사용자 얼굴 학습
def train(name):
    data_path = folderUrl + '/' + name + '/'
    #파일만 리스트로 만듬
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    
    Training_Data, Labels = [], []
    
    for i, files in enumerate(face_pics):
        image_path = data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # 이미지가 아니면 패스
        if images is None:
            continue   

        Training_Data.append(np.asarray(images, dtype = np.uint8))
        Labels.append(i)

    if len(Labels) == 0:
        print("There is no data to train.")
        return None

    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()  # 모델 생성
    model.train(np.asarray(Training_Data), np.asarray(Labels)) # 학습
    print(name + " : Model Training Complete!!!!!")

    return model

# 여러 사용자 학습
def trains():
    data_path = folderUrl + '/'
    # faces_learning 폴더의 하위 폴더를 학습하기 위해 폴더만 추출
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]
    
    #학습 모델 저장할 딕셔너리
    models = {}

    # 각 폴더의 얼굴 학습
    for model in model_dirs:
        print('model :' + model)
        # 학습 시작
        result = train(model)

        # 학습이 안되었다면 건너뜀
        if result is None:
            continue

        # 학습되었으면 저장
        print('model2 :' + model)
        models[model] = result

    return models    

#얼굴 검출
def face_detector(img, size = 0.5):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        if faces is():
            return img, []

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200, 200))

        return img, roi   #검출된 좌표에 사각 박스 그리고(img), 검출된 부위를 잘라(roi) 전달

# 인식 시작
def run(models):

    print(models)
    # mysql 연동
    conn = pymysql.connect( user='jiwon', passwd='1234', host='localhost', db='jiwondb', charset='utf8' )
    # studentCk = list(models.keys())
    # stNum = studentCk[0].split('_')[0]
    # stName = studentCk[0].split('_')[1]
    # stDate = datetime.now().strftime('%Y-%m-%d')
    
    # 카메라 실행 
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    mCheck = False
    while True:
        # 카메라로부터 사진 읽기
        ret, frame = cap.read()
        # 얼굴 검출 시도 
        image, face = face_detector(frame)

        try:            
            min_score = 999       # 가장 낮은 점수로 예측된 사람의 점수
            min_score_name = ""   # 가장 높은 점수로 예측된 사람의 이름
            
            # 검출된 사진을 흑백으로 변환 
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # 위에서 진행한 학습모델 예측시도
            for key, model in models.items():
                result = model.predict(face)

                if min_score > result[1]:
                    min_score = result[1]
                    min_score_name = key
                    
            # min_score 신뢰도 0에 가까울수록 자신과 일치
            if min_score < 500:
                confidence = int(100 * (1 - (min_score) / 300))
                # 유사도 화면에 표시 
                display_string = str(confidence)+'% Confidence it is ' + min_score_name
            cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
            
            #75 보다 크면 동일 인물로 출석 인정
            if confidence > 75:
                cv2.putText(image, "student check in class : " + min_score_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Cropper', image)

                studentCk = min_score_name
                stNum = studentCk.split('_')[0]
                stName = studentCk.split('_')[1]
                stDate = datetime.now().strftime('%Y-%m-%d')

                # selectSql = "SELECT ST_NUM, ST_DT FROM CLASS_CHECK WEHER  ST_NUM = ? AND ST_DT = ?"
                # cursor.execute(selectSql, (stNum, stDate))
                # result = cursor.fetchall()
                # pring(result)
                # stNum = min_score_name

                
                print(min_score_name)
                print(min_score)

                cursor = conn.cursor()
                sql = "INSERT INTO class_check VALUES ( %s, %s, %s )"
                
                cursor.execute(sql, (stNum , stName, stDate))
                conn.commit()
                conn.close()

                mCheck = True

            else:
            #75 이하면 타인으로 출석 체크 안됨
                cv2.putText(image, "student not found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Cropper', image)
        except:
            #얼굴 검출 안됨 
            # cv2.putText(image, "student not found in class", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            # cv2.imshow('Face Cropper', image)
            pass

        if mCheck:
            sec = 3
            while (sec != 0 ):
                sec = sec-1
                time.sleep(1)
                sys.exit()
        else:
            print("김성민 종료")

        
        if cv2.waitKey(1)==13:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 학습 시작
    models = trains()
    # 고!
    run(models)