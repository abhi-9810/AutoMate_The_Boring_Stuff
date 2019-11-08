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

predictor_path = "shape_predictor_5_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
faces_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]
detector = MTCNN()
count = 0
for filename in os.listdir(os.getcwd()+"/"+faces_folder_path):
	if not filename.endswith('.py'):
		try:
			print("Processing file: {}".format(filename), count)
			count += 1
			img = cv2.imread(faces_folder_path+"/"+filename)
			image = face_recognition.load_image_file(faces_folder_path+"/"+filename)
			face_locations = face_recognition.face_locations(image)
			i = 0
			for faces in face_locations:
				folder_name = faces_folder_path+"/FACE"
				if not os.path.isdir(folder_name):
					os.makedirs(folder_name)
				crop_img = img[faces[0]:faces[2], faces[3]:faces[1]]
				name = folder_name+"/"+str(i)+"--______1511145______--"+filename 
				cv2.imwrite(name,crop_img)
				i += 1	
			detects = detector.detect_faces(img)
			len_face = len(face_locations)
			len_mtcnn = len(detects)
			if len_face == 0:
				i = 0
				for detect in detects:
					box = detects[i].get('box')
					confidence = detects[i].get('confidence')
					i = i + 1
					crop_img = img[box[1]:box[1]+int(box[3]*1.2), box[0]:box[0]+int(box[2]*1.2)]
					folder_name = faces_folder_path+"/FACE"
					if not os.path.isdir(folder_name):
						os.makedirs(folder_name)
					name = folder_name+"/"+str(i)+"--______1511145______--"+filename 
					cv2.imwrite(name,crop_img)
		except Exception as e:
			print(e)
			pass


# Load all the models we need: a detector to find the faces, a shape predictor
# to find face landmarks so we can precisely localize the face, and finally the
# face recognition model.
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

descriptors = []
images = []
# Now find all the faces and compute 128D face descriptors for each face.
for f in glob.glob(os.path.join(faces_folder_path+"/FACE","*")):
    #print("Processing file: {}".format(f))
    filename = os.path.basename(f)
    try:
        img = dlib.load_rgb_image(f)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        
        
        dets, scores, idx = detector.run(img, 1, -0.45)
        print("Number of faces detected: {}".format(len(dets)))

        dets, scores, idx = detector.run(img, 1, -0.45)
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
    except Exception as e:
        print(e)
        pass

# Now let's cluster the faces.  
labels = dlib.chinese_whispers_clustering(descriptors, 0.47)
num_classes = len(set(labels))
print("Number of clusters: {}".format(num_classes))

# Find biggest class

indices = dict()
all_class = list()
for i in range(0, num_classes):
    class_length = len([label for label in labels if label == i])
    all_class.append(class_length)
    pics = list()
    indices[i] = pics


# Find the indices for the biggest class
for i, label in enumerate(labels):
    indices[label].append(i)


# Save the extracted faces
print("Saving faces in output folder...")
i = 0
pic_labels = dict()
for pics in indices:
    for j in indices[i]:
        img, shape, filename = images[j]
        indx = filename.find('--______1511145______--')
        filename = filename[indx+23:]
        if not filename in pic_labels:
            pic_labels[filename] = set()
        pic_labels[filename].add(i+1)
    i = i + 1

for pics in pic_labels:
    print(pics)
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
shutil.rmtree(os.getcwd()+"/"+faces_folder_path+"/FACE")
