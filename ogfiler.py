#!/home/esmaeel/Applications/ogfiler/venv/bin/python
import os,sys, shutil
from PyInquirer import prompt

from utils.categories import file_formats
from utils.functions import (ask_destinations, create_destination, organize_files, start_process, change_working_directory, get_dest_format_dict)


questions = [
    {
        'type': 'input',
        'name': 'organize_folder',
        'message': "enter the path of folder you want to organize( . for current path) :>",
    },
    {
        'type': 'checkbox',
        'message': 'select category :> ',
        'name': 'file_categories',
        'choices': [
                {'name': x} for x in file_formats
                # orginal was {'name': 'Document'}, {'name': 'Compressed'} and so on
            ],
        
        },
]


def start():
    try:
        answers = prompt(questions)
        
        if len(answers) == 0:
            raise KeyboardInterrupt

        change_working_directory(answers['organize_folder'])

        destination_folders = ask_destinations(answers['file_categories'])
        create_destination(answers['organize_folder'], destination_folders)

        selected_formats = get_dest_format_dict(answers['file_categories'],destination_folders, file_formats)


        print("your selected destinations and category formats are :")
        print(selected_formats)

        if start_process():
            organize_files(answers['organize_folder'], destination_folders, selected_formats)
        else:
            return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    start()
    print("good luck!")
    
