from .parts.system import *

partial_state_update_blocks = [
	{
		'policies': {
			'beLiquidityProvider'

		},
		'variables': {
			'addLiquidity': addLiquidity

		}
	},
	{
		'policies': {
			'beTrader'

		},
		'variables': {
			'tradeEnergy': tradeEnergy
		}
	},
    {
		'policies': {
			'shareAccounting'

		},
		'variables': {
			'distributeShares': distributeShares
		}
	}
]
