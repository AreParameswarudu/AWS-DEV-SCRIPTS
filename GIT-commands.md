# GITHUB

## 0. Initial setup for aws instance
Iam going to use AWS EC2 instance with RedHat linux machine to work with git.  
We can also go with local machine, or any other cloud providers as well.  

Instal gitbash or Launch RedHat EC2 instance and login

#### Initial steps to setup EC2 instance,  

> [!NOTE]
> If you are using local machine then no need of this setups.

This steps is only when you are using any instances from any Cloud services.

First elivate permissions to sudo.  
Set hostname  ( I am using gituser as name, you can choose as you wish).    
Reflect the changes

```
sudo -s
```
```
hostnamectl set-hostname gituser
```
```
sudo -i
```


**Chain of actions**.
<img width="1063" height="590" alt="image" src="https://github.com/user-attachments/assets/7320c4db-a83f-4c2c-86df-6677bfb097ec" />


# 1. Install git and verify the installation.

```
yum install git -y
```
```
git -v
```
```
git status
```
You get error, because this is not initialized yet.  

# 2. Initialize locally.
```
git init
```
Initialize git , this is local repo. .git directory will be create which contain files/dir maintained by git. The .git directory contains metadata and the entire history of the project,

```
git status
```

# 3. Create files or folders.

```
vi index.html
```
this is sample file.  
--> it has created locally, now move from working directory to staging area.  

```
git status
```
--> this is not tracked, Not tracked files shows in red color, if you want to track file move to staging area.  

--> following command is to move to staging area.
```
git add index.html
```

```
git status
```
--> now file is in staging area, tracked files shows green color, and now move to local repository


--> Lets commint the files, now file is in local repository
```
git commit -m "my first commit" index.html
```

what ever we do track, committing file etc will be in `.git` directory


# 4. Now time to commit to Remote Repo to GitHub

Sign up to GitHub and create a sample test public repository.  

---> copy this command from GitHub --> this will be done only first time. 
```
git remote add origin https://github.com/username/reponame.git
```
 

once above command executed , in `.git` folder, `cat config` file, remote origin got added --> show this file.  
```
git push -u origin main
```
--> this will be used to commit the changes from local to central repo.   


## Authenticating pull or push actions.
If any time asked for the authentication,  following things were asked.
```
git username:
git password or personal token [generate the token from github]
```

---> not to ask for the password every time
```
git config --global credential.helper cache
```

--> TO remove credentials
```
git credential-cache exit
```


```
git remote -v
```
-------------------------------------------------------------------------

-------------------------------------------------------------------------

### cleanup 

`rm -rf *`    --> to remove files from local dir.  
`git add .`	--> to add that changes to gitbash or local git repo.  
`git commit -m "clean" .`	--> adding the changes to remote repo.


This way the files form the remote repo can be deleted and cleaned.  

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

**Example**  
Now refresh the GitHub page and you can see the files.  

--> In Local, open `hello.txt` and add some content here.    
--> `git status` --> now you can see the file in red color which is modified, now you need to stage this file.  
--> `git add hello.txt` --> now you have stagged this file, if you want all the files to stage use.  
--> `git add --a`  
--> `git status` --> now this is green color, ready to commit  


--> `git commit -m 'modified hello.txt'` --> this is now committed to local repo, you need to push to central pro GitHub.  
--> `git push` --> no need to add origin, that is only for first time and also no need to add remote origin that is also for first time.  





--> now another example to create a file and add to staging and repo

```
touch hello.txt
```
```
git status
git add hello.txt
git commit -m "My second commit" hello.txt
git status
```


```
touch test.txt
```

```
git status
git add test.txt
git commit -m "My third commit" test.txt
git status
```

--> create mode 100644  means a normal file
--> 100755 means executable file

------------------------------------------
## got log

`git log` --> to see how many commits history.  
`git log --oneline` --> to see less lines.  
`git log --oneline -2` --> to see last 2 commits history.  
`git show` --> Show the changes of the last commit.  
`git show 150eb87` --> to see which file is committed for this id.  

`git log -p -2`  --> shows last 2 commits with diff.  
`git log --stat` --> summary of the changes. 

`git log    --pretty=oneline` --> to see less info about commit details in singleline.  
`git log --pretty=format:"%h-%an,%ar:%s"`   --> h = hash/commitnumber, an = authorname, ar = time, s = commit message.  
`git shortlog` --> Summarize git log output.  


