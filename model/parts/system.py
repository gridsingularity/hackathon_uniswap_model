import numpy as np
import pandas as pd
from .utils import *

# Behaviors
liquidity_providers_probability = 0.05
liquidity_amount_kwh = 50000
liquidity_amount_eur = 2500

def beLiquidityProvider(params, step, history, current_state):
    liquidity_provider_id = rand(1, 11)
    if rand() < liquidity_providers_probability:
        return({'amount_kwh': liquidity_amount_kwh})
    return({'amount_kwh': 0})

traders_probability = 0.2
maximum_trade_kwh = 100

def beTrader(params, step, history, current_state):
    trader_id = rand(1, 21)
    amount_kwh = rand(1, 1 + 2*maximum_trade_kwh) - maximum_trade_kwh
    if rand() < traders_probability:
        return {'trade_kwh': amount_kwh}
    return {'trade_kwh': 0}
