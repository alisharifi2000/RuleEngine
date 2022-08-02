from rules.range_rules import define_range_rules
from rules.len_rules import define_len_rules
from rules.fields_operation import define_field_operation
from rules.operation import define_operation

import pandas as pd


class Operation:
    def __init__(self, config, data):
        self.types = ['op_sum', 'op_multiply', 'op_subtract', 'op_division', 'op_sqrt', 'op_power']
        self.config = config
        self.data = data
        self.type_checker = 'O'

    def find_configs(self):
        op_par = self.types
        self.config = self.config[self.config.type.isin(op_par)]

    def validate_config(self):
        self.config['valid_type'] = self.config['col'].apply(lambda x:
                                                              True if (self.data[x].dtypes != self.type_checker)
                                                              else False)

        self.config = self.config[self.config.valid_type]

    def apply_rules(self):
        if len(self.config) > 0:
            # apply len rule
            operation_rule = list(map(define_operation, [(self.data.loc[:, [row['col']]], row)
                                                            for index, row in self.config.iterrows()]))
            operation_rules = pd.concat(operation_rule, axis=1)
            self.data = operation_rules


class FiledsOpertion:
    def __init__(self, config, data):
        self.types = ['sum', 'multiply', 'subtract', 'division']
        self.config = config
        self.data = data
        self.type_checker = 'O'

    def find_configs(self):
        fields_op_par = self.types
        self.config = self.config[self.config.type.isin(fields_op_par)]

    def validate_config(self):
        self.config['valid_type1'] = self.config['col'].apply(lambda x:
                                                              True if (self.data[x].dtypes != self.type_checker)
                                                              else False)

        self.config['valid_type2'] = self.config['parameters'].apply(lambda x:
                                                                     True if (self.data[x].dtypes != self.type_checker)
                                                                     else False)

        self.config['valid_type'] = (self.config['valid_type1'] & self.config['valid_type2'])
        self.config = self.config[self.config.valid_type]

    def apply_rules(self):
        if len(self.config) > 0:
            # apply len rule
            fields_rule = list(map(define_field_operation, [(self.data.loc[:, [row['col'],
                                                                               row['parameters']]], row)
                                                            for index, row in self.config.iterrows()]))
            fields_rules = pd.concat(fields_rule, axis=1)
            self.data = fields_rules


class RangeRule:
    def __init__(self, config, data):
        self.types = ['range', 'range_e', 'range_l', 'range_g', 'g', 'l', 'ge', 'le']
        self.type_checker = 'O'
        self.config = config
        self.data = data

    def find_configs(self):
        range_rule_par = self.types
        self.config = self.config[self.config.type.isin(range_rule_par)]

    def validate_config(self):
        self.config['valid_type'] = self.config['col'].apply(lambda x:
                                                             True if (self.data[x].dtypes != self.type_checker)
                                                             else False)

        self.config = self.config[self.config.valid_type]

    def apply_rules(self):
        if len(self.config) > 0:
            # apply len rule
            range_list = list(map(define_range_rules, [(self.data.loc[:, [row['col']]], row)
                                                       for index, row in self.config.iterrows()]))

            range_rules = pd.concat(range_list, axis=1)
            self.data = range_rules


class LengthRule:
    def __init__(self, config, data):
        self.types = ['len', 'len_g', 'len_l', 'len_ge', 'len_le']
        self.type_checker = 'O'
        self.config = config
        self.data = data

    def find_configs(self):
        len_rule_par = self.types
        self.config = self.config[self.config.type.isin(len_rule_par)]

    def validate_config(self):
        self.config['valid_type'] = self.config['col'].apply(lambda x:
                                                             True if (self.data[x].dtypes == self.type_checker)
                                                             else False)

        self.config = self.config[self.config.valid_type]

    def apply_rules(self):
        if len(self.config) > 0:
            # apply len rule
            len_list = list(map(define_len_rules, [(self.data.loc[:, [row['col']]], row)
                                                   for index, row in self.config.iterrows()]))

            len_rules = pd.concat(len_list, axis=1)
            self.data = len_rules
