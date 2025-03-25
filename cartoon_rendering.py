import cv2
import numpy as np

def resize_image(img, max_size=600):
    """Resize the image while maintaining aspect ratio."""
    h, w = img.shape[:2]
    scale_factor = max_size / max(h, w)
    new_size = (int(w * scale_factor), int(h * scale_factor))
    return cv2.resize(img, new_size)

def cartoonize_image(image_path, output_path="cartoonized_image.jpg", blur_intensity=7, bilateral_strength=100):
    """Apply a cartoon effect to an image."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    img = resize_image(img)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray_blur = cv2.medianBlur(gray, blur_intensity)

    # Edge detection using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray_blur, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter for smooth colors
    color = cv2.bilateralFilter(img, d=10, sigmaColor=bilateral_strength, sigmaSpace=bilateral_strength)

    # Combine edges with the smoothed image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save and display
    cv2.imwrite(output_path, cartoon)
    cv2.imshow("Cartoon Effect", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pencil_sketch(image_path, output_path="pencil_sketch.jpg", blur_intensity=21):
    """Convert an image to a pencil sketch."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    img = resize_image(img)

    # Convert to grayscale and invert
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)

    # Apply Gaussian blur to the inverted image
    blurred = cv2.GaussianBlur(inverted, (blur_intensity, blur_intensity), 0)

    # Invert the blurred image and create a pencil sketch
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    # Save and display
    cv2.imwrite(output_path, sketch)
    cv2.imshow("Pencil Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cartoonize_video(bilateral_strength=100):
    """Apply a cartoon effect to live video from the webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.resize(frame, (640, 480))

        # Convert to grayscale and apply blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, 7)

        # Edge detection
        edges = cv2.adaptiveThreshold(gray_blur, 255, 
                                      cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 9, 9)

        # Apply bilateral filter
        color = cv2.bilateralFilter(frame, d=10, sigmaColor=bilateral_strength, sigmaSpace=bilateral_strength)

        # Combine edges with color
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        # Show video output
        cv2.imshow("Cartoon Video", cartoon)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the functions
cartoonize_image("cartoon.png")  # Change image path as needed
pencil_sketch("image.jpg")  # Optional: Convert to pencil sketch
# cartoonize_video()  # Uncomment to run live cartoonization