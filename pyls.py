import os
import time
import argparse

#this checks whether it is a file or directory and returns either true or false
def directory_checker(file_path):
  return {
      'is_file': os.path.isfile(file_path),
      'is_dir': os.path.isdir(file_path),
  }
    
#this retrieves information regarding the file/path
def get_file_info(file_path):
  stat = os.stat(file_path)
  return {
      "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
      "size": stat.st_size 
  }

#this lists files and folders according to the input, -l, -F, -h
def list_files_and_folders(args):
    
  for item in os.listdir():
    full_path = os.path.join(os.getcwd(), item)
    if args.long:
      file_info = get_file_info(full_path)
      print(f"{file_info['mtime']} {file_info['size']} {item}")
      
    else:
      if args.format:
        if os.path.isdir(full_path):
          print(item + "/")
        elif os.access(full_path, os.X_OK):
          print(item + "*")
        else:
          print(item)
      else:
        print(item)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="List directory contents")
  parser.add_argument("-l", "--long", action="store_true", help="long listing format")
  parser.add_argument("-F", "--format", action="store_true", help="display file type")
  args = parser.parse_args()

  list_files_and_folders(args)
