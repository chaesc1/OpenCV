import numpy as np, cv2


def median_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2  # 마스크 절반 크기

    for i in range(center, rows - center):  # 입력 영상 순회
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1  # 마스크 높이 범위
            x1, x2 = j - center, j + center + 1  # 마스크 너비 범위
            mask = image[y1:y2, x1:x2].flatten()  # 마스크 영역 범위를 순회하여 마스크의 범위의 행렬을 가져와서 벡터로 전개함
            #원소를 정렬하기 위해서.

            sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN)  # 정렬 수행
            dst[i, j] = sort_mask[sort_mask.size // 2]  # 출력화소로 지정//전체클기를 2로 나누어 중간위치를 계산후 중간위치의 벡터원소를 가져와서
                                                        #출력 행렬의 화소로 결정
    return dst


def salt_pepper_noise(img, n): #소금후추잡음 생성 함수.
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for (x, y) in zip(x, y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
    return noise


image = cv2.imread("../images/median2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

noise = salt_pepper_noise(image, 10000)#숫자를 변경해 노이즈 정도 정해
med_img1 = median_filter(noise, 3)  # 사용자 정의 함수
med_img2 = cv2.medianBlur(noise, 3)  # OpenCV 제공 함수

cv2.imshow("image", image),
cv2.imshow("noise", noise),
cv2.imshow("median - User", med_img1)
cv2.imshow("median - OpenCV", med_img2)
cv2.waitKey(0)
