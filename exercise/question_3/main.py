'''
Questão 3 - Escolha um video de sua preferência com imagens reais
e sugira uma aplicação. Implemente um código com algum extrator
visto em aula para resolver essa aplicação. Algumas sugestões de
links estão disponíveis na planilha Live Cameras, disponibilizada
no ClassRoom.
'''
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt
import cv2 as cv

#Taking the video frames.
cap = cv.VideoCapture('\with_out_birds.mp4')#switch to the video with birds 'with_birds.mp4'
_, frame = cap.read()
r = cv.selectROI(frame)

#Graph showing differences
plt.style.use("ggplot")
(fig, ax) = plt.subplots()
fig.suptitle("Local Binary Patterns")
plt.ylabel("% of Pixels")
plt.xlabel("LBP pixel bucket")
plt.ion()

while (cap.isOpened()):
    _, frame = cap.read()
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    '''
    reference
    https://www.youtube.com/watch?v=bxd96VKJ4lM&t=203s
    '''
    #Region of interest
    roi = frameGray[int(r[1]):int(r[1] + r[3]),
                  int(r[0]):int(r[0] + r[2])]
    feature = local_binary_pattern(roi, 256, 1, method='uniform')

    plt.cla()
    plt.hist(feature.ravel(), bins='auto',range=(0,64))
    plt.pause(0.01)

    cv.imshow("LBP_Image", roi)
    cv.waitKey(1)

cap.release()
cv.destroyAllWindows()