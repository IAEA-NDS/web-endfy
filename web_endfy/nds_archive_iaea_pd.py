from .endf_archive_downloader import EndfArchiveDownloader


iaea_pd_libraries_dict = {
    'iaea_pd1999': {
        'liburl': 'IAEA-PD-1999',
        'sublibs': ('g',)
    },
    'iaea_pd2019': {
        'liburl': 'IAEA-PD-2019',
        'sublibs': ('g',)
    }
}


def create_iaea_pd_library_list(cache_dir=None, trafo_cache_ext=None):
    iaea_pd_list = []
    for curlibname, curlib in iaea_pd_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            iaea_pd_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return iaea_pd_list
