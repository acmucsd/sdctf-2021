# Attachment

all: challenge/una_acies.py una_acies.zip

# Needed before deployment
challenge/una_acies.py: una_acies_admin.py
	onelinerizer una_acies_admin.py challenge/una_acies.py

una_acies.zip: challenge/una_acies.py example-flag.txt
	rm -f una_acies.zip
	zip una_acies.zip challenge/una_acies.py example-flag.txt
	printf "@ example-flag.txt\n@=flag.txt\n" | zipnote -w una_acies.zip
	printf "@ challenge/una_acies.py\n@=una_acies.py" | zipnote -w una_acies.zip

clean:
	rm -f challenge/una_acies.py
	rm -f una_acies.zip

.PHONY: deploy clean all
