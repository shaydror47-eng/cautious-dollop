# Prompts

## Purpose
Reusable procedures, commands, and AI workflows for common tasks. How to use ChatGPT, Claude, Copilot, and agents effectively.

## AI Usage Rules
- **Small focused fixes**: Don't rewrite full projects
- **Ask before changes**: Especially for big changes
- **Keep stable versions safe**: Always test before deploying
- **Incremental improvement**: One fix at a time
- **Test on both phones**: Verify nothing breaks

## AI Tools Available
- ChatGPT: Quick questions, brainstorming
- Claude: Complex analysis, detailed code review
- GitHub Copilot: Code completion, inline suggestions
- Claude Code: Focused code changes, debugging
- Agents: Multi-step tasks, automation

## Android / ADB Commands

### Device Setup
```bash
# List connected devices
adb devices

# Check device details
adb shell getprop ro.build.version.release  # Android version
adb shell getprop ro.product.model          # Device model

# Enable USB debugging on phone
Settings > Developer Options > USB Debugging (ON)
```

### App Management
```bash
# Install app from APK
adb install app.apk

# Uninstall app
adb uninstall com.package.name

# List installed apps
adb shell pm list packages

# Clear app cache (no data loss)
adb shell pm clear com.package.name

# Force stop app
adb shell am force-stop com.package.name

# Start app
adb shell am start -n com.package.name/.MainActivity
```

### Debugging
```bash
# View live logs (all apps)
adb logcat

# Filter logs for specific app
adb logcat | grep PackageName

# Clear log buffer
adb logcat -c

# Save logs to file
adb logcat > log.txt

# Enter shell (like SSH)
adb shell
```

### Performance
```bash
# Check battery info
adb shell dumpsys battery

# Check storage
adb shell df -h

# Check processes
adb shell ps

# Monitor memory
adb shell dumpsys meminfo
```

### File Transfer
```bash
# Push file to phone
adb push local_file.txt /sdcard/

# Pull file from phone
adb pull /sdcard/file.txt .
```

## Git Commands

### Basic Workflow
```bash
# Clone repo
git clone https://github.com/user/repo.git

# Check status
git status

# Add changes
git add .

# Commit
git commit -m "Brief description of change"

# Push to GitHub
git push origin main
```

### Branches
```bash
# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# List branches
git branch -a

# Delete branch
git branch -d feature-name
```

### Undo Changes
```bash
# Undo uncommitted changes
git checkout -- file.txt

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

## Build & Compilation

### Android Studio / Gradle
```bash
# Build APK (debug)
./gradlew assembleDebug

# Build APK (release)
./gradlew assembleRelease

# Run tests
./gradlew test

# Clean build
./gradlew clean

# Install on device
./gradlew installDebug
```

### Common Build Errors & Fixes
```
Error: "Gradle sync failed"
→ File > Invalidate Caches > Restart

Error: "SDK not found"
→ Install SDK in Android Studio > SDK Manager

Error: "Gradle dependency error"
→ Update build.gradle dependencies, sync again
```

## Testing Procedures

### Before Any Release
1. **Build**: `./gradlew assembleDebug` (no errors)
2. **Phone 1 test**:
   - Install APK: `adb install build/outputs/apk/debug/app-debug.apk`
   - Open app
   - Test main features
   - Check logcat for errors: `adb logcat`
   - Verify Wolt still works
   - Verify Waze still works
3. **Phone 2 test**: Repeat all above
4. **Check performance**:
   - Battery usage: `adb shell dumpsys battery`
   - Memory: `adb shell dumpsys meminfo`
5. **Sign off**: Note results in APPS.md

### Quick Phone Test
```bash
# Connect phone
adb devices

# Check battery
adb shell dumpsys battery

# Check storage
adb shell df -h

# Check running apps
adb shell ps | grep wolt  # or other app name
```

## AI Prompts for Work

### For Bug Fixes
```
"I have a bug in [app/code]. [Describe issue].
- [Steps to reproduce]
- [Expected behavior]
- [Actual behavior]
What's the root cause and how do I fix it?"
```

### For New Features
```
"I want to add [feature] to [app].
Current flow: [How it works now]
Desired flow: [How it should work]
Constraints: [Limitations]
Can you suggest the smallest change to implement this?"
```

### For Code Review
```
"Review this code for bugs, efficiency, and Android best practices:
[Paste code]
Highlight: main issues and how to fix them.
Don't rewrite, just point out problems."
```

### For Help with AAPI Documentation
```
"I need to [implement feature]. 
I'm using [libraries/frameworks].
What's the best approach following Android best practices?"
```

## Troubleshooting Workflow

### App Crashes
1. Get logcat: `adb logcat > crash.log`
2. Search for "Exception" or "Error" in log
3. Paste error in AI tool: "Why does this crash? [Stack trace]"
4. Fix recommended issue
5. Test on both phones

### Phone Freezes
1. Try force restart: Power + Volume down (depends on phone)
2. If fixed, check PHONE.md for known issues
3. If repeats, switch to backup phone
4. Log issue in BUGS.md

### GPS/Navigation Issues
1. Disable Waze, restart phone
2. Re-enable location services
3. Restart Waze
4. If still broken, switch phone
5. Log in BUGS.md with time and location

## Daily Morning Checklist
```
☐ Check CURRENT_PRIORITY.md
☐ Check PHONE.md status
☐ Verify both phones charged 80%+
☐ Open Wolt on both phones
☐ Test Waze on one phone
☐ Check BUGS.md for known issues
☐ Ready to start shift
```

## Next Actions
- [ ] Bookmark this file for shift reference
- [ ] Add more custom commands you use
- [ ] Document successful fixes
- [ ] Share useful prompts with team
