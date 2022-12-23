from .endf_archive_downloader import EndfArchiveDownloader


def create_fendl21_library_list(cache_dir):
    fendl21_list = []
    for sublib in ('n',):
        fendl21_list.append(
            EndfArchiveDownloader(
                liburl=f'FENDL-2.1/{sublib}/',
                libspec=f'fendl21_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return fendl21_list


def create_fendl31c_library_list(cache_dir):
    fendl31c_list = []
    for sublib in ('n', 'p', 'd', 'photo'):
        fendl31c_list.append(
            EndfArchiveDownloader(
                liburl=f'FENDL-3.1c/{sublib}/',
                libspec=f'fendl31c_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return fendl31c_list


def create_fendl32_library_list(cache_dir):
    fendl32_list = []
    for sublib in ('n', 'p', 'd', 'photo'):
        fendl32_list.append(
            EndfArchiveDownloader(
                liburl=f'FENDL-3.2/{sublib}/',
                libspec=f'fendl32_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return fendl32_list


def create_fendl32b_library_list(cache_dir):
    fendl32b_list = []
    for sublib in ('n', 'p', 'd', 'photo'):
        fendl32b_list.append(
            EndfArchiveDownloader(
                liburl=f'FENDL-3.2b/{sublib}/',
                libspec=f'fendl32b_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return fendl32b_list


def create_fendl_library_list(cache_dir=None):
    fendl_list = []
    fendl_list.extend(create_fendl21_library_list(cache_dir))
    fendl_list.extend(create_fendl31c_library_list(cache_dir))
    fendl_list.extend(create_fendl32_library_list(cache_dir))
    fendl_list.extend(create_fendl32b_library_list(cache_dir))
    return fendl_list
