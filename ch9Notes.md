`shutil.copy(source,destination)` - copies file to destination

`shutil.copytree(source,destination)` - copies entire directory and subfolders

`shutil.move(source,destination)` - moves file

`shutil.rmtree(path)` - removes entire dir, even if not empty

`os.unlink(path)` - deletes a file

`os.rmdir(path)` - deletes an empty dir

`send2trash.send2trash(path)` - sends file or folder to trash (safe delete)

`os.walk(path)` - returns 3 strings (folder, subfolders, filenames)
- can be used with for loop to walk through a dir structure
- acts like `range()` does for numbers

`exampleZip = zipfile.ZipFile(filename, [mode])` - creates a zipfile object in exampleZip

`var = exampleZip.getinfo(fileInZipFile)` - assigns file info for fileInZipFile to var

`var.file_size` - gets file size

`var.compress_size` - gets compressed size of file

`exampleZip.extractall([destination])` - extracts files to destination

`exampleZip.write(filename,compress_type=zipfile.ZIP_DEFLATED)` - adds filename file to exampleZip file, compresses with default type
