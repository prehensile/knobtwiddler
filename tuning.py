from collections import namedtuple
import os
import random

Tuning = namedtuple( "Tuning", [ "frequency", "modulation" ] )

class MODULATION(object):
    NFM = "nfm"
    AM = "am"
    default = NFM
    modulations = [ NFM, AM ] 


def _self_path():
    return os.path.dirname(
        os.path.abspath( __file__ )
    )


def get_next_tuning():
    """ Returns a Tuning object"""
    return get_airband_tuning()


_AIRBANDS = None
def get_airband_tuning():
    global _AIRBANDS

    if _AIRBANDS is None:
        _AIRBANDS = []
        with open( os.path.join( _self_path(), "data/airband.txt")) as fh:
            for line in fh:
                if not line.startswith( "#" ):
                    c = line.split( ";" )
                    # first field is frequency
                    f = float(c[0])
                    # second field is modulation, needs remapping to MODULATION_NFM etc
                    _m = c[2].strip()
                    m = None
                    if _m == "Narrow FM":
                        m = MODULATION.NFM
                    elif _m == "AM":
                        m = MODULATION.AM
                    # add a new Tuning object to _AIRBANDS array
                    _AIRBANDS.append( Tuning( frequency=f, modulation=m ) )
    
    return random.choice( _AIRBANDS )

