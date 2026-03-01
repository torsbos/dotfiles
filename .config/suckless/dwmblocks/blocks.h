//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		                    /*Update Interval*/	/*Update Signal*/
	{"",  "wpctl status -n | grep alsa_output | awk '{print $7 }' | sed s/\]//",   5,   0},
	{"",  "exec /usr/local/bin/bat",   5,   1},
	{"",  "date '+%d/%m (%a) %R'",   1,    2},
};

//sets delimiter between status commands. NULL character ('\0') means no delimiter.
static char delim[] = " | ";
static unsigned int delimLen = 5;
