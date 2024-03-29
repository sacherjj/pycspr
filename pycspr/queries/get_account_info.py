import jsonrpcclient as rpc_client

import pycspr
from pycspr.crypto import get_account_hash



# RPC method to be invoked.
_API_ENDPOINT = "state_get_item"


def execute(
    account_key: str,
    state_root_hash=None,
    parse_response: bool = True,
    ) -> dict:
    """Queries account information at a certain state root hash.

    :param account_key: Key of an on-chain account.
    :param state_root_hash: A node's root state hash at some point in chain time.
    :param parse_response: Flag indicating whether to parse web-service response.

    :returns: Account information in JSON format.

    """
    account_hash = get_account_hash(account_key)

    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _API_ENDPOINT,
        key=f"account-hash-{account_hash}",
        state_root_hash=state_root_hash,
        path=[]
        )

    return response.data.result["stored_value"]["Account"] if parse_response else response.data.result
