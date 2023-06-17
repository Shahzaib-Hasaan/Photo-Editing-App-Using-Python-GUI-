from PySide6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFilter, ImageOps, ImageChops
from FilterApp_ui import Ui_MainWindow
from PySide6.QtGui import QIcon

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Filter App")
        self.set_window_icon()  # Add this line to set the window icon
        self.apply_styles()
        self.toolButton.clicked.connect(self.select_photo)
        self.pushButton.clicked.connect(self.image_show)
        self.flipup.clicked.connect(self.flip_up)
        self.fliplr.clicked.connect(self.flip_horizontal)
        self.rotate90.clicked.connect(self.rotate_90_degrees)
        self.filter1.clicked.connect(self.apply_blur)
        self.filter2.clicked.connect(self.apply_edge_enhance)
        self.filter3.clicked.connect(self.apply_pencil_sketch)
        self.save.clicked.connect(self.save_image)
        self.close.clicked.connect(self.clear_path)
        self.frame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.setFixedSize(self.size())
        self.num_flips = 0
        self.horizontal_flipped = False
        self.rotation_angle = 0
        self.current_image = None
    def set_window_icon(self):
        icon = QIcon("/media/solu/Local Disk/Programming/GUI Development/Filter App/Icons/icon.png")  # Replace with the actual path to your icon file
        self.setWindowIcon(icon)

    def flip_up(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            flipped_image = image.transpose(
                Image.FLIP_TOP_BOTTOM if self.num_flips % 2 == 0 else Image.FLIP_LEFT_RIGHT
            )
            self.num_flips += 1
            self.display_image(flipped_image)
        else:
            self.show_error_message("Please enter a photo")

    def select_photo(self):
        photo_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Photo", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if photo_path:
            self.path.setText(photo_path)

    def image_show(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            self.num_flips = 0
            self.horizontal_flipped = False
            self.rotation_angle = 0
            self.current_image = image
            self.display_image(image)
        else:
            self.show_error_message("Please enter a photo")

    def display_image(self, image):
        if image.mode != "RGBA":
            new_image = Image.new("RGBA", image.size)
            new_image.paste(image, (0, 0))
            image = new_image
        image.thumbnail((self.imageshow.width(), self.imageshow.height()), Image.ANTIALIAS)
        pixmap = QtGui.QPixmap.fromImage(
            QtGui.QImage(
                image.tobytes("raw", "RGBA"),
                image.size[0],
                image.size[1],
                QtGui.QImage.Format_RGBA8888,
            )
        )
        self.imageshow.clear()
        self.imageshow.setPixmap(pixmap)
        self.imageshow.setAlignment(QtCore.Qt.AlignCenter)
        self.imageshow.setScaledContents(True)
        self.imageshow.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.imageshow.adjustSize()
        self.frame_2.layout().addWidget(self.imageshow)
        self.frame_2.adjustSize()
        self.adjustSize()

    def show_error_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msg.setInformativeText("Photo is required")
        msg.exec_()

    def flip_horizontal(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            self.horizontal_flipped = not self.horizontal_flipped
            if self.horizontal_flipped:
                self.display_image(flipped_image)
            else:
                self.display_image(image)
        else:
            self.show_error_message("Please enter a photo")

    def rotate_90_degrees(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            rotated_image = image.rotate(90 * (self.rotation_angle % 4))
            self.rotation_angle += 1
            self.display_image(rotated_image)
        else:
            self.show_error_message("Please enter a photo")

    def apply_edge_enhance(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
            self.current_image = filtered_image
            self.display_image(filtered_image)
        else:
            self.show_error_message("Please enter a photo")

    def apply_blur(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            filtered_image = image.filter(ImageFilter.BLUR)
            self.current_image = filtered_image
            self.display_image(filtered_image)
        else:
            self.show_error_message("Please enter a photo")

    def apply_pencil_sketch(self):
        image_path = self.path.text()
        if image_path:
            image = Image.open(image_path)
            grayscale_image = image.convert("L")
            inverted_image = ImageOps.invert(grayscale_image)
            blurred_image = inverted_image.filter(ImageFilter.BLUR)
            pencil_sketch = ImageChops.difference(grayscale_image, blurred_image)
            pencil_sketch = pencil_sketch.convert("L")
            pencil_sketch = pencil_sketch.point(lambda x: 255 - x)
            self.current_image = pencil_sketch
            self.display_image(pencil_sketch)
        else:
            self.show_error_message("Please enter a photo")

    def clear_path(self):
        self.path.clear()
        self.imageshow.clear()
        self.current_image = None

    def save_image(self):
        if self.imageshow.pixmap() is not None:
            save_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)"
            )
            if save_path:
                self.imageshow.pixmap().save(save_path)
        else:
            self.show_error_message("No image to save")


    def closeEvent(self, event):
        confirm_exit = QtWidgets.QMessageBox.question(
            self, "Exit Confirmation", "Are you sure you want to exit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if confirm_exit == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def apply_styles(self):
        style_sheet = """
        QMainWindow {
            background-color: #f2f2f2;
        }
        
        QLabel#imageshow {
            background-color: #ffffff;
            border: 1px solid #cccccc;
        }

        label_2 {
            font-size: 16px;
            color: #333333;
            font-weight: bold;
        }
        
        label {
            font-size: 14px;
            color: #666666;
            margin-top: 8px;
        }
        
        QPushButton {
            background-color: #4c75af;
            color: #ffffff;
            padding: 8px 16px;
            border-radius: 4px;
        }
        
        QPushButton:hover {
            background-color: #5477b8;
        }
        
        QPushButton:pressed {
            background-color: #44629e;
        }
        
        QToolButton {
            background-color: #4c75af;
            color: #ffffff;
            padding: 8px 16px;
            border-radius: 4px;
        }
        
        QToolButton:hover {
            background-color: #5477b8;
        }
        
        QToolButton:pressed {
            background-color: #44629e;
        }
        
        QComboBox {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            padding: 4px 8px;
            border-radius: 4px;
        }
        
        QComboBox:hover {
            border: 1px solid #aaaaaa;
        }
        
        QLineEdit {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            padding: 4px 8px;
            border-radius: 4px;
        }
        
        QTextEdit {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            padding: 4px 8px;
            border-radius: 4px;
        }
        
        QMessageBox {
            background-color: #ffffff;
            border: 1px solid #cccccc;
        }
        
        QMessageBox QLabel {
            color: #333333;
        }
        
        QMessageBox QPushButton {
            background-color: #4c75af;
            color: #ffffff;
            padding: 8px 16px;
            border-radius: 4px;
        }
        
        QMessageBox QPushButton:hover {
            background-color: #5477b8;
        }
        
        QMessageBox QPushButton:pressed {
            background-color: #44629e;
        }
        """
        self.setStyleSheet(style_sheet)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
