"""
Comprehensive .gitignore templates
"""

COMPREHENSIVE_TEMPLATE = """
# Operating System Files
## Windows
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db
*.stackdump
[Dd]esktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msix
*.msm
*.msp
*.lnk

## macOS
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk
*.icloud

## Linux
*~
.fuse_hidden*
.directory
.Trash-*
.nfs*

# IDE and Editor Files
## Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace
.history/
.ionide

## JetBrains IDEs
.idea/
*.iml
*.iws
*.ipr
.idea_modules/
out/

## Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

## Vim
[._]*.s[a-v][a-z]
[._]*.sw[a-p]
[._]s[a-rt-v][a-z]
[._]ss[a-gi-z]
[._]sw[a-p]
Session.vim
Sessionx.vim
.netrwhist

# Programming Languages
## Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.python-version

## Node.js
node_modules/
jspm_packages/
.npm
.node_repl_history
*.tgz
.yarn-integrity
.env
.env.test
.env.production
.next
out/
.nuxt
dist/
.cache/
.parcel-cache

## Java
*.class
*.log
*.ctxt
.mtj.tmp/
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar
hs_err_pid*
replay_pid*
target/
.gradle/
build/
!gradle/wrapper/gradle-wrapper.jar

# Build and Package Files
## General
*.log
*.bak
*.swp
*.tmp
*.temp
.cache
.temp
temp/
tmp/

## Dependencies
vendor/
bower_components/
packages/
composer.phar

## Compiled files
*.com
*.class
*.dll
*.exe
*.o
*.so
*.dylib
*.bin

# Environment and Configuration
## General
.env
.env.local
.env.*.local
.env.development
.env.test
.env.production
*.env
.config
config.local.*
*.local
local.*

## Secrets and Keys
*.pem
*.key
*.keystore
*.p12
*.pfx
*.cer
*.der
id_rsa
id_dsa
*.gpg
*.asc
secrets.*
.secret
.secrets
credentials.*
.credentials

# Logs and Databases
*.log
*.sql
*.sqlite
*.sqlite3
*.db
*.db-shm
*.db-wal
logs/
log/

# Media and Generated Files
*.png
*.jpg
*.jpeg
*.gif
*.ico
*.pdf
*.mov
*.mp4
*.mp3
*.flv
*.fla
*.swf
*.wav
*.avi
*.mkv
*.webm
generated/
"""