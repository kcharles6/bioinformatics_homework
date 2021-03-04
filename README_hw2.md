# bioinformatics_homework
#### HOMEWORK 2: REPOSITORY CREATION
### I did this several different ways, because I apparently screwed it up the first time.

### To create this repository I took the directory on my computer called bioinformatics_homework which contained the homework files, then 
### initialized it as a github repository using git init, followed by git add to stage the files for commit
$ git init bioinformatics_homework
$ git add . ###adds both readme file and homework1 file to git staging area 
$ git commit -m "first commit" ###commits files with message "first commit"

### connect local repository to remote repository on github.com
$ git remote add origin https://github.com/kcharles6/bioinformatics_homework.git   

### push local files to remote 
$ git push origin main 

### at some point after this I was having trouble pushing files to github
## I then made the mistake of trying to re-clone the folder on github into my local repository in order to sync them, thus
## creating two repositories of the same name nested within another on my local computer. 
## I was no longer able to push files from the original local repository for some reason, so to avoid any additional confusion,
## I ended up moving the homework files into my main bioinformatics folder using mv,  deleting both the local repositories using rmdir, 
## then cloning the github folder again and moving the files back into it. this is what this looked like: 

$ rmdir bioinformatics_folder/bioinformatics_folder
$ rmdir bioinformatics_folder
$ git clone https://github.com/kcharles6/bioinformatics_homework
$ cd bioinformatics_homework
$ git pull origin main
$ mv readme_homework2.md readme_hw2.md
$ git add readme_hw2.md
$ git commit "This better work"
$ git push origin main 

## Git clone clones remote repository to local directory, 
## Pull files from remote directory using git pull to ensure no conflicts,
## mv moves homework 2 file into new cloned working directory and renames it
## git add stages homework for commit
## git push origin main pushes homework to remote repository


