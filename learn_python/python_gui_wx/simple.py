#!/usr/bin/env python
#coding: utf-8

"""
@Author: Well
@Date: 2014 - 07 - 27
"""

import wx
import smtplib

app = wx.App()

frame = wx.Frame(None)
frame.Show()

app.MainLoop()
smtp_obj = smtplib.SMTP