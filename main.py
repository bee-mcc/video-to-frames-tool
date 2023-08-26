import cv2
vidcap = cv2.VideoCapture('example.mkv')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

#now, take all frames and choose random one to extend. Then replace subsequent frames with chosen frame. Then choose a new one

#then splice all replaced frames together one after eachother and AUDIO!