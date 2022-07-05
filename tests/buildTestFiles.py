'''
The goal here is to create a directory full of files with similar names of JPG files
The content does not have to be different.

'''
def create_files():
    dir = 'data2'
    file_name = 'data/ArloReceipt.jpg'
    suffix = '.jpg'
    names = ['data01', 'data02', 'data03']
    filecontents = open(file_name, 'rb').read() #  b is important -> binary
    max_10 = 10
    counter = 0
    for name in names:
        for i in range(0, max_10):
            file_counter = "{}_({:0>2}){}".format(name, i+1, suffix)
            new_file_name = "{}/{}".format(dir, file_counter)
            out_file = open(new_file_name, "wb")
            out_file.write(filecontents)
            out_file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