## git blame
Create a file and add text to it.  
Add the file and commit it.  
Now you can use `git blame filename`  
```
vi index.html
this is first line
```

`git add index.html`  
`git commit -m "first line" index.html`  


`git blame index.html` --> Show **WHO** changed which line in a file.  

-------------------------------------

## git diff
--> modify index.html file
```
vi index.html
this is second line .. new line
```

`git add index.html`  
`git commit -m "new line" index.html`  

Now see the difference between the commits

```
git log --oneline -2
```
```
git diff 150eb87..1fg0e787
```
--> see the diff between commits


```
Vi index.html
This is the third line
```

------> compare changes working directory to staging area
```
git diff
```

```
git add index.html
```

--> compare changes staging to local repo
```
git diff --staged
```

commit the changes
```
git commit -m "comparison" index.html
```

```
vi index.html
change something
```
---> compare changes local directory to local repo [HEAD in caps]
```
git diff HEAD 
```
---------------------------------------------

git log  

--> you see root user in commit log --> in real time we should we our name not root

This is User Configuration  

git config user.name "reyaz"  
git config user.email "reyaz@gmail.com"  

git config user.name  [to see who is the user]  
git config user.email  


Another way of adding user configuration

`git config --list`  
`git config --global --edit`  
or  
`cd /root`  
`cat .gitconfig`  

vi index.html
added a new line

`git add index.html`  
`git commit -m "added new line" index.html`  

`git log --oneline --author='reyaz'`  --- this show only committed from certain person  
`git log --author="reyaz"`

--> now create a new file  
touch file1  
`git add file1`  
`git commit -m "file1 commit" file1`  
`git status`  
`git log`  
--> now we can see Reyaz username  


## git Amend  -- to Change the commit history

if you want to change the last commit history    
`git commit --amend -m "an updated commit message"`  --> this is replace latest commit message


## git rebase  -- to change multiple commit histories

Note: if you want to use this command, you need to have minimum 3 commits in your repo  

`git rebase -i HEAD~3`  

The option -i means interactive. HEAD~3 is a relative commit reference, which means the last 3 commits from the current branch HEAD.  

The git rebase command above will open your default text editor (Vim for example) in an interactive mode showing the last 3 commits  

Now replace pick with reword and keep changing the commit messages for 3 times and wq!  

`git log --oneline -2`  All commit messages has been changed

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


11 JUNE 2025      class missed 

Squashing in Git is the process of combining multiple commits into a single, consolidated commit. This is typically done to clean up the commit history before merging a feature branch into the main branch.

Create 4 commits
----------------
git log --oneline

abc123 Fourth commit
def456 Third commit
ghi789 Second commit
jkl012 First commit

if you want to combine second, third and fourth commits , put squash to third and fourth and have one commit which is second left

git rebase -i HEAD~3

output
----
pick abc123 Fourth commit
pick def456 Third commit
pick ghi789 Second commit

change
----
squash abc123 Fourth commit
squash def456 Third commit
pick  ghi789 Second commit

change: Combine or modify the commit message as needed.
-----
Combined commit: Second, Third, and Fourth changes

git rebase --continue

git log --oneline



## git checkout 
To restore previous version files in git  

Create a file `index.html` and add some content to it.  
commit those changes as well.  

`git add .`  
`git commit -m "version 1 commit" index.html`  

`vi index.html`  
```
This is version 1
This is version 2
```
again commit the changes.  

`git add .`  
`git commit -m "version 2 commit" index.html`

use the log cammand.  

`git log`   
or
`git log --oneline -2`  

`git show f86060a685535d6d68ecaa84f3d36e9f5d04814d:index.html`  

This will show first version file.  

If you want to restore previous version files,  

`git checkout f86060a685535d6d68ecaa84f3d36e9f5d04814d -- *`   --> * will restore all files in that commit.  

`git checkout f86060a685535d6d68ecaa84f3d36e9f5d04814d -- index.html` --> It will restore only index.html  

`cat index.html`  

Again if you want latest, 

`git checkout master -- index.html` --> it will restore to v2

`git checkout master -- *`  --> coming back to latest file.  



cat index.html

Another scenario of checkout
---------------------------
use git rm to remove the file and restore using checkout HEAD

vi test.html
this is test

git add test
git commit -m "test" test.html

git rm test.html                       --> this will remove the file

git checkout HEAD -- test.html         ---> this will restore the file

