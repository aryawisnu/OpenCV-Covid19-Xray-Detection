import cv2

cap = cv2.VideoCapture(0) #buka webcam
copid = cv2.CascadeClassifier('cascadecovid19.xml') #cascade hasil training

while True:
    #pembacaan
    ret, frame1 = cap.read()

    #pemrosesan
    grayframe1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    deteksicopid = copid.detectMultiScale(grayframe1, 1.3, 5)
    for (x, y, w, h) in deteksicopid:
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame1, 'copid iki lur',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
    #display
    cv2.imshow("testlurr",frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()