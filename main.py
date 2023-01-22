import cv2

img = cv2.imread("img.png", cv2.IMREAD_COLOR)
shrink = cv2.resize(img, None, fx = 1., fy = 1., interpolation = cv2.INTER_AREA)

cv2.imshow('image', shrink)

cv2.waitKey(0)
cv2.destroyAllWindows()