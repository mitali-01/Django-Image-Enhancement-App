import cv2
import numpy as np
from PIL import Image, ImageEnhance

def enhance_image(image_path, output_path, sharpness=4, contrast=1.3, blur=3):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    enhancer = ImageEnhance.Sharpness(pil_img)
    img_enhanced = enhancer.enhance(sharpness)
    enhancer = ImageEnhance.Contrast(img_enhanced)
    img_enhanced = enhancer.enhance(contrast)
    img_enhanced = np.array(img_enhanced)
    img_enhanced = cv2.GaussianBlur(img_enhanced, (blur, blur), 0)
    img_enhanced = Image.fromarray(img_enhanced)
    img_enhanced.save(output_path)