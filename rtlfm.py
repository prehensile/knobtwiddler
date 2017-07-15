import os, sys
import subprocess
import time

import tuning

class RTLFM:

    def fn_sample( self ):
        fn = "%0.10f.raw" % time.time()
        self_path = os.path.dirname(
            os.path.abspath( __file__ )
        )
        return os.path.join(
            self_path, "samples", fn
        )


    def sample_frequency( self, frequency=0, modulation=tuning.MODULATION.default, gain=50, duration=1000 ):

        # mostly cribbed from http://kmkeen.com/rtl-demod-guide/
        args = [
            # executable path
            "rtl_fm",
            # modulation
            "-M", modulation,
            # frequency
            "-f", "%2.10f" % frequency,
            # sample rate
            "-s", "12k",
            # gain, apparently 50 is about right?
            "-g", "%d" % gain,
            # squelch
            # "-l", "280"
            # filename
            self.fn_sample()
        ]

        proc = subprocess.Popen( args )
        time.sleep( duration/1000.0 )
        proc.terminate()
        
        # sleep a little bit to let the tuner recover
        time.sleep( 1/1000.0 )

        #print args