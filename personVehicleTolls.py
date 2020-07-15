import sys
import pandas as pd
import os

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('max_rows', 999)
import numpy as np

def main ():
    print(os.getcwd())
    #6651-903409-None-person.csv
    person = pd.read_csv('9546-903409-None-person.csv')
    print(person.head())
    toll_events = pd.read_csv('9546-903409-None-toll_event.csv')
    print(toll_events.head())
    toll_location = pd.read_csv('9546-903409-None-toll_location.csv')
    print(toll_location.head())
    vehicle = pd.read_csv('9546-903409-None-vehicle.csv')
    print(vehicle.head())
    veh_cert = pd.read_csv('9546-903409-None-vehicle_certification.csv')
    print(veh_cert.head())
    veh_per_link = pd.read_csv('9546-903409-None-vehicle_person_link.csv')
    print(veh_per_link.head())

    p2v = pd.merge(person,veh_per_link,how='inner',left_on='id',right_on='person_id',suffixes=('_per','_veh'))
    p2v.drop(columns=['id_per','data_set_id_per','data_set_id_veh','transaction_id_per','transaction_id_veh','id_veh'],inplace=True)
    print(p2v.head())

    p2veh = pd.merge(p2v,vehicle,how='inner',left_on='vehicle_id',right_on='id',suffixes=('_per','_veh'))
    p2veh.drop(columns=['id','data_set_id','transaction_id'],inplace=True)
    print(p2veh.head())

    p2veh = pd.merge(p2v,vehicle,how='inner',left_on='vehicle_id',right_on='id',suffixes=('_per','_veh'))
    p2veh.drop(columns=['id','data_set_id','transaction_id'],inplace=True)
    print(p2veh.head())

    p2v2t = pd.merge(p2veh,toll_events,how='inner',left_on='vehicle_id',right_on='vehicle_id',suffixes=('_veh','_toll'))
    p2v2t.drop(columns=['id','data_set_id','transaction_id'],inplace=True)
    print(p2v2t.head())

    p2v2t2l = pd.merge(p2v2t,toll_location,how='inner',left_on='toll_location_id',right_on='id',suffixes=('_toll','_loc'))
    p2v2t2l.drop(columns=['id','data_set_id','transaction_id'],inplace=True)
    p2v2t2l.sort_values(by='timestamp',ascending=False,inplace=True)
    print(p2v2t2l.head())
    p2v2t2l.drop_duplicates(inplace=True,subset=['name','birthdate','country_toll','person_id','vehicle_id','type','toll_location_id','latitude','longitude','locality','country_loc'])
    print(p2v2t2l)

if __name__ == "__main__":
    main()