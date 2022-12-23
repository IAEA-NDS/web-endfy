from .endf_archive_downloader import EndfArchiveDownloader


def create_iaea_pd1999_library_list(cache_dir):
    iaea_pd1999_list = []
    for sublib in ('g',):
        iaea_pd1999_list.append(
            EndfArchiveDownloader(
                liburl=f'IAEA-PD-1999/{sublib}/',
                libspec=f'iaea_pd1999_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int}
            )
        )
    return iaea_pd1999_list


def create_iaea_pd2019_library_list(cache_dir):
    iaea_pd2019_list = []
    for sublib in ('g',):
        iaea_pd2019_list.append(
            EndfArchiveDownloader(
                liburl=f'IAEA-PD-2019/{sublib}/',
                libspec=f'iaea_pd2019_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int}
            )
        )
    return iaea_pd2019_list


def create_iaea_pd_library_list(cache_dir=None):
    iaea_pd_list = []
    iaea_pd_list.extend(create_iaea_pd1999_library_list(cache_dir))
    iaea_pd_list.extend(create_iaea_pd2019_library_list(cache_dir))
    return iaea_pd_list
