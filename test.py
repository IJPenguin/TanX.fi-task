import unittest
import pandas as pd
from io import StringIO
from app import (
    read_data, 
    compute_total_revenue_per_month, 
    compute_total_revenue_per_product, 
    compute_total_revenue_per_customer, 
    top_10_customers_by_revenue
)

class TestOrders(unittest.TestCase):

    def setUp(self):
        # Sample CSV data for testing
        csv_data = StringIO("""
        order_id,customer_id,order_date,product_id,product_name,product_price,quantity
        1,1001,2021-01-15,2001,Product A,10.0,2
        2,1002,2021-01-20,2002,Product B,20.0,1
        3,1001,2021-02-10,2003,Product C,30.0,1
        4,1003,2021-02-15,2001,Product A,10.0,3
        5,1002,2021-03-01,2002,Product B,20.0,2
        """)
        self.data = pd.read_csv(csv_data)

    def test_read_data(self):
        # Test reading data from a correct path
        data = read_data('orders.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_compute_total_revenue_per_month(self):
        expected_output = pd.Series(
            [30.0, 40.0, 40.0], 
            index=pd.period_range(start='2021-01', periods=3, freq='M')
        )
        result = compute_total_revenue_per_month(self.data)
        pd.testing.assert_series_equal(result.sort_index(), expected_output.sort_index())

    def test_compute_total_revenue_per_product(self):
        expected_output = pd.Series(
            [40.0, 40.0, 30.0], 
            index=['Product A', 'Product B', 'Product C']
        )
        result = compute_total_revenue_per_product(self.data)
        pd.testing.assert_series_equal(result.sort_index(), expected_output.sort_index())

    def test_compute_total_revenue_per_customer(self):
        expected_output = pd.Series(
            [40.0, 40.0, 30.0], 
            index=[1001, 1002, 1003]
        )
        result = compute_total_revenue_per_customer(self.data)
        pd.testing.assert_series_equal(result.sort_index(), expected_output.sort_index())

    def test_top_10_customers_by_revenue(self):
        expected_output = pd.Series(
            [40.0, 40.0, 30.0], 
            index=[1001, 1002, 1003]
        )
        result = top_10_customers_by_revenue(self.data)
        pd.testing.assert_series_equal(result.sort_index(), expected_output.sort_index())

if __name__ == '__main__':
    unittest.main()
