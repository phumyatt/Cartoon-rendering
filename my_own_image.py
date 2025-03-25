import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

def apply_cartoon_anime_style(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Step 1: Reduce Harsh Whites & Add Color Depth
    img_array = np.array(img_rgb, dtype=np.float32) / 255.0  # Normalize
    img_array[:, :, 0] *= 1.1  # Enhance Reds slightly for warmth
    img_array[:, :, 1] *= 1.05  # Slightly boost Greens for balance
    img_array[:, :, 2] *= 1.2  # Enhance Blues for a winter feel
    img_array = np.clip(img_array, 0, 1) * 255  # Clip & convert back
    img_array = img_array.astype(np.uint8)

    # Step 2: Apply a Cartoon Effect (Edge Detection + Color Flattening)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    gray_img = cv2.medianBlur(gray_img, 5)

    edges = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    color_img = cv2.bilateralFilter(img_array, 9, 300, 300)  # Smoothing for cartoonish look
    cartoon_img = cv2.bitwise_and(color_img, color_img, mask=edges)

    # Step 3: Add Soft Glow Effect (Dreamy Vibe)
    glow_layer = np.full(img_array.shape, (100, 80, 200), dtype=np.uint8)  # Soft purple-pink tint
    cartoon_img = cv2.addWeighted(cartoon_img, 0.9, glow_layer, 0.1, 0)  # Blend for dreamy feel

    # Step 4: Enhance Vibrancy and Sharpen the Details
    pil_img = Image.fromarray(cartoon_img)
    enhancer = ImageEnhance.Color(pil_img)
    pil_img = enhancer.enhance(1.6)  # Boost color saturation to give anime style vibrancy
    pil_img = pil_img.filter(ImageFilter.SHARPEN)  # Slight sharpening for that crisp look

    # Step 5: Snow Overlay (Optional)
    snow_layer = np.random.randint(180, 250, cartoon_img.shape, dtype=np.uint8)  # Random light dots
    cartoon_img = cv2.addWeighted(cartoon_img, 0.97, snow_layer, 0.03, 0)  # Soft snowfall effect

    # Save the final image
    pil_img.save(output_path)

# Example Usage
apply_cartoon_anime_style("my_own_image.jpeg", "my_own_image_output.jpg")