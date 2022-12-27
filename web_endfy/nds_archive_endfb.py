from .endf_archive_downloader import EndfArchiveDownloader


endfb_libraries_dict = {
    'endfb70': {
        'liburl': 'ENDF-B-VII.0',
        'sublibs': ('ard', 'd', 'decay', 'e', 'g', 'he3', 'n',
                    'nfpy', 'p', 'photo', 'sfpy', 'std', 't', 'tsl')
    },
    'endfb71': {
        'liburl': 'ENDF-B-VII.1',
        'sublibs': ('ard', 'd', 'decay', 'e', 'g', 'he3', 'n',
                    'nfpy', 'p', 'photo', 'sfpy', 'std', 't', 'tsl')
    },
    'endfb80': {
        'liburl': 'ENDF-B-VIII.0',
        'sublibs': ('ard', 'd', 'decay', 'e', 'g', 'he3', 'he4',
                    'n', 'nfpy', 'p', 'photo', 'sfpy', 'std', 't', 'tsl')
    }
}


def create_endfb_library_list(cache_dir=None, trafo_cache_ext=None):
    endfb_list = []
    for curlibname, curlib in endfb_libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            endfb_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return endfb_list
