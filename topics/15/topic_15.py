'''
Questão 15
Abrir uma câmera, capturar uma imagem (frame), transforme em tom de cinza, visualizar imagem de entrada, aplique o filtro de canny e visualize os resultados.
Continue infinitamente capturando, transformando em tom de cinza, aplicando canny e visualizando.
'''
#library import
import cv2 as cv
#initialize the camera
cap = cv.VideoCapture(0)

while (True):
    # capture each frame
    ret,frame = cap.read()
    # transforming the image to grayscale
    grayscale_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # doing high-pass filtering producing sharpering, using the canny filter
    # the values 80 and 100 are the thresholds defined for such sharpening
    canny_frame = cv.Canny(grayscale_frame,70,255)
    # show the result
    cv.imshow('Video', canny_frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break