import os
import shutil

# 获取当前目录中的所有文件
current_dir = os.getcwd()
files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

# 创建 Lite-stage2 和 Go-stage2 根目录
lite_stage2_root = os.path.join(current_dir, "Lite-stage2")
go_stage2_root = os.path.join(current_dir, "Go-stage2")
os.makedirs(lite_stage2_root, exist_ok=True)
os.makedirs(go_stage2_root, exist_ok=True)

for file in files:
    # 检查文件名是否符合格式
    if file.startswith("stage2_") and file.endswith(".bin"):
        # 提取版本号
        version = file.split("_")[1].replace(".bin", "")
        version_no_dot = version.replace(".", "")  # 去掉点号的版本号
        
        # 创建原始版本号文件夹
        original_folder = os.path.join(current_dir, version)
        os.makedirs(original_folder, exist_ok=True)
        
        # 将文件复制到原始版本号文件夹并重命名
        src_path = os.path.join(current_dir, file)
        dest_path = os.path.join(original_folder, "stage2.bin")
        shutil.copy(src_path, dest_path)
        
        # 生成 Lite-stage2 文件夹
        lite_folder = os.path.join(lite_stage2_root, version_no_dot)
        os.makedirs(lite_folder, exist_ok=True)
        shutil.copy(dest_path, os.path.join(lite_folder, "stage2.bin"))
        
        # 生成 Go-stage2 文件夹
        go_folder = os.path.join(go_stage2_root, f"PS4-{version}")
        os.makedirs(go_folder, exist_ok=True)
        
        # 在 Go-stage2 文件夹中添加一层 stage2 文件夹
        go_stage2_subfolder = os.path.join(go_folder, "stage2")
        os.makedirs(go_stage2_subfolder, exist_ok=True)
        shutil.copy(dest_path, os.path.join(go_stage2_subfolder, "stage2.bin"))

print("文件已成功处理并复制到 Lite-stage2 和 Go-stage2 文件夹中。")
