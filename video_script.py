import os, sys, uuid, cv2

try:
    path_to_sd = sys.argv[1]
except Exception, e:
    print "Please pass path to SD card"
    exit()


video_folder = path_to_sd + "/video"
video_id = uuid.uuid4()

# check folder structure
if not os.path.exists(video_folder):
    os.makedirs(video_folder)

cap = cv2.VideoCapture(0)

out = cv2.VideoWriter(video_folder + '/' + str(video_id) + '.mp4', cv2.cv.CV_FOURCC('F', 'M', 'P', '4'), 25, (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH )),int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))), True)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)

        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

cap.realease()
out.realease()
cv2.destroyAllWindows()