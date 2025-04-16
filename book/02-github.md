# Chapter 2

## What is Github?

Where you store code. But more than just that.


## Saving to Github
First create `.gitignore` file. This is to specify which files shouldn't be uploaded into github

Add the following into the `.gitignore` file.

```
venv*
test*
```

We add an asterisk (*) to specify any file that begins with those letters shouldn't be pushed to Github.

Then create a repository in Github. I named mine `my_django`.

The follow these commands

1. `git init` - initialize git in your local repository

It should print out the following text.

```
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/sammigachuhi/my_django/.git/
```

2. `git add .` - the shortcut `(.)` adds everything. You can also specify files or folders.

3. `git commit -m "starting my first django project"` - write the message that explains what you did. It will be visible in Github.

It will print out this:

```
[master (root-commit) f87af2e] starting my first django project
 17 files changed, 332 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 book/01-installing.md
 create mode 100644 requirements.txt
 create mode 100644 sanitation/australia/__init__.py
 create mode 100644 sanitation/australia/admin.py
 create mode 100644 sanitation/australia/apps.py
 create mode 100644 sanitation/australia/migrations/__init__.py
 create mode 100644 sanitation/australia/models.py
 create mode 100644 sanitation/australia/views.py
 create mode 100755 sanitation/manage.py
 create mode 100644 sanitation/sanitation/__init__.py
 create mode 100644 sanitation/sanitation/__pycache__/__init__.cpython-310.pyc
 create mode 100644 sanitation/sanitation/__pycache__/settings.cpython-310.pyc
 create mode 100644 sanitation/sanitation/asgi.py
 create mode 100644 sanitation/sanitation/settings.py
 create mode 100644 sanitation/sanitation/urls.py
 create mode 100644 sanitation/sanitation/wsgi.py
 ```

 4. `git branch -M main` - set the branch to use. We specify `main` branch. We don't want the default of `master` as it may bring bad connotations to some.

 5. `git remote add origin https://github.com/sammigachuhi/my_django.git` - specify the specific online repository we will push to. Remember the repository we created on Github? It's https will be specified here.

 6. `git push -u origin main` - push our local repository to the remote (online) repository.

 Below is the output.

 ```
 Enumerating objects: 23, done.
Counting objects: 100% (23/23), done.
Delta compression using up to 4 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (23/23), 6.07 KiB | 98.00 KiB/s, done.
Total 23 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/sammigachuhi/my_django.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```
