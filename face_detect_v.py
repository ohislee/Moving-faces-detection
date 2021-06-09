import cv2 as cv

capture = cv.VideoCapture('Videos/Minimie.mp4')

fps = capture.get(cv.CAP_PROP_FPS)  #FPS How many frames are transmitted per second
w = int(capture.get(cv.CAP_PROP_FRAME_WIDTH)) 
h = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
size = (w, h)

video_output = cv.VideoWriter('Videos/moving faces.mp4', cv.VideoWriter_fourcc(*'mp4v'), fps, size)


i = 0  # nFrames: (0 -> nframes-1)
while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #convert color to gray
    
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 3, minSize = (30,30))
    print(f'Number of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    
    
        #saving output
    if isTrue:
        video_output.write(frame)
    else:
        break
    i += 1

    cv.imshow('Moving faces', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break    

capture.release()
video_output.release()
cv.destroyAllWindows()

print('The video was successfully saved.')
