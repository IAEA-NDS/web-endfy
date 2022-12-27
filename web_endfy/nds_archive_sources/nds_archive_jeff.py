from ..endf_archive_downloader import EndfArchiveDownloader

jeff_libraries_dict = {
    'jef22': {
        'liburl': 'JEF-2.2',
        'sublibs': ('decay', 'n', 'nfpy', 'sfpy', 'photo', 'tsl')
    },
    'jeff31': {
        'liburl': 'JEFF-3.1',
        'sublibs': ('decay', 'n', 'nfpy', 'p', 'sfpy', 'tsl')
    },
    'jeff311': {
        'liburl': 'JEFF-3.1.1',
        'sublibs': ('decay', 'n', 'nfpy', 'p', 'sfpy', 'tsl')
    },
    'jeff312': {
        'liburl': 'JEFF-3.1.2',
        'sublibs': ('n', )
    },
    'jeff32': {
        'liburl': 'JEFF-3.2',
        'sublibs': ('n', )
    },
    'jeff33': {
        'liburl': 'JEFF-3.3',
        'sublibs': ('decay', 'n', 'nfpy', 'sfpy', 'tsl')
    }
}


def create_jeff_library_list(cache_dir=None, trafo_cache_ext=None):
    jeff_list = []
    for curlibname, curlib in jeff_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            jeff_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return jeff_list
