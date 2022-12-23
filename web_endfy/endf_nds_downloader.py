from web_endfy.nds_library_archive import get_nds_library_df
import pandas as pd
from copy import deepcopy
import os


class EndfNDSDownloader:

    def __init__(self, cache_dir=None, trafo=None, print_cache_info=True):
        self._trafo = trafo
        self._library_dt = None
        self._isotope_dt = None
        if cache_dir is None:
            package_folder = os.path.dirname(__file__)
            cache_dir = os.path.join(package_folder, 'endflib_cache')
        self._cache_dir = cache_dir
        if print_cache_info:
            print(f'Using the directory {self._cache_dir} as cache for ENDF files')

    def get_library_dt(self):
        if self._library_dt is None:
            self._library_dt = get_nds_library_df(
                self._cache_dir
            )
        return self._library_dt

    def get_isotope_dt(self, libname=None, libtype=None):
        if self._isotope_dt is not None:
            return self._isotope_dt.copy()

        libdf = self.get_library_dt()
        if libname is not None:
            libdf = libdf[libdf['libname'] == libname]
        if libtype is not None:
            libdf = libdf[libdf['libtype'] == libtype]
        df_list = []
        for idx, row in libdf.iterrows():
            curdf = row['libobj'].get_isotope_dt()
            curdf['libname'] = row['libname']
            curdf['libtype'] = row['libtype']
            df_list.append(curdf)
        retdf = pd.concat(df_list, axis=0, ignore_index=True)
        # probably because of some NaN values
        # the charge column is not cast into integer but float
        # so make sure it is an integer
        retdf['charge'] = retdf['charge'].astype(pd.Int64Dtype())
        retdf['mass'] = retdf['mass'].astype(pd.Int64Dtype())
        self._isotope_dt = retdf
        return self._isotope_dt.copy()

    def _determine_isotope_dt_row_using_criteria(self, **criteria):
        infodt = self.get_isotope_dt()
        for k, v in criteria.items():
            infodt = infodt[infodt[k] == v]
        if len(infodt) == 0:
            raise IndexError('No file matches the criteria')
        elif len(infodt) > 1:
            raise IndexError('More than one file matches criteria')
        else:
            return infodt.iloc[0]

    def get_endf_file(self, trafo=None, **criteria):
        if trafo is None:
            trafo = self._trafo
        criteria = deepcopy(criteria)
        inforow = self._determine_isotope_dt_row_using_criteria(**criteria)
        libname = inforow['libname']
        libtype = inforow['libtype']
        libdt = self.get_library_dt()
        libdt = libdt[libdt['libname'] == libname]
        libdt = libdt[libdt['libtype'] == libtype]
        if len(libdt) > 1:
            raise IndexError('more than one library found, which should not happen')
        if len(libdt) == 0:
            raise IndexError('no library found that matches specification')
        if 'libname' in criteria:
            del criteria['libname']
        if 'libtype' in criteria:
            del criteria['libtype']
        return libdt['libobj'].iloc[0].get_endf_file(trafo=trafo, **criteria)
