"""

YaAlice v0.0.1

"""

import datetime
import json
from typing import Self
from YaAlice.base import Base
from YaAlice.errors.errors import AliceRequestErrors, SettingsErrors
from YaAlice.functions.bool import from_json_bool_to_py_bool
from YaAlice.functions.terminal import clear_terminal
from YaAlice.functions.valid_settings import new_settings_is_valid


class YaAlice(Base):

    def __init__(self: Self, alice_request: dict, settings: dict) -> None:
        super().__init__()
        self.start_time = datetime.datetime.now()
        
        if not hasattr(settings, "DEBUG"):
            if not hasattr(settings, "DEBUG_LANGUAGE"):
                # TODO: change to en
                settings.DEBUG_LANGUAGE = "ru"
            raise SettingsErrors("k_debug_language_not_set", language=settings.DEBUG_LANGUAGE)

        if settings.DEBUG:
            settings_is_valid = new_settings_is_valid(settings)
            if settings_is_valid != "success":
                raise SettingsErrors(settings_is_valid, language=settings.DEBUG_LANGUAGE)

        self.alice_request = alice_request if type(alice_request) is dict else json.loads(alice_request)
        self.settings = settings

        if self.settings.LOG_OUTPUT_IMMEDIATELY:
            clear_terminal()
        self.add_log("k_configuration_options_log", color="green")
        self.__processing_request()

    def __processing_request(self: Self) -> None:
        temp_new = from_json_bool_to_py_bool(self.alice_request["session"]["new"])
        if temp_new != -1:
            self.new = temp_new
        else:
            raise AliceRequestErrors("k_new_boolean_setting_error", language=self.settings.DEBUG_LANGUAGE)
        
        self.intents = self.alice_request["request"]["nlu"]["intents"]       

        if hasattr(self.settings, "CONSTANT_BUTTONS"):
            self.add_buttons(self.settings.CONSTANT_BUTTONS)

        if self.settings.SOURCE_TEXT in self.alice_request["request"].keys():
            self.came_message = self.alice_request["request"][self.settings.SOURCE_TEXT]
        elif "nlu" in self.alice_request["request"].keys():
            self.came_message = " ".join(self.alice_request["request"]["nlu"]["tokens"])
        else:
            self.came_message = ""
        
        if self.alice_request.get("state") is not None:
            self.storage = self.alice_request["state"]["session"]
            self.add_log("k_storage_fill", color="green", start_time=self.start_time)
            # TODO: add event
            # self.add_event({
            #                 "event": "storageFillEvent",
            #                 "storage": self.storage
            #                 }, "__init__")
        else:
            self.add_log("k_storage_not_fill", color="yellow", start_time=self.start_time)
        
        if self.new:
            # TODO: add message and buttons
            # self.add_message(self.settings.STARTING_MESSAGE)
            # self.add_buttons(self.settings.STARTING_BUTTONS) if hasattr(self.settings, "STARTING_BUTTONS") else None
            self.add_log("k_first_starting_end", color="green", start_time=self.start_time)
            return


        
        
