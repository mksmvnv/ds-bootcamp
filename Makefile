.PHONY: check-sh format-sh format-py
.SILENT: check-sh format-sh format-py

SRC=src/
FORMAT=*.sh
POETRY=poetry run

check-sh:
	find $(SRC) -name "$(FORMAT)" -exec $(POETRY) shellcheck {} + || true
	find $(SRC) -name "$(FORMAT)" -exec $(POETRY) shfmt -d {} + || true

format-sh:
	find $(SRC) -name "$(FORMAT)" -exec $(POETRY) shfmt -w {} +

format-py:
	$(POETRY) black $(SRC) --config pyproject.toml



