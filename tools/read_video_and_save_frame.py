import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/tamalsen/Desktop/Test-vdo-2.mp4')
count=0
while(cap.isOpened()):
    count = count +1
    ret, frame = cap.read()
    fileName =  format(count, '06d')+".jpg"
    fileName = '/Users/tamalsen/git/deep_sort/TEST/test/set-2/img1/' + fileName
    cv2.imwrite(fileName,frame)
    print(fileName + 'written')

    ''' r = 760.0 / frame.shape[1]
    dim = (760, int(frame.shape[0] * r))

    imS = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('frame',imS) '''

    if count==300:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()