======================================================
GIT RESTORE :
git checkout and git restore does the same work: reverting to previous state

Scenario 1: if you want to undo change after saving and before commit
----------

How to undo changes after save. If you are working on latest file, you do changes and saved. If you want previous one
use git restore index.html

vi test.html
This is demo

git add .
git commit -m "test" test.html

vi test.html
This is demo
ajffjkdhgdkjghdf
save it

cat test.html

if you want now to restore

git restore test.html

cat test.html

=================================
 Scenario 2 = To restore files from stagged to unstage

Accidently you have added to stage using "git add" command and if you want to unstage or untrack

How to untrack files

vi test.html
This is devops demo

git add test.html
git status --> now accidently i have stagged or tracked test.html , but I want to untrack/unstage

git restore --staged test.html
(or)
git restore --staged . -->  [. all]
(or)
git rm --cached test.html --> same like restore command above but another command to untrack/unstage

git status --> you can see now untracked

git add test.html  --> Add it to the stage again

git commit -m "test" test.html

Scenario - 3 : If you accidently delete the file from your directory and want to get back
--------------

touch newfile
git add newfile
git status ---> it shows green color, it is stagged

git add newfile  ----> now stage it

rm -rf newfile  -----> delete the file locally

ls  ---> no local file

git restore newfile   --> this will help to get the deleted file back from stage to local machine

git status

git commit -m "newfile" newfile



## git reset 
Uncommit last commit.   
if you committed accidentally and want to uncommit or come the file back to local repo to staging.  
or  
Unstage files that were mistakenly added to the staging area.

```
vi file.txt
Welcome to DevOps Classes
git add Reyaz.html
git commit -m "reyaz" Reyaz.html
```


```
vi file.txt
Welcome to DevOps Classes
ijkdfhgdkfghdkjfhgjdfhg
```

`git add file.txt`  
`git commit -m "first commit" file.txt`  

oh shit, i commit wrong code,   
Accidentally you commited now, but you want to get it back from local repo to staging.  

`git status` -->  all clean, nothing to commit.  

`git reset --soft HEAD^`   --> uncommit and keep the changes / bring back from local repo to stage.  

`git status`  --> we see file.txt now in stage.

again git add file.txt.  
`git commit -m "first commit" file.txt`  
now try  below.  

`git reset --hard HEAD^`   --> uncommit and discard the changes.  
`cat file.txt`  


| Feature       |             git restore              |              git reset		|
---------------| -------------------------------------| ---------------------------------------|
| Scope       	|   Working directory or staging area     |      Commit history, staging area, working directory |
| Affects Commit History     |              No              |                      Yes (can modify HEAD) |
| Primary Use Case	|    Undo changes or unstage files  |  Move HEAD or reset state to a previous commit |
| Safety                 |       Less destructive            |   Can be destructive, especially with --hard |



HEAD is a pointer to the current branch or commit you are working on.  
In Git, HEAD is a source to the current branch or commit you are working on. HEAD normally shows the recent commit of the current branch and moves when you switch branches or check out exact commits.  

**git Restore**: Does not modify commit history or the repository's HEAD pointer. It only reverts changes in the working directory or staging area.  

**git reset**:  Can modify commit history by moving the HEAD pointer and potentially discarding changes.  



## git stach  
If you want to hide/park all the changes you did on the repo locally to a tmp place and proceed with another story changes then stash the old story.  
The git stash command is a useful feature in Git that allows you to temporarily save changes in your working directory without committing them



Now create a story1 file
------------------------
vi story1
 i am working on story 1
 very difficult task
 it task 2 hours time

--> Now suddenly manager called and asked to work on story2

git status
git add story1

git stash --> story1 will be removed from the working dir, do ls, it will be placed in tmp location

ls -- story1 file is not there

git status --> working tree clean

using stash we kept story 1 aside

Now create story2 file
---------------------
vi story2
i need to complete this story2 first

git status
git add story2
git commit -m "story2" story2

git status

Now lets work back on story1
----------------------------

git stash apply --> now restore do ls
ls
git status -> you can see the file again

git stash list -- it will list the stashes
git stash clear -- it will clear the stash


if you want to stash multiple files

git stash push -m "commit message" -- story1 story2
git status


=========================================================

rm -rf *



Lets try again  

--> modify another file test.txt  
--> git status  
--> git add test.txt  

If you want to un-stage existing file use RESET command.  
if you want already added file to un-stage use reset command , for brand new file use rm command (difference rm - brand new file to un-stage , reset - existing file to un-stage)  

