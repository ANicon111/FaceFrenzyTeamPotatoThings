#!/bin/sh
sudo bash << HEREDOC
source /etc/profile.d/pynq_venv.sh
source /etc/profile.d/xrt_setup.sh
cd "$(dirname "$0")"
(cd templates;python3 -m http.server)&
export TO_KILL=$!
PLAYER_COUNT=$PLAYER_COUNT python3 app.py
killall python3
HEREDOC
