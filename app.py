import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from compare_logic import ImageCompare
from PIL.ImageQt import ImageQt

def create_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Comparison App")
    window.setGeometry(100, 100, 1280, 720)
    
    main_layout = QVBoxLayout(window)
    
    diff_label = QLabel("Difference image will appear here")
    diff_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    diff_label.setScaledContents(True) 

    status_label = QLabel("")
    status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    buttons_layout = QHBoxLayout()
    baseline_button = QPushButton("Upload Baseline")
    actual_button = QPushButton("Upload Actual")
    buttons_layout.addWidget(baseline_button)
    buttons_layout.addWidget(actual_button)
    
    main_layout.addWidget(diff_label, stretch=3)  
    main_layout.addWidget(status_label)
    main_layout.addLayout(buttons_layout)
    
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
    
    def compare_images():
        if baseline_path and actual_path:
            img_compare = ImageCompare()
            result = img_compare.comparison(baseline_path, actual_path)
            if result:
                diff_image, difference_percentage = result
                qim = ImageQt(diff_image)
                pixmap = QPixmap.fromImage(qim)
                diff_label.setPixmap(pixmap.scaled(diff_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                status_label.setText(f"Comparison complete. Difference: {difference_percentage:.2f}%")
            else:
                diff_label.setText("Difference exceeds threshold")
                status_label.setText("Difference exceeds threshold")
        else:
            status_label.setText("Please upload both images first")
    
    baseline_button.clicked.connect(on_baseline_click)
    actual_button.clicked.connect(on_actual_click)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    create_app()
