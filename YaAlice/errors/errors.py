from YaAlice.messages import embedded_errors_message


class BaseErrors(Exception):
    def __init__(self, text, context=None, language="en", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = text
        self.context = context
        self.language = language

    def get_dialog(self, key):
        return embedded_errors_message.embedded_errors_message.get(f"{key}-{self.language}")

    def __str__(self):
        return f"Base Error: {self.get_dialog(self.msg)}"


class SettingsErrors(BaseErrors):
    def __str__(self):
        return f"Settings Error: {self.get_dialog(self.msg).format(self.context)}"
    
class KeyWordsErrors(BaseErrors):
    def __str__(self):
        return f"Key words Error: {self.get_dialog(self.msg).format(self.context)}"
    
class MessageErrors(BaseErrors):
    def __str__(self):
        return f"Message Error: {self.get_dialog(self.msg).format(self.context)}"
    
class StorageErrors(BaseErrors):
    def __str__(self):
        return f"Storage Error: {self.get_dialog(self.msg).format(self.context)}"
    
class AliceRequestErrors(BaseErrors):
    def __str__(self):
        return f"Alice Request Error: {self.get_dialog(self.msg).format(self.context)}"