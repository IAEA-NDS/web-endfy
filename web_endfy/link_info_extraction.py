import re


dtype_conv_dict = {
    'str': str,
    'int': int,
    'int_with_missing_as_zero': lambda x: int(x) if x is not None else 0,
    'titlecase': lambda x: x.title()
}


def extract_info_from_string(string, rex):
    r = re.compile(rex)
    m = r.match(string)
    if not m:
        return None
    else:
        return m.groupdict()


def enable_missing_rex(rex, missing_allowed):
    if missing_allowed:
        return '(' + rex + ')?'
    else:
        return rex


def generate_projectile_rex(
    groupname, prefix='', suffix='', missing_allowed=False
):
    rex = prefix + f'(?P<{groupname}>[a-zA-Z0-9]+)' + suffix
    rex = enable_missing_rex(rex, missing_allowed)
    return rex


def generate_charge_rex(
    groupname, prefix='', suffix='', missing_allowed=False
):
    rex = prefix + f'(?P<{groupname}>[0-9][0-9]?[0-9]?)' + suffix
    rex = enable_missing_rex(rex, missing_allowed)
    return rex


def generate_element_rex(
    groupname, prefix='', suffix='', missing_allowed=False
):
    rex = prefix + f'(?P<{groupname}>[a-zA-Z][a-zA-Z]?)' + suffix
    rex = enable_missing_rex(rex, missing_allowed)
    return rex


def generate_mass_rex(
    groupname, prefix='', suffix='', missing_allowed=False
):
    rex = prefix + f'(?P<{groupname}>[0-9][0-9]?[0-9]?)' + suffix
    rex = enable_missing_rex(rex, missing_allowed)
    return rex


def generate_material_rex(
    groupname, prefix='', suffix='', missing_allowed=False
):
    rex = prefix + f'(?P<{groupname}>[0-9][0-9][0-9][0-9]?)' + suffix
    rex = enable_missing_rex(rex, missing_allowed)
    return rex


def generate_level_rex(
    groupname, prefix='', suffix='', missing_allowed=False
):
    rex = prefix + f'(?P<{groupname}>[a-zA-Z])' + suffix
    rex = enable_missing_rex(rex, missing_allowed)
    return rex


def generate_final_suffix_rex():
    return r'\.'


def convert_using_dtypes(value_dict, dtypes_dict):
    res_dict = {}
    for k, v in value_dict.items():
        if k not in dtypes_dict:
            res_dict[k] = v
        else:
            conv_fun = dtype_conv_dict[dtypes_dict[k]]
            res_dict[k] = conv_fun(v)
    return res_dict


def determine_rex_and_dtypes_from_links(links):

    generic_dtypes = {
        'projectile': 'str', 'charge': 'int',
        'element': 'titlecase',
        'mass': 'int_with_missing_as_zero',
        'mat': 'int', 'level': 'str'
    }

    candidates = [
        {
            'rex': (generate_projectile_rex('projectile', suffix='_') +
                    generate_material_rex('mat', suffix='_') +
                    generate_charge_rex('charge', suffix='-') +
                    generate_element_rex('element') +
                    generate_mass_rex('mass', prefix='-', missing_allowed=True) +
                    generate_level_rex('level', missing_allowed=True) +
                    generate_final_suffix_rex()),
            'dtypes': generic_dtypes
        },
        {
            'rex': (generate_projectile_rex('projectile', suffix='_') +
                    generate_charge_rex('charge', suffix='-') +
                    generate_element_rex('element') +
                    generate_mass_rex('mass', prefix='-', missing_allowed=True) +
                    generate_level_rex('level', missing_allowed=True) +
                    generate_material_rex('mat', prefix='_') +
                    generate_final_suffix_rex()),
            'dtypes': generic_dtypes
        }
    ]
    match_score_list = []
    for curcand in candidates:
        cur_rex = curcand['rex']
        cur_match_score = 0
        for lnk in links:
            curmatch = extract_info_from_string(lnk, cur_rex)
            if curmatch is not None:
                cur_match_score += 1
        match_score_list.append(cur_match_score)

    max_score = max(match_score_list)
    max_idcs = [i for i, x in enumerate(match_score_list) if x == max_score]
    if max_score == 0:
        breakpoint()  # debug
        raise IndexError('did not find any matching links')
    elif len(max_idcs) > 1:
        raise IndexError(
            'found multiple patterns that match the links equally well'
        )
    else:
        max_idx = max_idcs[0]
        return candidates[max_idx]
