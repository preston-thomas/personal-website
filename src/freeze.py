import os
import shutil
from flask_frozen import Freezer
from src import create_app

app = create_app()
app.config['FREEZER_DESTINATION'] = '../docs'
freezer = Freezer(app)

# Construct the absolute path for cleanup
destination = os.path.abspath(os.path.join(app.root_path, app.config['FREEZER_DESTINATION']))

# Clean up the build directory before freezing
if os.path.exists(destination):
    shutil.rmtree(destination)


if __name__ == '__main__':
    freezer.freeze()
