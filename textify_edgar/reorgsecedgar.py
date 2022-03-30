import os
import shutil
import math

def make_path(path, **kwargs):
    """Make directory based on filing info.

    Args:
        path (str): Path to be made if it doesn't exist.
        **kwargs: Keyword arguments to pass to ``os.makedirs``.

    Raises:
        OSError: If there is a problem making the path.

    Returns:
        None
    """
    if not os.path.exists(path):
        os.makedirs(path, **kwargs)

def save_to_new_path(path, year, quarter, cik):
    base_path = f"~/Projects/sec_edgar_qtr_k/{year}/QTR{quarter}/{cik}"
    new_path = os.path.expanduser(base_path)
    
    make_path(new_path)
    shutil.copy(path, new_path)

def delete_new_path(name, year, quarter, cik):
    base_path = f"~/Projects/sec_edgar_qtr/{year}/QTR{quarter}/{cik}/{name}"
    new_path = os.path.expanduser(base_path)
    
    os.remove(new_path)

top = "~/Projects/sec_edgar_k"
top = os.path.expanduser(top)
ld = ""
for root, dirs, files in os.walk(top):
    if files != ['.DS_Store'] and files != []:
        head, cik = os.path.split(root)
        head, date = os.path.split(head)
        year = date[0:4]
        month = date[4:6]
        quarter = str(math.ceil(int(month)/3))
        if date != ld:
            print(date, month, quarter)
            ld = date
        for file in files:
            path = os.path.join(root, file)
            save_to_new_path(path, year, quarter, cik)
        
    