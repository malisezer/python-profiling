from algo import run_algo, generate_data, filter_data, process_data, form_output

import pandas as pd


def test_generate_data():
    factor = 1
    result_df = generate_data(factor)
    assert result_df.shape[0] == 10
    assert result_df["item_id"][0] == 1000
    assert result_df["item_id"][5] == 1005
    assert result_df["item_id"][9] == 1009


def test_filter_data():
    test_df = pd.DataFrame(data={"id": [1, 2], "price": [50, 50], "price_constant": [0, 5]})

    result_df = filter_data(test_df)
    assert result_df.shape[0] == 1
    assert result_df["id"].iloc[0] == 1


def test_run_algo_with_zero_factor():
    result = run_algo(0)[0]
    assert result["itemId"] == 1000
    assert result["priceVars"]["price"] == 51.97
    assert result["priceVars"]["priceConstant"] == -4.75
    assert result["units"] == 27
    assert result["revenue"] == 1274.94


def test_process_data():
    test_df = pd.DataFrame(data={"price": [5], "price_constant": [0.5], "units": [2]})
    assert process_data(test_df)["revenue"][0] == 11


def test_form_output():
    test_df = pd.DataFrame(
        data={
            "item_id": [1],
            "price": [20],
            "price_constant": [2.4],
            "units": [5],
            "revenue": [112],
        }
    )

    result = form_output(test_df)[0]
    result["itemId"] = 1
    result["priceVars"]["price"] = 20
    result["priceVars"]["price_constant"] = 2.4
    result["units"] = 1
    result["revenue"] = 1


def test_run_algo_with_one_factor():
    result = run_algo(1)
    assert len(result) == 7
    assert result[0]["itemId"] == 1000
    assert result[-1]["itemId"] == 1007
    for i in range(len(result) - 1):
        assert result[i]["revenue"] > result[i + 1]["revenue"]
