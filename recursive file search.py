import os


def find_files(suffix, path):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limit to the depth of the subdirectories can be.

  Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

  Returns:
     a list of paths
  """
  files = []

  def recursive_search(path):
    os.chdir(path)
    listo = os.listdir()
    directories = []
    for val in listo:
      if os.path.isfile(val) and val.endswith(suffix):
        files.append(str(path+'\\'+val))
      elif os.path.isdir(val):
        directories.append(val)
    for values in directories:
      recursive_search(os.path.join(path, values))
  recursive_search(path)
  return files 


path = r'C:\Users\Salvee\Desktop\Project 2\testdir'
suffix = '.c'
print(find_files(suffix, path))
suffix_two = ".h"
print(find_files(suffix_two, path))
suffix_three =".py"
print(find_files(suffix_three, path))
