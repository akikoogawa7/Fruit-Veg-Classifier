from os import walk

def convert_path_to_txt(mypath):
    text_file = open('labels.txt', 'w')
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(dirnames)
        break
    for element in sorted(f):
        text_file.write(element+'\n')
    text_file.close
    return text_file