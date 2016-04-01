#!/usr/bin/python
import db, os, logging, web

logging.basicConfig(level = logging.INFO)
db.init()
app = web.init()

if __name__ == '__main__':
    app.run(debug=True)
