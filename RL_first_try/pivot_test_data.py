import pandas as pd

local_path = "/Users/adamrida/Documents/Rebellion/13F_Equity_portfolios/"
df = pd.read_csv(local_path + "RL_first_try/test_data_all_quarters.csv")
df.drop(columns="Unnamed: 0", inplace = True)
pivoted_df = df.pivot(index="date", columns = "stock_id", values = ["percent_good_subfund", "close", "numShares"])
pivoted_df.columns = [a + "_" + b for a, b in pivoted_df.columns]
pivoted_df.to_csv(local_path + "RL_first_try/pivoted_test_data.csv")
