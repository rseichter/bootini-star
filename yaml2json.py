"""
Convert EVE groups and types from YAML to JSON. Uses PyYaml.
"""
__author__ = 'Ralph Seichter'

import json
import sys

import yaml

# python yaml2json.py < groupIDs.yaml > groupIDs.json
# python yaml2json.py < typeIDs.yaml  > typeIDs.json

# mongoimport -d bs -c eve_groups --drop groupIDs.json
# mongoimport -d bs -c eve_types  --drop typeIDs.json

if __name__ == '__main__':
    data_dict = yaml.load(sys.stdin)
    for key, val_dict in data_dict.items():
        val_dict['eve_id'] = key
        json.dump(val_dict, sys.stdout, indent=2)
