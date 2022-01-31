import pytest
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.testing.contract import StarknetContract

# Start tests with 'test_'

@pytest.mark.asyncio
async def test_main_logic():
    # Create local network
    starknet = await Starknet.empty()
    # Deploy the contract
    contract = await starknet.deploy("contracts/TEMPLATE.cairo")

    # Modify a contract
    await contract.EXTERNAL_FUNCTION_NAME(INPUT_1, INPUT_2).invoke()

    # Read from a contract
    VAL = await contract.VIEW_FUNCTION_NAME().call()
    assert VAL == EXPECTED_RESULT
    print('Value is as expected')
