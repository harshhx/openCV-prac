import cv2
img = cv2.imread("logo.png")
newImg = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
grayImg = cv2.imread("logo.PNG" , cv2.IMREAD_GRAYSCALE)
cv2.imshow("img",img)
cv2.imshow("BGR2RGB",newImg)
cv2.imshow("gray",grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()