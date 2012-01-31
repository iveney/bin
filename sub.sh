#!/bin/bash

MOVIE_DIR=/Users/iveney/Movies
MOVIE_LIST=`mktemp -t movielist`
SSCL=/Users/iveney/bin/sscl
 
find -E $MOVIE_DIR  -iregex '.*\.(mkv|avi)$'|grep -iv sample >$MOVIE_LIST
 
while read movie_file_path
do
    movie_filename=`basename "$movie_file_path"`
    movie_path=`dirname "$movie_file_path"`
    if [ ! -e "${movie_file_path%.*}.chn.srt" ]
    then
        $SSCL --video-file "$movie_file_path" --pull >/dev/null 2>&1
        ls "$HOME/Library/Application Support/SPlayerX/SVPSub/${movie_filename%.*}.chn.srt" >/dev/null 2>&1 \
            && mv "$HOME/Library/Application Support/SPlayerX/SVPSub/${movie_filename%.*}".*.srt "$movie_path" \
            || echo $movie_file_path subtitle not found
    fi
done < $MOVIE_LIST
