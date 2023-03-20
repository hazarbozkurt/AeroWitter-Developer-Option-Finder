import os
import json
import urllib.request
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QProgressBar, QProgressDialog, QMessageBox, QComboBox, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AeroWitter - Developer Options Finder (boolean type)")
        self.window_width = 800
        self.window_height = 600
        self.resize(self.window_width, self.window_height)
        
        url = 'https://raw.githubusercontent.com/hazarbozkurt/AeroWitter-Developer-Option-Finder/main/AeroWitter-boolean.json'
        with urllib.request.urlopen(url) as f:
            data = json.loads(f.read().decode())
            self.version_codes = data['version_codes']
            self.search_codes = data['search_codes']

        self.combobox = QComboBox()
        self.combobox.addItems(self.version_codes)
        self.combobox.currentIndexChanged.connect(self.update_version_hackc)
        self.default_text = self.search_codes[0]
        self.folder_path_label = QLabel("Decompiled AeroWitter APK Folder Path:")
        self.folder_path_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.folder_path_line_edit = QLineEdit()
        self.folder_path_line_edit.setPlaceholderText("Select folder path...")
        self.folder_path_line_edit.setStyleSheet("font-size: 18px; padding: 10px;")
        self.folder_path_button = QPushButton("Select AeroWitter decompiled folder")
        self.folder_path_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.output_file_path_label = QLabel("Output File Path:")
        self.output_file_path_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.output_file_path_line_edit = QLineEdit()
        self.output_file_path_line_edit.setPlaceholderText("Select output.json file path...")
        self.output_file_path_line_edit.setStyleSheet("font-size: 18px; padding: 10px;")
        self.output_file_path_button = QPushButton("Select json save path")
        self.output_file_path_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.search_text_label = QLabel("Search Text:")
        self.search_text_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.search_text_line_edit = QLineEdit()
        self.search_text_line_edit.setStyleSheet("font-size: 18px; padding: 10px;")
        self.search_text_line_edit.setText(self.default_text)
        self.search_button = QPushButton("Find all const-string boolean values and save!")
        self.search_button.setStyleSheet("font-size: 18px; padding: 10px;")
        layout = QVBoxLayout()
        layout.addWidget(self.folder_path_label)
        layout.addWidget(self.folder_path_line_edit)
        layout.addWidget(self.folder_path_button)
        layout.addWidget(self.output_file_path_label)
        layout.addWidget(self.output_file_path_line_edit)
        layout.addWidget(self.output_file_path_button)
        layout.addWidget(self.search_text_label)
        layout.addWidget(self.combobox)
        layout.addWidget(self.search_text_line_edit)
        layout.addWidget(self.search_button)
        self.setLayout(layout)
        self.folder_path_button.clicked.connect(self.select_folder_path)
        self.output_file_path_button.clicked.connect(self.select_output_file_path)
        self.search_button.clicked.connect(self.search)
        

    def select_folder_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folder_path_line_edit.setText(folder_path)

    def select_output_file_path(self):
        output_file_path, _ = QFileDialog.getSaveFileName(self, "Save File")
        self.output_file_path_line_edit.setText(output_file_path)

    def update_version_hackc(self, index):
        self.default_text = self.search_codes[index]
        self.search_text_line_edit.setText(self.default_text)

    def search(self):
        folder_path = self.folder_path_line_edit.text()
        output_file_path = self.output_file_path_line_edit.text()
        search_text = self.search_text_line_edit.text()
    
        output_list = []
        counter = 1
    
        total_files = sum([len(files) for _, _, files in os.walk(folder_path)])
        processed_files = 0
    
        progress_bar = QProgressDialog("Processing...", "Cancel", 0, total_files, self)
        progress_bar.setWindowModality(Qt.WindowModal)
        progress_bar.setAutoClose(True)
        progress_bar.setAutoReset(True)
        progress_bar.setWindowTitle("Processing...")
        progress_bar.setStyleSheet("font-size: 12px;")
    
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith(".smali"):
                    file_path = os.path.join(root, filename)
                    with open(file_path, "r") as f:
                        lines = f.readlines()
    
                    for i in range(len(lines)):
                        line = lines[i]
                        if search_text in line:
                            for j in range(i-1, -1, -1):
                                if "const-string" in lines[j]:
                                    value_line = lines[j]
                                    value = value_line.split(",")[1].strip().strip('"')
                                    output_list.append({"title": f"Value {counter}", "description": value})
                                    counter += 1
                                    break
    
                    processed_files += 1
                    completion_percentage = processed_files / total_files * 100
                    progress_bar.setValue(processed_files)
                    progress_bar.setLabelText(f"Processing {processed_files}/{total_files} ({completion_percentage:.2f}%)")
                    QApplication.processEvents()
    
                    if progress_bar.wasCanceled():
                        progress_bar.reset()
                        return
    
        progress_bar.setValue(total_files)
        progress_bar.setLabelText("Processing completed.")
        QMessageBox.information(self, "Processing completed", "Processing completed.")
    
        with open(output_file_path, "w") as output_file:
            json.dump(output_list, output_file)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
