from RoRCheker import *
import requests
import sys
import ConfigParser
import logging
import argparse

settingsFile=ConfigParser.ConfigParser()
settingsFile.read("SETTINGS")

parser = argparse.ArgumentParser(description=settingsFile.get('GENERAL','description'))

parser.add_argument(
	'-t',
	'--timeout', 
	help='checkers timout in seconds',
	required=False
	)

parser.add_argument(
	'-w', 
	'--use_weight',
	help='use plugins weight',
	action='store_true',
	required=False)

parser.add_argument(
	'-v', 
	'--verbose',
	help='use this function to debug',
	action='store_true',
	required=False)

requiredArgs = parser.add_argument_group('required named arguments')

requiredArgs.add_argument(
	'-u',
	'--urls',
	help='URLs comma separated list',
	required=True)

args = parser.parse_args()

#show logs in verbose mode
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

#retrieve optional parameters from SETTINGS if they were not defined
if args.use_weight==False:
	if settingsFile.get('GENERAL','use_weight').lower()=="true":
		UseWeight=True
	else:
		UseWeight=False
else:
	UseWeight=True

if args.timeout==None:
	timeout=float(settingsFile.get('GENERAL','timeout'))
else:
	timeout=float(args.timeout)

#check each URL with all the plugins
for URL in args.urls.split(","):

	print "\n----------------------------------- Checking "+URL

	logging.debug(" Scripts arguments")
	logging.debug("======== URL:"+str(URL))
	logging.debug("======== UseWeight:"+str(UseWeight))
	logging.debug("======== timeout:"+str(timeout))


	#get plugins
	PluginConfig = ConfigParser.ConfigParser()
	PluginConfig.read("PLUGINS.conf")
	plugins=PluginConfig.sections()

	GlobalScore=0
	TotalWeight=0

	for plugin in plugins:
		
		CheckerInstance=RoRCheker(plugin,PluginConfig.get(plugin,'weight'),PluginConfig.get(plugin,'lang'),PluginConfig.get(plugin,'code'),timeout)

		score=int(CheckerInstance.check(URL))

		#this will be displayed only in verbose mode 
		logging.debug(("\n\n====================== Testing "+plugin))
		logging.debug(CheckerInstance.getCMD())
		logging.debug(CheckerInstance.getOutput())
		logging.debug(("\n======================"))
		
		if UseWeight:
			score=score*int(CheckerInstance.weight)
			TotalWeight=TotalWeight+float(CheckerInstance.weight)
			
		GlobalScore=GlobalScore+score
		print CheckerInstance.name+"\t\t"+str(score)

	if UseWeight:
		print "\nGlobal Score\t\t"+str(GlobalScore)+"/"+str(int(TotalWeight))
		print "RoR website percent rate is "+str(round(GlobalScore*100/TotalWeight,2))+"%"
	else:
		print "\nGlobal Score\t\t"+str(GlobalScore)+"/"+str(len(plugins))
		print "RoR website percent rate is "+str(round(GlobalScore*100/len(plugins),2))+"%"



