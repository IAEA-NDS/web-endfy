from .endf_archive_downloader import EndfArchiveDownloader


def create_jef22_library_list(cache_dir, trafo_cache_ext):
    jeff22_list = []
    for sublib in ('decay', 'n', 'nfpy', 'sfpy'):
        jeff22_list.append(
            EndfArchiveDownloader(
                liburl=f'JEF-2.2/{sublib}/',
                libspec=f'jef22_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    jeff22_list.append(
        EndfArchiveDownloader(
            liburl=f'JEF-2.2/photo/',
            libspec=f'jef22_photo',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    jeff22_list.append(
        EndfArchiveDownloader(
            liburl='JEF-2.2/tsl/',
            libspec='jef22_tsl',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    return jeff22_list



def create_jeff31_library_list(cache_dir, trafo_cache_ext):
    jeff31_list = []
    for sublib in ('decay', 'n', 'nfpy', 'p', 'sfpy'):
        jeff31_list.append(
            EndfArchiveDownloader(
                liburl=f'JEFF-3.1/{sublib}/',
                libspec=f'jeff31_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    jeff31_list.append(
        EndfArchiveDownloader(
            liburl='JEFF-3.1/tsl/',
            libspec='jeff31_tsl',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    return jeff31_list


def create_jeff311_library_list(cache_dir, trafo_cache_ext):
    jeff311_list = []
    for sublib in ('decay', 'n', 'nfpy', 'p', 'sfpy'):
        jeff311_list.append(
            EndfArchiveDownloader(
                liburl=f'JEFF-3.1.1/{sublib}/',
                libspec=f'jeff311_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    jeff311_list.append(
        EndfArchiveDownloader(
            liburl='JEFF-3.1.1/tsl/',
            libspec='jeff311_tsl',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    return jeff311_list


def create_jeff312_library_list(cache_dir, trafo_cache_ext):
    jeff312_list = []
    for sublib in ('n',):
        jeff312_list.append(
            EndfArchiveDownloader(
                liburl=f'JEFF-3.1.2/{sublib}/',
                libspec=f'jeff312_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jeff312_list


def create_jeff32_library_list(cache_dir, trafo_cache_ext):
    jeff32_list = []
    for sublib in ('n',):
        jeff32_list.append(
            EndfArchiveDownloader(
                liburl=f'JEFF-3.2/{sublib}/',
                libspec=f'jeff32_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jeff32_list


def create_jeff33_library_list(cache_dir, trafo_cache_ext):
    jeff33_list = []
    for sublib in ('decay', 'n', 'nfpy', 'sfpy'):
        jeff33_list.append(
            EndfArchiveDownloader(
                liburl=f'JEFF-3.3/{sublib}/',
                libspec=f'jeff33_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    jeff33_list.append(
        EndfArchiveDownloader(
            liburl='JEFF-3.3/tsl/',
            libspec='jeff33_tsl',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    return jeff33_list


def create_jeff_library_list(cache_dir=None, trafo_cache_ext=None):
    jeff_list = []
    jeff_list.extend(create_jef22_library_list(cache_dir, trafo_cache_ext))
    jeff_list.extend(create_jeff31_library_list(cache_dir, trafo_cache_ext))
    jeff_list.extend(create_jeff311_library_list(cache_dir, trafo_cache_ext))
    jeff_list.extend(create_jeff312_library_list(cache_dir, trafo_cache_ext))
    jeff_list.extend(create_jeff32_library_list(cache_dir, trafo_cache_ext))
    jeff_list.extend(create_jeff33_library_list(cache_dir, trafo_cache_ext))
    return jeff_list
