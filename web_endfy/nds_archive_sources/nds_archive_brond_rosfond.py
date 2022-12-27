from ..endf_archive_downloader import EndfArchiveDownloader


brond_rosfond_libraries_dict = {
    'rosfond2010': {
        'liburl': 'ROSFOND-2010',
        'sublibs': ('n',)
    },
    'brond22': {
        'liburl': 'BROND-2-2',
        'sublibs': ('n',)
    },
    'brond31': {
        'liburl': 'BROND-3.1',
        'sublibs': ('n',)
    }
}


def create_brond_rosfond_library_list(cache_dir=None, trafo_cache_ext=None):
    brond_rosfond_list = []
    for curlibname, curlib in brond_rosfond_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            brond_rosfond_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return brond_rosfond_list
