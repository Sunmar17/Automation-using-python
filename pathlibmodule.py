from pathlib import Path


def file_finder():
    path = Path()
    listoffiles = []
    for files in path.glob('*.xlsx'):
        listoffiles.append(files)
    return listoffiles


