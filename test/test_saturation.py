import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.saturation import saturation


class TestSaturation(unittest.TestCase):

    def test_saturation(self):
        test_datas = [
            {'value': 1, 'high': 10, 'low': 5, 'expect': 5},
            {'value': 7, 'high': 10, 'low': 5, 'expect': 7},
            {'value': 15, 'high': 10, 'low': 5, 'expect': 10}
        ]
        for data in test_datas:
            actual = saturation(data['value'], data['high'], data['low'])
            self.assertEqual(actual, data['expect'])


    # saturation無しの動作確認
    def test_path_through(self):
        expected = saturation(10, 11, 9)
        self.assertEqual(expected, 10)

    # 最大値saturationの動作確認
    def test_max_saturation(self):
        expected = saturation(11, 10, 5)
        self.assertEqual(expected, 10)

    # 最小値saturationの動作確認
    def test_min_saturation(self):
        expected = saturation(9, 15, 10)
        self.assertEqual(expected, 10)

    # 最大値データ型の不一致時の動作確認
    def test_max_datatype_mismatch(self):
        with self.assertRaises(ValueError):
            saturation(11, '10', 5)

    # 最小値データ型の不一致時の動作確認
    def test_min_datatype_mismatch(self):
        with self.assertRaises(ValueError):
            saturation(9, 15, '10')
