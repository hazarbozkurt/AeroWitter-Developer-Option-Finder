import os
import json
import urllib.request
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QProgressBar, QProgressDialog, QMessageBox, QComboBox, QVBoxLayout
from PyQt5.QtCore import Qt


class AeroWitterBooleanDevFinder(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AeroWitter - Developer Options Finder (boolean type) - V1.1")
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
        self.folder_path_label = QLabel("Decompiled AeroWitter/Twitter APK Folder Path:")
        self.folder_path_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.folder_path_line_edit = QLineEdit()
        self.folder_path_line_edit.setPlaceholderText("Select folder path...")
        self.folder_path_line_edit.setStyleSheet("font-size: 18px; padding: 10px;")
        self.folder_path_button = QPushButton("Select decompiled folder")
        self.folder_path_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.output_file_path_label = QLabel("Output File Path:")
        self.output_file_path_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.output_file_path_line_edit = QLineEdit()
        self.output_file_path_line_edit.setPlaceholderText("Select output.json file path...")
        self.output_file_path_line_edit.setStyleSheet("font-size: 18px; padding: 10px;")
        self.output_file_path_button = QPushButton("Select json save path")
        self.output_file_path_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.search_text_label = QLabel("Search Caller Code:")
        self.search_text_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.search_text_line_edit = QLineEdit()
        self.search_text_line_edit.setStyleSheet("font-size: 18px; padding: 10px;")
        self.search_text_line_edit.setText(self.default_text)
        self.search_button = QPushButton("Find All Developer Settings Values And Save!")
        self.search_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.set_combobox_width()
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


    def set_combobox_width(self):
        max_width = 0
        for i in range(self.combobox.count()):
            item_width = self.combobox.fontMetrics().boundingRect(self.combobox.itemText(i)).width()
            max_width = max(max_width, item_width)
        self.combobox.setFixedWidth(max_width + 30)


    def select_folder_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folder_path_line_edit.setText(folder_path)
        
    def select_output_file_path(self):
        default_file_name = "TwitterDeveloperOptions.json"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseCustomDirectoryIcons
        options |= QFileDialog.ShowDirsOnly
        options |= QFileDialog.HideNameFilterDetails
        file_filter = f"JSON files (*{default_file_name})"
        output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Twitter Developer Options", default_file_name, file_filter, options=options)
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
            new_output_list = []
            duplicates = set()
            for item in output_list:
                if "description" in item:
                    while any(d["description"] == item["description"] for d in new_output_list):
                        if item["description"] not in duplicates:
                            if "YesToAll" not in locals() or not YesToAll:
                                choice = QMessageBox.question(self, "Duplicate developer options found", f'Duplicate value "{item["description"]}" found. Do you want to remove it?\n\n'
                                                                                               'Click "Yes" to remove this duplicate developer option value only.\n'
                                                                                               'Click "Yes to all" to remove all duplicate developer option values and avoid future prompts.\n'
                                                                                               'Click "Cancel" to cancel processing and keep all duplicate developer option values.', 
                                                               QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.YesToAll, QMessageBox.Cancel)
                                if choice == QMessageBox.Yes:
                                    new_output_list = [d for d in new_output_list if d.get("description") != item["description"]]
                                elif choice == QMessageBox.Cancel:
                                    progress_bar.reset()
                                    QMessageBox.information(self, "Processing cancelled", f'Processing cancelled \n\n' 'No duplicate developer option value was deleted.')
                                    json.dump(output_list, output_file)
                                    return
                                elif choice == QMessageBox.YesToAll:
                                    duplicates.add(item["description"])
                                    YesToAll = True
                                    new_output_list = [d for d in new_output_list if d.get("description") != item["description"]]
                                    break
                            else:
                                duplicates.add(item["description"])
                                new_output_list = [d for d in new_output_list if d.get("description") != item["description"]]
                                break
                        else:
                            new_output_list = [d for d in new_output_list if d.get("description") != item["description"]]
                            break
                new_output_list.append(item)
            json.dump(new_output_list, output_file)
            QMessageBox.information(self, "Processing completed", "Processing completed.")

            
if __name__ == "__main__":
    app = QApplication([])
    window = AeroWitterBooleanDevFinder()
    window.show()
    app.exec_()
    
