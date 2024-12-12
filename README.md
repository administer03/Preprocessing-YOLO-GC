# Object Detection Using Machine Learning: Project Setup Guide

## Overview
This repository provides resources and setup instructions for preprocessing globular cluster detection using YOLO-GC.

## Prerequisites
- Anaconda or Miniconda installed
- NVIDIA GPU with compatible drivers

## Installation and Environment Setup

### 1. Create Conda Environment
```bash
# Create a new conda environment with Python 3.7
conda create -n pre_yologc python=3.7

# Activate the environment
conda activate pre_yologc
```

### 2. Install TensorFlow GPU
```bash
# Install TensorFlow GPU (compatible versions)
conda install tensorflow-gpu=2.1
pip install tensorflow-gpu==2.3.1
```

### 3. Set Up Python Kernel
```bash
# Install ipykernel for Jupyter Notebook support
pip install --user ipykernel

# Register the kernel with Jupyter
python -m ipykernel install --user --name=object_detection
```

## Recommended Additional Packages
```bash
# Install common ML and CV libraries
pip install numpy pandas matplotlib scikit-learn opencv-python
```

## Preprocessing
The main file for processing is [fits_to_npy.ipynb](./python_files/npy_extraction/fits_to_npy.ipynb). Open this file to begin preprocessing your data.

## Post-processing
Follow [post_processing.ipynb](./python_files/npy_extraction/post_processing.ipynb) for more details.
