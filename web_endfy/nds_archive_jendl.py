from .endf_archive_downloader import EndfArchiveDownloader


def create_jendl_pd_2016_library_list(cache_dir, trafo_cache_ext):
    jendl_pd_2016_list = []
    for sublib in ('g',):
        jendl_pd_2016_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-PD-2016/{sublib}/',
                libspec=f'jendl-pd-2016_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl_pd_2016_list


def create_jendl_pd_2016_1_library_list(cache_dir, trafo_cache_ext):
    jendl_pd_2016_1_list = []
    for sublib in ('g',):
        jendl_pd_2016_1_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-PD-2016.1/{sublib}/',
                libspec=f'jendl-pd-2016.1_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl_pd_2016_1_list


def create_jendl_he_2007_library_list(cache_dir, trafo_cache_ext):
    jendl_he_2007_list = []
    for sublib in ('n', 'p'):
        jendl_he_2007_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-HE-2007/{sublib}/',
                libspec=f'jendl-he-2007_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl_he_2007_list


def create_jendl40_he_library_list(cache_dir, trafo_cache_ext):
    jendl40_he_list = []
    for sublib in ('n', 'p'):
        jendl40_he_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-4.0-HE/{sublib}/',
                libspec=f'jendl40-he_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl40_he_list


def create_jendl_deu_2020_library_list(cache_dir, trafo_cache_ext):
    jendl_deu_2020_list = []
    for sublib in ('d',):
        jendl_deu_2020_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-DEU-2020/{sublib}/',
                libspec=f'jendl-deu-2020_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl_deu_2020_list


def create_jendl_ad_2017_library_list(cache_dir, trafo_cache_ext):
    jendl_ad_2017_list = []
    for sublib in ('n', 'p'):
        jendl_ad_2017_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-AD-2017/{sublib}/',
                libspec=f'jendl-ad-2017_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl_ad_2017_list


def create_jendl32_library_list(cache_dir, trafo_cache_ext):
    jendl32_list = []
    for sublib in ('n', 'nfpy'):
        jendl32_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-3.2/{sublib}/',
                libspec=f'jendl32_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl32_list


def create_jendl33_library_list(cache_dir, trafo_cache_ext):
    jendl33_list = []
    for sublib in ('n', 'nfpy'):
        jendl33_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-3.3/{sublib}/',
                libspec=f'jendl33_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return jendl33_list


def create_jendl40_library_list(cache_dir, trafo_cache_ext):
    jendl40_list = []
    for sublib in ('e', 'n', 'nfpy', 'photo', 'sfpy'):
        jendl40_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-4.0/{sublib}/',
                libspec=f'jendl40_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    jendl40_list.append(
        EndfArchiveDownloader(
            liburl='JENDL-4.0/tsl/',
            libspec='jendl40_tsl',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    return jendl40_list


def create_jendl5_library_list(cache_dir, trafo_cache_ext):
    jendl50_list = []
    for sublib in ('ard', 'd', 'decay', 'e', 'g', 'he4', 'n', 'nfpy', 'p', 'photo', 'sfpy'):
        jendl50_list.append(
            EndfArchiveDownloader(
                liburl=f'JENDL-5/{sublib}/',
                libspec=f'jendl5_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    jendl50_list.append(
        EndfArchiveDownloader(
            liburl='JENDL-5/tsl/',
            libspec='jendl5_tsl',
            cache_dir=cache_dir,
            trafo_cache_ext=trafo_cache_ext
        )
    )
    return jendl50_list


def create_jendl_library_list(cache_dir=None, trafo_cache_ext=None):
    jendl_list = []
    jendl_list.extend(create_jendl_pd_2016_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl_pd_2016_1_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl_he_2007_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl40_he_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl_deu_2020_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl_ad_2017_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl32_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl33_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl40_library_list(cache_dir, trafo_cache_ext))
    jendl_list.extend(create_jendl5_library_list(cache_dir, trafo_cache_ext))
    return jendl_list
