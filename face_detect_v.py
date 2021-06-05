import cv2 as cv

def rescaleFrame(frame, scale = 0.6):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

capture = cv.VideoCapture('Videos/Minimie.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
    #canny = cv.Canny(frame_resized,125,175)

    #cv.imshow('Video', frame)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 3, minSize = (30,30))

    print(f'Number of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame_resized, (x,y), (x+w, y+h), (0,255,0), thickness=2)

 
    
    cv.imshow('Video Resized', frame_resized)
    #cv.imshow('Gray', gray)
    #cv.imshow('Detected Faces', canny)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

