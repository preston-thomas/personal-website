import os
import shutil
from flask_frozen import Freezer
from src import create_app

app = create_app()
app.config['FREEZER_DESTINATION'] = 'docs'
freezer = Freezer(app)

# Clean up the build directory before freezing
if os.path.exists('docs'):
    shutil.rmtree('docs')


if __name__ == '__main__':
    freezer.freeze()
