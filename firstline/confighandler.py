#!/usr/bin/python3
import os
import json
import logging
#from pathlib import Path
import click

class ConfigHandler:

    def __init__(self, configfile, config, interactive=False):

        self.log = logging.getLogger()
        self.configfile = configfile

        if os.path.isdir('conf'):
            self.configfile = 'conf/{0}'.format(self.configfile)

        if not self.__config_exists(self.configfile):
            if interactive:
                self.config = self.__create_config_interactive(config)
            else:
                self.config = config
            self.__write()
        else:
            self.config = self.__read()
            if interactive:
                if click.confirm('Do you want to reconfigure interactively?', default = True):
                    self.log.debug('Reconfiguring interactively')
                    self.config = self.__create_config_interactive(self.config)
                    self.__write()
                    click.confirm('Continue running?', abort=True, default=True)

    def __config_exists(self, configfile):
        if not os.path.exists(configfile):
            self.log.warning('Config file %s not found', configfile)
            return False
        self.log.info('Found config file %s', configfile)
        return True

    def __create_config_interactive(self, config):
        for key, value in config.items():
            config[key] = click.prompt('Enter value for ' + key, default=value)
        return config

    def add_path_entry(self, key, path):
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
            self.config[key].append(value)
            self.__write()

    def set_list(self):
        pass

    def __read(self):
        self.log.debug("Reading configfile %s", self.configfile)
        with open(self.configfile, 'r') as infile:
            config = json.load(infile)
            infile.close()
            return config

    def __write(self):
        self.log.debug("Writing configfile %s", self.configfile)
        with open(self.configfile, 'w') as outfile:
            json.dump(self.config, outfile, indent=4)
            outfile.close()
