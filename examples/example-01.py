from web_endfy import EndfArchiveDownloader


rex = ('^(?P<projectile>[npdth])_' +
       '(?P<charge>[0-9]+)-' +
       '(?P<element>[a-zA-Z]+)-' +
       '(?P<mass>[0-9]+)_' +
       '(?P<mat>[0-9]+)')

liburl = 'FENDL-3.2/n/'


dl = EndfArchiveDownloader(
        liburl=liburl,
        rex=rex,
        libspec='fendl32',
        cache_dir='tmpcache',
        dtypes={'charge': int, 'mass': int,
                'element': lambda s: s.title()}
    )

dl.get_isotope_dt()
dl.get_endf_file(mass=209)
