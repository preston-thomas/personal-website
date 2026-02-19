import os
import shutil
from flask_frozen import Freezer
from src import create_app

app = create_app()
freezer = Freezer(app)

# Clean up the build directory before freezing
if os.path.exists('src/build'):
    shutil.rmtree('src/build')


if __name__ == '__main__':
    freezer.freeze()
