from typing import Final

__version__: Final[str] = ...

def dottedQuadToNum(ip): ...
def numToDottedQuad(num): ...

class ValidateError(Exception): ...
class VdtMissingValue(ValidateError): ...
class VdtUnknownCheckError(ValidateError): ...
class VdtParamError(SyntaxError): ...
class VdtTypeError(ValidateError): ...
class VdtValueError(ValidateError): ...
class VdtValueTooSmallError(VdtValueError): ...
class VdtValueTooBigError(VdtValueError): ...
class VdtValueTooShortError(VdtValueError): ...
class VdtValueTooLongError(VdtValueError): ...

class Validator:
    def __init__(self, functions=...) -> None: ...
    def check(self, check, value, missing=...): ...
    def get_default_value(self, check): ...

def is_integer(value, min=..., max=...): ...
def is_float(value, min=..., max=...): ...
def is_boolean(value): ...
def is_ip_addr(value): ...
def is_list(value, min=..., max=...): ...
def is_tuple(value, min=..., max=...): ...
def is_string(value, min=..., max=...): ...
def is_int_list(value, min=..., max=...): ...
def is_bool_list(value, min=..., max=...): ...
def is_float_list(value, min=..., max=...): ...
def is_string_list(value, min=..., max=...): ...
def is_ip_addr_list(value, min=..., max=...): ...
def force_list(value, min=..., max=...): ...
def is_mixed_list(value, *args): ...
def is_option(value, *options): ...

__all__ = (
    "__version__",
    "dottedQuadToNum",
    "numToDottedQuad",
    "ValidateError",
    "VdtUnknownCheckError",
    "VdtParamError",
    "VdtTypeError",
    "VdtValueError",
    "VdtValueTooSmallError",
    "VdtValueTooBigError",
    "VdtValueTooShortError",
    "VdtValueTooLongError",
    "VdtMissingValue",
    "Validator",
    "is_integer",
    "is_float",
    "is_boolean",
    "is_list",
    "is_tuple",
    "is_ip_addr",
    "is_string",
    "is_int_list",
    "is_bool_list",
    "is_float_list",
    "is_string_list",
    "is_ip_addr_list",
    "is_mixed_list",
    "is_option",
)
