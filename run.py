from flask import Flask
from flask import render_template

app = Flask(
    import_name=__name__,
    template_folder='app/templates'
)

@app.route('/')
def main() -> str:
    return render_template('index.html')
