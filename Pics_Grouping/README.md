# Group Pics Based on Different Faces
This repository contains the code to organize set of pics of differnt people into different groups based on Face.

## Getting Started
 At first you need to have "python3" installed on your system and you also need to have some python libraries.
 1. face_recognition
 2. dlib 
 3. opencv
 4. tensorflow
 
### Prerequisites

To install face_recognition use 

```
pip install face_recognition
```
To install dlib use 

```
pip install dlib
```
To install opencv use 

```
pip install opencv-python
```
To install tensorflow 

```
pip install tensorflow
```


### Using

To use the above code.
1. Download the repository.
2. Install all the requirements
3. Open Command Prompt(cmd) and type 

```
python group_pics.py "Name of Folder containing Pics" "Name of Folder to save Pics to"
```

For Example (You can run this command for testing purposes, pics has been included with the output)

```
python3 group_pics.py dataset dataset_group
```

### Output

1. You will get output in the folder you specified, First folder will be 'all_faces_with_label' in this folder there will be different folders with (label as their name) and they will contain the faces of person with that label.
2. Then there will be many other folders with group or single pics of people in folder whose names are specified by the label of the person. 

### Issues
1. It takes too much time 5-10 seconds per pic based on your computer architecture.
2. It takes person with stylish specs and without as different, can't able to identify if the person is wearing stylish specs.

## Built With

* [Python3](https://www.python.org/) - Python3
* [opencv](https://pypi.org/project/opencv-python/) -opencv
* [dlib](https://pypi.org/project/dlib/) - dlib
* [face_recognition](https://pypi.org/project/face_recognition/)- face_recognition