use scripting additions
use framework "Foundation"

tell application "Firefox" to activate

set urls to {}
set cur_out to {}
set end of cur_out to "---"
set end of cur_out to "title: Links - " & (do shell script "date \"+%B %d, %Y\"")
set end of cur_out to "layout: links"
set end of cur_out to "category: links"
set end of cur_out to "articles:"
set the_title to ""
set the_url to ""

repeat
	-- get the tab the_title from FF
	tell application "System Events" to tell process "Firefox"
		set frontmost to true
		set the_title to name of windows's item 1
	end tell

	set thePasteboard to current application's NSPasteboard's generalPasteboard()
	set theCount to thePasteboard's changeCount()

	-- send cmd+l and cmd+c keystrokes to FF to highlight and copy the URL
	tell application "System Events"
		keystroke "lc" using {command down}
	end tell

	-- wait for the clipboard content change to have been detected
	repeat 20 times
		if thePasteboard's changeCount() is not theCount then exit repeat
		delay 0.01
	end repeat

	-- get the clipboard contents
	set the_url to the clipboard
	if the_url is in urls then exit repeat
	set end of urls to the_url

	set end of cur_out to "  - title: " & the_title
	set end of cur_out to "    author:"
	set end of cur_out to "    source:"
	set end of cur_out to "    note:"
	set end of cur_out to "    url: " & the_url
	set end of cur_out to "    tags:"
	set end of cur_out to "        - "

	tell application "System Events"
		keystroke tab using control down
	end tell
end repeat
set end of cur_out to "---"

tell application "Terminal" to activate

-- Copy the URLs to the clipboard, one per line.
set oldDelims to AppleScript's text item delimiters
set AppleScript's text item delimiters to (ASCII character 10)
set the clipboard to cur_out as text
set AppleScript's text item delimiters to oldDelims
