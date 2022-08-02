from rules.range_rules import define_range_rules
from rules.len_rules import define_len_rules
from rules.fields_operation import define_field_operation
from rules.operation import define_operation
from rules.bool_operation import define_boolian_operation
import pandas as pd


class Rule:
    """
    base class for rules

    Parameters:
           config (pandas dataframe): config for rules.
           data (pandas dataframe): data that we want apply rules on it.
    """

    def __init__(self, config, data):
        self.config = config
        self.data = data
        self.type_checker = 'O'

    def find_configs(self):
        par = self.types
        self.config = self.config[self.config.type.isin(par)]


class BoolianOperator(Rule):
    def __init__(self, config, data):
        super().__init__(config, data)
        self.types = ['and', 'or']
        self.type_checker = 'bool'

    def validate_config(self):
        self.config['valid_type1'] = self.config['col'].apply(lambda x:
                                                              True if (self.data[x].dtypes == self.type_checker)
                                                              else False)

        self.config['valid_type2'] = self.config['parameters'].apply(lambda x:
                                                                     True if (self.data[x].dtypes == self.type_checker)
                                                                     else False)
        self.config['valid_type'] = (self.config['valid_type1'] & self.config['valid_type2'])
        self.config = self.config[self.config.valid_type]

    def apply_rules(self):
        if len(self.config) > 0:
            # apply len rule
            fields_rule = list(map(define_boolian_operation, [(self.data.loc[:, [row['col'],
                                                                                 row['parameters']]], row)
                                                              for index, row in self.config.iterrows()]))
            fields_rules = pd.concat(fields_rule, axis=1)
            self.data = fields_rules


class RegexRule(Rule):
    def __init__(self, config, data):
        super().__init__(config, data)
        self.types = ['regex']

    def validate_config(self):
        self.config['valid_type'] = self.config['col'].apply(lambda x:
                                                             True if (self.data[x].dtypes == self.type_checker)
                                                             else False)

        self.config = self.config[self.config.valid_type]

    def apply_rules(self):
        if len(self.config) > 0:
            # apply len rule
            pass


class Operation(Rule):
    def __init__(self, config, data):
        super().__init__(config, data)
        self.types = ['op_sum', 'op_multiply', 'op_subtract', 'op_division', 'op_sqrt', 'op_power']

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


class FiledsOpertion(Rule):
    def __init__(self, config, data):
        super().__init__(config, data)
        self.types = ['sum', 'multiply', 'subtract', 'division']

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


class RangeRule(Rule):
    def __init__(self, config, data):
        super().__init__(config, data)
        self.types = ['range', 'range_e', 'range_l', 'range_g', 'g', 'l', 'ge', 'le']

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


class LengthRule(Rule):
    def __init__(self, config, data):
        super().__init__(config, data)
        self.types = ['len', 'len_g', 'len_l', 'len_ge', 'len_le']

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
