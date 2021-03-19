import time

import cv2

cap = cv2.VideoCapture('../Taiwan.mp4')

ret, frame = cap.read()
res = cv2.resize(frame, None, fx=.7, fy=.7, interpolation=cv2.INTER_BITS)
res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)


selected = [0,0]
while selected == [0,0]:
    _, frame = cap.read()
    res = cv2.resize(frame, None, fx=.7, fy=.7, interpolation=cv2.INTER_BITS)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    r = cv2.selectROI(res)
    selected = [r[1],r[0]]

print(int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2]))
template = res[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
detector = cv2.ORB_create(nfeatures=500)

w = template.shape[1]
h = template.shape[0]


previous_box = []
i = 0
while(cap.isOpened()):
    current_box = []
    ret, img = cap.read()
    res = cv2.resize(img, None, fx=.7, fy=.7, interpolation=cv2.INTER_BITS)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    res1 = cv2.matchTemplate(res, template, cv2.TM_CCOEFF_NORMED)  # TM_CCOEFF_NORMED TM_CCOEFF

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res1)
    # print(min_val, max_val, min_loc, max_loc)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    print(top_left, bottom_right)
    a, b = top_left
    c, d = bottom_right
    current_box.extend([b,d,a,c])
    print(current_box)
    # cut = cv2.getRectSubPix(res, top_left, bottom_right)
    cut = res[b:d, a:c]
    cv2.imshow('cut', cut)
    cv2.rectangle(res, top_left, bottom_right, 255, 2)

    cv2.imshow('Normal', res)

    if cv2.waitKey(0) & 0xFF == ord('q'):
         break

    i += 1
cap.release()
cv2.destroyAllWindows()

# https://www.youtube.com/watch?v=QK-Z1K67uaA