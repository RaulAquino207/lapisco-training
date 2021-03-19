import cv2 as cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture('./bread.mp4')
detector = cv.ORB_create(nfeatures=500)

selected = [0,0]
while (selected == [0,0]):
    _, frame = cap.read()
    res = cv.resize(frame, None, fx=.7, fy=.7, interpolation=cv.INTER_BITS)
    res = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    r = cv.selectROI(frame)
    selected = [r[1], r[0]]

roi = res[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
detector = cv.ORB_create(nfeatures=500)

w = roi.shape[1]
h = roi.shape[0]

xSize, ySize, zSize = frame.shape
aux = 0;
print(xSize,ySize)

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
i = 0
current_min_1 = 0
current_min_2 = 0
previous_min_1 = 0
previous_min_2 = 0
variation_1 = 0
variation_2 = 0
while(cap.isOpened()):
    ret, img = cap.read()
    res = cv.resize(img, None, fx=.7, fy=.7, interpolation=cv.INTER_BITS)
    res = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    res1 = cv.matchTemplate(res, roi, eval(methods[2]))

    # print(res1)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res1)
    print(min_val, max_val, min_loc, max_loc)

    if i == 0:
        previous_min_1 = min_loc[0]
        previous_min_2 = min_loc[1]
        print('PREVIOUS {} | {}'.format(previous_min_1, previous_min_2))
        print('CURRENT {} | {}'.format(current_min_1, current_min_2))

    elif i == 1:
        previous_min_1 = current_min_1
        previous_min_2 = current_min_2
        current_min_1 = min_loc[0]
        current_min_2 = min_loc[1]

        variation_1 = 0
        variation_2 = 0
        print('PREVIOUS {} | {}'.format(previous_min_1, previous_min_2))
        print('CURRENT {} | {}'.format(current_min_1, current_min_2))
        print('VARIATION {} | {}'.format('None', 'None'))

    else:
        previous_min_1 = current_min_1
        previous_min_2 = current_min_2
        current_min_1 = min_loc[0]
        current_min_2 = min_loc[1]

        variation_1 = (previous_min_1 - current_min_1)**2
        variation_2 = (previous_min_2 - current_min_2)**2
        print('PREVIOUS {} | {}'.format(previous_min_1, previous_min_2))
        print('CURRENT {} | {}'.format(current_min_1, current_min_2))
        print('VARIATION {} | {}'.format(variation_1, variation_2))

    previous_min_1 = min_loc[0]
    previous_min_2 = min_loc[1]

    if (variation_1 > 200000 or variation_2 >= 1):
        w = int(w + 0.2)
        h = int(h + 0.2)
        roi = cv.resize(roi, (w,h), interpolation=cv.INTER_LINEAR)


    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv.rectangle(res, top_left, bottom_right, 255, 2)
    print('SHAPE {}'.format(roi.shape))
    cv.imshow('Normal', res)

    # plt.subplot(121), plt.imshow(res1, cmap='gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(img, cmap='gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.show()

    if cv.waitKey(0) & 0xFF == ord('q'):
         break

    i += 1

cap.release()
cv.destroyAllWindows()