import os
import yaml

def open_config_file():
    try:
        with open(os.path.join('auth.yaml'), 'r') as config_file:
            return yaml.safe_load(config_file)
        
    except yaml.YAMLError as exc:
        print(f'🚨 There was an exception in the YAML : {exc}')
        return None