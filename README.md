# Image Enhancement App

A web-based application built with Django that allows users to upload an image, enhance it using custom filters (sharpness, contrast, and blur), and download the enhanced version. The app provides a simple and user-friendly interface for image enhancement tasks.

## Features

- **Image Upload**: Users can upload their image files.
- **Automatic Enhancement**: The image is automatically enhanced with predefined settings (sharpness=4.0, contrast=1.3, blur=3).
- **Custom Enhancement**: Users can adjust sharpness, contrast, and blur values and apply custom enhancements to the image.
- **Side-by-Side Comparison**: Displays both the original and enhanced images side by side.
- **Download Enhanced Image**: Provides a download button to get the enhanced image.

## Technologies Used

- **Django**: Python web framework for building the app.
- **Python**: Backend programming language.
- **HTML/CSS**: For structuring and styling the frontend.
- **JavaScript (optional)**: For any dynamic frontend interactions (if added in the future).
- **OpoenCV** (or other image processing libraries): For the actual image enhancement (e.g., applying sharpness, contrast, and blur).

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

Make sure you have Python 3.x installed on your system.

1. **Clone the repository**:
   ```bash
    git clone https://github.com/mitali-01/Django-Image-Enhancement-App
   ```
2. **Create and activate a Virtual Environment**
  ```bash
   python -m venv venv
   venv\Scripts\activate
  ```
3. **Install Required Dependencies**
  ```bash
   pip install -r requirements.txt
  ```
4. **Apply Migrations**
  ```bash
   python manage.py migrate
  ```
5. **Run the Development Server**
  ```bash
   python manage.py runserver
  ```
6. **Visit the App**
   Open your browser and navigate to http://127.0.0.1:8000/upload/ to start using the Image Enhancement App.

## Usage
1. **Upload an Image:**
  - Click on the "Upload Image" button to select and upload an image.
2. **Apply Automatic Enhancement:**
  - Once the image is uploaded, it will be automatically enhanced with default settings (sharpness=4.0, contrast=1.3, blur=3).
3. **Custom Enhancement:**
 - Adjust the sharpness, contrast, and blur values in the form and click "Apply Changes" to enhance the image according to your custom settings.
4. **Download Enhanced Image:**
  - After enhancing the image, you can download the enhanced version by clicking the "Download Enhanced Image" button.

##  Directory Structure
  ```bash
image-enhancement-app/
├── enhancer/                # Main app folder
│   ├── migrations/          # Database migrations
│   ├── static/              # Static files (e.g., CSS, images)
│   ├── templates/           # HTML templates
│   ├── forms.py             # Django forms for handling image uploads and custom enhancements
│   ├── image_processing.py  # Python file with image enhancement logic (e.g., sharpness, contrast, blur)
│   ├── models.py            # Database models (if applicable)
│   └── views.py             # View logic for handling requests and rendering responses
├── media/                   # Folder for uploaded images (handled by Django)
├── manage.py                # Django management commands
├── requirements.txt         # List of Python dependencies
└── README.md                # This file
  ```
