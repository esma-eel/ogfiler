import os
import shutil

main_path = "/home/esmaeel/Downloads/"

tutorial_folders_name = [
    "udemy", "packt", "lynda", "course", "tutorial", "treehouse", "git.ir", "Udemy", "PACKPUB","OReilly", "TeamTreehouse", "Architecture"
]

except_folder_name = ["0.tut"]

for filename in os.listdir(main_path):
    list_dir_name_path = os.path.join(main_path, filename)
   
    if os.path.isdir(list_dir_name_path):
        for tutorial_related_name in tutorial_folders_name:
            if (tutorial_related_name in filename) and (filename not in except_folder_name):
                full_folder_name = os.path.join(main_path, filename)
                dest_folder = "0.tut"
                destination_path_tut = os.path.join(main_path, dest_folder+"/")
                try:
                    if os.path.exists(full_folder_name):
                        shutil.move(full_folder_name, destination_path_tut)
                        print("{} moved to {} successfully".format(filename, dest_folder+"/"))
                except shutil.Error:
                    if os.path.exists(full_folder_name):
                        shutil.copy(full_folder_name, destination_path_tut)
                        print("{} copied to {} successfully".format(filename, dest_folder))
                        os.remove(full_folder_name)
                        print("{} file deleted successfully".format(filename))