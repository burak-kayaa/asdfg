import cv2
import numpy as np

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# from PIL import ImageGrab
# from PIL import Image
# from io import BytesIO

# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Headless modu etkinleştir
# # chrome_options.add_argument("--window-size=1280,720")  # Pencere boyutunu belirle (örneğin: 800x600)

# # Selenium'un Chrome WebDriver'ını başlatma
# #options=chrome_options
# driver = webdriver.Chrome(options=chrome_options)


# # URL'ye gitme
# url = "http://agarz.com"
# driver.get(url)
# action_chains = ActionChains(driver)



# wait = WebDriverWait(driver, 10)

# # '#playBtn' elementinin varlığını bekleyerek bulma
# play_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#playBtn")))
# # document.querySelector("#yesno_settings > label:nth-child(10) > input[type=checkbox]").click() 

# checkbox_element = driver.find_element(By.CSS_SELECTOR, "#yesno_settings > label:nth-child(10) > input[type=checkbox]")
# checkbox_element.click()


# driver.maximize_window()

# # Element bulunduğunda kodun devam etmesi
# if play_btn:
#     print("'#playBtn' elementi bulundu.")
#     play_btn.click()
#     print("'#playBtn' elementine tıklandı.")


# window_height = driver.execute_script("return window.screen.height;")
# window_width = driver.execute_script("return window.screen.width;")
# print(f"Window height: {window_height}, Window width: {window_width}")





# # frameWidth = 640
# # frameHeigh = 480
# # cap = cv2.VideoCapture(0)
# # cap.set(3, frameWidth)
# # cap.set(4, frameHeigh)


# def empty(a):
#     pass


# cv2.namedWindow("Parameters")
# cv2.resizeWindow("Parameters", 640, 240)
# cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)


# def find_shape(approx, imgContour, x, y, w, h):
#     if len(approx) == 3:
#         cv2.putText(
#             imgContour,
#             "Triangle",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )
#     elif len(approx) == 4:
#         aspectRatio = w / float(h)
#         if aspectRatio > 0.95 and aspectRatio < 1.05:
#             cv2.putText(
#                 imgContour,
#                 "Square",
#                 (x + w + 20, y + 20),
#                 cv2.FONT_HERSHEY_COMPLEX,
#                 0.7,
#                 (0, 255, 0),
#                 2,
#             )
#         else:
#             cv2.putText(
#                 imgContour,
#                 "Rectangle",
#                 (x + w + 20, y + 20),
#                 cv2.FONT_HERSHEY_COMPLEX,
#                 0.7,
#                 (0, 255, 0),
#                 2,
#             )
#     elif len(approx) == 5:
#         cv2.putText(
#             imgContour,
#             "Pentagon",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )
#     elif len(approx) == 6:
#         cv2.putText(
#             imgContour,
#             "Hexagon",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )
#     else:
#         cv2.putText(
#             imgContour,
#             "Circle",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )


# def closest_contour(contours, imgContour):
#     closest_contour_helper = []
#     i = 0
#     for cnt in contours:
#         x, y, w, h = cv2.boundingRect(cnt)
#         if len(closest_contour_helper) == 0:
#             closest_contour_helper = [cnt[0][0][0], cnt[0][0][1], i]
#         else:
#             if (cnt[0][0][0] ** 2 + cnt[0][0][1] ** 2) < (
#                 closest_contour_helper[0] ** 2 + closest_contour_helper[1] ** 2
#             ):
#                 closest_contour_helper = [cnt[0][0][0], cnt[0][0][1], i]
#         i += 1
#     return contours[closest_contour_helper[2]]


# def getContours(img, imgContour):
#     contours, hierarchy = cv2.findContours(
#         img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
#     )
#     tmp =9999
#     xtmp = 0
#     ytmp = 0

