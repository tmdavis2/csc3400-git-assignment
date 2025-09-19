## Branching strategy
#### Main
-Will contain all tested and files ready for release
-will only merge files in here using pull requests

### Feature Branches
-will contain in progress features 

### Hotfix Branches
-Used to patch issues from main branch 


## Commit Message Conventions 

we will add title of feature or release, and then a short description

title:description

## Code Review Process
-We will create pull requests for each new feature 
-One person will be designated to review the request(this will rotate)
-This person will test the code and ensure it works and document if any changes are made
-Once inspected, the reviewer will merge the request

## Release Workflow 
-will create feature branches from main
-once feature is completed, user will open a pull request
-once approved will be merged into main
-will then tag the release 
-hotfixes will be made as needed

## Common git Commands Reference 

### Branching 
- git switch (branch name) #change branches 
- git branch -b (branch name) #created branch
- git branch #displays all branches 

### Staging and Commiting 
- git add . #stages changes
- git commit -m "message" #commit with message

### Syncing
- git pull #updates local repository
- git push -u origin (branch) #pushes changes from local branch to remote