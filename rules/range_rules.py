def define_range_rules(parameter):
    data = parameter[0]
    types = parameter[1]['type']
    col = parameter[1]['col']
    parameters = tuple(parameter[1]['parameters'].split(','))

    if types == 'range_e':
        data[f'{col}_range_rule'] = ((data[col] >= float(parameters[0])) &
                                     (data[col] <= float(parameters[1])))

        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'range_l':
        data[f'{col}_range_rule'] = ((data[col] >= float(parameters[0])) &
                                     (data[col] < float(parameters[1])))

        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'range_r':
        data[f'{col}_range_rule'] = ((data[col] > float(parameters[0])) &
                                     (data[col] <= float(parameters[1])))

        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'range':
        data[f'{col}_range_rule'] = ((data[col] > float(parameters[0])) &
                                     (data[col] < float(parameters[1])))
        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'g':
        data[f'{col}_range_rule'] = (data[col] > float(parameters[0]))
        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'ge':
        data[f'{col}_range_rule'] = (data[col] >= float(parameters[0]))
        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'l':
        data[f'{col}_range_rule'] = (data[col] < float(parameters[0]))
        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    elif types == 'le':
        data[f'{col}_range_rule'] = (data[col] < float(parameters[0]))
        data[f'{col}_range_rule'] = data[f'{col}_range_rule'].astype(bool)

    return data[[f'{col}_range_rule']]
