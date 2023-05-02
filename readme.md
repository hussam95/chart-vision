# Chart Vision App
This is a simple Django web application that allows users to upload an image and predicts the class of the image using a pre-trained machine learning/ CV model. The price action of finanical securities often form informing patterns. Traders often use these patterns to predict the future price movement. It is hence very valueable to have an automatic system that can detect these chart patterns. The model trained for this app achieves an accuracy of 82% on prediciting seven different chart patterns. These chart patterns include Breakout Pattern, DB, DT, Final Flag, TR, Wedge Bottom and Wedge Top patterns. 

**You can view the hosted app [here](https://hussam94.pythonanywhere.com/).**

# Prerequisites
To run this application, you need the following software installed on your system:

- Python 3.9
- Django==4.1.7
- djangorestframework==3.14.0
- Pillow==9.4.0
- torch==1.13.1+cu117
- torchaudio==0.13.1+cu117
- torchvision==0.14.1+cu117


# Installation
Clone the repository:
```python
git clone https://github.com/yourusername/chart-vision.git
```
cd into Django-project:
```python
cd chart-vision
```
Install the required packages:
```python
pip install -r requirements.txt
```
Run the server:
```python
python manage.py runserver
```
You can also consdier running the django project inside a virtual envrionment to avoid conflicts.

Open your browser and go to http://localhost:8000 to access the application.

# Usage
To use the application, follow these steps:

1. Make sure you update the `model_utils.py` of `predict` django-app. You can load your own model from this file into your app.

2. Make sure to have a media directory at the root of django project. This will handle file uploads.

3. Run the django server

4. Upload an image using the form on the home page.

5. Wait for the application to predict the class of the image.

6. View the predicted class on the results page.


# Acknowledgments
This project was created using the Django web framework.
The machine learning model was trained using the pytorch library.



