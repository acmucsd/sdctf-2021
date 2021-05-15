#! /usr/bin/env bash
# This is just so secure

cd "$(dirname -- "${BASH_SOURCE[0]}")" || { echo "Failed to change to working directory"; exit 1; }

# shellcheck disable=SC2153
if [[ -z "$PIPE_DIR" ]]; then
    pipe_dir=.
else
    pipe_dir="$PIPE_DIR"
fi

pipe_in="$(mktemp -u pipe-in-XXXXXXXXXX -p "$pipe_dir")"
pipe_stop="$(mktemp -u pipe-stop-XXXXXXXXXX -p "$pipe_dir")"
export pipe_in
export pipe_stop

mkfifo "$pipe_in" "$pipe_stop" || { echo "mkfifo failed"; exit 1; }

# shellcheck disable=SC2016
commands='python3 haxlabs.py < "$pipe_in"; bash --rcfile ./.bashrc'

# Use unbuffer to make an interactive shell so our fancy prompt actually show up!

# ADMIN Using redirection (< "$pipe_stop") will break correctness due to bash getting stuck in `open` syscall
# ADMIN when redirecting from a FIFO with no data, therefore confusingly not starting unbuffer command:
# shellcheck disable=SC2002
cat "$pipe_stop" | unbuffer -p bash -c "$commands" 2>&1 &

function on_exit() {
    echo "Stopping..." >&2
    # ADMIN TODO: avoid blocking when cat exits/crashes
    echo > "$pipe_stop"
    rm "$pipe_in" "$pipe_stop"
}

trap on_exit EXIT

cat > "$pipe_in"
exit 0
