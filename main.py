import pandas as pd
from config import api_key, sandbox_api_key, sandbox_finnhub_client

def get_eqs(TICKER, FREQUENCY):
    eqs = sandbox_finnhub_client.company_earnings_quality_score(TICKER, FREQUENCY)
    eqs_df = pd.DataFrame(eqs['data']).head(8)
    eqs_df.to_csv(f'{TICKER}_eqs.csv', index=False)

inp = input('Enter symbol: ')

get_eqs(TICKER=inp, FREQUENCY='quarterly')
