from .endf_archive_downloader import EndfArchiveDownloader


def create_irdff1_library_list(cache_dir, trafo_cache_ext):
    irdff_list = []
    for sublib in ('n',):
        irdff_list.append(
            EndfArchiveDownloader(
                liburl=f'IRDFF/{sublib}/',
                libspec=f'irdff_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return irdff_list


def create_irdff2_library_list(cache_dir, trafo_cache_ext):
    irdff2_list = []
    for sublib in ('n',):
        irdff2_list.append(
            EndfArchiveDownloader(
                liburl=f'IRDFF-II/{sublib}/',
                libspec=f'irdff2_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return irdff2_list


def create_irdff_library_list(cache_dir=None, trafo_cache_ext=None):
    irdff_list = []
    irdff_list.extend(create_irdff1_library_list(cache_dir, trafo_cache_ext))
    irdff_list.extend(create_irdff2_library_list(cache_dir, trafo_cache_ext))
    return irdff_list
