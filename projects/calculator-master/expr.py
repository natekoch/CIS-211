"""
Nate Koch
CIS 211
Calculator
"""

# One global environment (scope) for the calculator
ENV = dict()

def env_clear():
    """Clear all variables in calculator memory"""
    global ENV
    ENV = dict()

class UndefinedVariable(Exception):
    """Raised when expression tries to use a variable that is not in ENV"""
    pass

class Expr(object):
    """Abstract base class of all expressions."""

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        raise NotImplementedError("Each concrete Expr class must define 'eval'")

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        raise NotImplementedError("Each concrete Expr class must define __str__")

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        raise NotImplementedError("Each concrete Expr class must define __repr__")

class IntConst(Expr):

    def __init__(self, value: int):
        self.value = value

    def eval(self) -> "IntConst":
        return self

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"IntConst({self.value})"

    def __eq__(self, other: Expr):
        return isinstance(other, IntConst) and self.value == other.value

class BinOp(Expr):
    
    def __init__(self):
        raise NotImplementedError("Do not instantiate BinOp")

    def _binop_init(self, left: Expr, right: Expr, op_sym: str, op_name: str):
        self.left = left
        self.right = right
        self.op_sym = op_sym
        self.op_name = op_name

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return f"({str(self.left)} {self.op_sym} {str(self.right)})"

    def __repr__(self) -> str:
        return f"{self.op_name}({repr(self.left)}, {repr(self.right)})"

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int, int)->int"""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(self._apply(left_val.value, right_val.value))

class Plus(BinOp):
    """Expr + Expr"""

    def __init__(self, left: IntConst, right: IntConst):
        self._binop_init(left, right, "+", "Plus")

    def _apply(self, left: int, right: int) -> int:
        return left + right

class Times(BinOp):
    """Expr * Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, "*", "Times")

    def _apply(self, left: int, right: int) -> int:
        return left * right

class Div(BinOp):
    """Expr / Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, "/", "Div")

    def _apply(self, left: int, right: int) -> int:
        return left // right

class Minus(BinOp):
    """Expr - Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, "-", "Minus")
    
    def _apply(self, left: int, right: int) -> int:
        return left - right

class Unop(Expr):

    def __init__(self):
        raise NotImplementedError("Do not instantiate Unop")

    def _unop_init(self, left: Expr, op_sym: str, op_name: str):
        self.left = left
        self.op_sym = op_sym
        self.op_name = op_name

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return f"{self.op_sym} {str(self.left)}"

    def __repr__(self) -> str:
        return f"{self.op_name}({repr(self.left)})"

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int)->int"""
        left_val = self.left.eval()
        return IntConst(self._apply(left_val.value))

class Abs(Unop):
    """@ Expr"""

    def __init__(self, left: Expr):
        self._unop_init(left, "@", "Abs")

    def _apply(self, left: int) -> int:
        if left < 0:
            left *= -1
            return left
        else:
            return left

class Neg(Unop):
    """~ Expr"""

    def __init__(self, left: Expr):
        self._unop_init(left, "~", "Neg")

    def _apply(self, left: int) -> int:
        return left * -1

class Var(Expr):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Var({self.name})"

    def eval(self):
        global ENV
        if self.name in ENV:
            return ENV[self.name]
        else:
            raise UndefinedVariable(f"{self.name} has not been assigned a value")

    def assign(self, value: IntConst):
        global ENV
        ENV[self.name] = value

class Assign(Expr):
    """Assignment: x = E represented as Assign(x, E)"""

    def __init__(self, left: Var, right: Expr):
        assert isinstance(left, Var) # Can only assign to variables
        self.left = left
        self.right = right

    def eval(self) -> IntConst:
        r_val = self.right.eval()
        self.left.assign(r_val)
        return r_val
    
    def __str__(self) -> str:
        return f"{self.left} = {self.right}"

    def __repr__(self) -> str:
        return f"Assign({self.left}, {self.right})"