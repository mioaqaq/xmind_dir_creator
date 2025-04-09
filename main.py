import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QPushButton, QLabel, QFileDialog)
from PyQt5.QtCore import Qt
from xmind_dir import XmindDirCreator
class FolderSelectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("xmind目录生成")
        self.setGeometry(300, 300, 800, 800)

        # 初始化UI
        self.init_ui()

        # 存储选择的文件夹路径
        self.selected_folder = ""

    def init_ui(self):
        # 创建主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 创建布局
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # 添加标题标签
        title_label = QLabel("请选择文件夹:")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # 添加显示选择路径的标签
        self.path_label = QLabel("未选择文件夹")
        self.path_label.setAlignment(Qt.AlignCenter)
        self.path_label.setWordWrap(True)
        layout.addWidget(self.path_label)

        # 添加选择文件夹按钮
        select_btn = QPushButton("选择文件夹")
        select_btn.clicked.connect(self.select_folder)
        layout.addWidget(select_btn)

        # 添加确认按钮
        confirm_btn = QPushButton("确认")
        confirm_btn.clicked.connect(self.process_folder)
        layout.addWidget(confirm_btn)

    def select_folder(self):
        """打开文件夹选择对话框"""
        folder = QFileDialog.getExistingDirectory(
            self,
            "选择文件夹",
            "",  # 默认路径，空表示当前目录
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        if folder:
            self.selected_folder = folder
            self.path_label.setText(f"已选择: {folder}")

    def process_folder(self):
        """处理选择的文件夹"""

        if not self.selected_folder:
            self.path_label.setText("请先选择文件夹！")
            return

        # 这里调用另一个函数处理文件夹
        self.process_selected_folder(self.selected_folder)

    def process_selected_folder(self, folder_path):
        xm=XmindDirCreator(folder_path)
        xm.create_xmind_from_directory()
        self.path_label.setText(f"xmind 导出完成 ✅\n路径: {folder_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderSelectionApp()
    window.show()
    sys.exit(app.exec_())