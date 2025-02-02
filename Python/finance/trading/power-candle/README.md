Ticker symbol sources:
    0
        https://www.cboe.com/us/equities/market_statistics/listed_symbols/
            CSV
    1
        https://github.com/shilewenuw/get_all_tickers/blob/master/get_all_tickers/tickers.csv
    2
        For American stocks: if you are using Python 3, you can first, from a terminal, do

        uv add get-all-tickers

        then

        from get_all_tickers import get_tickers as gt

        list_of_tickers = gt.get_tickers()
        # or if you want to save them to a CSV file
        get.save_tickers()

