import os
import time
import argparse

def get_file_info(file_path):
  """Gets file information including modification time and size.

  Args:
      file_path (str): Path to the file.

  Returns:
      dict: Dictionary containing modification time, size, and is_dir flag.
  """
  stat = os.stat(file_path)
  return {
      "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
      "size": stat.st_size if os.path.isfile(file_path) else 0,
      "is_dir": os.path.isdir(file_path),
  }

def list_files_and_folders(args):
  """Lists files and folders in the current working directory.

  Args:
      args (argparse.Namespace): Parsed arguments.
  """
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
