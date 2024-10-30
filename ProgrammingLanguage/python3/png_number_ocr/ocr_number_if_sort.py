# uft-8
import pytesseract
# If Tesseract is not in your PATH, specify the full path to the executable
# pytesseract.pytesseract.tesseract_cmd = r'D:/Software/Tesseract'
from PIL import Image, ImageFilter, ImageOps
import re

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = ImageOps.grayscale(image)
    image = image.point(lambda x: 0 if x < 128 else 255, '1')
    image = image.filter(ImageFilter.MedianFilter(size=3))
    return image
def extract_numbers(image_path):
    image = preprocess_image(image_path)
    text = pytesseract.image_to_string(image, config='--oem 3 --psm 7')
    numbers = re.findall(r'\d+', text)
    return [int(num) for num in numbers]
def check_sequence1(numbers):
    missing_numbers = []
    reversed_numbers = []
    sorted_numbers = sorted(numbers)
    # 检查是否按升序排列
    if numbers != sorted_numbers:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                reversed_numbers.append((numbers[i], numbers[i + 1]))
    # 检查是否有缺失的数字
    full_range = list(range(min(numbers), max(numbers) + 1))
    missing_numbers = list(set(full_range) - set(numbers))
    return missing_numbers, reversed_numbers
def check_missing_and_disordered(numbers):
    # 找到最小和最大值
    min_num = min(numbers)
    max_num = max(numbers)
    # 生成完整的数字范围
    full_range = set(range(min_num, max_num + 1))
    # 找出缺失的数字
    missing_numbers = full_range - set(numbers)
    # 找出顺序颠倒的数字
    disordered_pairs = []
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            disordered_pairs.append((numbers[i], numbers[i + 1]))
    return missing_numbers, disordered_pairs
def main(image_path):
    numbers = extract_numbers(image_path)
    print(numbers)
    if not numbers:
        print("未能识别出任何数字。")
        return
    missing_numbers, reversed_numbers = check_missing_and_disordered(numbers)
    if not missing_numbers and not reversed_numbers:
        print("数字按顺序排列，没有缺失或颠倒的数字。")
    else:
        if missing_numbers:
            print("缺失的数字:", missing_numbers)
        if reversed_numbers:
            print("顺序颠倒的数字对:", reversed_numbers)
# 用法：
image_path = 'F:\\002Dev\\github\\for-my-dream\\ProgrammingLanguage\\python3\\png_number_ocr\\aaa.png'
main(image_path)