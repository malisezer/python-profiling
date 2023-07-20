import random
import pandas as pd


def generate_data(factor):
    random.seed(42)

    item_ids = [1000 + i for i in range(10**factor)]
    prices = [round(20 + random.random() * 50, 2) for _ in range(10**factor)]
    price_constants = [
        round((random.random() - 0.5) * 10, 2) for _ in range(10**factor)
    ]
    units = [int(random.random() * 100) for _ in range(10**factor)]

    data_df = pd.DataFrame(
        data={
            "item_id": item_ids,
            "price": prices,
            "price_constant": price_constants,
            "units": units,
        }
    )
    return data_df


def filter_data(data_df):
    required_indexes = []
    for i in range(len(data_df)):
        if data_df.loc[i, "price"] + data_df.loc[i, "price_constant"] < 51:
            required_indexes.append(i)

    data_df = data_df.iloc[required_indexes]
    data_df = data_df.reset_index(drop=True)
    return data_df


def process_data(data_df):
    revenues = []
    for i in range(len(data_df)):
        revenue = (
            data_df.loc[i, "price"] + data_df.loc[i, "price_constant"]
        ) * data_df.loc[i, "units"]
        revenues.append(revenue)

    data_df["revenue"] = revenues
    return data_df


def form_output(data_df):
    data_df = data_df.sort_values(by=["revenue"], ascending=[False]).reset_index(
        drop=True
    )
    items = []

    for i in range(len(data_df)):
        item_output = {
            "itemId": data_df.loc[i, "item_id"],
            "priceVars": {
                "price": data_df.loc[i, "price"],
                "priceConstant": data_df.loc[i, "price_constant"],
            },
            "units": data_df.loc[i, "units"],
            "revenue": data_df.loc[i, "revenue"],
        }
        items.append(item_output)
    return items


def run_algo(factor):
    data_df = generate_data(factor=factor)
    data_df = filter_data(data_df=data_df)
    data_df = process_data(data_df=data_df)
    output = form_output(data_df=data_df)
    return output
