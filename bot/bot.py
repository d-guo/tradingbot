from alpaca.alpaca import Alpaca

tb = Alpaca('keys.cfg')
print(tb.getAllAssets()[0])