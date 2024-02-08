# Data pre-processing
This repository was created for working in the topic Object Detection Using Machine Learning

## Installation For using GPU
1. conda create -n ENV_NAME python=3.7
2. conda activate ENV_NAME
3. conda install tensorflow-gpu=2.1
4. pip install tensorflow-gpu==2.3.1

## Active python kernel
1. pip install --user ipykernel
2. python -m ipykernel install --user --name=ENV_NAME

## Command for Check if GPU is available
1. nvidia-smi
2. import tensorflow as tf;tf.config.list_physical_devices("GPU")