git reset HEAD <filename>

git add .

-Now, redo what ever you have modified in the file

--> git commit -m 'modified test'
--> git push


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Branch Concept
======================
keep the master branch clean first

If you dont have any single commit, it will not show the branch. Once you do 1 commit, it shows master branch

touch index.html
git add index.html
git commit -m "index commit" index.html
git status
git branch --> it will show the branch master, default branch

if you commit at least 1 file, it will show the master branch

Its not good to work everyone on master branch, individual developer create their own branch

dev1branch
==========
	git branch dev1branch	  --> it will create a new branch dev1branch from master
	git branch				  --> to list the branches, * represent the current branch
	git checkout dev1branch	  --> to switch branch
	git branch
	touch dev1file{1..5}
	git add dev1file*
	git commit -m "dev1" dev1file*

dev1branch has 1 + 5 files = 6 (it got 1 file from master)

dev2branch
==========
	git branch dev2branch --> this will create a new branch dev2branch from dev1branch as we are now in dev1branch
	git branch
	git checkout dev2branch
	git branch
	touch dev2file{1..5}
	git add dev2*
	git commit -m "dev2 commit" dev2*

dev2branch has 1 + 5 + 5 = 11

dev3branch
===========
	git branch
	git branch dev3branch --> this will create a new branch from dev2branch
	git checkout dev3branch
              or
              git checkout -b dev3branch --> this will also create and checkout branch dev3branch, 2 commands in 1 shot
	git branch
	touch dev3file{1..5}
	git add dev3*
	git commit -m "dev3 commit" dev3*
	
dev3branch has 11 + 5= 16

dev4branch
===========
	Now i want to create a new branch from master not from dev3

	Now I want to checkout from master not from dev3 , so first checkout to master and create a branch, it will get only

	git branch
	git checkout master
	ls
	git branch dev4branch
	git checkout dev4branch
	ls

	ls --> it should list only index.html
	touch dev4file{1..5}
	git add dev4*
	git commit -m "dev4 commit" dev4*

dev4branch has 1 + 5 = 6


**** rename branch

git branch -m dev5branch devnewbranch  [renaming dev5branch to devnewbranch]

=======================
GIT MERGE - Merge between 2 branches
======================

git branch
be in master

git checkout master

git merge dev1branch  --- what ever we have files in dev1branch will come to master

Now push to GitHub, create a GitHub account
========================================
git branch

git remote add origin https://github.com/ReyazShaik/testrepo.git

git config --global credential.helper cache  


git push origin master --> push the code of master to GitHub
username:
password: paste the token here
GitHub removed password authentication and put token system for better security
Generate token from GitHub
Profile --> settings --> developer settings --> personal access token --> classic -->
Generate new token --> classic --> name:gitlearn --> select repo scopes --> generate

Now push dev1branch files

git push origin dev1branch --> now see 2 branches in GitHub
git push origin dev2branch --> now see 3 branches in GitHub
git push origin dev3branch --> now see 4 branches in GitHub
git push origin dev4branch --> now see 5 branches in GitHub

=======================
GIT MERGE - Merge between 2 branches
======================

git branch

git checkout dev2branch -- see the files

git checkout dev1branch -- see the files

git merge dev2branch  --- what ever we have files in dev2branch will come to dev1branch

another command instead merge use rebase

git rebase dev4branch

Git Merge: Keeps the history intact and is safer for shared branches. Ideal for collaborative projects.
Git Rebase: Rewrites history for a cleaner, linear commit log. Best suited for private or feature branches.

======================
GIT REVERT -- accidental merges from one branch to another branch and undo those

git branch

git merge dev2branch

ls

