@echo off
echo 🚀 Starting Standalone Build for AI Local Sync Engine (Windows)...

:: PyInstaller ইনস্টল আছে কিনা চেক করা এবং ইনস্টল করা
pip install pyinstaller

:: পাইথন স্ক্রিপ্টকে স্ট্যান্ডঅ্যালোন ফোল্ডারে রূপান্তর করা
pyinstaller --noconfirm --onedir --console --name ai-sync src/ai_local_engine/cli.py

echo.
echo ✅ Build Successful! Your standalone executable is located in the "dist/ai-sync" folder.
pause
