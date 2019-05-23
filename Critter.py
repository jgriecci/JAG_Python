# Simple Critter
# Demostrates a basic class and object
# Joseph Griecci - 8/24/2015

class Critter(object):
	""" A virtual pet"""
	def talk(self):
		print "Hi, I'm an instance of class Critter."
		
# main
crit = Critter()
crit.talk()

raw_input("\n\nPress the enter key to exit.")