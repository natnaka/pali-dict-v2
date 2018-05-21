import os
from flask_script import Manager, Shell
from application import create_app
from application.models import db
import application.models as models

app = create_app()
manager = Manager(app)

def _make_shell_context():
    d = {}
    d['app'] = app
    d['db'] = db
    d['m'] = models
    return d

manager.add_command('shell', Shell(make_context=_make_shell_context))

@manager.option("--port", "-p", dest="port", default=5000)
@manager.option("--host", "-h", dest="bind", default='0.0.0.0')
def run(port, bind):
    """Run app"""
    app.run(port=int(port), host=bind)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()


@manager.command
def group_the_pali_word():
    rs = models.ThePali.query.all()
    words = {}
    for r in rs:
        words.setdefault(r.word, []).append(r.mean)
    print("Word count = %d" %len(words))

    for w in words:
        m = ', '.join(words[w])
        o = models.ThePaliCompact(word=w, mean=m)
        db.session.add(o)
        if len(db.session.new) >= 500:
            print("Insert %d records" %len(db.session.new))
            db.session.commit()

    if len(db.session.new) > 0:
        print("Insert %d records" %len(db.session.new))
        db.session.commit()

    print("Finished")


@manager.option("--file", "-f", dest="f", default=None)
def load_the_pali(f):
    if not os.path.isfile(f):
        print("%s is not valid file.")
        return

    import csv
    data = {}
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        header = None
        #i = 0
        for row in reader:
            if not header:
                header = [c.strip().lower() for c in row]
                print("header = ", header)
                continue

            #print("row = ", row)

            d = dict(zip(header, row))
            #print("dict = ", d)

            data.setdefault(int(d['id']), []).append(d)

    total = len(data)
    print("Record count = %d" %total)

    sorted_ids = sorted(data.keys())
    for i in sorted_ids:
        l = data[i]
        if len(l) > 1:
            print("id = %d has %d records" %(i, len(l)))
        for r in l:
            r.pop('id')
            o = models.ThePali(**r)
            db.session.add(o)
        if len(db.session.new) >= 500:
            print("Insert %d records" %len(db.session.new))
            db.session.commit()

    if len(db.session.new) > 0:
        print("Insert %d records" %len(db.session.new))
        db.session.commit()

    print("Finished")
 

 
@manager.option("--file", "-f", dest="f", default=None)
def load_tware_pali(f):
    if not os.path.isfile(f):
        print("%s is not valid file.")
        return

    import csv
    data = {}
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        header = None
        #i = 0
        for row in reader:
            if not header:
                header = [c.strip().lower() for c in row]
                header[2] = 'word_type' # override, prevent from keyword dup
                print("header = ", header)
                continue

            #print("row = ", row)

            d = dict(zip(header, row))
            #print("dict = ", d)

            data.setdefault(int(d['id']), []).append(d)

            #i += 1
            #if i > 5: break

    total = len(data)
    print("Record count = %d" %total)

    sorted_ids = sorted(data.keys())
    for i in sorted_ids:
        l = data[i]
        if len(l) > 1:
            print("id = %d has %d records" %(i, len(l)))
        for r in l:
            r.pop('id')
            o = models.TwarePaliWord(**r)
            db.session.add(o)
        if len(db.session.new) >= 500:
            print("Insert %d records" %len(db.session.new))
            db.session.commit()

    if len(db.session.new) > 0:
        print("Insert %d records" %len(db.session.new))
        db.session.commit()

    print("Finished")
            
    
            

if __name__ == '__main__':
    manager.run()
