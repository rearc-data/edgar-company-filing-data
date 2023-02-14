
# Checkout via command line
If the conflicts on this branch are too complex to resolve in the web editor, you can check it out via command line to resolve the conflicts.
#https:www.bitore.net:
https://github.com/mowjoejoejoejoe/WORKSFLOW.git
Step 1: Clone the repository or update your local repository with the latest changes.
git pull origin main
Step 2: Switch to the head branch of the pull request.
git checkout Master
Step 3: Merge the base branch into the head branch.
git merge main
Step 4: Fix the conflicts and commit the result.
See Resolving a merge conflict using the command line for step-by-step instructions on resolving merge conflicts.
Step 5: Push the changes.
git push -u origin Master WORKSFLOW
 AUTOMATE AUTOMATES BEGIN GLOW4 AUTOMATES#Test :tests :tests :Run'@ci:
:BSkip to content
github
/ Projects
/  GitHub public roadmap
Search or jump to…

@mowjoejoejoejoe 
roadmap #616
Actions: Self-hosted runners now support Windows ARM64#616
Item statusClosed
github-product-roadmap opened 3 months ago
Description

github-product-roadmap
3 months ago
Summary
The GitHub Actions Runner now supports Windows ARM64 architecture.

Intended Outcome
Previously, the Actions runner did not include Windows ARM64 as a supported OS & Arch combination. This new release of the runner enables customers to use their Windows ARM64 environments as self-hosted runners for GitHub Actions.

How will it work?
During the self-hosted runner creation flow, customers will select the Windows ARM64 release for deployment. For additional information on how to set up a self-hosted Windows ARM64 runner, please refer to our documentation. If you have any feedback or questions for Actions self-hosted Windows ARM support, you can submit an issue in the runner repository.

Comments
Properties
Assignees
No Assignees
Labels
actions
cloud
ga
all
server
shipped
runners
Milestone
No Milestone
Status
Q3 2022 – Jul-Sep
Repository
roadmap
Linked pull requests
No linked pull requests
Tracks
None yet
Tracked by
None yet
 Hide extra fields
Open in new tab
Copy link
GitHub public roadmap
Board
Table
Generally available
Cloud (github.com)
Server (GHES)
GitHub Advanced Security
GitHub Issues
GitHub Actions
-status:"Q4 2021 – Oct-Dec","Q1 2022 – Jan-Mar","Q2 2022 – Apr-Jun" 
189
 (189)
Q3 2022 – Jul-Sep
41
 (41)
Mobile: Feature updates Q3 2022
Projects: Auto-archive automation
Projects: Add projects to team index
Actions: Self-hosted runners now support Windows ARM64
Q4 2022 – Oct-Dec
51
 (51)
Billing Usage API
Kotlin security analysis support in CodeQL code scanning (public beta)
API Versioning (GA)
Fine-grained PATs (v2 PATs) - [Public Beta]
Q1 2023 – Jan-Mar
43
 (43)
Git LFS moves to metered billing
Dependabot: grouped updates
Actions: Required workflows
Pull Request Merge Queue
Q2 2023 – Apr-Jun
17
 (17)
Swift security analysis support in CodeQL code scanning (beta)
Actions: Custom deployment protection rules (gates)
Command Palette
Bulk-enable code scanning for multiple repositories (GHES)
Q3 2023 – Jul-Sep
1
 (1)
Actions: GitHub-hosted macOS runners now offer Apple M1 silicon options (Beta)
Q4 2023 – Oct-Dec
1
 (1)
Future
35
 (35)
Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore

@mowjoejoejoejoe 
mowjoejoejoejoe
/
WORKSFLOW
Public
Cannot fork because you own this repository and are not a member of any organizations.
Code
Issues
4
Pull requests
8
Actions
Projects
Wiki
Security
Insights
Settings
WORKSFLOW
/
Checkout via command line If the conflicts on this branch are too complex to resolve in the web editor, you can check it out via command line to resolve the conflicts. https:
/
github.com
/
mowjoejoejoejoe
/
WORKSFLOW.git Step 1: Clone the repository or update your local repository with the latest changes.  git pull origin main Step 2: Switch to the head branch of the pull request.  git checkout Master Step 3: Merge the base branch into the head branch.  git merge main Step 4: Fix the conflicts and commit the result.  See Resolving a merge conflict using the command line for step-by-step instructions on resolving merge conflicts. Step 5: Push the changes.  git push -u origin Master
in
bitore.sig


