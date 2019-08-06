from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Company(Base):
	__tablename__ = 'Companies'
	id = Column(Integer , primary_key=True)
	companyName = Column(String)
	email = Column(String)
	companyInfo = Column(String)

	def __repr__(self):
		return ("Company: {} \nEmail: {} \nCompany Info: {}").format(self.companyName , self.email , self.companyInfo)


