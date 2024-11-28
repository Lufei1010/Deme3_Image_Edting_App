# Import
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt #alignment tool

# Main App Setting
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(900, 700)

#All app widgets/objects
btn_folder = QPushButton("Folder")
file_list = QListWidget()

# List of button names (excluding 'Original')
button_names = ["Left", "Right", "Mirror", "Sharpen", "B/W", "Color", "Contrast", "Blur"]

# Create buttons in a loop
buttons = {}
for name in button_names:
    buttons[name] = QPushButton(name)

# Dropdown box with "Original" first
filter_box = QComboBox()
filter_box.addItem("Original")  # Adding "Original" as the first item
for name in button_names:
    filter_box.addItem(name)

picture_box = QLabel("Image will appear here")

# Design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
# Add buttons to col1 dynamically
for button in buttons.values():
    col1.addWidget(button) # values(), returns all the values of a dictionary.

col2.addWidget(picture_box)

master_layout.addLayout(col1, 20) # 20 the argument is called stretch. justify how much of the screen
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)





main_window.show()
app.exec_()