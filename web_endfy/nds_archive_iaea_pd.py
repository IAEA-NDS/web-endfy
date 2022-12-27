from .endf_archive_downloader import EndfArchiveDownloader


def create_iaea_pd1999_library_list(cache_dir, trafo_cache_ext):
    iaea_pd1999_list = []
    for sublib in ('g',):
        iaea_pd1999_list.append(
            EndfArchiveDownloader(
                liburl=f'IAEA-PD-1999/{sublib}/',
                libspec=f'iaea_pd1999_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return iaea_pd1999_list


def create_iaea_pd2019_library_list(cache_dir, trafo_cache_ext):
    iaea_pd2019_list = []
    for sublib in ('g',):
        iaea_pd2019_list.append(
            EndfArchiveDownloader(
                liburl=f'IAEA-PD-2019/{sublib}/',
                libspec=f'iaea_pd2019_{sublib}',
                cache_dir=cache_dir,
                trafo_cache_ext=trafo_cache_ext
            )
        )
    return iaea_pd2019_list


def create_iaea_pd_library_list(cache_dir=None, trafo_cache_ext=None):
    iaea_pd_list = []
    iaea_pd_list.extend(create_iaea_pd1999_library_list(cache_dir, trafo_cache_ext))
    iaea_pd_list.extend(create_iaea_pd2019_library_list(cache_dir, trafo_cache_ext))
    return iaea_pd_list
