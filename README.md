My cartoon rendering using OpenCV
# 만화 스타일 이미지 변환기

이 Python 프로그램은 이미지를 만화 스타일로 변환하여 독특하고 예술적인 효과를 제공합니다. OpenCV와 NumPy를 사용하여 색상 강조, 에지 검출, 블러 처리 등의 기법을 통해 만화 같은 느낌을 구현합니다.

기능
- 만화 스타일 변환**: 입력 이미지를 만화 스타일로 변환하여 색상과 선명도를 강조합니다.
- 에지 검출**: 이미지의 윤곽선을 감지하여 만화 효과를 극대화합니다.
- 색상 향상**: 자연스러운 색감을 유지하면서 색상을 더욱 풍부하게 만듭니다.

요구사항
이 프로그램을 실행하려면 다음 Python 라이브러리가 필요합니다:
- OpenCV
- NumPy

다음 명령어를 사용하여 필요한 라이브러리를 설치할 수 있습니다:
```bash
pip install opencv-python numpy
```

사용 방법
1. 변환할 이미지를 준비합니다. 예를 들어, 'cartoon.png`라는 이름의 파일을 사용합니다.
2. 아래의 함수를 호출하여 이미지를 변환합니다:
```python
cartoonize_image("cartoon.png", "cartoon_output.jpg")
```
3. 실행 후 `cartoon_output.jpg`로 저장된 결과를 확인합니다.
데모 및 한계점 논의
 1. 만화 같은 느낌이 잘 표현되는 이미지 데모 

아래 이미지는 알고리즘이 만화 스타일로 잘 변환된 예시입니다:

[Cartoon Demo](cartoon_output.jpg)
 2. 만화 같은 느낌이 잘 표현되지 않는 이미지 데모 

아래 이미지는 알고리즘이 제대로 작동하지 않는 경우를 보여줍니다:

[Non-Demo](cartoon_output1.jpg)

 3. 알고리즘의 한계점
- 복잡한 배경: 복잡한 배경이 있는 이미지에서는 에지 검출이 어려워 만화 스타일이 잘 표현되지 않을 수 있습니다.
- 세부 사항 손실: 세부 사항이 많은 이미지에서는 중요한 요소가 손실될 수 있습니다.
- 색상 균형: 색상 강조가 과도해지면 이미지의 자연스러움이 줄어들 수 있습니다.
- 조명 조건: 조명이 고르지 않거나 그림자가 많은 이미지에서는 원하는 효과를 얻기 어려울 수 있습니다.

#My_own_image to animation(just my pratice)
#Cartoon Animation Style Effect

This Python script applies a **cartoon anime style** effect to a given image. The output will have bright colors, soft blur, and **vivid anime-like features**.

Requirements
You need the following libraries installed:
- opencv-python: For image processing.
- numpy: For numerical operations.
- Pillow (PIL): For advanced image manipulation (e.g., Gaussian blur, color enhancement).

You can install the dependencies using `pip`:
```bash
pip install opencv-python numpy Pillow
```
Usage
1. Download the script as `cartoon_anime_style.py`.
2. Place the image you want to transform into the same directory (or specify its path).
3. Run the script with the following command:

```bash
python my_own_image.py input_image.jpg output_image.jpg
```

- input_image.jpeg: Path to the photo you want to apply the cartoon effect to.
- output_image.jpg: Path where the transformed image will be saved.

```bash
python cartoon_anime_style.py my_photo.jpg my_cartoon_output.jpg
```

This will process `my_own_image.jpeg` and save the result as `my_own_image_output.jpg`.

How It Works:
- Color Enhancement: The script enhances the image colors to make them more vibrant and cartoon-like by modifying the RGB channels.
- Soft Blur: A Gaussian blur is applied to simulate the smooth, soft look found in anime.
- Color Saturation: Increases color vibrancy to make the image pop.
- Dreamy Glow: Adds a soft purple-pink glow to create a dreamy effect.
- Posterization: Reduces the number of colors to create a flat, cartoonish look.

