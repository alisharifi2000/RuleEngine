from rules.rule_classes import RangeRule, LengthRule, FiledsOpertion, Operation , BoolianOperator
import pandas as pd

# make sample data
df = pd.DataFrame({'age': [10, 12, 26, 5, 67, 8, 99, 100],
                   'value': [10, 12, 26, 5, 67, 85, 99, 100],
                   'nid': ['100000000', '02023240506', '122949214949',
                           '99990020021020102', '0000001221312',
                           '99990020021020102', '0000001221312',
                           '99990020021020102']})

# read rules config
rules = pd.read_json(path_or_buf='./configs/rules.json', orient='records')
print(rules.head(5))

# define class object
len_rule_obj = LengthRule(config=rules, data=df)
range_rule_obj = RangeRule(config=rules, data=df)
field_rule_obj = FiledsOpertion(config=rules, data=df)
op_rule_obj = Operation(config=rules, data=df)

# lenght rules
len_rule_obj.find_configs()
len_rule_obj.validate_config()
len_rule_obj.apply_rules()
df = pd.concat([df, len_rule_obj.data], axis=1)
print(df)

# range rules
range_rule_obj.find_configs()
range_rule_obj.validate_config()
range_rule_obj.apply_rules()
df = pd.concat([df, range_rule_obj.data], axis=1)
print(df)

# field rules
field_rule_obj.find_configs()
field_rule_obj.validate_config()
field_rule_obj.apply_rules()
df = pd.concat([df, field_rule_obj.data], axis=1)
print(df)

# operation rules
op_rule_obj.find_configs()
op_rule_obj.validate_config()
op_rule_obj.apply_rules()
df = pd.concat([df, op_rule_obj.data], axis=1)
print(df)


# bool operation rules
bool_rule_obj = BoolianOperator(config=rules, data=df)
bool_rule_obj.find_configs()
bool_rule_obj.validate_config()
bool_rule_obj.apply_rules()
df = pd.concat([df, bool_rule_obj.data], axis=1)
print(df)

# save data
df.to_csv('result.csv', index=False)
