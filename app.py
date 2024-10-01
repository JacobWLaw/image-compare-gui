import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from compare_logic import image_compare
from PIL.ImageQt import ImageQt

def create_app():
    app = QApplication(sys.argv)
    window = QWidget()
    
    window.setWindowTitle("Comparison App")
    window.setGeometry(100, 100, 400, 400)
    
    baseline_button = QPushButton("Upload Baseline", window)
    baseline_button.setGeometry(50, 300, 100, 50)
    
    actual_button = QPushButton("Upload Actual", window)
    actual_button.setGeometry(250, 300, 100, 50)
    
    status_label = QLabel("", window)
    status_label.setGeometry(50, 250, 300, 30)
    
    threshold_label = QLabel("Define a threshold from 0-100:", window)
    threshold_label.setGeometry(50, 350, 200, 50)
    
    threshold_value = QLineEdit(window)
    threshold_value.setGeometry(225, 360, 50, 25)
    threshold_value.setPlaceholderText("100")
    
    diff_label = QLabel(window)
    diff_label.setGeometry(50, 50, 300, 200)
    diff_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    diff_label.setText("Difference image will appear here")
    
    baseline_path = ""
    actual_path = ""
    curr_threshold = 100
    
    def on_baseline_click():
        nonlocal baseline_path
        file_path, _ = QFileDialog.getOpenFileName(
            window, "Select Baseline Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)")
        if file_path:
            baseline_path = file_path
            status_label.setText("Baseline image uploaded")
    
    def on_actual_click():
        nonlocal actual_path
        file_path, _ = QFileDialog.getOpenFileName(
            window, "Select Actual Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)")
        if file_path:
            actual_path = file_path
            status_label.setText("Actual image uploaded")
            compare_images()
    
    def update_threshold_value(value):
        nonlocal curr_threshold
        try:
            threshold = int(value)
            if 0 <= threshold <= 100:
                curr_threshold = threshold
        except ValueError:
            status_label.setText("Invalid input. Please enter an integer.")
    
    def compare_images():
        if baseline_path and actual_path:
            img_compare = image_compare()
            diff_image, difference_percentage = img_compare.comparison(baseline_path, actual_path, curr_threshold)
            if diff_image:
                qim = ImageQt(diff_image)
                pixmap = QPixmap.fromImage(qim)
                scaled_pixmap = pixmap.scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio)
                diff_label.setPixmap(scaled_pixmap)
                status_label.setText(f"Comparison complete. Similarity: {difference_percentage}")
            else:
                diff_label.setText("Images are similar (within threshold)")
                status_label.setText("Images are similar (within threshold)")
        else:
            status_label.setText("Please upload both images first")
    
    baseline_button.clicked.connect(on_baseline_click)
    actual_button.clicked.connect(on_actual_click)
    threshold_value.textChanged.connect(update_threshold_value)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    create_app()
