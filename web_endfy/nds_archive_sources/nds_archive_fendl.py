from ..endf_archive_downloader import EndfArchiveDownloader


fendl_libraries_dict = {
    'fendl21': {
        'liburl': 'FENDL-2.1',
        'sublibs': ('n',)
    },
    'fendl31c': {
        'liburl': 'FENDL-3.1c',
        'sublibs': ('n', 'p', 'd', 'photo')
    },
    'fendl32': {
        'liburl': 'FENDL-3.2',
        'sublibs': ('n', 'p', 'd', 'photo')
    },
    'fendl32b': {
        'liburl': 'FENDL-3.2b',
        'sublibs': ('n', 'p', 'd', 'photo')
    }
}


def create_fendl_library_list(cache_dir=None, trafo_cache_ext=None):
    fendl_list = []
    for curlibname, curlib in fendl_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            fendl_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return fendl_list
