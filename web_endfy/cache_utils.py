import os
import tempfile
import logging


def fetch_file_from_cachedir(cachedir, fname, mode='binary'):
    if mode not in ('text', 'binary'):
        raise ValueError('mode arg must be either "text" or "binary"')
    if cachedir is None:
        return None
    os.makedirs(cachedir, exist_ok=True)
    fp = os.path.join(cachedir, fname)
    if os.path.exists(fp):
        logging.info(f'retrieve content of file {fname} from cache')
        fmode = 'rb' if mode == 'binary' else 'rt'
        with open(fp, fmode) as fr:
            cont = fr.read()
        return cont
    else:
        return None


def store_file_in_cachedir(cachedir, fname, cont, mode='binary'):
    if mode not in ('text', 'binary'):
        raise ValueError('mode arg must be either "text" or "binary"')
    if cachedir is None:
        return
    fp = os.path.join(cachedir, fname)
    # jump through some hoops to guarantee atomicity
    # of the file creation process
    if not os.path.exists(fp):
        logging.info(f'store file {fname} in cache')
        fmode = 'wb' if mode == 'binary' else 'wt'
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, dir=cachedir, mode=fmode
        )
        temp_file.write(cont)
        temp_file.close()
        temp_filepath = temp_file.name
        os.rename(temp_filepath, fp)
