import os

path=os.getcwd()
file=os.walk(path)
for dirpath,dirname,filename in file:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('-----------------------')'''

    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file2 in filename:
        print(os.path.join(dirpath,file2))

    print('-----------------------------------')
