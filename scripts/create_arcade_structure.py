import os

def main():

  directory = 'arcade/python/'
  new_language = 'go'
  file_extension = '.go'
  not_implemented_text = '# Not implemented yet!'

  for root, dirs, files in os.walk(directory):
     for file in files:
        #with open(os.path.join(root, file), "r") as auto:
        print("{} - {}".format(root, file))
        file_name = file.split('.')[0]
        new_directory = root.replace('python', new_language)
        if not os.path.exists(new_directory):
          os.makedirs(new_directory)
        fullName = new_directory + '/' + file_name + file_extension
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.write(not_implemented_text)
        f.close()


if __name__ == "__main__":
    main()
