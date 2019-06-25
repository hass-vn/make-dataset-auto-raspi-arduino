#your code save image use button arduino to save img webcam image
#hass vn

import serial  # import serial library
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
arduino = serial.Serial('/dev/ttyUSB0', 9600)  # create serial object named arduino use your serial
i = 0
while True:  # create loop
    ret, frame = cap.read()
    reachedPos = str(arduino.readline().decode())  # read serial port for arduino echo to decode
    #print(reachedPos)
    a = int(reachedPos)
    if (a == 1):
        i = i+1
        print(i)
        cv2.imwrite('img{}.png'.format(i), frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
