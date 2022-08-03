from convert import currency_exchange

def selling(game_sell):
    curren = currency_exchange()
    sel = game_sell.replace('2.', '2')
    sell = sel.replace('1.', '1')
    sell1 = sell.replace(',', '.')
    sell_clear = sell1.replace('TL', '')
    procent = round(float(sell_clear) * curren / 2)
    finish_sell_ps5 = round(float(sell_clear) * curren + procent)
    return finish_sell_ps5