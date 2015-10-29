#/bin/bash
#----------------------------------------
# bloggist - Avy's take at simplifying jbh
_version="0.0.1"
# JBH: http://github.com/alanbarber/jbh
# me: http://github.com/alanbarber/jbh
#----------------------------------------
# Settings
# Note: Always set leading and trailing slashes in path! Paths are relative.

_sitePath="/_site/"	
_postPath="/_posts/"
_draftPath="/_drafts/"


########################################
# DO NOT EDIT BELOW THIS LINE
########################################
# Helper Function
function fnConvertTitleToFilenameFormat {
	# lowercase, remove non alphanumerics and non spaces, convert spaces to dash
	local _title=$(echo $1 | tr " _" "-")
	_title=$(echo $_title | tr '[:upper:]' '[:lower:]')
	_title=$(echo $_title | tr -cd '[[:alnum:]]._-')
	echo "$_title"
}
function fnGetFileName { 
	local _title=$(fnConvertTitleToFilenameFormat "$1")
	local _date=$(date +%Y-%m-%d)
	echo "$_date-$_title.md"

}

# Feature Functions
# Version
function fnVersion {
	echo "Jekyll Blog Helper $_version"
	echo "Report bugs to <github.com/alanbarber/jbh>"
	echo ""
}
# Help Info
function fnHelpInfo {
	echo "Usage: jbh.sh [OPTIONS]..."
	echo "Jekyll Blog Helper $_version - A command line blog management tool"
	echo ""
	echo "Options:"
	echo ""
	echo "  -n, --new      creates a new post or draft"
	echo "  -v, --version  displays version of the script"
	echo ""
	echo "Examples:"
	echo ""
	echo "  jbh.sh --new \"Blog title\""
	echo "    Creates a new post with the given title"
	echo ""
	echo "  jbh.sh --new \"Blog title\" \"1/1/2015\""
	echo "    Create a new post on a specific date"
	echo ""
	echo "  jbh.sh --new --draft \"Blog title\""
	echo "    Creates a new draft post with the given title"
	echo ""
}

# New Post
function fnNew {
	echo "Creating new post..."
	local _title="$1"
	local _kind="$2"
	local _path="$_postPath"

	local _fileName=$(fnGetFileName "$_title")
	local _outputFile="$_path$_fileName"

	# Create file and write Jekyll header info
	echo "  Creating file '$_fileName'"

	echo "---" > ".$_outputFile"
	if [[ "$_title" == "links" ]]; then
		echo "title: Links - $(date "+%B %d, %Y")" >> ".$_outputFile"
	else
		echo "title: \"$_title\"" >> ".$_outputFile"
	fi

	echo "main_image: " >> ".$_outputFile"
	echo "description: " >> ".$_outputFile"	
	echo "tags: []" >> ".$_outputFile"

	if [[ "$_title" == "links" ]]; then
		echo "layout: links" >> ".$_outputFile"
		echo "category: links" >> ".$_outputFile"
		echo "articles:" >> ".$_outputFile"
		local _num_links="$2"
		if [[ "$_num_links" != "" ]]; then
			while [ $_num_links -lt 10 ]
			do
			   echo " - title:\n   author:\n   source:\n   url:" >> ".$_outputFile"
			   _num_links=`expr $_num_links + 1`
			done
		else 
			echo " - title:\n   author:\n   source:\n   url:" >> ".$_outputFile"
		fi
	fi

	case "$_kind" in
		"") 
			echo "layout: post" >> ".$_outputFile"
			echo "category: drafts" >> ".$_outputFile"
	    ;;
	    "--project") 
			echo "layout: post" >> ".$_outputFile"
			echo "category: projects" >> ".$_outputFile"
	    ;;
	esac

	echo "---" >> ".$_outputFile"
	# echo "\n\n$_excerptSeparator\n" >> ".$_outputFile"
}


# Process command line# Parse options
case "$1" in
	-n)
		fnNew "$2" "$3" "$4"
		;;
	--new)
		fnNew "$2" "$3" "$4"
		;;
	-v)
		fnVersion
		;;
	--version)
		fnVersion
		;;
	*)
		fnHelpInfo
		;;
esac
exit 0