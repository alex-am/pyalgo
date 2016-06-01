import unittest

from ..play.trade import bf_left
from ..play.trade import bf_right
from ..play.trade import dyn_trader

class TestTrade(unittest.TestCase):
    def test_play(self):
        p = [4, 9, 1, 3, 8, 7, 1]
        check_k_1 = [None, 5, 5, 5, 7, 7, 7]
        check_k_2 = [None, None, None, 7, 12, 12, 12]
        check_k_3 = [None, None, None, None, None, 6, 6]
        check_k_4 = [None, None, None, None, None, None, None]
        res_k_1, o_n, o_v = dyn_trader(p, 1)
        self.assertEqual(check_k_1, res_k_1[0])
        res_k_2, o_n, o_v = dyn_trader(p, 2)
        self.assertEqual(check_k_2, res_k_2[1])
        res_k_3, o_n, o_v = dyn_trader(p, 3)
        self.assertEqual(check_k_3, res_k_3[2])
        res_k_4, o_n, o_v = dyn_trader(p, 4)
        self.assertEqual(check_k_4, res_k_4[3])
        print(o_n, o_v)
