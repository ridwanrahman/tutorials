import re
from contextvars import ContextVar, Token


validation_context: ContextVar[bool] = ContextVar("validation_context", default=True)

def using_validation_context():
    token = validation_context.get(False)

    validation_context.reset(token)