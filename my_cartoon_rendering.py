import cv2
import numpy as np

def cartoonize_image(image_path, output_path):
    # 이미지 읽기
    img = cv2.imread(image_path)
    
    # 이미지 크기를 줄이기
    img = cv2.resize(img, (800, 600))
    
    # 색상 강조를 위한 블러 처리
    img_color = cv2.pyrDown(img)
    img_color = cv2.pyrDown(img_color)
    img_color = cv2.pyrUp(img_color)
    img_color = cv2.pyrUp(img_color)
    
    # 에지 검출을 위한 그레이스케일 변환
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 5)
    
    # 에지 추출
    edges = cv2.adaptiveThreshold(img_gray, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 9, 9)
    
    # 색상 이미지와 에지 결합
    cartoon = cv2.bitwise_and(img_color, img_color, mask=edges)
    
    # 결과 이미지 저장
    cv2.imwrite(output_path, cartoon)

# 예시 사용법
cartoonize_image("cartoon.png", "cartoon_output.jpg")
cartoonize_image("cartoon1.jpeg","cartoon_output1.jpg")