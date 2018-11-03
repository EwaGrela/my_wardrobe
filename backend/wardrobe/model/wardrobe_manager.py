import os
import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import collate
from datetime import datetime

from wardrobe.model.models import Clothes, Garment

class WardrobeManager:
    def __init__(self):
        engine = create_engine(os.environ['DATABASE_URL'])
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def show_garments(self):
        all_garments = self.session.query(Garment).all()
        return all_garments

    def create_garment(self, name):
        new_garment = Garment(name=name)
        if not self.verify_garment_type(new_garment):
            self.add_garment(new_garment)
        
    def add_garment(self, item):
        self.session.add(item)
        self.session.commit()

    def verify_garment_type(self, item):
        garments = self.show_garments()
        garment_types = [garment.name for garment in garments]
        if item.name in garment_types:
            return True
        return False

    def add_clothing(self, item):
        self.session.add(item)
        self.session.commit()

    def create_clothing(self, model, name, info):
        new_item = Clothes(model=model, name=name, info=info)
        if self.verify_garment_type(new_item):
            self.add_clothing(new_item)
        else:
            self.create_garment(new_item.name)
            self.add_clothing(new_item)
    
    def show_clothes(self):
        clothes = self.session.query(Clothes).all()
        clothes = [item.to_json() for item in clothes]
        return clothes
    
    def query_wardrobe(self, **filters):
        print("filters", filters)
        return "OK"
    
    def delete_clothing(self, cloth_id):
        to_delete = self.session.query(Clothes).filter(Clothes.id == cloth_id).one_or_none()
        self.session.delete(to_delete)
        self.session.commit()
        return "Deleted"

