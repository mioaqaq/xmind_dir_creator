import os
import xmind
from xmind_fix import xmind_recover

class XmindDirCreator:
    def __init__(self, directory):
        self.directory = directory
        self.xmind_name = "目录结构.xmind"
        self.dir_name = os.path.join(directory, self.xmind_name)

    def safe_load_or_create_xmind(self):
        # 删除旧文件
        if os.path.exists(self.dir_name):
            os.remove(self.dir_name)

        # 加载（不存在时将自动新建结构）
        workbook = xmind.load(self.dir_name)
        sheet = workbook.getPrimarySheet()
        sheet.setTitle("目录结构")
        root_topic = sheet.getRootTopic()
        return workbook, root_topic

    def create_xmind_from_directory(self):
        workbook, root_topic = self.safe_load_or_create_xmind()

        # 设置根主题为目录名
        root_topic.setTitle(os.path.basename(self.directory))

        def add_items_to_xmind(parent_topic, current_directory):
            items = os.listdir(current_directory)
            dirs = sorted([i for i in items if os.path.isdir(os.path.join(current_directory, i))])
            files = sorted([i for i in items if os.path.isfile(os.path.join(current_directory, i))])

            for item in dirs:
                sub_topic = parent_topic.addSubTopic()
                sub_topic.setTitle(item)
                add_items_to_xmind(sub_topic, os.path.join(current_directory, item))

            for item in files:
                file_topic = parent_topic.addSubTopic()
                file_topic.setTitle(item)

        add_items_to_xmind(root_topic, self.directory)
        xmind.save(workbook, path=self.dir_name)
        xmind_recover(self.dir_name)
        print(f"✅ xmind文档创建成功：{self.dir_name}")

        return self.dir_name
