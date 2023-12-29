# Food adulteration detection in Red Chilli and turmeric powder 

## Image Classification Project

This repository contains Jupyter Notebooks and scripts for image classification using Convolutional Neural Networks (CNNs), VGG16 model, data augmentation, and making predictions using TensorFlow and Keras.

### Convolutional Neural Network (`cnn.ipynb`)

The `cnn.ipynb` notebook implements a simple Convolutional Neural Network for image classification. It covers data preprocessing, model building, training, and evaluation.

#### Usage

1. Open the `cnn.ipynb` notebook.
2. Follow the step-by-step instructions for loading data, building the CNN model, and training it.

### VGG16 Implementation (`vgg16.ipynb`)

The `vgg16.ipynb` notebook contains the implementation of a VGG16 model for image classification. It covers image preprocessing, data loading, model building, compilation, training, and evaluation.

#### Usage

1. Open the `vgg16.ipynb` notebook.
2. Follow the instructions for loading data, building the VGG16 model, and training it.


### Data Augmentation (`augmentation.py`)

The `augmentation.py` script provides a function for augmenting image data using the Keras `ImageDataGenerator`. It is designed to augment images in specified directories and save the generated samples to a specified directory.

#### Usage

1. Modify the `path`, `n_generated_samples`, and `save_to_dir` parameters in the script.
2. Run the script in a Python environment.

### Prediction (`prediction.ipynb`)

The `prediction.ipynb` notebook demonstrates how to load a pre-trained model (`CNNmodel1.h5`) and make predictions on new images. It uses TensorFlow and Keras to load an image, preprocess it, and obtain class predictions.

#### Usage

1. Open the `prediction.ipynb` notebook.
2. Replace the `path` variable with the path to the image you want to predict.
3. Execute the notebook to obtain class predictions.

#### Requirements
###      
#bash   pip install -r requirements.txt
- TensorFlow
- Keras
- OpenCV
- Matplotlib

### Data Summary (`augmentation.py`)

The repository includes a `data_summary` function in the `augmentation.py` script to print a summary of the number of images before and after augmentation.

#### Usage

1. Run the `data_summary` function in the `augmentation.py` script.

### Prerequisites

- Python 3.x
- Jupyter Notebooks


### Running the Notebooks and Scripts

Make sure to have the required dependencies installed. You can run the notebooks in a Jupyter environment, and for the scripts, execute them in a Python environment.


