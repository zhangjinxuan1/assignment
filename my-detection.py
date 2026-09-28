#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput
import jetson.inference
import jetson.utils
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
img = jetson.utils.loadImage("/home/nvidia/jetson-inference/python/training/detection/ssd/data/test/067a21d43b856f7a.jpg") 
detections = net.Detect(img)
jetson.utils.saveImage("result_test2.jpg", img)
for detect in detections:
	print("===================================")
	print(f"ClassID:{detect.ClassID}")
	print(f"Confidence:{detect.Confidence:.3f}")
	print(f"Left:{detect.Left:.2f}")
	print(f"Top:{detect.Top:.2f}")
	print(f"Right:{detect.Right:.2f}")
	print(f"Bottom:{detect.Bottom:.2f}")
	print(f"Width:{detect.Width:.2f}")
	print(f"Height:{detect.Height:.2f}")
	print(f"Area:{detect.Area:.2f}")
	print(f"Center: ({detect.Center[0]:.2f}, {detect.Center[1]:.2f})")

