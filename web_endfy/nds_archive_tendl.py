from .endf_archive_downloader import EndfArchiveDownloader


tendl_libraries_dict = {
    'tendl2008': {
        'liburl': 'TENDL-2008',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    },
    'tendl2009': {
        'liburl': 'TENDL-2009',
        'sublibs': ('d', 'dfpy', 'g', 'he3', 'he3fp', 'he4', 'he4fp',
                    'n', 'nfpy', 'p', 'pfpy', 'sfpy', 't', 'tfpy')
    },
    'tendl2010': {
        'liburl': 'TENDL-2010',
        'sublibs': ('d', 'dfpy', 'g', 'he3', 'he3fp', 'he4', 'he4fp',
                    'n', 'nfpy', 'p', 'pfpy', 'sfpy', 't', 'tfpy')
    },
    'tendl2011': {
        'liburl': 'TENDL-2011',
        'sublibs': ('d', 'dfpy', 'g', 'he3', 'he3fp', 'he4', 'he4fp',
                    'n', 'nfpy', 'p', 'pfpy', 'sfpy', 't', 'tfpy')
    },
    'tendl2012': {
        'liburl': 'TENDL-2012',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    },
    'tendl2014': {
        'liburl': 'TENDL-2014',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    },
    'tendl2015': {
        'liburl': 'TENDL-2015',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    },
    'tendl2017': {
        'liburl': 'TENDL-2017',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    },
    'tendl2019': {
        'liburl': 'TENDL-2019',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    },
    'tendl2021': {
        'liburl': 'TENDL-2021',
        'sublibs': ('d', 'g', 'he3', 'he4', 'n', 'p', 't')
    }
}


def create_tendl_library_list(cache_dir=None, trafo_cache_ext=None):
    tendl_list = []
    for curlibname, curlib in tendl_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            tendl_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return tendl_list
