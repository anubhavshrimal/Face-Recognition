# FaceRecognition

Machine Learning project to recognise people from an Image just like facebook.

Built with the help of [dlib's](http://dlib.net/) state-of-the-art face recognition built with deep learning.
The model has an accuracy of 99.38% on the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

## Dependencies:

- Python 3.x
- Numpy
- Scipy
- [Scikit-learn](http://scikit-learn.org/stable/install.html)
- [dlib](http://dlib.net/)

    Tip: Installing dlib can be a tedious job. On macOS or Linux you may follow [this link](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf).

- Extras:
    For using `./demo-python-files/projecting_faces.py` you will need to install [openface](https://cmusatyalab.github.io/openface/setup/).
    ```
    To install openface, follow the below instructions:
        git clone https://github.com/cmusatyalab/openface.git
        cd openface
        pip install -r requirements.txt
        sudo python setup.py install
    ```

## Procedure:

- Clone this repository `git clone git@github.com:anubhavshrimal/FaceRecognition.git`.

### Training:
- Make folder `training-images`.
- Add images of each person you want to recognise to a folder by their name in `training-images`.

    Example
    ```bash
    $ mkdir training-images
    $ cd training-images
    $ mkdir Name_Of_Person
    ```
    Then copy all the images of that person in `./training-images/Name_Of_Person` folder.

    <img src='./screenshorts/training-images-folder-view.png' width='300px'>

- Run on cmd `python create_encodings.py` to get the encodings of the images and the labels.
    This will create `encoded-images-data.csv` and `labels.pkl` files.

    <img src='./screenshorts/create-encodings.png' width='700px'>

    Note: There has to be only one face per image otherwise encoding will be for the first face found in the image.

- Run on cmd `python train.py` to train and save the face recognition classifier.
    This will create `classifier.pkl` file.
    It will also create `classifier.pkl.bak` backup file if the classifier with that name already exists.

    <img src='./screenshorts/train.png' width='700px'>

### Prediction:
- Make folder `test-images` which contains all the images you want to find people in.

    <img src='./screenshorts/test-images-folder-view.png' width='300px'>

- Run on cmd `python predict.py` to predict the faces in each image.

    <img src='./screenshorts/predict.png' width='700px'>


## Vote of Thanks
- Thanks to [Adam Geitgey](https://github.com/ageitgey) whose blog inspired me to make this project.
- Thanks to [Davis King](https://github.com/davisking) for creating dlib and for providing the trained facial feature
  detection and face encoding models used in this library.