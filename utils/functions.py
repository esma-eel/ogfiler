from PyInquirer import prompt
import os, shutil

def ask_destinations(categories):
    destinations = {}

    for category in categories:
        question = {
            'type': 'input',
            'name': category,
            'message': category + " folder name :>",
        }

        cat_dest = prompt(question)
        destinations.update(cat_dest)

    return destinations


def create_destination(main_path, destinations):
    for destination in destinations.values():
        path = os.path.join(main_path, destination)
        print("creating directory in .../" + path[len(path)//2:])
        print("name is " + destination)
        if not os.path.exists(path):
            os.mkdir(path)
            print("directory created!")
        else:
            print("this directory already exists!")


def organize_files(main_path, destination_folders, selected_formats):
    action_counter = 0
    for filename in os.listdir(main_path):
        list_dir_name_path = os.path.join(main_path, filename)

        if os.path.isfile(list_dir_name_path):

            for folder_name, formats in selected_formats.items():
                destination_path = os.path.join(main_path, folder_name+"/")

                for format in formats:
                    if filename.endswith(format):
                        file_path = os.path.join(main_path, filename)
                        try:
                            if os.path.exists(file_path):
                                shutil.move(file_path, destination_path)
                                print("{} moved to {} successfully".format(filename, folder_name))
                                action_counter += 1
                        except shutil.Error:
                            if os.path.exists(file_path):
                                shutil.copy(file_path, destination_path)
                                print("{} copied to {} successfully".format(filename, folder_name))
                                os.remove(file_path)
                                print("{} file deleted successfully".format(filename))
                                action_counter += 1

    if action_counter < 1:
        print("be happy, every thing is organized already.")


def change_working_directory(new_working_directory):
    print("changing working directory...")
    os.chdir(new_working_directory)
    print("working directory changed to %s!"%(new_working_directory))


def get_dest_format_dict(file_categories, destination_folders, file_formats):
    selected_formats = {}
    for category in file_categories:
        selected_formats[destination_folders[category]] = file_formats[category]
    
    return selected_formats
        

def start_process():
    confirm_qs = {
        'type': 'confirm',
        'name': 'start_process',
        'message': "do you want to start process ? :>",
        "default": False
    }

    return prompt(confirm_qs)['start_process']


if __name__ == "__main__":
    pass