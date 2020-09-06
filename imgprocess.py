import cv2 as cv2
import numpy as np

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 10)

def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)

    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines, color=[255,255,255], thickness=3):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
                            minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    if lines is None:
        return line_img
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img, a=0.8, b=1., c=0.):
    return cv2.addWeighted(initial_img, a, img, b, c)

def print_processing(count, frameLen):
    msg='\rImage processing'
    msg2=['    ', '.   ', '..  ', '... ']
    msg+=msg2[count]
    msg+=str(frameLen)
    print(msg+' ', end='')
    count+=1
    if count==4: count=0
    return count

def video_to_edgedFrame(url, input_Imgsize=(640, 480), output_Imgsize=(640, 280), showImg=False):
    #이미지는 (가로,세로) 픽셀
    cap = cv2.VideoCapture(url)
    mask_array = []
    iprc=0
    while (cap.isOpened()):
        iprc=print_processing(iprc, len(mask_array))
        
        # 프레임마다 캡쳐
        ret, frame = cap.read()
        if ret == True:
            # 흑백만들기
            gray = grayscale(frame)
            # 블러처리
            kernel_size = 3
            blur_gray = gaussian_blur(gray, kernel_size)
            # canny 처리 선따오기
            low_threshold = 130
            high_threshold = 200
            edges = canny(blur_gray, low_threshold, high_threshold)
            #처리한 이미지 잘라서 넣기
            mask_array.append(edges[200:][:])

            if showImg:
                cv2.imshow('win_0', edges[200:][:])

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    if len(mask_array)==0:
        print('\rNo frames on video. Empty list returned.')
    else :
        print('\r%d frames on video.'%(len(mask_array)+1))

    return mask_array

if __name__ == "__main__":
    video_to_edgedFrame('200905.avi')