Spaces

2

No wrap
1
# Checkout via command line
2
If the conflicts on this branch are too complex to resolve in the web editor, you can check it out via command line to resolve the conflicts.
3
#https:www.bitore.net:
4
https://github.com/mowjoejoejoejoe/WORKSFLOW.git
5
Step 1: Clone the repository or update your local repository with the latest changes.
6
git pull origin main
7
Step 2: Switch to the head branch of the pull request.
8
git checkout Master
9
Step 3: Merge the base branch into the head branch.
10
git merge main
11
Step 4: Fix the conflicts and commit the result.
12
See Resolving a merge conflict using the command line for step-by-step instructions on resolving merge conflicts.
13
Step 5: Push the changes.
14
git push -u origin Master WORKSFLOW
15
 AUTOMATE AUTOMATES BEGIN GLOW4 AUTOMATES#Test :tests :tests :Run'@ci:
16
​
@mowjoejoejoejoe
Commit new file
Commit summary
Create WORKSFLOW.git Step 1: Clone the repository or update your local repository with the latest changes.  git pull origin main Step 2: Switch to the head branch of the pull request.  git checkout Master Step 3: Merge the base branch into the head branch.  git merge main Step 4: Fix the conflicts and commit the result.  See Resolving a merge conflict using the command line for step-by-step instructions on resolving merge conflicts. Step 5: Push the changes.  git push -u origin Master
Optional extended description
Add an optional extended description…
 Commit directly to the bitore.sig branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.

Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
 47  
README.md
@@ -0,0 +1,47 @@
# WORKSFLOW
 AUTOMATE AUTOMATES BEGIN GLOW4 AUTOMATES#Test :tests :tests :Run'@ci:
:Build::
:Pull :pulls_request :
pulls_request :Patch 5'@index.md :
#README.md/README.md :
:Build::
Publish :
access :Public :
#access :Public :
Private :
WORKFLOWS :
BEGIN GLOW4 AUTOMATES#Test :tests :tests :Run'@ci:
GLOW4:'
BEGIN'
STARt'
RUN'
FROM'
'--'[dev']''
'#'Title'' ':'Nan.yml'' :
-on :ON :
  starts-on :GLOW7 :
  workflows_call-on :dispatch ::':repositories/WORKFLOW.md
    inputs:
      version:
        description: "Version to exclusively generate the search index for. E.g. 'dotcom', 'ghes-3.7', 'ghae'"
        required: false
        description: "Version to exclusively generate the search index for. E.g. 'dotcom', 'ghcr'@v'"-3.7.9.11.10'"'' :
        , 'ghrc/cadd.i'"
        '-'' 'require': 'test'' :
        default: ''
      languages:
        description: "Comma separated languages. E.g. 'en,ja, es' (defaults to all)"
        required: false
        default: ''
  schedule:
    - cron: '20 */24 * * *' # Run every 24 hours at 20 minutes past the hour
  workflow_run:
    workflows: ['Azure Production - Build and Deploy']
    types:
      - completed
permissions:
  contents: read
# This allows a subsequently queued workflow run to cancel previous runs
concurrency:
  group: '${{ github.workflow }} @ ${{ github.head_ref }} ${{ github.event_name }}'
  cancel-in-progress: true
  5  
Request.md
@@ -4,4 +4,7 @@ pulls_request :Patch 5'@index.md :
#README.md/README.md :	#README.md/README.md :
:Build::	:Build::
Publish :	Publish :
access :Public :	#access :Public :
Private :
# WORKSFLOW
 AUTOMATE AUTOMATES BEGIN GLOW4 AUTOMATES#Test :tests :tests :Run'@ci# edgar-company-filing-data
Code to publish all company filings data from EDGAR on ADX
#README.md/README.md :
:Build::
Publish :
#access :Public :
Private :
# WORKSFLOW
 AUTOMATE AUTOMATES BEGIN GLOW4 AUTOMATES#Test :tests :tests :Run'@ci
