#!/bin/env zsh

# Import settings from env.sh
source env.sh

function urlencode {
  echo "$1" | nkf -WwMQ | sed 's/=$//g' | tr = % | tr -d '\n'
}

query=$1
queryEncoded=$(urlencode $query)

searchresult=$(curl -s "https://scrapbox.io/api/pages/${projectName}/search/query?q=${queryEncoded}" -H "Cookie: connect.sid=${scrapboxToken}")

pagetitle=$(echo $searchresult | jq -r '.pages[] | .title' | fzf)
pagetitleEncoded=$(urlencode $pagetitle)

pageinfo=$(curl -s "https://scrapbox.io/api/pages/${projectName}/${pagetitleEncoded}" -H "Cookie: connect.sid=${scrapboxToken}")

url=$(echo $pageinfo | jq -r '.descriptions[]' | grep "http" | head -n 1 | sed 's/^\[\(http[^ <]*\)\(.*\)/\1/g')

# echo "${pagetitle}"
echo "${url}"
