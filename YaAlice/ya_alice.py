"""

YaAlice v0.0.1

"""

import datetime
import json
from typing import Self
from YaAlice.base import Base
from YaAlice.errors.errors import SettingsErrors
from YaAlice.functions.terminal import clear_terminal
from YaAlice.functions.valid_settings import new_settings_is_valid


class YaAlice(Base):

    def __init__(self: Self, alice_request: dict, settings: dict) -> None:
        super().__init__()
        self.start_time = datetime.datetime.now()
        
        if settings.DEBUG:
            settings_is_valid = new_settings_is_valid(settings)
            if settings_is_valid != "success":
                raise SettingsErrors(settings_is_valid, language=settings.DEBUG_LANGUAGE)

        self.alice_request = alice_request if type(alice_request) is dict else json.loads(alice_request)
        self.settings = settings

        if self.settings.LOG_OUTPUT_IMMEDIATELY:
            clear_terminal()
        self.add_log("configuration_options_log", color="green")
        self.__processing_request()

    def __processing_request(self: Self) -> None:
        self.new = self.params_alice["session"]["new"]
        self.intents = self.params_alice["request"]["nlu"]["intents"]       

        if hasattr(self.settings, "CONSTANT_BUTTONS"):
            self.add_buttons(self.settings.CONSTANT_BUTTONS)

        if self.settings.SOURCE_TEXT in self.params_alice["request"].keys():
            self.came_message = self.params_alice["request"][self.settings.SOURCE_TEXT]
        elif "nlu" in self.params_alice["request"].keys():
            self.came_message = " ".join(self.params_alice["request"]["nlu"]["tokens"])
        else:
            self.came_message = ""

        
        
