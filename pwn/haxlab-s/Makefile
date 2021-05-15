COMMON = admin/.bashrc admin/haxlabs.py admin/launcher.sh

SHELL_FILTER = '/^ *\# (ADMIN|shellcheck )/d'

all: deploy attachment.zip

# Run this target on the deployment machine afetr updating the challenge, before running
# kctf chal start
# This generates the necessary deployment files
deploy: $(COMMON) admin/flag.txt
	cp admin/haxlabs.py admin/flag.txt challenge/
	sed -E $(SHELL_FILTER) admin/launcher.sh > challenge/launcher.sh
	sed -E $(SHELL_FILTER) admin/.bashrc > challenge/.bashrc

# Run this target to generate the attachment zip file
attachment.zip: $(COMMON) admin/README.md fake-local-flag.txt
	mkdir -p attachment/
	cp admin/haxlabs.py admin/README.md attachment/
	cp fake-local-flag.txt attachment/flag.txt
	sed -E $(SHELL_FILTER) admin/launcher.sh > attachment/launcher.sh
	sed -E $(SHELL_FILTER) admin/.bashrc > attachment/.bashrc
	zip -r attachment.zip attachment/

clean:
	rm -f attachment.zip
	rm -rf attachment/
	rm -f challenge/launcher.sh
	rm -f challenge/.bashrc
	rm -f challenge/flag.txt
	rm -f challenge/haxlabs.py

.PHONY: deploy clean all
