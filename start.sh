# Start the Django dev server: creates a venv, installs deps, migrates, runs.
# Usage: ./start.sh [port]     (default port: 8000)
set -euo pipefail

cd "$(dirname "$0")"

PORT="${1:-8000}"
VENV_DIR=".venv"

# Create the virtual environment on first run
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# Reinstall only when requirements.txt changed
STAMP="$VENV_DIR/.requirements.stamp"
if [ ! -f "$STAMP" ] || [ requirements.txt -nt "$STAMP" ]; then
    echo "Installing dependencies..."
    pip install --quiet -r requirements.txt
    touch "$STAMP"
fi

export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-backend.settings.dev}"

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Starting server on http://127.0.0.1:${PORT}/api/status/"
exec python manage.py runserver "127.0.0.1:${PORT}"