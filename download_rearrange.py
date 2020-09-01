#!/usr/bin/python3
import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class File_specs():
    def __init__(self,specs):
        self.name = specs[0]
        self.extention = specs[1]
    def folder_thing(self,dir_name):
        if os.path.isdir(dir_name):
            return dir_name
        else:
            os.mkdir(dir_name)
            return dir_name
    def check_dir(self):
        # array fotos
        arr_fotos = [".png",".jpg",".jpeg",".favicon"]

        # array dev
        arr_dev = [".py",".php",".css",".html",".js",".db",".sql",".scss",".cpp",".c",".cs"]

        # array documentos
        arr_documentos = [".csv",".doc",".docx",".ppt",".pdf",".xlsx"]

        # array audios
        arr_audios = [".mp3",".wav",".wam"]

        # array videos
        arr_videos = [".mov",".avi",".gif",".qt"]

        # array instaladores
        arr_instaladores = [".dmg",".pkg"]

        if self.extention in arr_fotos:
            dir_name = sys.argv[1]+"/fotos"
            
        elif self.extention in arr_dev:
            dir_name = sys.argv[1]+"/dev"

        elif self.extention in arr_documentos:
            dir_name = sys.argv[1]+"/documentos"

        elif self.extention in arr_audios:
            dir_name = sys.argv[1]+"/audios"

        elif self.extention in arr_videos:
            dir_name = sys.argv[1]+"/videos"

        elif self.extention in arr_instaladores:
            dir_name = sys.argv[1]+"/instaladores"
        else:
            self.folder_thing(sys.argv[1]+"/outros")
            dir_name = sys.argv[1]+"/outros/"+self.extention.replace(".","")
        
        return self.folder_thing(dir_name)

class Handler(FileSystemEventHandler):
    def on_created(self,event):
        src_path = event.src_path
        # check if is dir
        if event.is_directory == False:
            # check if the file is in a subdir
            list_dir_raw = os.listdir(sys.argv[1])
            list_dir = []
            for path in list_dir_raw:
                list_dir.append(sys.argv[1]+"/"+path)
            
            src_dirname = os.path.dirname(src_path)
            rest = src_dirname.replace(sys.argv[1]," ")
            if rest != " ":
                pass
                # print(f"nao muda!")
            # if not, continue the process of rearrange the files
            else:
                # print(f"muda!")
                base = os.path.basename(src_path)
                file_specs = File_specs(os.path.splitext(base))
                dir_name = file_specs.check_dir()
                dir_name = dir_name+"/"+base
                os.rename(src_path,dir_name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=sys.argv[1], recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()