#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 200 and area < 2000:
#             peri = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.085 * peri, True)
#             (x, y, w, h) = cv2.boundingRect(approx)
#             cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
#             if len(approx) > 3:
#                 cv2.putText(
#                     imgContour,
#                     "Area: " + str(int(area)) + "x, y: " + str(x) + " " + str(y),
#                     (x + w + 20, y + 45),
#                     cv2.FONT_HERSHEY_COMPLEX,
#                     0.7,
#                     (0, 255, 0),
#                     2,
#                 )
#                 wh = driver.execute_script("return document.documentElement.clientHeight;")
#                 ww = driver.execute_script("return document.documentElement.clientWidth;")
#                 dx = x - ww
#                 dy = y - wh
#                 pis = (dx ** 2 + dy ** 2) ** 0.5
#                 if pis < tmp:
#                     tmp = pis
#                     xtmp = x
#                     ytmp = y
    
#     cv2.line(imgContour, (0, 0), (xtmp, ytmp), (0, 0, 255), 3)
#     print(xtmp, ytmp)
#     driver.execute_script(f"rawMouseX={xtmp/2}")
#     driver.execute_script(f"rawMouseY={ytmp/2}")

    
#     # if min_x or min_y:
#     #     min_cor = min(min_x)
#     #     min_cor_y = min(min_y)
#     #     cnt = closest_contour(contours, imgContour)
#     #     print(cnt)
#     #     area = cv2.contourArea(cnt)
#     #     if area > 1000:
#     #         peri = cv2.arcLength(cnt, True)
#     #         approx = cv2.approxPolyDP(cnt, 0.075 * peri, True)
#     #         (x, y, w, h) = cv2.boundingRect(approx)
#     #         if x == min_cor or y == min_cor_y:
#     #             x_c, y_c = int(x + (w / 2)), int(y + (h / 2))
#     #             cv2.line(imgContour, (0, 0), (x_c, y_c), (255, 0, 0), 3)


# while True:
#     # succes, img = cap.read()
#     # if succes != 1:
#     #     break

#     left = 0
#     top = 0
#     right = window_width
#     bottom = window_height
#     screenshot = driver.get_screenshot_as_png()

#     # Pillow kütüphanesiyle ekran görüntüsünü işleme
#     img = Image.open(BytesIO(screenshot))
#     img_cropped = img.crop((left, top, right, bottom))
#     # görseli kopyala cv2 ile
#     img_cropped_copy = img_cropped.copy()

#     # NumPy dizisine dönüştürme
#     img_np = np.array(img_cropped_copy)
#     frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    

#     threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#     threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
#     imgCanny = cv2.Canny(frame, threshold1, threshold2)
#     kernel = np.ones((5, 5))
#     imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
#     getContours(imgDil, img_np)
#     cv2.imshow("final", img_np)
    
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# # cap.release()
# cv2.destroyAllWindows()

# driver.quit()

# # imgContour = img.copy()

#     # imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
#     # imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

   
   
#     # kernel = np.ones((5, 5))

#     # imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

#     # getContours(imgDil, imgContour)
#     # cv2.imshow("canny", imgCanny)
#     # cv2.imshow("final", imgContour)













#PİSAGOR İLE YOL BUL


# frameWidth = 640
# frameHeigh = 480
# cap = cv2.VideoCapture("/Users/burkaya/Desktop/Python/Shape/find_path.mp4")
# cap.set(3, frameWidth)
# cap.set(4, frameHeigh)


# def empty(a):
#     pass


# cv2.namedWindow("Parameters")
# cv2.resizeWindow("Parameters", 640, 240)
# cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)


