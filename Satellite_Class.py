# dependencies
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table

class SatLauch():

    def __init__(self, connect_string):
        self.engine = create_engine(connect_string)
        # self.conn = self.engine.connect()
        self.connect_string = connect_string
        self.inspector = inspect(self.engine)
        self.tables = self.inspector.get_table_names()
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        self.MasterRecord = self.Base.classes['UCS_Satellite_Master']
        self.DemoGData = self.Base.classes['demoGData']
        self.LaunchDate = self.Base.classes['lauchDate']
        self.SatCount40yr = self.Base.classes['satCount40yr']
        self.meta = MetaData()
        
    def display_db_info(self):
        inspector = inspect(self.engine)
        tables = self.inspector.get_table_names()
        for table in self.tables:
            print("\n")
            print('=' * 12)
            print(f"Table '{table}' has the following columns: ")
            print('-' * 12)
            for column in self.inspector.get_columns(table):
                print(f"name: {column['name']}   column type: {column['type']}")
    
    # return all satellite names
    def get_satellite_names(self):
        session = Session(self.engine)

        results = session.query(self.DemoGData.Satellite_Names)
            
        df = pd.read_sql(results.statement, session.connection())

        session.close()  
        return list(df.Satellite_Names)
    
    # get all demo data based on chosen satellite name
    def get_demographic_data(self, sat_name=0):
        session = Session(self.engine)

        if sat_name == 0:
            results = session.query(self.DemoGData)
        else:
            results = session.query(self.DemoGData).filter_by(self.DemoGData.Satellite_Names == sat_name)    
            
        df = pd.read_sql(results.statement, session.connection())

        session.close()  
        return df.to_dict(orient="records")
    
    # get the lauch date table
    def get_launch_date(self):
        session = Session(self.engine)

        results = session.query(self.LaunchDate)
            
        df = pd.read_sql(results.statement, session.connection())

        session.close()  
        return df.to_dict(orient="records")
    
    # 40 years of satellite launch counts by country 
    def get_40yr_sat_lauch_by_country(self):
        session = Session(self.engine)

        results = session.query(self.SatCount40yr)
            
        df = pd.read_sql(results.statement, session.connection())

        session.close()  
        return df.to_dict(orient="records")
                      
     # 40 years of satellite launch - master records 
    def get_40yr_sat_lauch(self):
        session = Session(self.engine)

        results = session.query(self.MasterRecord)
            
        df = pd.read_sql(results.statement, session.connection())

        session.close()  
        return df.to_dict(orient="records")
                      
if __name__ == '__main__':
    info = SatLauch("sqlite:///Data/UCS_Satellite.sqlite")
    info.display_db_info()
    print("\nSubject IDs\n", info.get_subject_ids())
    print("\nsubject 1286:\n", info.get_subjects(1286))
    print("\nResults 1286:\n", info.get_test_results(1286))
    print("\nData for user 1286:\n", info.get_data_by_user(1286))