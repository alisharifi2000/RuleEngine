import pandas as pd


class Config:
    def __init__(self, config_path):
        self.rules = pd.read_json(path_or_buf=config_path, orient='records')
        self.len_rules = (True if self.rules['type'].isin(['len', 'len_g', 'len_l', 'len_ge',
                                                           'len_le']).any() else False)
        self.range_rules = (True if self.rules['type'].isin(['range', 'range_e', 'range_l',
                                                             'range_g', 'gt', 'lt', 'ge', 'le']).any() else False)
        self.op_rules = (True if self.rules['type'].isin(['op_sum', 'op_multiply', 'op_subtract', 'op_division',
                                                          'op_sqrt', 'op_power']).any() else False)
        self.field_op_rules = (True if self.rules['type'].isin(['sum', 'multiply',
                                                                'subtract', 'division']).any() else False)
        self.bool_rules = (True if self.rules['type'].isin(['and', 'or']).any() else False)