# def find_shape(approx, imgContour, x, y, w, h):
#     if len(approx) == 3:
#         cv2.putText(
#             imgContour,
#             "Triangle",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )
#     elif len(approx) == 4:
#         aspectRatio = w / float(h)
#         if aspectRatio > 0.95 and aspectRatio < 1.05:
#             cv2.putText(
#                 imgContour,
#                 "Square",
#                 (x + w + 20, y + 20),
#                 cv2.FONT_HERSHEY_COMPLEX,
#                 0.7,
#                 (0, 255, 0),
#                 2,
#             )
#         else:
#             cv2.putText(
#                 imgContour,
#                 "Rectangle",
#                 (x + w + 20, y + 20),
#                 cv2.FONT_HERSHEY_COMPLEX,
#                 0.7,
#                 (0, 255, 0),
#                 2,
#             )
#     elif len(approx) == 5:
#         cv2.putText(
#             imgContour,
#             "Pentagon",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )
#     elif len(approx) == 6:
#         cv2.putText(
#             imgContour,
#             "Hexagon",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )
#     else:
#         cv2.putText(
#             imgContour,
#             "Circle",
#             (x + w + 20, y + 20),
#             cv2.FONT_HERSHEY_COMPLEX,
#             0.7,
#             (0, 255, 0),
#             2,
#         )


# def closest_contour(contours, imgContour):
#     closest_contour_helper = []
#     i = 0
#     for cnt in contours:
#         x, y, w, h = cv2.boundingRect(cnt)
#         if len(closest_contour_helper) == 0:
#             closest_contour_helper = [cnt[0][0][0], cnt[0][0][1], i]
#         else:
#             if (cnt[0][0][0] ** 2 + cnt[0][0][1] ** 2) < (
#                 closest_contour_helper[0] ** 2 + closest_contour_helper[1] ** 2
#             ):
#                 closest_contour_helper = [cnt[0][0][0], cnt[0][0][1], i]
#         i += 1
#     return contours[closest_contour_helper[2]]


# def getContours(img, imgContour):
#     min_x = []
#     min_y = []
#     contours, hierarchy = cv2.findContours(
#         img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
#     )
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 2000 and area < 50000:
#             peri = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.085 * peri, True)
#             print(len(approx))
#             (x, y, w, h) = cv2.boundingRect(approx)
#             cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
#             min_x.append(x)
#             min_y.append(y)
#             if len(approx) > 4:
#                 find_shape(approx, imgContour, x, y, w, h)
#                 cv2.putText(
#                     imgContour,
#                     "Area: " + str(int(area)),
#                     (x + w + 20, y + 45),
#                     cv2.FONT_HERSHEY_COMPLEX,
#                     0.7,
#                     (0, 255, 0),
#                     2,
#                 )
#     if min_x or min_y:
#         min_cor = min(min_x)
#         min_cor_y = min(min_y)
#         cnt = closest_contour(contours, imgContour)
#         print(cnt)
#         area = cv2.contourArea(cnt)
#         if area > 1000:
#             peri = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.075 * peri, True)
#             (x, y, w, h) = cv2.boundingRect(approx)
#             if x == min_cor or y == min_cor_y:
#                 x_c, y_c = int(x + (w / 2)), int(y + (h / 2))
#                 cv2.line(imgContour, (0, 0), (x_c, y_c), (255, 0, 0), 3)


# while True:
#     succes, img = cap.read()
#     if succes != 1:
#         break
#     imgContour = img.copy()

#     imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
#     imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

#     threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#     threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
#     imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
#     kernel = np.ones((5, 5))

#     imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

#     getContours(imgDil, imgContour)
#     cv2.imshow("canny", imgCanny)
#     cv2.imshow("final", imgContour)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()


# // MERKEZ BUL


# frameWidth = 640
# frameHeigh = 480
# cap = cv2.VideoCapture("/Users/burkaya/Desktop/Python/Shape/find_path.mp4")
# cap.set(3, frameWidth)
# cap.set(4, frameHeigh)


# def empty(a):
#     pass

# cv2.namedWindow("Parameters")
# cv2.resizeWindow("Parameters", 640, 240)
# cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)


