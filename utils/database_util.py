import os
from pathlib import Path
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseUtil:
    
    def __init__(self, table, path='', file_name='', logger=None):
        self.table = table
        self.path = path
        self.file_name = file_name + "_{:%Y-%m-%d_%H-%M-%S}".format(datetime.now())
        self.file_name = self.file_name + ".sqlite3"
        self.logger = logger

        try:
            if not os.path.exists(self.path + '/data'):
                os.makedirs(self.path + '/data')
            Path(self.path + '/data/' + self.file_name).touch()
            self.engine = create_engine('sqlite:///{}'.format(self.path + '/data/' + self.file_name))
            self.table.metadata.create_all(self.engine)
        except Exception as error:
            self.logger.exception(error)

    @property
    def session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def save(self, data):
        session = self.session
        objs = []
        for obj in data:
            objs.append(self.table(**obj))
        session.bulk_save_objects(objs)
        session.commit()
