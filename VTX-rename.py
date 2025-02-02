import os
import shutil

# 获取当前目录中的所有文件
current_dir = os.getcwd()
files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

# 创建目标根目录
lite_stage2_root = os.path.join(current_dir, "Lite-stage2")
go_stage2_root = os.path.join(current_dir, "Go-stage2")
ps4_goldhen_root = os.path.join(current_dir, "PS4_GoldHEN_all")
os.makedirs(lite_stage2_root, exist_ok=True)
os.makedirs(go_stage2_root, exist_ok=True)
os.makedirs(ps4_goldhen_root, exist_ok=True)

for file in files:
    # 处理 stage2_ 相关文件
    if file.startswith("stage2_") and file.endswith(".bin"):
        # 提取版本号并保留完整的 "."
        version = file.split("_")[1].split(".bin")[0]  # 获取版本号
        
        # 删除版本号中的 "."
        version_folder = version.replace(".", "")  # 删除 .

        # 处理 Lite-stage2 文件夹
        lite_folder = os.path.join(lite_stage2_root, version_folder)
        os.makedirs(lite_folder, exist_ok=True)
        shutil.copy(os.path.join(current_dir, file), os.path.join(lite_folder, "stage2.bin"))

        # 处理 Go-stage2 文件夹，拼接 "PS4-" 在版本号前，保留 . 点
        go_folder = os.path.join(go_stage2_root, f"PS4-{version}", "stage2")
        os.makedirs(go_folder, exist_ok=True)
        shutil.copy(os.path.join(current_dir, file), os.path.join(go_folder, "stage2.bin"))

    # 处理 ps4-hen- 相关文件
    elif file.startswith("ps4-hen-") and "-PPPwn-vtx.bin" in file:
        # 提取版本号
        version_with_vtx = file.split("-")[2]  # 获取从 ps4-hen- 后面开始的部分
        version = version_with_vtx.split("-PPPwn-vtx.bin")[0]  # 保留版本号

        # 从右往左数两个字符插入一个 "."
        if len(version) > 2:
            version = version[:-2] + "." + version[-2:]  # 插入 .

        # 调试打印：查看生成的版本号
        print(f"Processing PS4-HEN file: {file}, Version: {version}")

        # 创建 PS4-版本号(VTX) 文件夹
        goldhen_folder = os.path.join(ps4_goldhen_root, f"PS4-{version}(VTX)")
        os.makedirs(goldhen_folder, exist_ok=True)

        # 将文件复制到 PS4_GoldHEN_all 并重命名为 payload.bin
        src_path = os.path.join(current_dir, file)
        dest_path = os.path.join(goldhen_folder, "payload.bin")
        shutil.copy(src_path, dest_path)

print("文件已成功处理并按要求分类。")
