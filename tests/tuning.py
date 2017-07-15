import unittest 
import os, sys

sys.path.insert( 0, os.path.realpath("..") )
import tuning


class TestTuning( unittest.TestCase ):

    def test_boolean(self):
        for i in range( 10 ):
            
            t = tuning.get_next_tuning()
            
            self.assertIsInstance( t.frequency, float )
            self.assertGreater( t.frequency, 0 )

            self.assertTrue( t.modulation in tuning.MODULATION.modulations )
            
            print t

if __name__ == '__main__':
    unittest.main()