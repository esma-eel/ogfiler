import os
import shutil

main_path = "/home/esmaeel/Downloads/"

dest_folders = {
    "Documents": ["txt", "pdf", "docx", "odt", "xlsx", "epub", 'doc', 'html', 'json', 'ppt', 'pptx', 'xml', 'css', 'csv'],
    "Pictures": ["jpeg", "jpg", "png", "gif", "tiff", "psd", "ai"],
    "Compressed": ["rar", "zip", "tar", "gz", "lrzip", "kbg", "kgb", "7z", "7zip", 'xz', 'bz2'],
    "Music": ['mp3', 'wma', 'wav', 'voc', 'ogg', 'oga', 'm4a', 'amr', 'aac'],
    "Software": ["exe", "run", 'bash', "deb", 'rpm', 'msi', 'iso', 'sh', 'apk'],
    "Videos": ["mp4", 'mkv', 'mpeg4', 'flv', 'srt', '3gp']
}


for filename in os.listdir(main_path):
    list_dir_name_path = os.path.join(main_path, filename)
    if os.path.isfile(list_dir_name_path):
        for foldername, file_formats in dest_folders.items():
            destination_path = os.path.join(main_path, foldername+"/")
            for format in file_formats:
                if filename.endswith(format):
                    file_path = os.path.join(main_path, filename)
                    try:
                        if os.path.exists(file_path):
                            shutil.move(file_path, destination_path)
                            print("{} moved to {} successfully".format(filename, foldername))
                    except shutil.Error:
                        if os.path.exists(file_path):
                            shutil.copy(file_path, destination_path)
                            print("{} copied to {} successfully".format(filename, foldername))
                            os.remove(file_path)
                            print("{} file deleted successfully".format(filename))