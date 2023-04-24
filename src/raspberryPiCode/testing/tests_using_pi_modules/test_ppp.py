import unittest
from ModulePackage.PPPSetup import PPP

class TestPPP(unittest.TestCase):
    """
    Tests for ppp aka (internet connection on command)
    """
    def test_ppp_start_connection(self):
        """
        Test for starting a connection using ppp
        """
        ppp = PPP()
        self.assertTrue(ppp.startConnection())
        self.assertTrue(ppp.state)
    
    def test_ppp_end_connection(self):
        """
        Test for ending a connection using ppp
        """
        ppp = PPP()
        self.assertTrue(ppp.endConnection())
        self.assertFalse(ppp.state)

if __name__ == '__main__':
    unittest.main(TestPPP().test_ppp_start_connection())
    unittest.main(TestPPP().test_ppp_end_connection())