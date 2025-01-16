Published at https://github.com/shoes/shoes3/wiki/git-better .

## Prerequisites
Create a free GitHub account. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your computer and [configure it](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

### Forking the repository
On the [page of the Shoes3 repository](https://github.com/shoes/shoes3), click **Fork**. This will put a copy of the Shoes3 repository onto your web GitHub account.

### Cloning the fork
In order to edit the fork on your computer, you need to clone it. On the page of your forked repository, click **Clone**. This shows the URL you need to give to git. (If you have configured GitHub with SSH, you should rather use the URL you get with the link _Use SSH_.) Using the command line, go to the directory where you want the repository folder, and type <code>$&nbsp;git&nbsp;clone&nbsp;URL</code>. (You can tell Git how to name the repository folder: <code>$&nbsp;git&nbsp;clone&nbsp;URL&nbsp;FOLDER</code>.)

### Connecting your local repository to the official repository
In order to get updates from the official Shoes3 repository, you need first to add it as a remote. You can check your current remotes: <code>$&nbsp;git&nbsp;remote&nbsp;-v</code>. Right now, you should only have one remote, named `origin`: your GitHub fork. To add the official repository as a remote named `upstream`, type <code>$&nbsp;git&nbsp;remote&nbsp;add&nbsp;upstream&nbsp;URL</code>. (You can get the URL from the [official page of the Shoes3 repository](https://github.com/shoes/shoes3) with the _Clone_ button.) You can check again your list of remotes: <code>$&nbsp;git&nbsp;remote&nbsp;-v</code>.

***

## Workflow
### Syncing your local clone with the official repository
Go to your local `master` branch: <code>$&nbsp;git&nbsp;checkout&nbsp;master</code>. Assuming you named the official repository `upstream`, integrate the changes of the official repository's `master` branch into your branch: <code>$&nbsp;git&nbsp;pull&nbsp;upstream&nbsp;master</code>. You can use <code>$&nbsp;git&nbsp;log</code> to see the latest commits.

### Branching
You can list your branches with <code>$&nbsp;git&nbsp;branch</code> If you want details: <code>$&nbsp;git&nbsp;branch&nbsp;-v</code> or <code>$&nbsp;git&nbsp;branch&nbsp;-vv</code>.

Create a branch named `testing` based on your `master` branch: <code>$&nbsp;git&nbsp;checkout&nbsp;-b&nbsp;testing&nbsp;master</code>. (If you omit the last argument, Git may base the new local `testing` branch on a `testing` branch of your GitHub fork if there is already such a branch there. Here, we prefer to base our new branch on the local `master` branch, because we just updated that branch at the previous step.)

Make your changes to the code. You can check your changes with <code>$&nbsp;git&nbsp;status</code> and <code>$&nbsp;git&nbsp;diff</code>. Mark any file you want to commit: <code>$&nbsp;git&nbsp;add&nbsp;FILE</code>. Save the changes to the branch: <code>$&nbsp;git&nbsp;commit</code>.

If you made commits you dislike and which you did not publish online, you can make the branch come back to a past commit:<code>$&nbsp;git&nbsp;reset&nbsp;COMMIT_ID</code>. (You can get commit IDs with <code>$&nbsp;git&nbsp;branch&nbsp;-v</code> and <code>$&nbsp;git&nbsp;log</code>.)

### Cleaning (optional)
Once you are satisfied with your committed changes, you may want to create a specific branch for your pull request: <code>$&nbsp;git&nbsp;checkout&nbsp;-b&nbsp;patch-1&nbsp;testing</code>. One reason for doing so is that you can have only one open pull request by branch. Another reason is that if you make the decision to rebase (as explained below), doing so on a new branch allows you to come back to the `testing` branch in case you dislike the result.

To simplify the commit history of that new `patch-1` branch (to make it easier for maintainers to understand your changes), you can type <code>$&nbsp;git&nbsp;rebase&nbsp;-i&nbsp;BASE_BRANCH</code>, which allows you to manually omit commits, reorder them, change their description, or squash (combine) them into a single commit. The command uses `BASE_BRANCH` as the new base for these commits, so it makes sense in our case to use `master` as the base branch. (As a rule of thumb, never rebase a branch which is already public. Here, it's ok because `patch-1` is a branch which is only on your private local repository, assuming you created that branch there and did not push it to any repository.)

If you are unhappy with your `patch-1` branch, you can still come back to the `testing` branch and delete the `patch-1` branch: <code>$&nbsp;git&nbsp;checkout&nbsp;testing;&nbsp;git&nbsp;branch&nbsp;-d&nbsp;patch-1</code>.

If you are happy with the `patch-1` branch, you can remove the `testing` branch: <code>$&nbsp;git&nbsp;branch&nbsp;-d&nbsp;testing</code>.

### Making a pull request (invite the maintainers to pull your changes)
Update your GitHub fork with the branch you want to share: <code>$&nbsp;git&nbsp;push&nbsp;origin&nbsp;BRANCH_TO_SHARE</code>. If there is an error due to a branch which was already on your GitHub repository, you can pick a new branch name and run <code>$&nbsp;git&nbsp;push&nbsp;origin&nbsp;BRANCH_TO_SHARE:NEW_BRANCH</code> to create on your GitHub fork a branch reflecting the local branch you want to share.

On your GitHub fork webpage, create a pull request. As the **base**, choose the official repository (shoes/shoes3) and the `master` branch. As the **head**, choose your fork and the `testing` branch.

Even once a pull request for a branch is open, you can still commit to that branch.

When the pull request for a branch is closed, GitHub invites you to delete the branch. If you delete it, GitHub allows you to restore it. Either way, the discussion board remains open.

***

## Resources
This guide was mostly based on these wonderful resources:
* https://www.atlassian.com/git/tutorials
* https://git-scm.com/book/en/
* https://help.github.com/articles/
* http://rogerdudler.github.io/git-guide/
