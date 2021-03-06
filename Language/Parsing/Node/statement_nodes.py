from sqlite3 import paramstyle
from .node import Node


class StatementNode(Node):
    pass


class AssignmentNode(StatementNode):
    def __init__(self, ida, expr) -> None:
        super().__init__()
        self.id = ida
        self.expr = expr


class AgentDefNode(StatementNode):
    def __init__(self, idt, idn, conditions, t, rep, act, supply=None) -> None:
        super().__init__()
        self.idt = idt
        self.idn = idn
        self.conditions = conditions
        self.t = t
        self.rep = rep
        self.act = act
        self.supply = supply


class AttrDeclarationNode(StatementNode):
    def __init__(self, type, id, expr) -> None:
        super().__init__()
        self.type = type
        self.id = id
        self.expr = expr


class RandomVariableNode(StatementNode):
    def __init__(self, expr) -> None:
        super().__init__()
        self.expr = expr
        self.type = None


class ForNode(StatementNode):
    def __init__(self, var, expr, body) -> None:
        super().__init__()
        self.body = body
        self.var = var
        self.expr = expr


class IfElseNode(StatementNode):
    def __init__(self, condition_if, body_if, body_else) -> None:
        super().__init__()
        self.condition_if = condition_if
        self.body_if = body_if
        self.body_else = body_else


class IfNode(StatementNode):
    def __init__(self, expr, body) -> None:
        super().__init__()
        self.expr = expr
        self.body = body


class ReturnNode(StatementNode):
    def __init__(self, expr) -> None:
        super().__init__()
        self.expr = expr


class ReturnNode(StatementNode):
    def __init__(self, expr) -> None:
        super().__init__()
        self.expr = expr
