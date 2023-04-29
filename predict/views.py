from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .model_utils import predict_image
from PIL import Image

# Create home view
def home(request):
    return render(request, 'predict/home.html')


def is_image(file):
    try:
        Image.open(file)
        return True
    except:
        return False


def predict(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            if not is_image(image_file):
                return render(request, 'predict/predict.html', {'message': 'File format not supported'})
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            uploaded_image_url = fs.url(filename)
            image_path = settings.MEDIA_ROOT + "/" + filename
            prediction = predict_image(image_path)
            if prediction:
                return render(request, 'predict/predict.html', {'uploaded_image_url': uploaded_image_url, 'prediction': prediction})
            else:
                fs.delete(filename)
                return render(request, 'predict/predict.html', {'message': 'Invalid image file'})
        else:
            return render(request, 'predict/predict.html', {'message': 'Please upload an image file'})
    return render(request, 'predict/predict.html')
