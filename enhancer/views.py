from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import ImageUploadForm, CustomEnhancementForm
from .image_processing import enhance_image

def upload_image(request):
    # Handle image upload
    if request.method == 'POST' and 'upload' in request.POST:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(image.name, image)
            uploaded_file_url = settings.MEDIA_URL + filename

            # Clear any previously stored file in the session to prevent using old files
            request.session['uploaded_file'] = filename

            # Apply default enhancement (sharpness=4, contrast=1.3, blur=3)
            enhanced_image_path = 'enhanced_' + filename
            enhance_image(fs.path(filename), fs.path(enhanced_image_path), sharpness=4, contrast=1.3, blur=3)
            enhanced_file_url = settings.MEDIA_URL + enhanced_image_path

            return render(request, 'enhancer/upload_image.html', {
                'form': form,
                'uploaded_file_url': uploaded_file_url,
                'enhanced_file_url': enhanced_file_url,
                'enhancement_form': CustomEnhancementForm()
            })
        else:
            return render(request, 'enhancer/upload_image.html', {
                'form': form,
                'enhancement_form': CustomEnhancementForm()
            })

    # Handle custom enhancements (applying changes)
    elif request.method == 'POST' and 'apply_changes' in request.POST:
        enhancement_form = CustomEnhancementForm(request.POST)
        if enhancement_form.is_valid():
            # Get the uploaded image file path from the session
            filename = request.session.get('uploaded_file', None)
            if filename:
                fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                uploaded_file_url = settings.MEDIA_URL + filename

                # Get the custom enhancement parameters
                sharpness = enhancement_form.cleaned_data['sharpness']
                contrast = enhancement_form.cleaned_data['contrast']
                blur = enhancement_form.cleaned_data['blur']

                # Apply custom enhancement
                enhanced_image_path = 'enhanced_' + filename
                enhance_image(fs.path(filename), fs.path(enhanced_image_path), sharpness=sharpness, contrast=contrast, blur=blur)
                enhanced_file_url = settings.MEDIA_URL + enhanced_image_path

                return render(request, 'enhancer/upload_image.html', {
                    'uploaded_file_url': uploaded_file_url,
                    'enhanced_file_url': enhanced_file_url,
                    'enhancement_form': enhancement_form
                })
            else:
                return render(request, 'enhancer/upload_image.html', {
                    'error': 'No uploaded image found in session.',
                    'enhancement_form': enhancement_form
                })

    # If it's a GET request or the form isn't valid, show the upload page
    else:
        form = ImageUploadForm()
        enhancement_form = CustomEnhancementForm()

        # Check if there's an uploaded image in the session
        uploaded_file_url = None
        if 'uploaded_file' in request.session:
            del request.session['uploaded_file']

        return render(request, 'enhancer/upload_image.html', {
            'form': form,
            'uploaded_file_url': uploaded_file_url,
            'enhancement_form': enhancement_form
        })
