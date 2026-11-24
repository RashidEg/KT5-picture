import cv2

img = cv2.imread('gelik.jpg')

if img is None:
    print("Ошибка: файл не найден.")
else:
    # 2. Преобразуем в оттенки серого
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Применяем размытие по Гауссу для удаления шума

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Выделяем границы перед поиском контуров
    edges = cv2.Canny(blurred, 50, 150)

    # 4. Находим все контуры
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 5. Рисуем все контуры (-1) зелёным цветом поверх оригинального изображения
    # OpenCV используется формат BGR, поэтому зелёный - это (0, 255, 0)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # 6. Сохраняем результат
    cv2.imwrite('result.jpg', img)
    print(f"Готово! Найдено контуров: {len(contours)}. Результат сохранён в result.jpg")