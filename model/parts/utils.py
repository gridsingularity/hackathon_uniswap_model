import numpy as np

def updateTotalKwhBalance(params, step, history, current_state, input_):
    variable = 'KWH'
    value = current_state['KWH'] + input_['trade_kwh']
    return (variable, value)

def updateTotalEurBalance(params, step, history, current_state, input_):
    variable = 'EUR'
    value = current_state['EUR'] + input_['trade_eur']
    return (variable, value)

def addKwhLiquidity(params, step, history, current_state, input_):
    variable = 'KWH'
    value = current_state['KWH'] + input_['liquidity_amount_kwh']
    return (variable, value)

def addEurLiquidity(params, step, history, current_state, input_):
    variable = 'EUR'
    value = current_state['EUR'] + input_['liquidity_amount_eur']
    return (variable, value)

def swapKwhEur(params, step, history, current_state, input_):
    price = current_state['price']
    return None

def shareAccounting(params, step, history, current_state):
    pass