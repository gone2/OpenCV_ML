import cv2
import numpy as np
from os import makedirs
from os.path import isdir

# 얼굴 저장 함수
face_dirs = 'faces_learning/'
# 얼국 인식용 xml 파일
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 얼굴 검출 함수
def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)             # 흑백처리 
    faces = face_classifier.detectMultiScale(gray,1.3,5)    # 얼굴찾기

    # 얼굴 유무 확인
    if faces is():
        return None

    # 얼굴 크기만큼 이미지 생성
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face

    print('success!!! ::: face_extractor')

# 얼굴 저장 함수
def take_pictures(num, name):
    # 해당 폴더 없으면 생성
    if not isdir(face_dirs + num + '_' + name):
        makedirs(face_dirs + num + '_' + name)

    # 카메라 실행
    cap = cv2.VideoCapture(0)
    # 저장할 이미지 카운트 변수
    count = 0

    while True:
        # 카메라로부터 사진 읽기
        ret, frame = cap.read()

        # 얼굴 검출 되었으면
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (300,300)) # 얼굴 이미지 크기 설정
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)       # 이미지 흑백 처리

            # 폴더를 지정 후, 이미지확장자(jpg, png etc..)로 파일 저장
            file_name_path = face_dirs + num + '_' + name + '/' + num + '_' + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)

            # 화면에 얼굴과 현재 저장 개수 표시
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)
        else:
            print("Face not Found")
            pass

        # 얼굴 사진 100장 or enter key 누르면 종료
        if cv2.waitKey(1)==13 or count==100:
            break

    cap.release()
    cv2.destroyAllWindows()
    print('Colleting Samples Complete!!!')

if __name__=="__main__":
    num = input('학번을 입력해주세요 : ')
    name = input('이름을 입력해주세요 : ')
    take_pictures(num, name)
