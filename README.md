# Python Repo

1. To-do Scripts
	* One way sync script between /WorldEdit/Schematics from Vanilla -> Creative on 5min cron job
	* Offload old Schematics (60+ days) to remote FTP backup and add entry to /SavedSchematics.php on website
	* Class to push updates to different channels at asov.slack.com
	* Whitelist sync from Vanilla -> Creative
	* Update /AScoopOfVanilla/ASOV/WhitelistMaint.py to remove old users (30/60/90) from whitelist.
	* Hidden Achievements sidebar update via PRAW.
	* Online players on Sidebar via PRAW & RCON.
	* Change consle chat to python and enable direct messaging and console commands.
	* Console Chat
	* Prism purge remediation
	* Test
---

# Console Chat Scripts
	* Enable chat to the following:
		- All Users
		- ModChat
		- Direct Message (/tell)
		- Commands

	* Features:
		- Notify server upon connect ('Kazra has connected to the console')
		- Nofify on leave ('Kazra has disconnected from the console')
		- Quiet arg to not notify for that session
