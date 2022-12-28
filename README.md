## web-endfy: access ENDF files on the web

This Python package provides convenience functions
to access the ENDF files of the major nuclear data
libraries from Python.

*Note: This package has not been extensively tested
and may contain bugs and maybe does not work as
expected under all circumstances. If you test it
and encounter any issues, feel free to report back
by opening an issue here.*

### Installation

We recommend the creation of a virtual environment.
For instance, with conda this can be done by
```
conda create -y -n web-endfy pip 
conda activate web-endfy
```

The package `web-endfy` itself can be installed using pip by
```
pip install git+https://github.com/iaea-nds/web-endfy.git  
```

### Usage

This package contains two classes. The class `EndfNDSDownloader`
allows to access the content of ENDF files available in the
[public archive][public-archive] of the Nuclear Data Section of the IAEA.
The other class, `EndfArchiveDownloader` is a low-level interface and can
be employed by the user to access content of ENDF files at custom
internet locations.

#### EndfNDSDownloader

The `EndfNDSDownloader` class contains three relevant methods:
`get_library_dt()`, `get_isotope_dt()` and `get_endf_file()`.
To list all ENDF files known by the `EndfNDSDownloader` class
including information about the projectile, target and material number,
you can use the instructions:
```python
nds_endf_dl = EndfNDSDownloader()
nds_endf_dl.get_isotope_dt()
```
The second instruction will take a couple of minutes as it accesses many
websites in the NDS archive to determine the available ENDF files.
The information of downloaded files is stored in a cache directory
whose location is determined by the [appdirs] package and printed out upon
loading the `web-endfy` package.
Subsequent calls will retrieve the information from the cache directory
in order to avoid the slow download from the internet.
The location of the cache directory can be adjusted
by providing the `cache_dir` argument in the
call to `EndfNDSDownloader()`:
```python
from web_endfy import EndfNDSDownloader
nds_endf_dl = EndfNDSDownloader(cache_dir='mycachedir')
```

The result of the `nds_endf_dl.get_isotope_dt()` call is a `pandas`
dataframe with the information about each available ENDF file:
```
       projectile   mat  charge  ...        libname  libtype level
0               g   128       1  ...  jendl-pd-2016        g   NaN
1               g   225       2  ...  jendl-pd-2016        g   NaN
2               g   301     100  ...  jendl-pd-2016        g   NaN
3               g   302     100  ...  jendl-pd-2016        g   NaN
4               g   303     100  ...  jendl-pd-2016        g   NaN
...           ...   ...     ...  ...            ...      ...   ...
```

Finally, the content of an ENDF file can be retrieved by the 
method `.get_endf_file()`:
```
endf_cont = nds_endf_dl.get_endf_file(charge=2, libname='jendl-pd-2016')
```
Any column name available in the isotope dataframe above can be used
as filter. If the provided filters match more than one line in the
dataframe, an exception will be raised. Usually, you will also need
at least a `libtype` and `mass` specification.

The `.get_endf_file()` method can also take an optional argument `trafo`
with a function that transforms the string representation of the content
of an ENDF file into something else. For instance, you could immediately
parse the content with the [endf-parserpy] package to obtain a nested
dictionary:
```python
from endf_parserpy import BasicEndfParser
parser = BasicEndfParser()
endf_cont = nds_endf_dl.get_endf_file(
    charge=2, libname='jendl-pd-2016', trafo=parser.parse
)
```
If the execution of the `trafo` function takes a lot of time,
its result can also be cached for faster subsequent retrievals.
To enable the caching, provide the `trafo_cache_ext` argument
while instantiating the `EndfNDSDownloader` class to specify
the file extension for storing the transformed content:
```python
nds_endf_dl = EndfNDSDownloader(trafo_cache_ext='.trafo')
```

#### EndfArchiveDownloader

The `EndfArchiveDownloader` class provides a low-level interface
that can be used to access ENDF data stored on the web.
It can be used if the ENDF files are available as a list of links
on a website that can be discerned from other links by matching
the `href` string with a regular expression. 

As an example, the following instruction instantiates the
`EndfArchiveDownloader` class to allow downloads of ENDF files
from the JEFF 3.3 neutron sublibrary as provided in the
[public archive][public-archive-jeff33-neutron] of the NDS:
```python
from web_endfy import EndfArchiveDownloader
jeff_dl = EndfArchiveDownloader(
    liburl='https://nds.iaea.org/public/download-endf/JEFF-3.3/n/',
    libspec=f'jeff33_n',
    rex='^(?P<projectile>[a-zA-Z0-9]+)_(?P<mat>[0-9]+)_' +
        '(?P<charge>[0-9]+)-(?P<element>[a-zA-Z]+)-(?P<mass>[0-9]+)',
    dtypes={
        'projectile': str, 'charge': int, 'element': 'titlecase',
        'mass': int, 'mat': int
    },
    use_nds_prefix=False,
    cache_dir=None
)
```
The argument `liburl` specifies the url of the website that contains the
links to the ENDF files. The argument `libspec` is a library designation,
which should qualify as a valid directory name. `cache_dir` specifies the
path to a cache directory to avoid re-downloading ENDF files. `cache_dir=None`
means that no caching is performed.

The regular expression given in `rex` is matched against the `href` attributes of
all links to extract only links to ENDF files. Please note that named capture
groups `(?P<colname> ... )` must be present. The name of the group (e.g., `projectile`) 
will be used to create a column in a dataframe that contains the captured content,
such as `n`, `p`, etc. The `dtypes` argument contains a dictionary that
specifies to which type the matched string of each capture group should be cast
before being stored in a dataframe. The keys are given by the names of the
capture groups and the values are the names of conversion functions, e.g.
`int`, `str`, and `titlecase`. Currently available conversion functions can be
found at the beginning of the file `web-endf/link_info_extraction.py`.

After creating the instance of the `EndfArchiveDownloader`, you can
obtain a `pandas` dataframe with a list of all available ENDF files by
```python
jeff_dl.get_isotope_dt()
```

To access an ENDF file, use the `.get_endf_file()` method:
```python
jeff_dl.get_endf_file(element='He', mass=4)
```
As for the `EndfNDSDownloader` class, you can also
provide a `trafo` argument with a function to transform
the string representation of the ENDF file to something else.

In contrast to the `EndfNDSDownloader` class, downloaded files
are not cached by default. To enable caching, specify the
cache directory via the `cache_dir` argument. If you have specified
a transformation and want results to be cached, too, you need to
provide the `trafo_cache_ext` argument as well:
```python
jeff_dl = EndfNDSDownloader(
   ...
   cache_dir='mycache',
   trafo_cache_ext='.parsed'
)
```

[public-archive]: https://nds.iaea.org/public/download-endf/
[endf-parserpy]: https://github.com/iaea-nds/endf-parserpy.git
[public-archive-jeff33-neutron]: https://nds.iaea.org/public/download-endf/JEFF-3.3/n/
[appdirs]: https://github.com/ActiveState/appdirs 

### Legal note

This code is distributed under the MIT license,
see the accompanying license file for more information.

Copyright (c) International Atomic Energy Agency
