# Config helper variable
PYTHON = python # Windows doesnt treat Python & Python3 the same way. Thus, it makes confusion if you wrote Python3
UVICORN = uvicorn
APP = api:app
ENV = .venv

# Target to run test
test: test_ml.py
	@echo "Running tests..."
	$(PYTHON) -m pytest $(TEST)

# Target to run the main app
run: 
	@echo "Running api.py..."
	$(UVICORN) $(APP)

# Target to start uvicorn server
serve: 
	@echo "Starting uvicorn server..."
	$(UVICORN) $(APP) --host 0.0.0.0 --port 8000 --reload

# Clean target (optional, if needed for cleaning up)
clean:
	@echo "Cleaning up..."
	rm -rf $(ENV)

# All in one command
all: test run serve
	@echo "All tasks completed."