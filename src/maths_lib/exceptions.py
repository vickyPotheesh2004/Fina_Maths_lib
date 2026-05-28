class MathsLibError(Exception):
    """Base exception for maths_lib."""


class MissingInputError(MathsLibError):
    """Raised when a required input is absent."""


class DivisionGuard(MathsLibError):
    """Raised when division by zero guard trips."""


class DomainError(MathsLibError):
    """Raised for invalid domain-level computations."""
