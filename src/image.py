import cv2
import time

def match(src, template, display=True):
    if src is None:
        print("Source image is None")
    elif template is None:
        print("Template image is None")
    result = cv2.matchTemplate(template, src, cv2.TM_SQDIFF_NORMED)
    _, _, loc, _ = cv2.minMaxLoc(result)
    x_shift = template.shape[1]
    y_shift = template.shape[0]
    x = loc[0] + x_shift // 2
    y = loc[1] + y_shift // 2
    if display:
        width = 10
        photo_name = "[" + time.strftime("%H-%M-%S", time.localtime()) + "]result.png"
        # cv2.imshow("result", result)
        # cv2.rectangle(src, (x - width, y-width), (x+width, y+width), (0,0,255), 2)
        # cv2.imshow("src", src)
        # print(loc)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        src = drawRectangle(src, x, y, width, 2)
        cv2.imwrite(photo_name, src)
    return x, y

def imLoad(filename):
    return cv2.imread(filename)

def templateLoad(filename):
    return cv2.imread("./../image/{}".format(filename))


def drawRectangle(image, x, y, width, linewidth):
    newImage = cv2.rectangle(image, (x-width, y-width), (x+width, y+width), (0, 0, 255), linewidth)
    # cv2.imshow("image", image)
    # print("({}, {})".format(str(x), str(y)))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return newImage