import datetime
from typing import Optional, Self
from YaAlice.functions.terminal import print_log
from YaAlice.messages import embedded_message


class Base:
    """
    Base class for all YaAlice classes.
    """

    # bool
    new, end_session, inaction = False, False, True
    # str
    result_message, came_message = "", ""
    # dict
    intents, storage, events, logs, more_data_message = {}, {}, {}, {}, {}
    # list
    buttons, alice_buttons, key_words = [], [], []
    
    EMBEDDED_MESSAGE = embedded_message.embedded_message

    def add_log(self: Self, log: str, color: str = None, bg_color: Optional[str] = None, context: str = "", start_time: datetime = datetime.datetime.now()):
        if not self.settings.DEBUG:
            return
        delta_time = datetime.datetime.now() - start_time
        time = f"{delta_time.seconds}s {delta_time.microseconds} micros"
        log_text = self.EMBEDDED_MESSAGE.get(f"{log}-{self.settings.DEBUG_LANGUAGE}").format(context)
        self.logs[time] = f"{log_text}"
        print_log(
            log_text,
            time,
            text_color=color,
            bg_color=bg_color
        )
        
    
    
    