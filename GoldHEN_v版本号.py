import os
import shutil

# 获取当前目录中的所有文件
current_dir = os.getcwd()
files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

# 获取当前脚本文件名（无扩展名）
script_name = os.path.splitext(os.path.basename(__file__))[0]

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

# 创建 GoldHEN_stage2 文件夹
goldhen_stage2_root = os.path.join(current_dir, "GoldHEN_stage2")
os.makedirs(goldhen_stage2_root, exist_ok=True)

# 创建 PPPwn 文件夹结构
pppwn_folder = os.path.join(goldhen_stage2_root, "PPPwn", "stage2")
os.makedirs(pppwn_folder, exist_ok=True)

# 将 Lite-stage2 文件夹中的所有文件夹和文件复制到 PPPwn/stage2
for item in os.listdir(lite_stage2_root):
    src_path = os.path.join(lite_stage2_root, item)
    dest_path = os.path.join(pppwn_folder, item)
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dest_path)  # 复制整个文件夹
    else:
        shutil.copy(src_path, dest_path)  # 复制单个文件

# 创建 PS4_GoldHEN_all 文件夹结构
goldhen_all_folder = os.path.join(goldhen_stage2_root, "PS4_GoldHEN_all")
os.makedirs(goldhen_all_folder, exist_ok=True)

# 获取 Go-stage2 目录中的文件夹名称
go_stage2_folders = [d for d in os.listdir(go_stage2_root) if os.path.isdir(os.path.join(go_stage2_root, d))]

# 创建与 Go-stage2 同名的空文件夹
for folder_name in go_stage2_folders:
    new_folder = os.path.join(goldhen_all_folder, folder_name)
    os.makedirs(new_folder, exist_ok=True)
    
    # 在每个空文件夹中创建一个与脚本同名的文件夹
    script_named_folder = os.path.join(new_folder, script_name)
    os.makedirs(script_named_folder, exist_ok=True)
    
    # 将根目录的 goldhen.bin 文件复制到每个脚本同名的文件夹
    goldhen_bin_path = os.path.join(current_dir, "goldhen.bin")
    if os.path.exists(goldhen_bin_path):
        shutil.copy(goldhen_bin_path, script_named_folder)

# 新需求：将包含“goldhen”关键字的文件夹复制到 PS4_GoldHEN_all 的对应文件夹中
goldhen_folders = [d for d in os.listdir(current_dir) if "GoldHEN_v" in d.lower() and os.path.isdir(os.path.join(current_dir, d))]

for goldhen_folder in goldhen_folders:
    src_folder = os.path.join(current_dir, goldhen_folder)
    for go_folder in go_stage2_folders:
        dest_folder = os.path.join(goldhen_all_folder, go_folder)
        target_path = os.path.join(dest_folder, goldhen_folder)
        shutil.copytree(src_folder, target_path)

print("文件已成功处理并复制到 GoldHEN_stage2 文件夹中，同时 GoldHEN 相关操作完成。")
