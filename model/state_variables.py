# Dependences
from .parts.utils import *
from .sys_params import initial_values


## Initial state object
'''
genesis_states = {
    'DAI_balance': initial_values['DAI_balance'],
    'ETH_balance': initial_values['ETH_balance'],
    'UNI_supply': initial_values['UNI_supply']
}
'''


genesis_states = {
	'KWH':1000000,
	'EUR':20000,
	'price':20,
	'LP':1000,
	'liquidity_providers_shares': {
		'provider_1':0,
		'provider_2':0,
		'provider_3':0,
		'provider_4':0,
		'provider_5':0,
		'provider_6':0,
		'provider_7':0,
		'provider_8':0,
		'provider_9':0,
		'provider_10':0
	},
	'liquidity_providers_fees': {
		'provider_1':0,
		'provider_2':0,
		'provider_3':0,
		'provider_4':0,
		'provider_5':0,
		'provider_6':0,
		'provider_7':0,
		'provider_8':0,
		'provider_9':0,
		'provider_10':0
	},
	'trader_profits': {
		'trader_1':0,
		'trader_2':0,
		'trader_3':0,
		'trader_4':0,
		'trader_5':0,
		'trader_6':0,
		'trader_7':0,
		'trader_8':0,
		'trader_9':0,
		'trader_10':0,
		'trader_11':0,
		'trader_12':0,
		'trader_13':0,
		'trader_14':0,
		'trader_15':0,
		'trader_16':0,
		'trader_17':0,
		'trader_18':0,
		'trader_19':0,
		'trader_20':0
	},
    'trader_balances_kwh': {
		'trader_1':1000,
		'trader_2':1000,
		'trader_3':1000,
		'trader_4':1000,
		'trader_5':1000,
		'trader_6':1000,
		'trader_7':1000,
		'trader_8':1000,
		'trader_9':1000,
		'trader_10':1000,
		'trader_11':1000,
		'trader_12':1000,
		'trader_13':1000,
		'trader_14':1000,
		'trader_15':1000,
		'trader_16':1000,
		'trader_17':1000,
		'trader_18':1000,
		'trader_19':1000,
		'trader_20':1000
	},
    'trader_balances_eur': {
		'trader_1':1000,
		'trader_2':1000,
		'trader_3':1000,
		'trader_4':1000,
		'trader_5':1000,
		'trader_6':1000,
		'trader_7':1000,
		'trader_8':1000,
		'trader_9':1000,
		'trader_10':1000,
		'trader_11':1000,
		'trader_12':1000,
		'trader_13':1000,
		'trader_14':1000,
		'trader_15':1000,
		'trader_16':1000,
		'trader_17':1000,
		'trader_18':1000,
		'trader_19':1000,
		'trader_20':1000
	}

}