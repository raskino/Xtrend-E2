# -*- coding: utf-8 -*-
import sys
import os
import time
from Tools.HardwareInfo import HardwareInfo

def getVersionString():
	return getImageVersionString()

def getImageVersionString():
	try:
		if os.path.isfile('/var/lib/opkg/status'):
			st = os.stat('/var/lib/opkg/status')
		else:
			st = os.stat('/usr/lib/ipkg/status')
		tm = time.localtime(st.st_mtime)
		if tm.tm_year >= 2011:
			return time.strftime("%Y-%m-%d %H:%M:%S", tm)
	except:
		pass
	return _("unavailable")

def getEnigmaVersionString():
	import enigma
	enigma_version = enigma.getEnigmaVersionString()
	if '-(no branch)' in enigma_version:
		enigma_version = enigma_version [:-12]
	return enigma_version

def getGStreamerVersionString():
	import enigma
	return enigma.getGStreamerVersionString()

def getKernelVersionString():
	try:
		return open("/proc/version","r").read().split(' ', 4)[2].split('-',2)[0]
	except:
		return _("unknown")

def getHardwareTypeString():
	return HardwareInfo().get_device_string()

def getImageTypeString():
	try:
		return open("/etc/issue").readlines()[-2].capitalize().strip()[:-6]
	except:
		return _("undefined")

def getCPUInfoString():
	try:
		cpu_count = 0
		for line in open("/proc/cpuinfo").readlines():
			line = [x.strip() for x in line.strip().split(":")]
			if line[0] == "system type":
				processor = line[1].split()[0]
			if line[0] == "cpu MHz":
				cpu_speed = "%1.0f" % float(line[1])
				cpu_count += 1
		if os.path.isfile('/proc/stb/fp/temp_sensor_avs'):
			temperature = open("/proc/stb/fp/temp_sensor_avs").readline().replace('\n','')
			return "%s %s MHz (%s) %s�C" % (processor, cpu_speed, ngettext("%d core", "%d cores", cpu_count) % cpu_count, temperature)
		return "%s %s MHz (%s)" % (processor, cpu_speed, ngettext("%d core", "%d cores", cpu_count) % cpu_count)
	except:
		return _("undefined")


# For modules that do "from About import about"
about = sys.modules[__name__]
