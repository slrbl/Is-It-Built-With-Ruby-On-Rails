import requests
import commands

class RoRCheker(object):

	def __init__(self,name,weight,lang,heuristic,timeout):
		self.name =name
		self.weight=weight
		self.lang=lang
		self.heuristic=heuristic
		self.timeout=timeout

	def check(self,url):
		cmd=self.lang+" "+self.heuristic+" "+url+" "+str(self.timeout)
		cmdResult=commands.getstatusoutput(cmd)
		self.cmd=cmd
		self.output=cmdResult[1]
		if cmdResult[0]==0:
			return 1
		else:
			return 0

	def getCMD(self):
		return self.cmd

	def getOutput(self):
		return self.output
