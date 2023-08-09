from django.shortcuts import render, redirect  # Import the redirect function
from django.contrib import messages
from .forms import ImageUploadForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('image_upload_demo:upload_image')  # Redirect to the upload page
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload_demo/upload.html', {'form': form})
