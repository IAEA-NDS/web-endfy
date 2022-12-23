from .endf_archive_downloader import EndfArchiveDownloader


def create_tendl2008_library_list(cache_dir):
    tendl2008_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2008_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2008/{sublib}/',
                libspec=f'tendl2008_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2008_list


def create_tendl2009_library_list(cache_dir):
    tendl2009_list = []
    for sublib in ('d', 'dfpy', 'g', 'he3', 'he3fp', 'he4', 'he4fp', 'n', 'nfpy', 'p', 'pfpy', 'sfpy', 't', 'tfpy'):
        tendl2009_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2009/{sublib}/',
                libspec=f'tendl2009_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2009_list


def create_tendl2010_library_list(cache_dir):
    tendl2010_list = []
    for sublib in ('d', 'dfpy', 'g', 'he3', 'he3fp', 'he4', 'he4fp', 'n', 'nfpy', 'p', 'pfpy', 'sfpy', 't', 'tfpy'):
        tendl2010_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2010/{sublib}/',
                libspec=f'tendl2010_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2010_list


def create_tendl2011_library_list(cache_dir):
    tendl2011_list = []
    for sublib in ('d', 'dfpy', 'g', 'he3', 'he3fp', 'he4', 'he4fp', 'n', 'nfpy', 'p', 'pfpy', 'sfpy', 't', 'tfpy'):
        tendl2011_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2011/{sublib}/',
                libspec=f'tendl2011_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2011_list


def create_tendl2012_library_list(cache_dir):
    tendl2012_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2012_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2012/{sublib}/',
                libspec=f'tendl2012_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2012_list


def create_tendl2014_library_list(cache_dir):
    tendl2014_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2014_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2014/{sublib}/',
                libspec=f'tendl2014_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2014_list


def create_tendl2015_library_list(cache_dir):
    tendl2015_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2015_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2015/{sublib}/',
                libspec=f'tendl2015_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2015_list


def create_tendl2017_library_list(cache_dir):
    tendl2017_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2017_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2017/{sublib}/',
                libspec=f'tendl2017_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2017_list


def create_tendl2019_library_list(cache_dir):
    tendl2019_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2019_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2019/{sublib}/',
                libspec=f'tendl2019_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2019_list


def create_tendl2021_library_list(cache_dir):
    tendl2021_list = []
    for sublib in ('d', 'g', 'he3', 'he4', 'n', 'p', 't'):
        tendl2021_list.append(
            EndfArchiveDownloader(
                liburl=f'TENDL-2021/{sublib}/',
                libspec=f'tendl2021_{sublib}',
                cache_dir=cache_dir,
                rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)(?P<level>M?)_(?P<mat>[0-9]+)',
                dtypes={'projectile': str, 'charge': int, 'element': lambda x: x.title(), 'mass': int, 'mat': int, 'level': str}
            )
        )
    return tendl2021_list


def create_tendl_library_list(cache_dir=None):
    tendl_list = []
    tendl_list.extend(create_tendl2008_library_list(cache_dir))
    tendl_list.extend(create_tendl2009_library_list(cache_dir))
    tendl_list.extend(create_tendl2010_library_list(cache_dir))
    tendl_list.extend(create_tendl2011_library_list(cache_dir))
    tendl_list.extend(create_tendl2012_library_list(cache_dir))
    tendl_list.extend(create_tendl2014_library_list(cache_dir))
    tendl_list.extend(create_tendl2015_library_list(cache_dir))
    tendl_list.extend(create_tendl2017_library_list(cache_dir))
    tendl_list.extend(create_tendl2019_library_list(cache_dir))
    tendl_list.extend(create_tendl2021_library_list(cache_dir))
    return tendl_list
