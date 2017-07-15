import sys, os
import tuning
import rtlfm

# main runloop
rtl = rtlfm.RTLFM()
#while True:
for i in range( 10 ):

    # get a tuning
    t = tuning.get_next_tuning()

    # sample a bit
    rtl.sample_frequency(
        frequency = t.frequency, 
        modulation = t.modulation,
        duration = 5 * 1000
    )
    
    # TODO: detect non-silence

    # if not silence
    #   TODO: sample more
    #   TODO: detect voice
