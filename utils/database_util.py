import os
from pathlib import Path
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def init_database(table, path='', file_name='', logger=None):
    if table:
        database = DatabaseUtil(table=table, path=path, file_name=file_name, logger=logger)
    else:
        database = JsonUtil(path=path, file_name=file_name, logger=logger)
    return database

class DatabaseUtil:
    
    def __init__(self, table, path='', file_name='', logger=None):
        self.table = table
        self.path = path + '/data'
        self.file_name = file_name + "_{:%Y-%m-%d_%H-%M-%S}".format(datetime.now()) + ".sqlite3"
        self.logger = logger

        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            Path(self.path + '/' + self.file_name).touch()
            self.engine = create_engine('sqlite:///{}'.format(self.path + '/' + self.file_name))
            self.table.metadata.create_all(self.engine)
        except Exception as error:
            self.logger.exception(error)
            exit()

    @property
    def session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def save(self, data):
        try:
            session = self.session
            objs = []
            for obj in data:
                objs.append(self.table(**obj))
            session.bulk_save_objects(objs)
            session.commit()
        except Exception as error:
            self.logger.exception(error)

class JsonUtil:
    def __init__(self, path='', file_name='', logger=None):
        self.path = path + '/data'
        self.file_name = file_name + "_{:%Y-%m-%d_%H-%M-%S}".format(datetime.now())
        self.logger = logger

        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
        except Exception as error:
            self.logger.exception(error)
            exit()

    def save(self, data):
        origin_data = []

        with open(self.file_name + '.json', 'r') as json_file:
            try:
                origin_data = json.load(json_file)
            except Exception as error:
                pass
        
        with open(self.file_name + '_tmp.json', 'w') as json_file:
            try:
                origin_data.extend(data)
                json_file.write(json.dumps(origin_data))
                os.rename(self.path + self.file_name + '_tmp.json', self.path + self.file_name + '.json')
            except Exception as error:
                self.logger.exception(error)

        