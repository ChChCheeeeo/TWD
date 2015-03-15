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
git push

git checkout master
git pull origin master
git merge "$old"
git push origin master

git checkout -b "$new"
git push -u origin "$new"
