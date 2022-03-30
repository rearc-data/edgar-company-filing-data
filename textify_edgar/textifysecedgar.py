import os
import shutil
import math

import os
import re
from bs4 import BeautifulSoup
import pandas as pd

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

def save_text(path, new_path):
    with open(path) as fh:
        raw_10k = fh.read()
        
    # Regex to find <DOCUMENT> tags
    doc_start_pattern = re.compile(r'<DOCUMENT>')
    doc_start_is = doc_start_pattern.finditer(raw_10k)

    doc_end_pattern = re.compile(r'</DOCUMENT>')
    doc_end_is = doc_end_pattern.finditer(raw_10k)

    # Regex to find <TYPE> tag prceeding any characters, terminating at new line
    type_pattern = re.compile(r'(<TYPE>)([^\n]+)')
    doc_types = type_pattern.finditer(raw_10k)

    document = {}

    # Create a loop to go through each section type and save documents in the dictionary
    for doc_type, doc_start, doc_end in zip(doc_types, doc_start_is, doc_end_is):
        doc_type = doc_type[2]
        document[doc_type] = raw_10k[doc_start.end():doc_end.start()]
    print(path)
    html_start = re.search("(<\?xml)|(<html)", document["10-K"]).start()


    html = document["10-K"][html_start:]
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text(" ")
    start_idx = re.search("UNITED", text).start()
    text = text[start_idx:]
    with open(new_path, "w") as fh:
        for ix, line in enumerate(text.splitlines()):
            line = line.strip()
            chunks = []
            for phrase in line.split("    "):
                phrase = phrase.replace("Table of Contents", "").strip()
                if phrase != "":
                    chunks.append(phrase.strip())
            line_text = ' '.join(chunks)
            if line_text.strip() != "":
                fh.write(line_text + "\n")

def save_textified(path, base, year, quarter, cik):
    name = os.path.basename(path)
    base_path = os.path.join(base, f"{year}/QTR{quarter}/{cik}")
    new_path = os.path.expanduser(base_path)
    
    make_path(new_path)
    new_file = os.path.join(new_path, name)
    save_text(path, new_file)


top = "~/Projects/sec_edgar_10k_oneday_sample"
base = "~/Projects/sec_edgar_k_txt"
top = os.path.expanduser(top)
ld = ""
for root, dirs, files in os.walk(top):
    if files != ['.DS_Store'] and files != []:
        head, cik = os.path.split(root)
        head, quarter = os.path.split(head)
        quarter = quarter.replace("QTR", "")

        for file in files:
            path = os.path.join(root, file)
            save_textified(path, base, "2022", quarter, cik)
        
    