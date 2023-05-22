## Overview
### Problem
Given a list of N photo files of N people and a video (N>3); 

Build a demo system that can identify the faces of those people in the list from the video. 

Input: a video.

Output: the video after processing in which detects the faces of those people and recognizes exactly the identification in the list N photo.

### Inspiration
This repository is inspired from the ["Face Recognition using Tensorflow"](https://github.com/davidsandberg/facene) repository of David Sandberg and this ["https://www.miai.vn/2019/09/11/face-recog-2-0-nhan-dien-khuon-mat-trong-video-bang-mtcnn-va-facenet/"](Miai blog).

I have studied and modified the above repository to build a Flask server with RESTful API to demonstrate the result required from the problem. 

## Steps to run the project:
1. Go to the folder of Project: FaceRecognition
2. Install necessary libraries:
    pip install -r requirements.txt
3. Process raw images of face data:
    python src/align_dataset_mtcnn.py dataset/facedata/raw dataset/facedata/processed --image_size 160 --margin 32 --random_orde --gpu_memory_fraction 0.25
4. Train model with pretrained weights of FaceNet to classify face classes:
    python src/classifier.py TRAIN dataset/facedata/processed models/20180402-114759.pb models/facemodel.pkl --batch_size 1000    
5. Process and create video from existing one:
    python src/face_rec.py --path app/static/video_slow.mp4
6. Go to folder ./app from root directory, then run the server: 
    python server.py
7. On local, open your favorite web browser and type this URL to test the result:
    http://127.0.0.1:5000/video

## Quick run
If you just want to test the API, just do step 6 and 7.