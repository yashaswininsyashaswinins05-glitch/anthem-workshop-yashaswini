from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def load_anthem() -> str:
    """Read the anthem text from the project's text file."""
    anthem_file = BASE_DIR / "anthem.txt"
    try:
        return anthem_file.read_text(encoding="utf-8")
    except OSError:
        return "The anthem text file could not be loaded. Please check anthem.txt."


@app.route("/")
def home():
    return render_template("index.html", anthem=load_anthem())


if __name__ == "__main__":
    app.run(debug=True)
