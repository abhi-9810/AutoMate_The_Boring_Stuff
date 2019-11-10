from mtcnn.mtcnn import MTCNN
import cv2
import os
import sys
import face_recognition
import dlib
import glob
from shutil import copyfile
import shutil

if len(sys.argv) != 3:
    print(
        "Call this program like this:\n"
        "   python group_pics.py folder_containing_pics folder_to_save_pics_to"
        )
    exit()
cascPath = "haarcascade_frontalface_default.xml" #loading the haarcascade for face detection
faceCascade = cv2.CascadeClassifier(cascPath)
faces_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]
detector = MTCNN()
count = 0
for filename in os.listdir(os.getcwd()+"/"+faces_folder_path): #for all files in given folder
	try:
		print("Processing file: {}".format(filename), count)
		count += 1
		
		img = cv2.imread(faces_folder_path+"/"+filename) #reading the image file
		""" Detecting the Face using Haarcascade """
		faces = faceCascade.detectMultiScale( 
					img,
					scaleFactor=1.1,
					minNeighbors=27,
					flags=cv2.CASCADE_SCALE_IMAGE,
					minSize=(30, 30),
				)

		image = face_recognition.load_image_file(faces_folder_path+"/"+filename) #Detecting face using face_recognition
		face_locations = face_recognition.face_locations(image) #getting face location
		len_cascade = len(faces)
		len_face = len(face_locations)
		print(len_cascade, len_face)
		# For each face
		if len_face <= len_cascade and len_cascade!=0 : #if len_cascade detected more faces and is not equal to 0
			i = 0
			for (x, y, w, h) in faces: 
			    try:
				    folder_name = faces_folder_path+"/FACE" #make a temprory folder to store all Faces
				    if not os.path.isdir(folder_name):
				    	os.makedirs(folder_name)
				    crop_img = img[y:y+h, x:x+w] #crop the face from image
				    name = folder_name+"/"+str(i)+"--______1511145______--"+filename
				    cv2.imwrite(name,crop_img)
				    i += 1
			    except:
			    	pass

		elif  len_cascade <= len_face and len_face!=0: #if len_face detected more faces and is not equal to 0
			i = 0
			for faces in face_locations:
				folder_name = faces_folder_path+"/FACE"
				if not os.path.isdir(folder_name):
					os.makedirs(folder_name)
				crop_img = img[faces[0]:faces[2], faces[3]:faces[1]]
				name = folder_name+"/"+str(i)+"--______1511145______--"+filename #just add a random string to the name so that it will be easy to get actual name later
				cv2.imwrite(name,crop_img)
				i += 1
		else: #If none of the moethod above were able to detect and faces then we will use MTCNN
			i = 0
			detects = detector.detect_faces(img)
			print(len(detects))
			for detect in detects:
				box = detects[i].get('box')
				confidence = detects[i].get('confidence')
				crop_img = img[box[1]:box[1]+int(box[3]*1.2), box[0]:box[0]+int(box[2]*1.2)]
				folder_name = faces_folder_path+"/FACE"
				if not os.path.isdir(folder_name):
					os.makedirs(folder_name)
				name = folder_name+"/"+str(i)+"--______1511145______--"+filename 
				cv2.imwrite(name,crop_img)
				i += 1
		
	except Exception as e:
		print(e)
		pass
			

# Load all the models we need: a detector to find the faces, a shape predictor
# to find face landmarks so we can precisely localize the face, and finally the
# face recognition model.
predictor_path = "shape_predictor_5_face_landmarks.dat" 
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

descriptors = []
images = []
# Now find all the faces and compute 128D face descriptors for each face.
for f in glob.glob(os.path.join(faces_folder_path+"/FACE","*")):
    filename = os.path.basename(f)
    try:
        img = dlib.load_rgb_image(f)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        # the parameter is threshold for image detection [-1,1] ; 1 for very strict detection and -1 for very loose detection 
        
        dets, scores, idx = detector.run(img, 1, -0.45)
        print(filename)
        print("Number of faces detected : {}".format(len(dets)))
        # Now process each face we found.
        for k, d in enumerate(dets):
            # Get the landmarks/parts for the face in box d.
            shape = sp(img, d)

            print("Detection {}, score: {}, face_type:{}".format(d, scores[k], idx[k]))
            # Compute the 128D vector that describes the face in img identified by
            # shape.  
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            descriptors.append(face_descriptor)
            images.append((img, shape, filename))
            if True: #As we have already cropped single faces from 
            	break
    except Exception as e:
        print(e)
        pass

# Now let's cluster the faces.  
"""
 The threshold in the chinese_whispers should be kept around 0.4 - 0.5, our result may vary significantly based on the threshold
 if the pics is family pic then threshold should be kept around 0.42-0.43 as we need more cluster as faces of family members may be same 
 and it may classify them into same cluster, so threshold should be strict and if we want less cluster more people to classify in same group threshols should be more 
"""
labels = dlib.chinese_whispers_clustering(descriptors, 0.45)
num_classes = len(set(labels))
print("Number of clusters: {}".format(num_classes))


indices = dict()
for i in range(0, num_classes):
    class_length = len([label for label in labels if label == i])
    if class_length>=5:
	    pics = list()
	    indices[i] = pics

for i, label in enumerate(labels):
	if label in indices:
		indices[label].append(i)

#saving Faces of persons with label
all_label_path = output_folder_path+'/all_faces_with_label'
if not os.path.isdir(all_label_path):
	os.makedirs(all_label_path)
for i, label in enumerate(labels):
	if label in indices:
		label_path = all_label_path+"/"+str(label)
		if not os.path.isdir(label_path):
			os.makedirs(label_path)
		img, shape, filename = images[i]
		file_path = os.path.join(label_path, filename)
		pre_file_path = os.path.join(faces_folder_path+"/FACE", filename)
		copyfile(pre_file_path, file_path)



# Save the extracted faces
print("Saving faces in output folder...")
i = 0
pic_labels = dict()
for label in indices:
    for pics in indices[label]:
        img, shape, filename = images[pics]
        indx = filename.find('--______1511145______--')
        filename = filename[indx+23:]
        if not filename in pic_labels:
            pic_labels[filename] = set()
        pic_labels[filename].add(label)
    i = i + 1

for pics in pic_labels:
    folder_temp = output_folder_path+"/Pics_"
    for label in pic_labels[pics]:
        folder_temp = folder_temp + str(label)+"_"
    folder_temp += "E/"
    if not os.path.isdir(folder_temp):
        os.makedirs(folder_temp)
    file_path = os.path.join(folder_temp, pics)
    pre_file_path = os.path.join(faces_folder_path, pics)
    copyfile(pre_file_path, file_path)


folder_temp = output_folder_path+"/unknown_pics/"
if not os.path.isdir(folder_temp):
    os.makedirs(folder_temp)
for f in glob.glob(os.path.join(faces_folder_path,"*")):
    images = os.path.basename(f)
    if not images in pic_labels:
        try:
            file_path = os.path.join(folder_temp, images)
            pre_file_path = os.path.join(faces_folder_path, images)
            print(file_path)
            print(pre_file_path)
            print(images)
            copyfile(pre_file_path, file_path)
        except Exception as e:
            print(e)
            pass
shutil.rmtree(os.getcwd()+"/"+faces_folder_path+"/FACE") # removing the temprory created folder
