import unittest
from get_tropo_IPs import clean_ip


class TestIpProcess(unittest.TestCase):
    def test_clean_ip(self):
        line = '_netblocks.tropo.com text = "169.45.108.128/29"'
        prefix = "tropo"
        ip = clean_ip(line, prefix)

        # check that it returns something
        self.assertIsNotNone(ip, '"ip" should exist')
        # check that it returns the correct string
        self.assertEqual(prefix + ',' + '169.45.108.128/29', ip,
                         'Wrong string for "Ip" it output: {}'.format(ip))


if __name__ == '__main__':
    unittest.main()
