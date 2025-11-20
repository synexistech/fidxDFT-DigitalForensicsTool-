@echo off
echo ===================================================
echo FidxDFT-Toolkit - GitHub Portfolio Setup
echo ===================================================
echo.
echo This script will help you initialize a Git repository and push it to GitHub.
echo.
echo IMPORTANT: You must create a NEW repository on GitHub first!
echo Go to https://github.com/new and create a repo named 'FidxDFT-Toolkit'.
echo.
set /p repo_url="Enter your GitHub Repository URL (e.g., https://github.com/username/FidxDFT-Toolkit.git): "

if "%repo_url%"=="" (
    echo Error: Repository URL cannot be empty.
    pause
    exit /b
)

echo.
echo [1/5] Initializing Git...
git init

echo [2/5] Adding files...
git add .

echo [3/5] Committing files...
git commit -m "Initial commit: FidxDFT-Toolkit v1 Release"

echo [4/5] Renaming branch to main...
git branch -M main

echo [5/5] Adding remote origin...
git remote add origin %repo_url%

echo.
echo Ready to push!
echo Run the following command manually if the next step fails (requires login):
echo git push -u origin main
echo.
pause

echo Pushing to GitHub...
git push -u origin main

pause
