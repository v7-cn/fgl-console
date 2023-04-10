from contextlib import contextmanager
import contextvars

context_mode = contextvars.ContextVar('mode')
context_mode.set({})
class Context:
    @contextmanager
    @staticmethod
    def mode(mode):
        context_mode.get().add(mode)
        yield None
        context_mode.get().remove(mode)
        
        
    @staticmethod
    def isin(mode=""):
        mode in context_mode.get()