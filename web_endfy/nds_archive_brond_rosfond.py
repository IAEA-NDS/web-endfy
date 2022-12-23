from .endf_archive_downloader import EndfArchiveDownloader


def create_rosfond2010_library_list(cache_dir=None):
    rosfond2010_list = []
    for sublib in ('n',):
        rosfond2010_list.append(
            EndfArchiveDownloader(
                liburl=f'ROSFOND-2010/{sublib}/',
                libspec=f'rosfond2010_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return rosfond2010_list


def create_brond22_library_list(cache_dir=None):
    brond22_list = []
    for sublib in ('n',):
        brond22_list.append(
            EndfArchiveDownloader(
                liburl=f'BROND-2-2/{sublib}/',
                libspec=f'brond22_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return brond22_list


def create_brond31_library_list(cache_dir=None):
    brond31_list = []
    for sublib in ('n',):
        brond31_list.append(
            EndfArchiveDownloader(
                liburl=f'BROND-3.1/{sublib}/',
                libspec=f'brond31_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)(-(?P<mass>[0-9]+)(?P<level>M?))?',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': lambda x: int(x) if x is not None else 0, 'mat': int, 'level': str}
            )
        )
    return brond31_list


def create_brond_rosfond_library_list(cache_dir=None):
    brond_list = []
    brond_list.extend(create_rosfond2010_library_list(cache_dir))
    brond_list.extend(create_brond22_library_list(cache_dir))
    brond_list.extend(create_brond31_library_list(cache_dir))
    return brond_list
