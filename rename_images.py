import os
import sys

def rename_images(folder_path):
    """Đổi tên các file hình ảnh trong thư mục chỉ định từ 1 đến n."""
    files = os.listdir(folder_path)
    for index, file in enumerate(files, start=1):
        file_extension = os.path.splitext(file)[1]
        new_file_name = os.path.join(folder_path, f"{index}{file_extension}")
        current_file_path = os.path.join(folder_path, file)
        os.rename(current_file_path, new_file_name)
    print("Đã đổi tên thành công tất cả các file hình ảnh.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Vui lòng cung cấp đường dẫn đến thư mục chứa hình ảnh.")
    else:
        folder_path = sys.argv[1]
        rename_images(folder_path)