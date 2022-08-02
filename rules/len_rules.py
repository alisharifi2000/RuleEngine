def define_len_rules(parameter):
    data = parameter[0]
    types = parameter[1]['type']
    col = parameter[1]['col']
    rule_name = parameter[1]['rule_name']
    parameters = tuple(parameter[1]['parameters'].split(','))

    if types == 'len':
        data[f'{col}_len'] = data[col].str.len()
        data[rule_name] = (data[f'{col}_len'] == int(parameters[0]))

    elif types == 'len_g':
        data[f'{col}_len'] = data[col].str.len()
        data[rule_name] = (data[f'{col}_len'] > int(parameters[0]))

    elif types == 'len_ge':
        data[f'{col}_len'] = data[col].str.len()
        data[rule_name] = (data[f'{col}_len'] >= int(parameters[0]))

    elif types == 'len_l':
        data[f'{col}_len'] = data[col].str.len()
        data[rule_name] = (data[f'{col}_len'] < int(parameters[0]))

    elif types == 'len_le':
        data[f'{col}_len'] = data[col].str.len()
        data[rule_name] = (data[f'{col}_len'] <= int(parameters[0]))

    return data[[rule_name]]
