from .endf_archive_downloader import EndfArchiveDownloader


def create_cendl2_library_list(cache_dir):
    cendl2_list = []
    for sublib in ('n'):
        cendl2_list.append(
            EndfArchiveDownloader(
                liburl=f'CENDL-2/{sublib}/',
                libspec=f'cendl2_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return cendl2_list


def create_cendl31_library_list(cache_dir):
    cendl31_list = []
    for sublib in ('n'):
        cendl31_list.append(
            EndfArchiveDownloader(
                liburl=f'CENDL-3.1/n/',
                libspec=f'cendl31_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return cendl31_list


def create_cendl32_library_list(cache_dir):
    cendl32_list = []
    for sublib in ('n'):
        cendl32_list.append(
            EndfArchiveDownloader(
                liburl=f'CENDL-3.2/n/',
                libspec=f'cendl32_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?_(?P<mat>[0-9]+))',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return cendl32_list


def create_cendl_library_list(cache_dir=None):
    cendl_list = []
    cendl_list.extend(create_cendl2_library_list(cache_dir))
    cendl_list.extend(create_cendl31_library_list(cache_dir))
    cendl_list.extend(create_cendl32_library_list(cache_dir))
    return cendl_list
