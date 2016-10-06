
# -*- coding: utf-8 -*-

'''
    ExtroPower Add-on
    Copyright (C) 2016 Extro All Rights Reserved
    
    This software, the information and data which form part of such
    software disclosed herein are the exclusive property of Extro
    and their copyrights belong to Extro and are not to be used, 
    disclosed to others or reproduced without the written consent 
    of Extro The recipient of this software, by its retention 
    and use agrees to hold in confidence the data and information 
    which form part of such software contained herein.  

    It is forbidden to erase or obliterate this legend in whole or 
    in part.
'''


import xbmcgui
import xbmcaddon
import ExtroCore

language = xbmcaddon.Addon().getLocalizedString
deviceSuspend = language(32001).encode('utf-8')
rebootLinux = language(32002).encode('utf-8')
rebootAndroid = language(32003).encode('utf-8')
rebootDebian = language(32004).encode('utf-8')
header = language(32005).encode('utf-8')

menuItems = [ deviceSuspend, rebootLinux, rebootAndroid ]

try:
    menu = xbmcgui.Dialog().contextmenu(menuItems)
except:
    menu = xbmcgui.Dialog().select(header, menuItems)

if menu == -1:
    pass
elif menu == 0:
    ExtroCore.deviceSuspend()
elif menu == 1:
    ExtroCore.rebootLinux()
elif menu == 2:
    ExtroCore.rebootAndroid()
elif menu == 3:
    ExtroCore.rebootDebian()
