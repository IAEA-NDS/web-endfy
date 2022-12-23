from .endf_archive_downloader import EndfArchiveDownloader


def create_endfb70_library_list(cache_dir):
    endfb70_list = []
    for sublib in ('ard', 'd', 'decay', 'e', 'g', 'he3', 'n', 'nfpy', 'p', 'photo', 'sfpy', 'std', 't'):
        endfb70_list.append(
            EndfArchiveDownloader(
                liburl=f'ENDF-B-VII.0/{sublib}/',
                libspec=f'endfb70_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    endfb70_list.append(
        EndfArchiveDownloader(
            liburl=f'ENDF-B-VII.0/tsl/',
            libspec=f'endfb70_tsl',
            cache_dir=cache_dir,
            rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<element>[^.]+)',
            dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
        )
    )
    return endfb70_list


def create_endfb71_library_list(cache_dir):
    endfb71_list = []
    for sublib in ('ard', 'd', 'decay', 'e', 'g', 'he3', 'n', 'nfpy', 'p', 'photo', 'sfpy', 'std', 't'):
        endfb71_list.append(
            EndfArchiveDownloader(
                liburl=f'ENDF-B-VII.1/{sublib}/',
                libspec=f'endfb71_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    endfb71_list.append(
        EndfArchiveDownloader(
            liburl=f'ENDF-B-VII.1/tsl/',
            libspec=f'endfb71_tsl',
            cache_dir=cache_dir,
            rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<element>[^.]+)',
            dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
        )
    )
    return endfb71_list


def create_endfb80_library_list(cache_dir):
    endfb80_list = []
    for sublib in ('ard', 'd', 'decay', 'e', 'g', 'he3', 'he4', 'n', 'nfpy', 'p', 'photo', 'sfpy', 'std', 't'):
        endfb80_list.append(
            EndfArchiveDownloader(
                liburl=f'ENDF-B-VIII.0/{sublib}/',
                libspec=f'endfb80_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    endfb80_list.append(
        EndfArchiveDownloader(
            liburl=f'ENDF-B-VIII.0/tsl/',
            libspec=f'endfb80_tsl',
            cache_dir=cache_dir,
            rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<element>[^.]+)',
            dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
        )
    )
    return endfb80_list


def create_endfb_library_list(cache_dir=None):
    endfb_list = []
    endfb_list.extend(create_endfb70_library_list(cache_dir))
    endfb_list.extend(create_endfb71_library_list(cache_dir))
    endfb_list.extend(create_endfb80_library_list(cache_dir))
    return endfb_list
