import requests
from io import BytesIO
from bs4 import BeautifulSoup
import zipfile
import logging
import re


def fetch_links(url):
    logging.info(f'fetch all links on {url}')
    indexhtml = requests.get(url)
    soup = BeautifulSoup(indexhtml.content, 'html.parser')
    link_els = soup.find_all('a')
    links = [lnk['href'] for lnk in link_els]
    return links


def fetch_zipfile_content(url, fname=None, encoding=None):
    logging.info(f'downloading zipfile from {url}')
    webfile = requests.get(url)
    fobj = BytesIO(webfile.content)
    archive = zipfile.ZipFile(fobj, 'r')
    if fname is not None:
        fcont = archive.read(fname)
    else:
        members = archive.namelist()
        if len(members) != 1:
            raise IndexError(
                'exactly one file must be present ' +
                ' zip file or provide fname option')
        fcont = archive.read(members[0])
    return fcont if encoding is None else fcont.decode(encoding)


def extract_info_from_string(string, rex):
    r = re.compile(rex)
    m = r.match(string)
    if not m:
        return None
    else:
        return m.groupdict()
