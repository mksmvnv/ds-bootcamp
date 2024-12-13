.PHONY: check
.SILENT: check

SRC=.
FORMAT=*.sh

check:
	find $(SRC) -name "$(FORMAT)" -exec shellcheck {} + || true



