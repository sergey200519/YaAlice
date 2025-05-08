"""

YaAlice v0.0.1

"""

import datetime
from typing import Self
from YaAlice.base import Base


class YaAlice(Base):

    def __init__(self: Self, alice_params: dict, settings: dict) -> None:
        super().__init__()
        self.start_time = datetime.datetime.now()
        
        if settings.DEBUG:
            settings_is_valid = new_settings_is_valid(settings)
            if settings_is_valid != "success":
                raise SettingsErrors(settings_is_valid, language=settings.DEBUG_LANGUAGE)

        self.params = alice_params
        self.settings = settings
        self.add_log("configuration_options_log", color="yellow")
        
