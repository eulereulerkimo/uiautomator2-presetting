import sys
import time
import uiautomator2 as u2

class UiPresetting():    		
    def dConn(self, pid):
	    d = u2.connect(pid)
    	
    def dInfo(self, pid):
        self.dConn(pid)
        print(d.info)
		
    def clickSingleEvent(self, textName, clickName, sleeper=5, timer=20):
        if (d(text = textName).exists(timeout=timer)):
            time.sleep(sleeper)
            d(text = clickName).click()
			
    def clickSingleResource(self, textName, resourceName, sleeper=5, timer=20):
        if (d(text = textName).exists(timeout=timer)):
            time.sleep(sleeper)
            d(resourceId = resourceName).click()
			
    def clickSingleClass(self, textName, classname, sleeper=5, timer=20):
        if (d(text = textName).exists(timeout=timer)):
            time.sleep(sleeper)
            d(className = classname, instance=10).click()
			
    def checkSendkey(self, textName, key, sleeper=5, timer=20):
        if (d(text = textName).exists(timeout=timer)):
            time.sleep(sleeper)
            d.send_keys(key)
			
    def clickMultiEvent(self, textTuple, clickTuple, sleeper=5, timer=20):
        i=0
        for textName in textTuple:   
            print(textName)
            if (d(text = textName).exists(timeout=timer)):
                time.sleep(sleeper)
                d(text = clickTuple[i]).click()
	        i+=1
			
''' initial setup '''
uiPreset = UiPresetting()
uiPreset.dInfo("PDAGA8E851600134")
uiPreset.clickSingleClass("Sign in", "android.view.View")
d.send_keys("Lincorn0002@gmail.com")	
uiPreset.clickSingleEvent("Next", "Next")
uiPreset.checkSendkey("Welcome", "Corn123456")
uiPreset.clickSingleEvent("Next", "Next")
uiPreset.clickSingleEvent("I agree", "I agree")
uiPreset.clickSingleResource("Google Services", "com.google.android.gms:id/suw_items_switch")
uiPreset.clickSingleEvent("More", "More")
d(resourceId="com.google.android.gms:id/suw_items_switch", text=u"ON").click()").click()
d(resourceId="com.google.android.gms:id/suw_items_switch", text=u"ON").click()text=u"ON").click()").click()
settingsTuple = ("More", "Accept", "Unlock with fingerprint", "Protect your phone", "Skip screen lock?", "Access your Assistant with Voice Match", "Anything else?", "You are nearly ready to go...!")
settingPresssTuple = ("More", "Accept", "Skip", "Not now", "SKIP ANYWAY", "No thanks", "No thanks", "NOT NOW…")
uiPreset.clickMultiEvent(settingsTuple, settingPresssTuple)

''' launch Google Play Store and issue all apps updated '''
d.app_start("com.android.vending")
d(resourceId="com.android.vending:id/navigation_button").click()
uiPreset.clickSingleEvent("My apps & games", "My apps & games")
time.sleep(5)
d(resourceId="com.android.vending:id/updates_refresh_button").click()

''' launch setting and set time out to 30s '''
d.app_start("com.android.settings")
uiPreset.clickSingleEvent("Display", "Display")
settingsTuple = ("Display", "Advanced", "Sleep")
settingPresssTuple = ("Display", "Advanced", "Sleep")
uiPreset.clickMultiEvent(settingsTuple, settingPresssTuple)
uiPreset.clickSingleResource("30 minutes", "com.android.settings:id/text1")

''' launch Google Photos and set backup/restore to disable '''
d.app_start("com.google.android.apps.photos")
uiPreset.clickSingleResource("Back up & sync", "com.google.android.apps.photos:id/auto_backup_switch")
uiPreset.clickSingleEvent("Confirm", "Confirm")
uiPreset.clickSingleEvent("Keep off", "Keep off")

''' launch all apps set the permission '''
#contacks
d.app_start("com.google.android.contacts")
#Messages
d.app_start("com.google.android.apps.messaging")
uiPreset.clickSingleEvent("Start chat", "Start chat")
#Gmail
d.app_start("com.google.android.gm")
uiPreset.clickSingleEvent("GOT IT", "GOT IT")
uiPreset.clickSingleEvent("TAKE ME TO GMAIL", "TAKE ME TO GMAIL")
#Chrome
d.app_start("com.android.chrome")
uiPreset.clickSingleEvent("ACCEPT & CONTINUE", "ACCEPT & CONTINUE")
uiPreset.clickSingleEvent("CONTINUE", "CONTINUE")
uiPreset.clickSingleEvent("OK, GOT IT", "OK, GOT IT")
#Calendar
d.app_start("com.google.android.calendar")
uiPreset.clickSingleResource("Google Calendar", "com.google.android.calendar:id/right_arrow")
uiPreset.clickSingleResource("Easy to scan and lovely to look at", "com.google.android.calendar:id/right_arrow")
uiPreset.clickSingleEvent("Events from Gmail", "Got it")
#Clock 
d.app_start("com.google.android.deskclock")
#Camera
d.app_start("com.hmdglobal.camera2")
uiPreset.clickSingleEvent("ALLOW", "ALLOW")
for i in range(3): uiPreset.clickSingleEvent("NEXT", "NEXT")
#uiPreset.clickSingleEvent("NEXT", "NEXT") for i in range(3)

uiPreset.clickSingleEvent("GOT IT", "GOT IT")
#Maps 
d.app_start("com.google.android.apps.maps")
#Music 
d.app_start("com.google.android.music")
for i in range(2): uiPreset.clickSingleEvent("OK", "OK")

#Google 
d.app_start("com.google.android.googlequicksearchbox")
#Calculator 
d.app_start("com.google.android.calculator")
#Files 
d.app_start("com.google.android.apps.nbu.files")
#Wallpapers 
d.app_start("com.google.android.apps.wallpaper")
uiPreset.clickSingleEvent("ALLOW ACCESS", "ALLOW ACCESS")
uiPreset.clickSingleEvent("ALLOW", "ALLOW")
#

