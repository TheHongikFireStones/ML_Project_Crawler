import os
import dlib
import cv2

# 얼굴 탐지기 로드
detector = dlib.get_frontal_face_detector()

# 이미지가 저장된 디렉토리 경로
image_dir = './img/'
actors_list = ["Aditya_Roy_Kapur", "Arjun_Rampal", "Hrithik_Roshan", "John_Abraham", "Kartik_Aaryan", "Ranveer_Singh",
               "Shahid_Kapoor", "Sidharth_Malhotra", "Sidharth_Malhotra", "Varun_Dhawan"]


def delete_non_face_images(directory):
    # 디렉토리 내의 모든 파일을 순회
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(directory, filename)

            # 이미지 로드
            image = cv2.imread(file_path)
            if image is None:
                print(f"이미지 파일을 열 수 없습니다: {filename}")
                continue

            # dlib은 RGB 이미지를 사용하므로 BGR을 RGB로 변환
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # 얼굴 탐지
            faces = detector(rgb_image)

            # 얼굴이 없는 경우 파일 삭제
            if len(faces) == 0:
                os.remove(file_path)
                print(f"얼굴이 없어 파일을 삭제했습니다: {filename}")


for actor in actors_list:
    path = image_dir + actor
    print(path)
    delete_non_face_images(path)
