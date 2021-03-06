class SemanticError(Exception):
    def __init__(self, text=None) -> None:
        super().__init__(text)
        self.text = text


METHOD_NOT_DEFINED = 'Method "%s" is not defined.'
WRONG_SIGNATURE = 'Method "%s" already defined in "%s" with a different signature.'
SELF_IS_READONLY = 'Variable "self" is read-only.'
LOCAL_ALREADY_DEFINED = 'Variable "%s" is already defined.'
INCOMPATIBLE_TYPES = 'Cannot convert "%s" into "%s".'
VARIABLE_NOT_DEFINED = 'Variable "%s" is not defined in "%s".'
ATTRIBUTE_ALREADY_DEFINED = 'Attribute "%s" already defined.'
TYPE_ALREADY_DEFINED = 'Type "%s" already defined.'
VARIABLE_ALREADY_DEFINED = 'Variable "%s" already defined.'
INVALID_OPERATION = 'Operation is not defined between "%s" and "%s".'
INVALID_OPERATION_UNARY = 'Operation is not for "%s".'
RETURN_ERROR = '"return" outside function'
