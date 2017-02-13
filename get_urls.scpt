set theURLs to {}
set end of theURLs to "---"
set end of theURLs to "title: Links - " & (do shell script "date \"+%B %d, %Y\"")
set end of theURLs to "layout: links"
set end of theURLs to "category: links"
set end of theURLs to "articles:"
tell application "Google Chrome"
	tell window 1
		set i to 1
		repeat until i > (count of tabs)
			set end of theURLs to "  - title: " & (title of tab i)
			set end of theURLs to "    author:"
			set end of theURLs to "    source:"
			set end of theURLs to "    url: " & (URL of tab i)
			set end of theURLs to "    tags:"
			set end of theURLs to "        - "
			set i to i + 1
		end repeat
	end tell
end tell
set end of theURLs to "---"

-- Copy the URLs to the clipboard, one per line.
set oldDelims to AppleScript's text item delimiters
set AppleScript's text item delimiters to (ASCII character 10)
set the clipboard to theURLs as text
set AppleScript's text item delimiters to oldDelims
