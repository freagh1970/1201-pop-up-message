import time

class PopUp_Message:

    def __init__(self, alarm_state, volume_level, popup_window,wavefile,alarm):
        self.alarm_state = alarm_state
        self.volume_level = volume_level
        self.popup_window = popup_window
        self.wavefile = wavefile
        self.alarm = alarm
        
        
    def play_wave(self):
    
        # Setting the variables
        
        value = 1
        volume = system.tag.writeBlocking([self.volume_level], [value])
        state = system.tag.readBlocking([self.alarm_state])[0].value
        
        # logic
        
        
        if state == True:
			
			step = 1
			system.tag.writeBlocking(['[site_01]SampleData/System/Basic/step'], [step])
				
			mute = system.tag.readBlocking([self.volume_level])[0].value
			popup = str(self.popup_window)
			alarm_no = {'alarm_no' : 1876}
			alarm_no['alarm_no'] = self.alarm
			#time.sleep(2)
			window = system.nav.openWindowInstance(popup,alarm_no)
			
			
			while mute == 1.0:
				mute = system.tag.readBlocking([self.volume_level])[0].value
				mute_float = float("{:.2f}".format(mute))
				system.util.playSoundClip(self.wavefile,mute_float,1)
				if mute == 0:
					continue
			
        elif state == False:
			step = 2
			system.tag.writeBlocking(['[site_01]SampleData/System/Basic/step'], [step])
			
			mute = 0
			value = 0
			system.tag.writeBlocking([self.volume_level], [value])
			#mute_float = float("{:.2f}".format(mute))
			#system.util.playSoundClip(self.wavefile,mute_float,1)
			window = system.nav.closeWindow(self.popup_window)
