import os

from socketto import ws, app

if __name__ == "__main__":
    ws.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=True,
    )
