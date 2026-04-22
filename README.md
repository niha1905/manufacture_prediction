# Manufacture Prediction

A machine learning project focused on predicting food spoilage and manufacturing quality using computer vision and ML classification models.

## Overview

This repository contains a collection of Jupyter notebooks and Python scripts designed to detect and predict spoilage in food products, particularly vegetables and Indian food items. The project leverages machine learning techniques including Random Forest classification and object detection to identify spoiled items from images.

## Features

- **Spoilage Detection**: Predicts whether food items are spoiled using ML models
- **Object Detection**: Identifies and locates food items in images
- **Multiple Models**: Implements Random Forest and other classification algorithms
- **Dataset Processing**: Includes scripts for dataset creation and image conversion
- **Recipe Generation**: Notebook for recipe-related predictions

## Project Structure

```
manufacture_prediction/
├── Random_Forest_model.ipynb      # Random Forest classification model
├── convert.py                      # Image conversion utilities
├── dataset.py                      # Dataset creation and preprocessing
├── images.jpeg                     # Sample dataset image
├── jk/                             # Additional resources
├── large_indian_spoilage.ipynb     # Indian food spoilage dataset analysis
├── object_detector.ipynb           # Object detection implementation
├── recipe.ipynb                    # Recipe prediction notebook
├── spoiling_prediction.ipynb       # Main spoilage prediction model
└── vegetable_spoilage.ipynb        # Vegetable-specific spoilage detection
```

## Tech Stack

- **Language**: Python
- **Libraries**: TensorFlow/Keras, Scikit-learn, OpenCV, NumPy, Pandas
- **Environment**: Jupyter Notebook
- **ML Models**: Random Forest, CNN-based Object Detection

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- Required Python packages (see `requirements.txt` or install manually)

### Installation

```bash
# Clone the repository
git clone https://github.com/niha1905/manufacture_prediction.git
cd manufacture_prediction

# Install dependencies
pip install numpy pandas scikit-learn tensorflow opencv-python matplotlib
```

### Running the Notebooks

1. Open the desired notebook:
   ```bash
   jupyter notebook spoiling_prediction.ipynb
   ```
2. Run all cells in sequence
3. View results and predictions in the notebook output

## Usage

- **Spoilage Prediction**: Run `spoiling_prediction.ipynb` or `vegetable_spoilage.ipynb` to predict food spoilage
- **Object Detection**: Run `object_detector.ipynb` to detect food items in images
- **Dataset Creation**: Use `dataset.py` to prepare your own dataset
- **Random Forest Model**: Run `Random_Forest_model.ipynb` for classification-based predictions

## Dataset

The project includes sample images and dataset files for training and testing the models. The datasets focus on Indian food items and vegetables to detect spoilage patterns.

## License

This project is open-source and available under the MIT License.

## Author

**Nihaarika S**

- GitHub: [@niha1905](https://github.com/niha1905)
