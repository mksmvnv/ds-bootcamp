.PHONY: check format
.SILENT: check format

SRC=.
FORMAT=*.sh

check:
	find $(SRC) -name "$(FORMAT)" -exec shellcheck {} + || true
	find $(SRC) -name "$(FORMAT)" -exec shfmt -d {} + || true

format:
	find $(SRC) -name "$(FORMAT)" -exec shfmt -w {} +



