# Crowd Counting CNN Model

## Overview
The purpose of this repository is to create a simple crowd counting model.
Crowd counting here represents a task in counting/estimating the number of people in an image.

## Features
Convolutional Neural Network represents the model that was implemented in this project.

## Installation
For model training, the libraries, framework and packages used can be found in the jupyter notebook and be retrieved with the following command.
```
! wget "https://raw.githubusercontent.com/NigelGoh16/Crowd_Counting_Model/main/Crowd_Counting.ipynb"
```

## Usage
To use the simple CNN model that was trained in this repository, use the following command to retrieve the model and the preprocessing function.
```
! wget "https://raw.githubusercontent.com/NigelGoh16/Crowd_Counting_Model/main/crowd_counting_simpleCNN.h5"
! wget "https://raw.githubusercontent.com/NigelGoh16/Crowd_Counting_Model/main/functions.py"
```
Use the following commands to perform crowd counting with images.
```
from functions import preprocess, pred_and_plot

image_path = "Please fill in your image path here"
model = tf.keras.models.load_model("crowd_counting_simpleCNN.h5")
pred_and_plot(image_path, model)
```

## Datasets
List the datasets used in the repository for crowd counting experiments. Include details such as dataset name, brief description, citation information, and download links if available.
Dataset Name: Mall Dataset (Crowd Counting)

Link: https://www.kaggle.com/datasets/fmena14/crowd-counting/data

## Acknowledgments
The dataset used is intended for research purposes only and as such cannot be used commercially. Please cite the following publication(s) when this dataset is used in any academic and research reports.
- From Semi-Supervised to Transfer Counting of Crowds
C. C. Loy, S. Gong, and T. Xiang
in Proceedings of IEEE International Conference on Computer Vision, pp. 2256-2263, 2013 (ICCV)
- Cumulative Attribute Space for Age and Crowd Density Estimation
K. Chen, S. Gong, T. Xiang, and C. C. Loy
in Proceedings of IEEE Conference on Computer Vision and Pattern Recognition, pp. 2467-2474, 2013 (CVPR, Oral)
- Crowd Counting and Profiling: Methodology and Evaluation
C. C. Loy, K. Chen, S. Gong, T. Xiang
in S. Ali, K. Nishino, D. Manocha, and M. Shah (Eds.), Modeling, Simulation and Visual Analysis of Crowds, Springer, vol. 11, pp. 347-382, 2013
- Feature Mining for Localised Crowd Counting
K. Chen, C. C. Loy, S. Gong, and T. Xiang
British Machine Vision Conference, 2012 (BMVC)
