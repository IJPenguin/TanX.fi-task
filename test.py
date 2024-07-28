import pandas as pd
import pytest
from app import (
    read_data, compute_total_revenue_per_month,
    compute_total_revenue_per_product, compute_total_revenue_per_customer,
    top_10_customers_by_revenue
)

@pytest.fixture
def sample_data():
    data = {
        "order_id": [1, 2, 3],
        "customer_id": [1, 2, 1],
        "order_date": ["2023-01-01", "2023-02-01", "2023-01-15"],
        "product_id": [101, 102, 101],
        "product_name": ["Product A", "Product B", "Product A"],
        "product_price": [10.0, 20.0, 10.0],
        "quantity": [1, 2, 1]
    }
    return pd.DataFrame(data)

@pytest.fixture
def empty_data():
    return pd.DataFrame(columns=["order_id", "customer_id", "order_date", "product_id", "product_name", "product_price", "quantity"])

def test_read_data(tmp_path):
    test_file = tmp_path / "test_orders.csv"
    test_file.write_text(
        "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n"
        "1,1,2023-01-01,101,Product A,10.0,1\n"
        "2,2,2023-02-01,102,Product B,20.0,2\n"
        "3,1,2023-01-15,101,Product A,10.0,1\n"
    )
    data = read_data(test_file)
    assert not data.empty
    assert len(data) == 3

def test_read_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_data("non_existent_file.csv")

def test_read_data_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    test_file.write_text("")
    with pytest.raises(ValueError):
        read_data(test_file)

def test_compute_total_revenue_per_month(sample_data):
    revenue_per_month = compute_total_revenue_per_month(sample_data)
    assert len(revenue_per_month) == 2
    assert revenue_per_month.loc["2023-01"] == 20.0
    assert revenue_per_month.loc["2023-02"] == 20.0

def test_compute_total_revenue_per_product(sample_data):
    revenue_per_product = compute_total_revenue_per_product(sample_data)
    assert len(revenue_per_product) == 2
    assert revenue_per_product["Product A"] == 20.0
    assert revenue_per_product["Product B"] == 20.0

def test_compute_total_revenue_per_customer(sample_data):
    revenue_per_customer = compute_total_revenue_per_customer(sample_data)
    assert len(revenue_per_customer) == 2
    assert revenue_per_customer[1] == 20.0
    assert revenue_per_customer[2] == 20.0

def test_top_10_customers_by_revenue(sample_data):
    top_customers = top_10_customers_by_revenue(sample_data)
    assert len(top_customers) == 2
    assert top_customers.iloc[0] == 20.0
    assert top_customers.iloc[1] == 20.0

def test_empty_data(empty_data):
    assert compute_total_revenue_per_month(empty_data).empty
    assert compute_total_revenue_per_product(empty_data).empty
    assert compute_total_revenue_per_customer(empty_data).empty
    assert top_10_customers_by_revenue(empty_data).empty
