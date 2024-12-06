import os
import cv2
import pickle
import torchvision.transforms as transforms
import random

image_folder = "croped_images"
image_tensors = []

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])  # Нормализация тензора  # Преобразуем изображение в тензор
])


# Чтение и преобразование каждой картинки
for file_name in os.listdir(image_folder):
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        image_path = os.path.join(image_folder, file_name)
        
        # Загружаем изображение с помощью OpenCV
        image = cv2.imread(image_path)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #image2 = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
        image2 = image
        num = random.randint(0, 100)
        _, encoded_image = cv2.imencode('.jpg', image2, [cv2.IMWRITE_JPEG_QUALITY, 15])
        image2 = cv2.imdecode(encoded_image, 1)
        image_tensor = transform(image)
        image_tensor2 = transform(image2)
        image_tensors.append((image_tensor, image_tensor2))

with open('dataset.pickle', 'wb') as f:
    pickle.dump(image_tensors, f)
