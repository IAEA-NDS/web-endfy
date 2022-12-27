from .endf_archive_downloader import EndfArchiveDownloader
from .nds_archive_sources.nds_archive_jendl import jendl_libraries_dict
from .nds_archive_sources.nds_archive_jeff import jeff_libraries_dict
from .nds_archive_sources.nds_archive_tendl import tendl_libraries_dict
from .nds_archive_sources.nds_archive_endfb import endfb_libraries_dict
from .nds_archive_sources.nds_archive_fendl import fendl_libraries_dict
from .nds_archive_sources.nds_archive_irdff import irdff_libraries_dict
from .nds_archive_sources.nds_archive_cendl import cendl_libraries_dict
from .nds_archive_sources.nds_archive_brond_rosfond import brond_rosfond_libraries_dict
from .nds_archive_sources.nds_archive_iaea_pd import iaea_pd_libraries_dict
import pandas as pd
import re


def create_library_list(libraries_dict, cache_dir=None, trafo_cache_ext=None):
    lib_list = []
    for curlibname, curlib in libraries_dict.items():
        for cursublib in curlib['sublibs']:
            liburl = curlib['liburl'] + '/' + cursublib + '/'
            libspec = curlibname + '_' + cursublib
            lib_list.append(
                EndfArchiveDownloader(
                    liburl=liburl,
                    libspec=libspec,
                    cache_dir=cache_dir,
                    trafo_cache_ext=trafo_cache_ext
                )
            )
    return lib_list


def create_nds_library_list(cache_dir=None, trafo_cache_ext=None):
    nds_library_list = []
    nds_library_list.extend(create_library_list(
        jendl_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        jeff_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        tendl_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        endfb_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        fendl_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        irdff_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        cendl_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        brond_rosfond_libraries_dict, cache_dir, trafo_cache_ext)
    )
    nds_library_list.extend(create_library_list(
        iaea_pd_libraries_dict, cache_dir, trafo_cache_ext)
    )
    return nds_library_list


def get_nds_library_df(cache_dir=None, trafo_cache_ext=None):
    library_db = []
    nds_library_list = create_nds_library_list(cache_dir, trafo_cache_ext)
    for curlib in nds_library_list:
        libspec = curlib.get_library_designation()
        m = re.match('^(.*)_(.*)$', libspec)
        if not m:
            raise ValueError('regular expression did not match library specification')
        libname = m.group(1)
        libtype = m.group(2)
        library_db.append({
            'libname': libname,
            'libtype': libtype,
            'libobj': curlib
        })
    library_df = pd.DataFrame.from_records(library_db)
    return library_df
