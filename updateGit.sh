#!/bin/bash

# update branch to github account
# and merge it with master branch
# then create a new branch to 
# continue 

old="$1"
new=$((old+1))

# double check pushing to correct branch
# doesnt push automaticallly since
# still have to input username and password

git branch
git add .
git commit -m "$2"
git push

git checkout master
git pull origin master
git merge "ch$old"
git push origin master

git checkout -b "ch$new"
git push -u origin "ch$new"
