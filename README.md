# Folder_rearranger

So folder_rearranger is a Python script that just organize files on a 
especific folder (in my case, my download folder).

## Installation

You need to install the watchdog package.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.

```bash
pip install watchdog
```

## Usage
You just has to run the folowing command on your prompt
```bash
python3 download_rearrange.py {path to the messy folder}
```
## Editions
This script recognize some extentions, but if you want to
edit the extentions and the name of the folder with will store it
just edit the function **check_dir**
```python
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

# selector to determitane the name of the folder
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
    dir_name = sys.argv[1]+"/outros/"+self.extention.replace(".","")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.