from .endf_archive_downloader import EndfArchiveDownloader
from .nds_archive_jendl import create_jendl_library_list
from .nds_archive_jeff import create_jeff_library_list
from .nds_archive_tendl import create_tendl_library_list
from .nds_archive_endfb import create_endfb_library_list
from .nds_archive_fendl import create_fendl_library_list
from .nds_archive_irdff import create_irdff_library_list
from .nds_archive_cendl import create_cendl_library_list
from .nds_archive_brond_rosfond import create_brond_rosfond_library_list
from .nds_archive_iaea_pd import create_iaea_pd_library_list
import pandas as pd
import re


def create_nds_library_list(cache_dir=None):
    nds_library_list = []
    nds_library_list.extend(create_jendl_library_list(cache_dir))
    nds_library_list.extend(create_jeff_library_list(cache_dir))
    nds_library_list.extend(create_tendl_library_list(cache_dir))
    nds_library_list.extend(create_endfb_library_list(cache_dir))
    nds_library_list.extend(create_fendl_library_list(cache_dir))
    nds_library_list.extend(create_irdff_library_list(cache_dir))
    nds_library_list.extend(create_cendl_library_list(cache_dir))
    nds_library_list.extend(create_brond_rosfond_library_list(cache_dir))
    nds_library_list.extend(create_iaea_pd_library_list(cache_dir))
    return nds_library_list


def get_nds_library_df(cache_dir=None):

    library_db = []
    nds_library_list = create_nds_library_list(cache_dir)
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
