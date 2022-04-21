import time


class PlaySound:
    
    '''Play sound file   '''

    def __init__(self,volume_level, wavefile):
    	self.volume_level = volume_level
    	self.wavefile = wavefile
    	

    def play_wave(self):
    	# Setting the variables        
        value = float(1)
		
    	mute = system.tag.readBlocking([self.volume_level])[0].value
    	volume = system.tag.writeBlocking([self.volume_level], [value])
    	# logic

    	if mute == 1:
            mute = system.tag.readBlocking([self.volume_level])[0].value
    	    while mute == 1.0:
                mute = system.tag.readBlocking([self.volume_level])[0].value
                mute_float = float("{:.2f}".format(mute))
                system.util.playSoundClip(self.wavefile, mute_float, 1)
                if mute == 0:
                    continue

    	elif mute == 0:
    	    value = float(0)
    	    system.tag.writeBlocking([self.volume_level], [value])
    	    
        else:
        	value = float(0)
        	system.tag.writeBlocking([self.volume_level], [value])
        	

