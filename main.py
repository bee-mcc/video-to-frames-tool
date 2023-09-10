
import random
import shutil
import cv2

def overwrite_file_content(source_file_path, destination_file_path):
  try:
      # Copy the contents of the source file to the destination file
      shutil.copy2(source_file_path, destination_file_path)
      print(f"File '{destination_file_path}' has been overwritten with contents from '{source_file_path}'.")
  except FileNotFoundError:
      print("One or both of the specified files does not exist.")
  except Exception as e:
      print(f"An error occurred: {e}")

vidcap = cv2.VideoCapture('example.mkv')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  count += 1

print(f'Files printed:{str(count)}')

# now, take all frames and choose random one to extend. Then replace subsequent frames with chosen frame. Then choose a new one
total = count

count = 1

while count != total:
  numberOfFramesToExtend = random.randint(12, min(48, total - count))
  extendedFrames = 0

  while extendedFrames != numberOfFramesToExtend:
    
    extendedFrames += 1
    frameToExtend = extendedFrames + count

    countString = str(count)
    frameToExtendString = str(frameToExtend)
    
    overwrite_file_content(f"frame{countString}.jpg", f"frame{frameToExtendString}.jpg")

  count = count + numberOfFramesToExtend + 1


#then splice all replaced frames together one after eachother and AUDIO!
