from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path
import os


class Config:
    """The config class used to store Ralsei's configuration."""
    def __init__(self, config_file="RalseiConfig.ini"):
        self.token, self.app_id, self.owner_id = None, None, None
        self.command_prefix, self.case_insensitive, self.pm_help = None, None, None
        self.command_not_found, self.command_has_no_subcommands = None, None
        self.ralsei_dir, self.cmds_dir, self.cogs_dir = None, None, None

        my_file = Path(os.getcwd()+"\\"+config_file)
        if not my_file.is_file():
            self.gen_config(config_file)
            self.__init__(config_file)
        else:
            self.read_config(config_file)

    @staticmethod
    def gen_config(config_file):
        config = ConfigParser(interpolation=ExtendedInterpolation())

        config["RalseiBase"] = {"token": "",
                                "owner_id": ""}
        config["RalseiConfig"] = {"command_prefix": "!",
                                  "case_insensitive": "False",
                                  "pm_help": "False",
                                  "command_not_found": "There is no command {}, Sorry!",
                                  "command_has_no_subcommands": "The {0.name} command does not have any subcommands, " +
                                                                "Sorry!"}
        config["RalseiPaths"] = {"Ralsei_Dir": "",
                                 "CMDs_Dir": "%{Ralsei_Dir}/cmds",
                                 "Cogs_Dir": "%{Ralsei_Dir}/cogs"}

        with open(config_file, 'w') as configfile:
            config.write(configfile)

    def read_config(self, config_file):
        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read(config_file)

        self.token = config["RalseiBase"]["token"]
        self.app_id = config["RalseiBase"]["App_ID"]
        self.owner_id = config["RalseiBase"]["owner_id"]

        self.command_prefix = config["RalseiConfig"]["command_prefix"]
        self.case_insensitive = config["RalseiConfig"]["case_insensitive"]
        self.pm_help = config["RalseiConfig"]["pm_help"]
        self.command_not_found = config["RalseiConfig"]["command_not_found"]
        self.command_has_no_subcommands = config["RalseiConfig"]["command_has_no_subcommands"]

        self.ralsei_dir = config["RalseiPaths"]["Ralsei_Dir"]
        self.cmds_dir = config["RalseiPaths"]["CMDs_Dir"]
        self.cogs_dir = config["RalseiPaths"]["Cogs_Dir"]

        try:
            self.owner_id = int(self.owner_id)
        except ValueError:
            pass
