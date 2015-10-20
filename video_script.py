# 
# Python Video Maker
# 
# The following script will create a new video in a loop with an interval delay.
# Set the run time of each video and the wait time between videos to produce a set
# amount of footage over a period of time.
# For example, if you want to produce an hour of footage over a 2 hour time period,
# set the run time to 5 minutes (60 * 5) and the wait time to 5 minutes (60 * 5).

import os, sys, uuid, cv2, time

try:
    path_to_sd = sys.argv[1]
except Exception, e:
    print "Please pass path to SD card"
    exit()

try:
    os.path.exists(path_to_sd)
except Exception, e:
    print "Not a valid path"
    exit()

# 
# Controls:
# 
# How long should each video be (in minutes)?
run_time = 5
# How much time should pass between videos (in minutes)?
wait_time = 5

for x in xrange(0,13):
    video_id = uuid.uuid4()

    cap = cv2.VideoCapture(0)

    video_path = path_to_sd + '/' + str(video_id) + '.mp4'
    codec = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
    fps = 7
    width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    color = True

    out = cv2.VideoWriter(video_path, codec, fps, size, color)

    stop = time.time() + (60 * run_time)
    while (cap.isOpened()):
        if time.time() >= stop:
            break
        ret, frame = cap.read()
        if ret==True:
            # cv2.imshow('frame',frame)
            out.write(frame)
        else:
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()
    time.sleep(60 * wait_time)
