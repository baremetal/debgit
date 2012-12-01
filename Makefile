all:

.PHONY: pylint
pylint:
	PYTHONPATH=lint pylint --load-plugins astng_sh debgit
