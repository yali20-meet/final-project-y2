from model import Base, Company

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_company(companyName , email , companyInfo):
	company_object = Company(companyName = companyName , email=email, companyInfo = companyInfo)
	session.add(company_object)
	session.commit()

def get_company(name):
	company = session.query(Company).filter_by(companyName = name).first()
	return company


print(get_company("google"))