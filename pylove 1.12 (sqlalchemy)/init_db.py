from sqlalchemy import create_engine

from main import db
import models


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    post_1 = models.BlogPost()
    post_1.sub = "Temat 1"
    post_1.content = "lalsdlajdwkjdna"
    db.session.add(post_1)
    db.session.commit()

if __name__ == '__main__':
    db_start()