# def getContours(img, imgContour):
#     contours, hierarchy = cv2.findContours(
#         img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
#     )
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 1000:
#             # cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
#             peri = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
#             print(len(approx))
#             (x, y, w, h) = cv2.boundingRect(approx)
#             # cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
#             x_c, y_c = int(x + (w / 2)), int(y + (h / 2))
#             cv2.line(imgContour,(0,0),(x_c,y_c),(255,0,0),3)
#             cv2.putText(
#                 imgContour,
#                 "Points: " + str(len(approx)),
#                 (x + w + 20, y + 20),
#                 cv2.FONT_HERSHEY_COMPLEX,
#                 0.7,
#                 (0, 255, 0),
#                 2,
#             )
#             cv2.putText(
#                 imgContour,
#                 "Area: " + str(int(area)),
#                 (x + w + 20, y + 45),
#                 cv2.FONT_HERSHEY_COMPLEX,
#                 0.7,
#                 (0, 255, 0),
#                 2,
#             )


# while True:
#     succes, img = cap.read()
#     if succes != 1:
#         break
#     imgContour = img.copy()

#     imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
#     imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

#     threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#     threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
#     imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
#     kernel = np.ones((5, 5))

#     imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

#     getContours(imgDil, imgContour)
#     cv2.imshow("canny", imgCanny)
#     cv2.imshow("final", imgContour)
#     # imgStack = stackImages(0.8, ([img, imgGray, imgCanny], [imgDil, imgContour, imgContour]))
#     # cv2.imshow("Result", imgStack)
#     if cv2.waitKey(5) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()


# def stackImages(scale, imgArray):
#   rows = len(imgArray)
#   cols = len(imgArray[0])
#   rowsAvailable = isinstance(imgArray[0], list)
#   width = imgArray[0][0].shape[1]
#   height = imgArray[0][0].shape[0]
#   if rowsAvailable:
#       for x in range(0, rows):
#           for y in range(0, cols):
#               if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                   imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#               else:
#                   imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#               if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#       imageBlank = np.zeros((height, width, 3), np.uint8)
#       hor = [imageBlank] * rows
#       hor_con = [imageBlank] * rows
#       for x in range(0, rows):
#           hor[x] = np.hstack(imgArray[x])
#       ver = np.vstack(hor)
#   else:
#       for x in range(0, rows):
#           if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#               imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#           else:
#               imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#           if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#       hor = np.hstack(imgArray)
#       ver = hor
#   return ver


# import cv2
# import numpy as np

# frameWidth = 640
# frameHeigh = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeigh)

# def empty(a):
#   pass

# cv2.namedWindow("Parameters")
# cv2.resizeWindow("Parameters", 640, 240)
# cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)

# def stackImages(scale, imgArray):
#   rows = len(imgArray)
#   cols = len(imgArray[0])
#   rowsAvailable = isinstance(imgArray[0], list)
#   width = imgArray[0][0].shape[1]
#   height = imgArray[0][0].shape[0]
#   if rowsAvailable:
#       for x in range(0, rows):
#           for y in range(0, cols):
#               if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                   imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#               else:
#                   imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#               if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#       imageBlank = np.zeros((height, width, 3), np.uint8)
#       hor = [imageBlank] * rows
#       hor_con = [imageBlank] * rows
#       for x in range(0, rows):
#           hor[x] = np.hstack(imgArray[x])
#       ver = np.vstack(hor)
#   else:
#       for x in range(0, rows):
#           if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#               imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#           else:
#               imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#           if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#       hor = np.hstack(imgArray)
#       ver = hor
#   return ver

# def getContours(img, imgContour):
#   contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#   for cnt in contours:
#       area = cv2.contourArea(cnt)
#       if area > 1000:
#           cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
#           peri = cv2.arcLength(cnt, True)
#           approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
#           print(len(approx))
#           (x, y, w, h) = cv2.boundingRect(approx)
#           cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
#           cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 2)
#           cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 2)

# while True:
#   succes, img = cap.read()
#   imgContour = img.copy()

#   imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
#   imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

#   threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#   threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
#   imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
#   kernel = np.ones((5, 5))
#   imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

#   getContours(imgDil, imgContour)

#   imgStack = stackImages(0.8, ([img, imgGray, imgCanny], [imgDil, imgContour, imgContour]))
#   cv2.imshow("Result", imgStack)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#       break
# cap.release()
# cv2.destroyAllWindows()
