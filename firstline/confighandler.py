#!/usr/bin/python3
import os
import sys
import logging
import json
import click
import logging
from pathlib import Path

class ConfigHandler: 


    def __init__(self, configfile, default_config=None, interactive=False):

        self.log = logging.getLogger()
        self.configfile = configfile
        if os.path.isdir('conf'):
            self.configfile = 'conf/{0}'.format(self.configfile)

        if not self.__config_exists(configfile):
            if interactive:
                self.config = self.__create_default_config_interactive(default_config)
            else:
                self.config = self.__create_default_config(default_config)
            self.__write()
        else:
            self.config = self.__read()
            """ Legacy check - leaving around """
            #if self.get_hostname() != os.uname()[1]:
            #    self.log.error('Config invalid: hostname is not %s' % self.get_hostname())
            #    sys.exit('Error. Config invalid: hostname is not %s' % self.get_hostname())

    def __config_exists(self, configfile):
        if not os.path.exists(configfile):
            self.log.warning('Config file %s not found' % configfile)
            return False 
        else:
            self.log.info('Found config file %s' % configfile)
            return True

    # Todo: wizardify to replace 
    def __create_default_config(self, default_config=None):

        # Some sort of default config
        #hostname = os.uname()[1]
        config = default_config

        return config

    def __create_default_config_interactive(self, default_config):
        config = {}
        for key, value in default_config.items():
                config[key] = click.prompt('Enter value for ' + key, default=value)
        return config

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
        self.log.info("Writing configfile %s" % self.configfile)

        with open(self.configfile, 'w') as outfile:
            json.dump(self.config, outfile, indent=4)
            outfile.close()
