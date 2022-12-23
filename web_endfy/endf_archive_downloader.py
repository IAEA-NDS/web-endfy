import pandas as pd
import os
import io
from .web_utils import (
    fetch_links,
    fetch_zipfile_content,
    extract_info_from_string
)
from .cache_utils import (
    fetch_file_from_cachedir,
    store_file_in_cachedir
)


class EndfArchiveDownloader(object):

    def __init__(self, liburl=None, libpath=None, libspec=None,
                 rex=None, dtypes=None, cache_dir=None,
                 use_nds_prefix=True, trafo=None,
                 encoding='utf-8'):
        self.__liburl = None
        self.__libpath = None
        if liburl is not None:
            if use_nds_prefix:
                baseurl = 'https://nds.iaea.org/public/download-endf/'
                liburl = baseurl + liburl
            self.__liburl = liburl
        elif libpath is not None:
            self.__libpath = libpath
        else:
            raise ValueError('Either liburl or libpath must be specified')

        if libspec is not None:
            self.__libspec = libspec
        else:
            raise ValueError('Please provide the library specification')

        self.__infodt = None
        if rex is None:
            rex = (r'^(?P<projectile>p)_(?P<mat>[0-9]+)_' +
                   r'(?P<charge>[0-9]+)-' +
                   r'(?P<element>[A-Za-z]+)-'
                   r'(?P<mass>[0-9]+)')
            dtypes = {'mat': int, 'charge': int,
                      'element': lambda x: str(x).title(),
                      'mass': int}
        if dtypes is None:
            dtypes = {}
        self.__rex = rex
        self.__dtypes = dtypes
        self.__encoding = encoding
        self.__trafo = trafo
        if cache_dir is not None:
            self.__cachedir = os.path.join(cache_dir, self.__libspec)
        else:
            self.__cachedir = None

    def _get_isotope_info_from_filename(self, filename):
        r = extract_info_from_string(filename, self.__rex)
        if r is None:
            return None
        r = {k: v if k not in self.__dtypes
             else self.__dtypes[k](v)
             for k, v in r.items()}
        r['filename'] = filename
        return r

    def _fetch_lib_info(self):
        if self.__liburl is not None:
            links = fetch_links(self.__liburl)
            sourcepaths = [self.__liburl + '/' + l for l in links]
        elif self.__libpath is not None:
            links = os.listdir(self.__libpath)
            sourcepaths = [os.path.join(self.__libpath, l) for l in links]
        records = []
        for lnk, sourcepath in zip(links, sourcepaths):
            finfo = self._get_isotope_info_from_filename(lnk)
            if finfo is None:
                continue
            finfo['sourcepath'] = sourcepath
            records.append(finfo)
        return pd.DataFrame.from_records(records)

    def _provide_libinfo_dt(self):
        if self.__infodt is not None:
            return self.__infodt.copy()

        libinfo_cachefile = 'index.csv'
        csvcont = fetch_file_from_cachedir(
            self.__cachedir, libinfo_cachefile, mode='text'
        )
        if csvcont is None:
            csv_stream = io.StringIO()
            self.__infodt = self._fetch_lib_info()
            self.__infodt.to_csv(csv_stream, index=False)
            csvcont = csv_stream.getvalue()
            store_file_in_cachedir(
                self.__cachedir, libinfo_cachefile,
                csvcont, mode='text'
            )
        else:
            csv_stream = io.StringIO(csvcont)
            try:
                self.__infodt = pd.read_csv(csv_stream)
            except Exception:
                print(self.__cachedir)
                print(libinfo_cachefile)
        return self.__infodt.copy()

    def _retrieve_endf_file(self, endf_file):
        if self.__liburl is not None:
            url = self.__liburl + endf_file
            if endf_file.endswith('.zip'):
                return fetch_zipfile_content(url)
            else:
                raise TypeError(f'retrieval of {endf_file} not implemented '
                                f'due to file type')
        elif self.__libpath is not None:
            fpath = os.path.join(self.__libpath, endf_file)
            with open(fpath, 'rb') as fw:
                endf_cont = fw.read()
            return endf_cont
        else:
            raise IndexError('neither libpath nor liburl were defined')

    def _determine_endf_file_using_criteria(self, **criteria):
        infodt = self._provide_libinfo_dt()
        for k, v in criteria.items():
            infodt = infodt[infodt[k] == v]
        if len(infodt) == 0:
            raise IndexError('No file matches the criteria')
        elif len(infodt) > 1:
            raise IndexError('More than one file matches criteria')
        else:
            return infodt['filename'].iat[0]

    def get_endf_file(self, trafo=None, **criteria):
        if trafo is None:
            trafo = self.__trafo
        endf_file = self._determine_endf_file_using_criteria(**criteria)
        endf_cont = fetch_file_from_cachedir(self.__cachedir, endf_file)
        if endf_cont is None:
            endf_cont = self._retrieve_endf_file(endf_file)
            store_file_in_cachedir(self.__cachedir, endf_file, endf_cont)
        endf_cont = endf_cont.decode(self.__encoding)
        if callable(trafo):
            return trafo(endf_cont)
        else:
            return endf_cont

    def get_isotope_dt(self):
        infodt = self._provide_libinfo_dt()
        return infodt

    def get_library_designation(self):
        return self.__libspec

    def get_library_url(self):
        return self.__liburl
