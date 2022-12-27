from ..endf_archive_downloader import EndfArchiveDownloader


jendl_libraries_dict = {
    'jendl-pd-2016': {
        'liburl': 'JENDL-PD-2016',
        'sublibs': ('g',)
    },
    'jendl-pd-2016.1': {
        'liburl': 'JENDL-PD-2016.1',
        'sublibs': ('g',)
    },
    'jendl-he-2007': {
        'liburl': 'JENDL-HE-2007',
        'sublibs': ('n', 'p')
    },
    'jendl40-he': {
        'liburl': 'JENDL-4.0-HE',
        'sublibs': ('n', 'p')
    },
    'jendl-deu-2020': {
        'liburl': 'JENDL-DEU-2020',
        'sublibs': ('d',)
    },
    'jendl-ad-2017': {
        'liburl': 'JENDL-AD-2017',
        'sublibs': ('n', 'p')
    },
    'jendl32': {
        'liburl': 'JENDL-3.2',
        'sublibs': ('n', 'nfpy')
    },
    'jendl33': {
        'liburl': 'JENDL-3.3',
        'sublibs': ('n', 'nfpy')
    },
    'jendl40': {
        'liburl': 'JENDL-4.0',
        'sublibs': ('e', 'n', 'nfpy', 'photo', 'sfpy', 'tsl')
    },
    'jendl50': {
        'liburl': 'JENDL-5',
        'sublibs': ('ard', 'd', 'decay', 'e', 'g', 'he4', 'n',
                    'nfpy', 'p', 'photo', 'sfpy', 'tsl')
    }
}


def create_jendl_library_list(cache_dir=None, trafo_cache_ext=None):
    jendl_list = []
    for curlibname, curlib in jendl_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            jendl_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return jendl_list
