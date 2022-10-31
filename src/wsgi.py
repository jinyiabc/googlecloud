"""App entry point."""
from flask1 import create_app
import os
app = create_app()

if __name__ == "__main__":
    server_port = os.environ.get('PORT', '8080')
    app.run(host="0.0.0.0", port=server_port)