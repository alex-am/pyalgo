import unittest

from ..play.trade import single_trade

class TestTrade(unittest.TestCase):
    def test_play(self):
        p = [4, 9, 1, 3, 8, 7, 1]
        check_p = [5, -1, 7, 5, -1, -6, 0]
        comp_p = single_trade(p)
        self.assertEqual(check_p, comp_p)
