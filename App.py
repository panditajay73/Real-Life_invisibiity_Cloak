import cv2
import numpy as np #Matrix Operation Array Matrizes

video=cv2.VideoCapture("GreenScreen.mp4")
image=cv2.imread("Img.jpg")

while True:
    ret, frame = video.read()   #ret check any error corruption in vdo if present then loop false ret=0=false  video ise save inside frame
    frame=cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_g=np.array([32,94,132])
    u_g=np.array([179,255,255])

    mask=cv2.inRange(hsv,l_g,u_g)
    res=cv2.bitwise_and(frame,frame ,mask=mask)
    f=frame-res
    green_screen=np.where(f==0, image,f) #if f=0 then replaced by image otherwise remains same

    #cv2.imshow("Frame", frame)  #frame is used to show the capture vdo , imshow does not have audio support
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Final Result",res)
    #cv2.imshow("f",f)
    #print(f)
    cv2.imshow("Final Result",green_screen)

    k=cv2.waitKey(1)   #wait for user to press any key to exit currently playing vdo ; pressed key button unicode(like ASCII value) saved in k
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()