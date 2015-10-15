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
	_title=$(echo -e $_title | tr '[:upper:]' '[:lower:]')
	_title=$(echo -e $_title | tr -cd '[[:alnum:]]._-')
	echo -e "$_title"
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
	echo "  -p, --post     moves a file from _drafts/ to _posts/"
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

# Move Posts
function fnPost {
	local _moveFile="$1"
	if [[ "$_moveFile" == "." ]]; then
		mv .$_draftPath* .$_postPath
	elif [[ "$_moveFile" != "" ]]; then
		echo "Moving $1 to post..."
		if [ -e ".$_draftPath$_moveFile" ]; then
			mv -f .$_draftPath$_moveFile .$_postPath$_moveFile
			echo -e "Now at $_postPath$_moveFile"
		else
			echo "ERROR: Unable to find draft '$_moveFile'"
			exit 1
		fi
	else
		echo "  Error: No file specified to move"
		echo ""
		exit 1
	fi
}

# New Post
function fnNew {
	echo "Creating new post..."
	local _title="$1"
	local _kind="$2"
	local _path="$_draftPath"

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
		echo -e "articles:" >> ".$_outputFile"
		local _num_links="$2"
		if [[ "$_num_links" != "" ]]; then
			while [ $_num_links -lt 10 ]
			do
			   echo -e " - title:\n   author:\n   source:\n   url:" >> ".$_outputFile"
			   _num_links=`expr $_num_links + 1`
			done
		else 
			echo -e " - title:\n   author:\n   source:\n   url:" >> ".$_outputFile"
		fi
	fi

	case "$_kind" in
		"") 
			echo "layout: post" >> ".$_outputFile"
			echo "category: articles" >> ".$_outputFile"
	    ;;
	    "--project") 
			echo "layout: post" >> ".$_outputFile"
			echo "category: projects	" >> ".$_outputFile"
	    ;;
	esac

	echo "---" >> ".$_outputFile"
	# echo -e "\n\n$_excerptSeparator\n" >> ".$_outputFile"
}


# Process command line# Parse options
case "$1" in
	-n)
		fnNew "$2" "$3" "$4"
		;;
	--new)
		fnNew "$2" "$3" "$4"
		;;
	-p)
		fnPost "$2" "$3" "$4"
		;;
	--post)
		fnPost "$2" "$3" "$4"
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