Steps to run the project:
1. Go to the folder of Project: FaceRecognition
2. Install necessary libraries:
    pip install -r requirements.txt
3. Process raw images of face data:
    python src/align_dataset_mtcnn.py dataset/facedata/raw dataset/facedata/processed --image_size 160 --margin 32 --random_orde --gpu_memory_fraction 0.25
4. Train model with pretrained weights of FaceNet to classify face classes:
    python src/classifier.py TRAIN dataset/facedata/processed models/20180402-114759.pb models/facemodel.pkl --batch_size 1000    
5. Generate video after processing:
    python src/face_rec.py --path app/static/video_slow.mp4

Have a look at RESTful API implemented with Flask Python:
6. Go to folder app from root directory, then run the server: 
    python server.py
7. On local, open your favorite web browser and type this URL to test the result:
    http://127.0.0.1:5000/video