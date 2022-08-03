def define_field_operation(parameter):
    data = parameter[0]
    types = parameter[1]['type']
    col = parameter[1]['col']
    rule_name = parameter[1]['rule_name']
    parameters = parameter[1]['parameters']

    if types == 'sum':
        data[rule_name] = data[col] + data[parameters]

    elif types == 'subtract':
        data[rule_name] = data[col] - data[parameters]

    elif types == 'multiply':
        data[rule_name] = data[col] * data[parameters]

    elif types == 'division':
        data[rule_name] = data[col] / data[parameters]

    return data[[rule_name]]
