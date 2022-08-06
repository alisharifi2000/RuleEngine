from rules.rule_classes import RangeRule, LengthRule, FiledsOpertion, Operation, BoolianOperator
from rules.config_class import Config
import pandas as pd

# read data
df = pd.read_csv(filepath_or_buffer='./data/sample.csv')
df.age = df.age.astype('int32')
df.value = df.value.astype('int32')
df.nid = df.nid.astype('object')

# read rules config
config_path = './configs/rules.json'
rule_object = Config(config_path=config_path)
print(rule_object.rules.head(5))


# define class object
len_rule_obj = LengthRule(config=rule_object.rules, data=df)
range_rule_obj = RangeRule(config=rule_object.rules, data=df)
field_rule_obj = FiledsOpertion(config=rule_object.rules, data=df)
op_rule_obj = Operation(config=rule_object.rules, data=df)

if rule_object.len_rules:
    # lenght rules
    len_rule_obj.find_configs()
    len_rule_obj.validate_config()
    len_rule_obj.apply_rules()
    df = pd.concat([df, len_rule_obj.data], axis=1)
    print(df)

if rule_object.range_rules:
    # range rules
    range_rule_obj.find_configs()
    range_rule_obj.validate_config()
    range_rule_obj.apply_rules()
    df = pd.concat([df, range_rule_obj.data], axis=1)
    print(df)

if rule_object.field_op_rules:
    # field rules
    field_rule_obj.find_configs()
    field_rule_obj.validate_config()
    field_rule_obj.apply_rules()
    df = pd.concat([df, field_rule_obj.data], axis=1)
    print(df)

if rule_object.op_rules:
    # operation rules
    op_rule_obj.find_configs()
    op_rule_obj.validate_config()
    op_rule_obj.apply_rules()
    df = pd.concat([df, op_rule_obj.data], axis=1)
    print(df)

bool_rule_obj = BoolianOperator(config=rule_object.rules, data=df)
if rule_object.bool_rules:
    # bool operation rules
    bool_rule_obj.find_configs()
    bool_rule_obj.validate_config()
    bool_rule_obj.apply_rules()
    df = pd.concat([df, bool_rule_obj.data], axis=1)
    print(df)

# save data
df.to_csv('result.csv', index=False)
