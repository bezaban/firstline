#!/usr/bin/python3
import os
import sys
import json
import click
from pathlib import Path

class ConfigHandler: 

    def __init__(self, configfile, default_config=None, interactive=False):

        self.configfile = configfile
 
       if os.path.isdir('conf'):
            self.configfile = 'conf/{0}'.format(self.configfile)

        logging_config = {
            'formatters': {
                    'standard': {
                        'format': '[%(asctime)s] [%(levelname)s] %(message)s',
                        'datefmt': '%Y-%m-%d %H:%M:%S'
                        }
                    },

            'handlers': {
                'default': { 
                    'level': 'INFO',
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout',  # Default is stderr
                    }
                },
                'loggers': { 
                    '': {  # root logger
                    'handlers': ['default'],
                    'level': 'WARNING',
                    'propagate': False
                    }
                }
            }

        if not self.__config_exists(configfile):
            if interactive:
                self.config = self.__create_default_config_interactive(logging_config, default_config)
            else:
                self.config = self.__create_default_config(logging_config, default_config)
            self.__write()
        else:
            self.config = self.__read()

    def __config_exists(self, configfile):
        if not os.path.exists(configfile):
            return False 
        else:
            return True

    # Todo: wizardify to replace 
    def __create_default_config(self, logging_config, default_config=None):

        # Some sort of default config
        #hostname = os.uname()[1]
        config = default_config + logging_config

        return config

    def __create_default_config_interactive(self, logging_config, default_config):
        config = {}
        for key, value in default_config.items():
                config[key] = click.prompt('Enter value for ' + key, default=value)
        return config + logging_config

    def get_hostname(self):
        return self.config['hostname']

    def add_path_entry(self, key, Path):
        pass

    def set_kv(self, key, value):
        self.config[key] = value
        self.__write()

    def get_kv(self, key):
        return self.config[key]

    def set_list_item(self, key, value):
        if isinstance(self.config[key], list):
            if value in self.config[key]:
                raise ValueError('Duplicate config entry in list')
            else:
                self.config[key].append(value)

        self.__write()

    def set_list(self):
        pass

    def __read(self):
        with open(self.configfile, 'r') as infile:
            config = json.load(infile)
            infile.close()

            return config

    def __write(self):

        with open(self.configfile, 'w') as outfile:
            json.dump(self.config, outfile, indent=4)
            outfile.close()
