def GetPages(path):
    page_file_path = path
    return page_file_path.split('/')[1][0:-3]
