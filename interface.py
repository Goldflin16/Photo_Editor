from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,QLabel, QListWidget, QFileDialog, QMessageBox, QSlider
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

app = QApplication([])
window = QWidget()
window.setFixedSize(1400, 800)

folder = QPushButton("Папка")
left = QPushButton("Вліво")
right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
sharpness = QPushButton("Різкість")
blur = QPushButton("Замилення")
wb = QPushButton("Ч/Б")
save = QPushButton("Зберегти")

photo_list_widget = QListWidget()
photo_label = QLabel("photo")
slider = QSlider(orientation=Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(50)

photo = QPixmap()

slider_layout = QVBoxLayout()
slider_layout.addWidget(blur)
slider_layout.addWidget(slider)


button_group = QHBoxLayout()
button_group.addWidget(left, stretch= 1)
button_group.addWidget(right, stretch= 1)
button_group.addWidget(mirror, stretch= 1)
button_group.addWidget(blur, stretch= 1)
button_group.addWidget(wb, stretch= 1)

layout_v = QVBoxLayout()
layout_v.addWidget(folder)
layout_v.addWidget(photo_list_widget)

big_layout = QVBoxLayout()
big_layout.addWidget(photo_label, alignment= Qt.AlignCenter)
big_layout.addLayout(button_group)

main_layout = QHBoxLayout()
main_layout.addLayout(layout_v, stretch= 1)
main_layout.addLayout(big_layout, stretch= 4)
window.setLayout(main_layout)

window.show()
