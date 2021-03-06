'''
Questão 14
Abrir uma câmera, capturar uma imagem (frame), transforme em tom de cinza, visualizar imagem de entrada.
Continue infinitamente capturando, transformando em tom de cinza e vizualizando.
'''
import cv2 as cv
#initialize the camera
cap = cv.VideoCapture(0)

while (True):
    ret,frame = cap.read()
    grayscale_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Video', grayscale_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
'''
i = 0
while i < 10:
    #capture each frame
    ret, frame = cap.read()

    #convert the frame from bgr to gray
    grayscale_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #canny_img = cv.Canny(grayscale_img, 80, 100)

    #show the result
    #cv.imshow('Video', canny_img)
    cv.imshow('Video', grayscale_img)
    cv.imwrite(f"frame_video{i + 1}.jpg", grayscale_img)
    i += 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
'''