git revert dev2branch --> this will delete the files from current branch which was merged
(don't to any changes to file, just quit the file)

========================
GIT BRANCH another example
=========================

--> Create one test repo in GitHub


mkdir branchdemo
cd branchdemo
git init
touch python{1..10}

vi python1
This is python1
nice code. log code
 
git add .
git commit -m "pythonfiles" .

git branch

== what ever we are doing is in master branch
== A new developer came and said i will do some changes, is it good to do directly in master?
== create a new branch for developer

git branch developer
git branch
git checkout developer

vi python11
This is python11

vi python1
added new lines

git add .

git commit -m "pythonfilesnew added" .

== No impact on master branch
== Now lets go to master branch and see the data

git checkout master

ls

== Here we dont have python11 and python1 changes

if i want developer changes to master

git merge developer  [merging code from developer branch]

git remote add origin https://github.com/ReyazShaik/branching.git

Note: if you want to change remote origin " git remote set-url origin https://github.com/ReyazShaik/branching.git&quot;

git push -u origin master

== Now see in GitHub, but you can see only one branch in GitHub because we pushed from master, GitHub dosent know developer branch yet

git checkout developer
vi python1
added worst code
version 1.2.3

git add .

git commit -m "pythonfilesnew added" .

git push origin developer [we need to push from developer branch]

== Now in GitHub, you get Compare and Pull Request --> Merge Request
== After merging master branch contains the code of Developer branch

In your terminal, if you want to get latest code from GitHub

git checkout master

git pull


git merge
========

git checkout developer
vi python1
version 1.2.3.4

git add .
git commit -m "1.2.3.4" python1

git checkout master
vi python1
version 1.2.3.4.5

git add .
git commit -m "1.2.3.4.5" python1

git merge developer
-- merge conflit

vi python1

remove which ever you need, we can commit only 1
save it

git add python1
git commit --> no need to put filename

merge file will come , just wq!

git status




=======================
GIT REBASE - same as MERGE
=======================

git rebase dev3branch -- now you see dev3 also in dev1branch

==========================

MERGE vs REBASE

Merge for public repos, rebase for Private
Merge stores history, rebase will not store the entire history (commits)
merge will show files, rebase will not show files


====================================

========================
GIT CLONE -- download remote repo to local
======================

Now delete the local directory gitproject and clone from GitHub

rm -rf gitproject

git clone https://github.com/ReyazShaik/branching.git
ls
cd branching
git checkout master
ls
git checkout dev1branch
ls
git checkout dev2branch
ls


=================================
 Another Example = MERGE CONFLIT - when we merge 2 branches with same files
===============================

mkdir abcd
cd abcd
git init

vi index.html
I am dev1 writing java on branch-1
git add index.html
git commit -m "dev1-commits" index.html

git branch

git branch -m master branch1 --> renaming master to branch1 (just for clarity)

git branch

git checkout -b branch2 --> this will create a new branch from master

vi index.html
I am dev2 writing python on branch-2
git add index.html
git commit -m "dev2-commits" index.html

git branch
*branch2
cat index.html

git checkout branch1
ls
cat index.html
vi index.html
add some line
git add index.html
git commit -m "dev1-newline-commits" index.html

Now in both branches we have same index.html --> see files ,

git merge branch2 -> error: conflit

git diff index.html

cat index.html

--- Now resolve conflit manually by developer, because he know what can be kept and removed

vi index.html
delete dev2 code
git add index.html
git commit -m "new-commits" [dont give filename]
git status

======================
GIT Conflit - Example - latest
=====================

mkdir git-conflict-demo

cd git-conflict-demo

git init

vi file.txt
"Hello World"

git add file.txt

git commit -m "Initial commit"


Create a new branch and switch to it:
------------------------------------

git checkout -b feature-branch

vi file.txt
Hello from feature branch

git commit -am "Update file.txt in feature-branch"


Switch back to the master branch:
-----------------------------
git checkout master

vi file.txt
Hello from master branch

git commit -am "Update file.txt in main"


Try merging feature-branch into master:
-----------------------------------

git merge feature-branch

Git detects a conflict:

Automatic merge failed; fix conflicts and then commit the result.

🔹 Step 4: Resolve the Conflict
-------------------------------
Open file.txt, and you will see:

<<<<<<< HEAD
Hello from main branch
=======
Hello from feature branch
>>>>>>> feature-branch

Manually edit the file to keep the correct version:

git add file.txt

git commit -m "Resolved merge conflict"

🔹 Step 5: Verify the Merge
----------------------------

Check the commit history to confirm the conflict resolution:


git log --oneline --graph --all

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

=======================
GIT FORK - same as clone (remote to local) but fork (download code from one GitHub account to another GitHub account)
=====================

= If i want to enhance the code of another guy who has his own repo and code, instead me doing changes in his account directly i will fork it in my GitHub repo and do changes



In GitHub browser - search for another GitHub account(https://github.com/ReyazShaik/test) and fork to my account(trainerreyaz account)

GIT FORK and GIT CLONE -- Both repos should be public, for private use token

you cannot unfork, you  need to delete the repo



PR - PULL REQUEST
---------------

Be in trainerreyaz account and add or modify python1 file and commit

--> contribute --> pull request --> Finish
--> Go to actual reyazshaik GitHub account --> on top --> pull requests --> Click on Request and Merge

-- Again go to trainerreyaz account modify the file --> save --> contribute --> Create pull request

-- Come to reyazshaik account --> pull requests --> see what exactly code change is --> click on commits --> REview changes --> Add comment --> i dont like --> close the request


Sqaush and merge : combining the commits history
Use squash and merge for branches with many small or work-in-progress commits to keep the history clean.

Squash and Merge is a method used during the pull request (PR) or branch merging process to combine all the commits from a feature branch into a single commit on the target branch. This is particularly useful for maintaining a clean and concise commit history.

Rebase and Merge :  Retains individual commits


======================
PR - Pull Request
=======================

Everything what we did on git, now its do on GitHub

merge, rebase etc we did on git(local),

TO merge in github use PR

MERGE ON GITHUB - PR should be done on GitHub - from one branch to another branch

create a repo in GitHub and add a file in master branch...

create another branch test and add a file

Now create a PR

In GitHub on top --> Pull request --> New Pull Request --> select branches from where to where (test to master) --> see differences  --> Create Pull request --> pull request --> Merge pull request and confirm

Now code merges from branch to master


====================
Rename the Branch Name - GIT
=====================

touch python{1..5}

git add .

git commit -m "python" .

git branch dev1branch

git branch -m dev1branch testbranch

git checkout testbranch

touch java{1..5}

git add .

git commit -m "java" .


create a repo and push the files and branch

git remote add origin https://github.com/ReyazShaik/branching.git

git push origin master
git push origin testbranch

create a pull request and merge in GitHub

===============
GIT REVERT in GITHUB
=============
select View all branches in branch section --> which branch you want to revert --> select that branch --> Click PR and revert
-> it will create a revertbranch and revert



=======
git clean : delete untrack files

create a file and dont track
git clean -n filename  -- first git will ask
git clean -f filename  -- delete without asking



=========================
CHERRY PICK - Merging the specific files based on commits
========================
mkdir Reyaz
cd Reyaz
git init

touch file1
git add file1
git commit -m "file1" file1

git branch

git branch -m master branch1  [Rename master branch to branch1 for clarity]

git checkout -b branch2  [create branch2]

git checkout branch1  [be in branch1]

touch java{1..5}
git add java*
git commit -m "javafiles" java*

touch python{1..5}
git add python*
git commit -m "pythonfiles" python*

touch php{1..5}
git add php*
git commit -m "phpfiles" php*

to see how many commits
--------
git log --oneline
ls

git checkout branch2 [switch to branch2, in this branch we have only one file]

i want to merge branch2 with branch1 we use git merge,  but i dont want all files, i need only few [cherry pick]

git cherry-pick commit-id

git cherry-pick 16dufg(pythonfiles)
git cherry-pick 13gh56g(phpfiles)
ls

Now, this merge only pythonfiles and phpfiles

if you want to revert -- git revert commit-id

GIT TAG - For reference
====== =
git log --oneline

git tag tagname commitid

example:  git tag dev/prod 0620179

git log --oneline

=========================
GIT IGNORE - if you don't want to track the file, add filename in .gitignore
========================

In Same directory

touch file1.txt
touch file2.txt
git status
-- If I don't want to track
vi .gitignore
file1.txt

-- git status --- cant see file1

================
Delete Branch in GIT
==================
- git branch -D branchname
To get Branch restore - git checkout branchname
git branch

Restore deleted branch in GIT
===========================

git reflog

git checkout -b dev 3e98e1c(commitid)

Be in deleted branch and ls

=====================
Host website on GitHub
=====================

Create a repo and create index.html --> put some html code

setting --> pages --> branch master --> /root --> save --> you get the link



=================
MAKE REPO Public to Private in GitHub --> Repo settings --> danger zone --> change visibility
=================


===================
Delete branch in GitHub
================
view branches --> delete icon -- undo there itself -- rename the branch also there


===========================================
HOW to add multiple developers to GitHub
============================================
In GitHub --> Repo --> Settings --> Collaborators --> Add people

Like Kanban board --

Create a Project --> Select Table --> Create Task --> press tab --> and fields and assign people(tasks, assignees, start date, enddate)

Go to Project Settings --> Manage access --> give permissions
