# import the necessary packages
import cv2
import argparse

#print("Digite a entrada do stream:")
#url = input()
#print("Stream ", url)

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output video")
args = vars(ap.parse_args())


url = 'https://5b33b873179a2.streamlock.net:1443/camerafozaduana/camerafozaduana.stream/chunklist_w1367170688.m3u8'
print(type(url))
vs = cv2.VideoCapture(url)
#writer = None
(W, H) = (None, None)

num_frames=0
while True:
	# read the next frame from the file
	(grabbed, frame) = vs.read()
	

	# if the frame was not grabbed, then we have reached the end
	# of the stream
	if not grabbed:
		break

	if frame is not None:
		#frame = cv2.resize(frame, (680,680))
		cv2.imshow('frame',frame)
	
		# Press q to close the video windows before it ends if you want
		if cv2.waitKey(22) & 0xFF == ord('q'):
			break
	else:
		print("Frame is None")
		break

	print("================NEW FRAME================")
	num_frames+= 1
	print("FRAME:\t", num_frames)

    
    # saves image file
	cv2.imwrite("output/frame-{}.jpg".format(num_frames), frame)

    # check if the video writer is None
	#if writer is None:
		# initialize our video writer
	#	fourcc = cv2.VideoWriter_fourcc(*"MJPG")
	#	writer = cv2.VideoWriter(args["output"], fourcc, 30,(frame.shape[1], frame.shape[0]), True)
	
	#writer.write(frame)
	if num_frames > 100:
		print("[INFO] cleaning up...")
		#writer.release()
		vs.release()
		exit()

# release the file pointers
print("[INFO] cleaning up...")
#writer.release()
vs.release()