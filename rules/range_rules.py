def define_range_rules(parameter):
    data = parameter[0]
    types = parameter[1]['type']
    col = parameter[1]['col']
    rule_name = parameter[1]['rule_name']
    parameters = tuple(parameter[1]['parameters'].split(','))

    if types == 'range_e':
        data[rule_name] = ((data[col] >= float(parameters[0])) &
                                     (data[col] <= float(parameters[1])))

        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'range_l':
        data[rule_name] = ((data[col] >= float(parameters[0])) &
                                     (data[col] < float(parameters[1])))

        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'range_r':
        data[rule_name] = ((data[col] > float(parameters[0])) &
                                     (data[col] <= float(parameters[1])))

        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'range':
        data[rule_name] = ((data[col] > float(parameters[0])) &
                                     (data[col] < float(parameters[1])))
        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'g':
        data[rule_name] = (data[col] > float(parameters[0]))
        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'ge':
        data[rule_name] = (data[col] >= float(parameters[0]))
        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'l':
        data[rule_name] = (data[col] < float(parameters[0]))
        data[rule_name] = data[rule_name].astype(bool)

    elif types == 'le':
        data[rule_name] = (data[col] < float(parameters[0]))
        data[rule_name] = data[rule_name].astype(bool)

    return data[[rule_name]]
