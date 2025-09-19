from statistics import correlation

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_recent_trend (df, time_period='M'):
    df['dt_time'] = df['purchase_date'].dt.to_period(time_period)
    period_stats = df.groupby(['user_id', 'dt_time']).agg({'purchase_amount':['sum', 'count', 'mean']}).reset_index()
    period_stats.columns = ['user_id', 'dt_time', 'total_spend', 'purchase_count', 'average_spend']
    period_stats['dt_time'] = period_stats['dt_time'].astype(str)

    user_period_counts = period_stats.groupby('user_id')['dt_time'].nunique()
    repeated_user_indices = user_period_counts[user_period_counts > 1].index

    period_stats = period_stats[period_stats['user_id'].isin(repeated_user_indices)]

    user_trends = []

    for user_id in period_stats['user_id'].unique():
        user_data = period_stats[period_stats['user_id'] == user_id].sort_values('dt_time')
        if len(user_data) > 1:
            x = np.arange(len(user_data))
            y = user_data['total_spend'].values

            if len(x) > 1 and np.std(x)>0:
                purchase_corr = np.corrcoef(x, y)[0, 1]

                # check if increasing trend
                # Check for monotonic increase
                over_period_increase = all(y[i] >= y[i - 1] for i in range(1, len(y)))
                # Calculate total increase amount
                increase_amount = sum(y[i] - y[i - 1] for i in range(1, len(y)))

                start_amount = user_data.iloc[0]['total_spend']
                end_amount = user_data.iloc[-1]['total_spend']
                growth_rate = (end_amount - start_amount) / start_amount*100

                user_trends.append({
                    'user_id': user_id,
                    'correlation': purchase_corr,
                    'monotonic increase': over_period_increase,
                    'total_increase': increase_amount,
                    'growth_rate (%)': growth_rate,
                    f'period ({time_period})': len(user_data)
                })
    return pd.DataFrame(user_trends), period_stats


def find_recent_user_purchase_trend(dataset_path:str):
    df = pd.read_csv(f"{dataset_path}", header=0, encoding='utf-8', delimiter='\x2C')
    df['purchase_date'] = pd.to_datetime(df['purchase_date'], format='%Y-%m-%d')

    end_date = df['purchase_date'].max()
    print(end_date)

    # start_date = end_date - timedelta(days=91)
    start_date = end_date - pd.DateOffset(months = 3)
    print("time window {} to {}".format(start_date.date(), end_date.date()))

    recent_months_df = df[df['purchase_date'] >= start_date]
    print(recent_months_df)
    user_trend_df, monthly_stats = get_recent_trend(recent_months_df, time_period='M')

    if not user_trend_df.empty:
        for index, user in user_trend_df.iterrows():
            print(f"row {index}:\n{user}")


    if monthly_stats is not None:
        print(monthly_stats)


ds_file = "user_purchase_ds.csv"
find_recent_user_purchase_trend(ds_file)