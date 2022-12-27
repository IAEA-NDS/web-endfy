from ..endf_archive_downloader import EndfArchiveDownloader


irdff_libraries_dict = {
    'irdff': {
        'liburl': 'IRDFF',
        'sublibs': ('n',)
    },
    'irdff2': {
        'liburl': 'IRDFF-II',
        'sublibs': ('n',)
    }
}


def create_irdff_library_list(cache_dir=None, trafo_cache_ext=None):
    irdff_list = []
    for curlibname, curlib in irdff_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            irdff_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return irdff_list
