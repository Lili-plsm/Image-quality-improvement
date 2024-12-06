import cv2
import os

# Папка с исходными изображениями
input_folder = "images"
# Папка для сохранения обрезанных изображений
output_folder = "croped_images"

# Создаем папку для сохранения, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Размер квадрата
square_size = 64

# Функция для обрезки изображений до квадратов
def crop_to_square(img):
    height, width = img.shape[:2]
    num_crops_width = width // square_size
    num_crops_height = height // square_size
    for i in range(num_crops_width):
        for j in range(num_crops_height):
            x = i * square_size
            y = j * square_size
            cropped_img = img[y:y+square_size, x:x+square_size]
            # Сохраняем только если обрезанный кусок имеет размер 64x64
            if cropped_img.shape[:2] == (square_size, square_size):
                cv2.imwrite(os.path.join(output_folder, f"{os.path.basename(image_path)}_{i}_{j}.png"), cropped_img)

# Обходим все изображения в папке и обрезаем их
for file_name in os.listdir(input_folder):

    image_path = os.path.join(input_folder, file_name)
    img = cv2.imread(image_path)
    if img is not None:
        crop_to_square(img)

    
