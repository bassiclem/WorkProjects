import unittest
from donnees import*
from word2hexa import*
from market import*
from encoder_RSA import*
D = Donnees(10011001)
M1 = Market()
M2 = Market()
M2.changer_enseigne("AH")
L=["0x0","0x1","0x2","0x3","0x4","0x5","0x6","0x7","0x8","0x9","0xa","0xb","0xc","0xd","0xe"]


class MyTestCase(unittest.TestCase):
    def setUp(self):
        ref = Donnees("testsadds")

    def test_Donnees_sequencage(self):
        print("testing seq function")
        self.assertEqual(D.sequencage(3,3,3,2), [hex(int('100',2)),hex(int('110',2)),hex(int('01',2))])
        self.assertFalse(D.sequencage(3,3,3,2)==[hex(100),hex(110),hex(01)])

    def test_w2hex(self):
        print("testing w2hexa function")
        self.assertEqual(word2hexa("COOL"), [hex(ord("c")),hex(ord("o")),hex(ord("o")),hex(ord("l"))])
        self.assertFalse((word2hexa("COOL")==[hex(ord("C")),hex(ord("O")),hex(ord("O")),hex(ord("L"))]))

    def test_market_add(self):
        print("testing adding 2 market")
        self.assertEqual((M1+M2).Enseigne, "Monoprix et AH")

    def test_encoder_RSA(self):
        expected_return=['0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0']
        print type(expected_return[0])
        self.assertEqual(encoder_RSA(L,1,1),expected_return)
        expected_return=['0x0', '0x1', '0x8', '0x9', '0xa', '0x11', '0x0', '0x1', '0x8', '0x9', '0xa', '0x11', '0x0', '0x1', '0x8']

        self.assertEqual(encoder_RSA(L, 3, 18), expected_return)

        with self.assertRaises(TypeError):
            encoder_RSA([0x0, 0x0], 1, 1)

        self.assertRaises(TypeError, encoder_RSA, ([0x0, 0x0], 1, 1))

if __name__ == '__main__':
    unittest.main()
