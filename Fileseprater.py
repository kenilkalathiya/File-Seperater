import os, shutil
dict_extension = {
    'audio_extension' : ('.mp3', '.mp4', '.wav','flac'),
    'vedio_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'documents_extension' : ('.doc','.docx','.pdf','.txt','.pptx'),
}

folderpath = input("Enter your folder path :")

def file_seprater(f_path, f_extension):
    return [file for file in os.listdir(f_path) for extension in f_extension if file.endswith(extension)]

for extension_type, extension_tuple in dict_extension.items():
    f_name = extension_type.split('_')[0] + 'Files'
    f_path = os.path.join(folderpath, f_name)
    if os.path.exists(f_path):
        break
    else:
        os.mkdir(f_path)
    for item in file_seprater(folderpath, extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(f_path,item)
        shutil.move(item_path,item_new_path)
