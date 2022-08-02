import math


def define_operation(parameter):
    data = parameter[0]
    types = parameter[1]['type']
    col = parameter[1]['col']
    rule_name = parameter[1]['rule_name']
    parameters = tuple(parameter[1]['parameters'].split(','))

    if types == 'op_sum':
        data[rule_name] = data[col] + float(parameters[0])

    elif types == 'op_subtract':
        data[rule_name] = data[col] - float(parameters[0])

    elif types == 'op_multiply':
        data[rule_name] = data[col] * float(parameters[0])

    elif types == 'op_division':
        data[rule_name] = data[col] / float(parameters[0])

    elif types == 'op_power':
        data[rule_name] = data[col] ** float(parameters[0])

    elif types == 'op_sqrt':
        data[rule_name] = math.sqrt(data[col])

    return data[[rule_name]]
