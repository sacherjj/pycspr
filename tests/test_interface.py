import enum
import inspect

import pytest



def _has_class(mod, cls):
    """Asserts that a container exposes a class.

    """
    _has_member(mod, cls)
    assert inspect.isclass(getattr(mod, cls)), '{} is not a class'.format(cls)


def _has_constant(mod, constant):
    """Asserts that a container exposes a constant.

    """
    _has_member(mod, constant)


def _has_enum(mod, enm):
    """Asserts that a container exposes an enumeration.

    """
    _has_member(mod, enm)
    assert issubclass(getattr(mod, enm), enum.Enum), '{} is not an enum'.format(enm)


def _has_exception(mod, err):
    """Asserts that a container exposes an exception.

    """
    _has_class(mod, err)
    assert issubclass(getattr(mod, err), Exception), \
           'Exception type does not inherit from builtin Exception class.'


def _has_function(mod, func):
    """Asserts that a container exposes a function.

    """
    _has_member(mod, func)
    assert inspect.isfunction(getattr(mod, func)), '{} is not a function'.format(func)


def _has_member(mod, member):
    """Asserts that a module exposes a member.

    """
    assert inspect.ismodule(mod)
    assert hasattr(mod, member), 'Missing member: {}'.format(member)


# Expected interface.
_INTERFACE = {
    _has_class: {
        "NodeConnectionInfo",
    },
    _has_enum: {
        "NodeEventType",
    },
    _has_constant: {
        "CONNECTION",
        "NODE_REST_ENDPOINTS",
        "NODE_RPC_ENDPOINTS",
        "NODE_SSE_ENDPOINTS",
    },
    _has_exception: set(),
    _has_function: {
        "get_account_balance",
        "get_account_hash",
        "get_account_info",
        "get_account_key",
        "get_account_main_purse_uref",
        "get_auction_info",
        "get_block",
        "get_era_info",
        "get_events",
        "get_node_metrics",
        "get_node_peers",
        "get_node_status",
        "get_rpc_endpoint",
        "get_rpc_schema",
        "get_state_root_hash",
        "get_switch_block",        
    },
}


def test_library_version(LIB):
    """Asserts library version.

    """
    assert LIB.__version__ == "0.1.0"


def test_library_exports(LIB):
    """Asserts that library is exposing expected interface.

    """
    for assertor, members in _INTERFACE.items():
        for member in members:
            assertor(LIB, member)
