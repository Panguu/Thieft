import unittest
from ModulePackage.SIMModule import SimModule

class TestSimModule(unittest.TestCase):
    """
    Tests for Sim module on raspberry pi
    - warning due to the nature of sending information to different information to the pi gpio ensure each test is run individually for all modules
    """
    def test_power_on(self):
        """
        Test to ensure that the module has powered on
        """
        sim_module = SimModule()
        self.assertTrue(sim_module.power_on())

    def test_power_off(self):
        """
        Test to ensure that the module has powered off
        """
        sim_module = SimModule()
        self.assertTrue(sim_module.power_off())
    
    def test_at_command(self):
        """
        Test to ensure that the module has powered off
        """
        sim_module = SimModule()
        self.assertTrue(sim_module.power_on())
        # asserts command at is ok
        self.assertTrue(sim_module.send_at_command("AT", "OK", 2))
        # asserts command at is error expected failure
        self.assertFalse(sim_module.send_at_command("AT", "ERROR", 2))
        self.assertTrue(sim_module.power_off())

if __name__ == '__main__':
    unittest.main(TestSimModule().test_power_on())
    unittest.main(TestSimModule().test_power_off())
    unittest.main(TestSimModule().test_at_command())