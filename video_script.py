import os, sys, uuid, cv2, time

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

video_path = video_folder + '/' + str(video_id) + '.mp4'
codec = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
fps = 16
width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
size = (width, height)
color = True

out = cv2.VideoWriter(video_path, codec, fps, size, color)

end_time = time.time() + 60 * 5
while (cap.isOpened()):
    if time.time() > end_time:
        break
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)

        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()