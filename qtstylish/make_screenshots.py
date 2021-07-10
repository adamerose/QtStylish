import math
from PIL import Image
from qtstylish.demo_widget import DemoWidget
import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
import qtstylish


def make_collage(image_paths, output_path, margin=10):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    print(image_paths)
    images = [Image.open(path) for path in image_paths]

    col_count = round(math.sqrt(len(images)))
    row_count = math.ceil(len(images) / col_count)

    print(row_count, col_count)
    image_height = max([image.height for image in images])
    image_width = max([image.width for image in images])
    background_size = (image_width * col_count, image_height * row_count)
    background = Image.new(
        'RGBA', background_size, (255, 255, 255, 0))
    print(background_size)
    for row in range(row_count):
        for col in range(col_count):
            try:
                image = images[col + row * col_count]
                offset = (col * (image_width + margin),
                          row * (image_height + margin))
                print(offset)
                background.paste(image, offset)
            except IndexError:
                break
    background.save(output_path)
    return True


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
    for theme in ['light', 'dark']:

        screenshots_dir = os.path.abspath(f'./screenshots/{theme}')
        collage_path = f'./screenshots/{theme}.png'
        os.makedirs(screenshots_dir, exist_ok=True)
        example = DemoWidget()
        if theme == 'light':
            example.setStyleSheet(qtstylish.light())
        elif theme == 'dark':
            example.setStyleSheet(qtstylish.dark())

        example.setFixedSize(900, 650)

        for ix, tab_name in enumerate(
                ['Buttons', 'Controls', 'Inputs', 'Displays', 'Containers', 'Tabs', 'Widgets', 'Main Window']):
            example.tabs.setCurrentIndex(ix)
            example.resize(750, 1000)
            pixmap = example.grab()
            save_path = os.path.abspath(os.path.join(
                screenshots_dir, tab_name + '.png'))
            print(save_path)
            pixmap.save(save_path, 'png')
        # Make collage

        image_paths = [os.path.abspath(os.path.join(
            screenshots_dir, path)) for path in os.listdir(screenshots_dir)]
        make_collage(image_paths, collage_path)
