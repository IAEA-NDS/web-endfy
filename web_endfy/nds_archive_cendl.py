from .endf_archive_downloader import EndfArchiveDownloader


def create_cendl2_library_list(cache_dir, trafo_cache_ext):
    cendl2_list = []
    for sublib in ('n'):
        cendl2_list.append(
            EndfArchiveDownloader(
                liburl=f'CENDL-2/{sublib}/',
                libspec=f'cendl2_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return cendl2_list


def create_cendl31_library_list(cache_dir, trafo_cache_ext):
    cendl31_list = []
    for sublib in ('n'):
        cendl31_list.append(
            EndfArchiveDownloader(
                liburl=f'CENDL-3.1/n/',
                libspec=f'cendl31_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return cendl31_list


def create_cendl32_library_list(cache_dir, trafo_cache_ext):
    cendl32_list = []
    for sublib in ('n'):
        cendl32_list.append(
            EndfArchiveDownloader(
                liburl=f'CENDL-3.2/n/',
                libspec=f'cendl32_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return cendl32_list


def create_cendl_library_list(cache_dir=None, trafo_cache_ext=None):
    cendl_list = []
    cendl_list.extend(create_cendl2_library_list(cache_dir, trafo_cache_ext))
    cendl_list.extend(create_cendl31_library_list(cache_dir, trafo_cache_ext))
    cendl_list.extend(create_cendl32_library_list(cache_dir, trafo_cache_ext))
    return cendl_list
