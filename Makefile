.PHONY: check-sh format-sh format-py
.SILENT: check-sh format-sh format-py

SRC=.
FORMAT=*.sh

check-sh:
	find $(SRC) -name "$(FORMAT)" -exec shellcheck {} + || true
	find $(SRC) -name "$(FORMAT)" -exec shfmt -d {} + || true

format_sh:
	find $(SRC) -name "$(FORMAT)" -exec shfmt -w {} +

format-py:
	poetry run black $(SRC)



