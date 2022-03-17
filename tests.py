import os
import sys
import unittest

if __name__ == '__main__':
    # Only set path if invoked as a script. Testrunners should have setup
    # the paths already
    sys.path.insert(0, os.path.abspath(os.path.join(os.curdir, 'src')))

import WeatherData as wd


class TestObs(unittest.TestCase):
    def setUp(self):
        pass

    def test_lat(self):
        data = wd.obs.get('台北市中正區')
        self.assertRaises(ValueError)

    def test_citytown(self):
        data = wd.obs.get(citytown='台北市中正區')
        self.assertEqual(data['lat'], 25.046058)


if __name__ == '__main__':
    unittest.main()
