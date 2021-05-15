#! /usr/bin/env bash

# Due to the way this challenge is structured, one need to echo back input using socat's ,pty option
# Assuming deployment uses something like
# socat TCP-LISTEN:1337,fork,reuseaddr EXEC:"python2 server.py"
# where there is no ",pty" option

if (( $# < 2 )); then
    echo "usage: ./solve.sh HOST PORT" >&2
    exit 2
fi

# host/port must not contain single quotes or special characters to socat
host="$1"
port="$2"

# Make sure this port is available
local_port=9999

# socat with pty
socat TCP-LISTEN:"$local_port",fork,reuseaddr,bind=localhost EXEC:"nc '$host' '$port'",pty &
SOCAT_PID=$!

./solver.py localhost "$local_port"

kill "$SOCAT_PID"
