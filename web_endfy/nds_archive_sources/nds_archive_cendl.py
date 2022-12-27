from ..endf_archive_downloader import EndfArchiveDownloader


cendl_libraries_dict = {
    'cendl2': {
        'liburl': 'CENDL-2',
        'sublibs': ('n',)
    },
    'cendl31': {
        'liburl': 'CENDL-3.1',
        'sublibs': ('n',)
    },
    'cendl32': {
        'liburl': 'CENDL-3.2',
        'sublibs': ('n',)
    }
}


def create_cendl_library_list(cache_dir=None, trafo_cache_ext=None):
    cendl_list = []
    for curlibname, curlib in cendl_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            cendl_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return cendl_list
