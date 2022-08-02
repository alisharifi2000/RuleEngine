def define_boolian_operation(parameter):
    data = parameter[0]
    types = parameter[1]['type']
    col = parameter[1]['col']
    rule_name = parameter[1]['rule_name']
    parameters = tuple(parameter[1]['parameters'].split(','))

    if types == 'and':
        data[rule_name] = (data[col] & data[parameters[0]])

    elif types == 'or':
        data[rule_name] = (data[col]  | data[parameters[0]])

    return data[[rule_name]]
