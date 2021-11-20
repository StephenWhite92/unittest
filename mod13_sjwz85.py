import unittest
import user_input
import datetime

class InputTest(unittest.TestCase):

    def symbol_test(get_stock_symbol):
        get_stock_symbol.assertEqual("googl", "GOOGL")
        get_stock_symbol.assertLess("googl", 8)

    def chart_type_test(get_chart_type):
        get_chart_type.assertCountEqual(2, 1)
        get_chart_type.assertLessEqual(2, 2)
        get_chart_type.assertGreater(1, 0)

    def time_series_test(get_time_series):
        get_time_series.assertCountEqual(3, 1)
        get_time_series.assertLessEqual(3, 4)
        get_time_series.assertGreater(3, 0)

    def start_date_test(get_start_date):
        get_start_date.assertIsInstance(2020-01-01, datetime.date)

    def end_date_test(get_end_date):
        get_date.assertIsInstance(2010-01-01, datetime.date)

if __name__ == '__main__':
    unittest.main()
