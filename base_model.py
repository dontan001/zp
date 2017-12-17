from sqlalchemy import create_engine, Column, Integer, String,Text,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()
url = 'mysql+pymysql://root:FanTan879@47.104.82.16/zp?charset=utf8'
engine = create_engine(url, echo=False)


class DB_Util(object):
    @staticmethod
    def get_session(url=None):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    @staticmethod
    def init_db():
        Base.metadata.create_all(engine)

class DD(Base):
    __tablename__='zp_dd'
    id = Column(Integer, primary_key=True)
    dd_name =Column(String(50), nullable=True)
    province=Column(String(50), nullable=True)

class Zwmc(Base):
    __tablename__='zp_zwmc'
    id = Column(Integer, primary_key=True)
    zwmc_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itszwmc')

class Gsmc(Base):
    __tablename__='zp_gsmc'
    id = Column(Integer, primary_key=True)
    gsmc_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itsgsmc')

class Zwlb(Base):
    __tablename__='zp_zwlb'
    id = Column(Integer, primary_key=True)
    zwlb_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itszwlb')
    #gwzz=relationship('GwzzFenCi')
    #rzyq=relationship('RzyqFenCi')
    flxx=relationship('Flxx',backref='itsflxx')

class Gshy(Base):
    __tablename__='zp_gshy'
    id = Column(Integer, primary_key=True)
    gshy_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itsgshy')

class Gsxz(Base):
    __tablename__='zp_gsxz'
    id = Column(Integer, primary_key=True)
    gsxz_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itsgsxz')

class Gzjy(Base):
    __tablename__='zp_gzjy'
    id = Column(Integer, primary_key=True)
    gzjy_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itsgzjy')

class Xl(Base):
    __tablename__='zp_xl'
    id = Column(Integer, primary_key=True)
    xl_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itsxl')

class Gsgm(Base):
    __tablename__='zp_gsgm'
    id = Column(Integer, primary_key=True)
    gsgm_name =Column(String(100), nullable=True)
    list=relationship('List',backref='itsgsgm')

class List(Base):
    __tablename__ = 'zp_list'
    id = Column(Integer, primary_key=True)
    zwmc_id = Column(Integer,ForeignKey('zp_zwmc.id'))
    gsmc_id = Column(Integer,ForeignKey('zp_gsmc.id'))
    min_zwyx = Column(Integer, nullable=True)
    max_zwyx = Column(Integer,nullable=True)
    dd_id = Column(Integer,ForeignKey('zp_dd.id'))
    fbrq = Column(String(100), nullable=True)
    gsxz_id = Column(Integer,ForeignKey('zp_gsxz.id'))
    gzjy_id = Column(Integer,ForeignKey('zp_gzjy.id'))
    xl_id = Column(Integer,ForeignKey('zp_xl.id'))
    zprs = Column(Integer, nullable=True)
    zwlb_id = Column(Integer,ForeignKey('zp_zwlb.id'))
    gsgm_id = Column(Integer,ForeignKey('zp_gsgm.id'))
    gshy_id = Column(Integer,ForeignKey('zp_gshy.id'))
    href = Column(String(100), nullable=False)

class ListOld(Base):
    __tablename__ = 'zp_list_old'
    id = Column(Integer, primary_key=True)
    zwmc = Column(String(300), nullable=True)
    gsmc = Column(String(300), nullable=True)
    min_zwyx = Column(Integer, nullable=True)
    max_zwyx = Column(Integer,nullable=True)
    dd = Column(String(100),nullable=True)
    fbrq = Column(String(100), nullable=True)
    gsxz = Column(String(100), nullable=True)
    gzjy = Column(String(100), nullable=True)
    xl = Column(String(100), nullable=True)
    zprs = Column(Integer, nullable=True)
    zwlb = Column(String(100), nullable=True)
    gsgm = Column(String(100), nullable=True)
    gshy = Column(String(100), nullable=False)
    gwzz = Column(Text, nullable=True)
    rzyq = Column(Text, nullable=True)
    href = Column(String(100), nullable=False)

class GwzzFenCi(Base):
    __tablename__='zp_gwzz_fenci'
    id = Column(Integer, primary_key=True)
    fenci=Column(String(100), nullable=False)
    list_id=Column(Integer,ForeignKey('zp_list.id'))
    zwlb_id=Column(Integer,ForeignKey('zp_zwlb.id'))

class RzyqFenCi(Base):
    __tablename__='zp_rzyq_fenci'
    id = Column(Integer, primary_key=True)
    fenci=Column(String(100), nullable=False)
    list_id=Column(Integer,ForeignKey('zp_list.id'))
    zwlb_id=Column(Integer,ForeignKey('zp_zwlb.id'))

class Flxx(Base):
    __tablename__='zp_flxx'
    id = Column(Integer, primary_key=True)
    flxx_name=Column(String(100), nullable=False)
    list_id=Column(Integer,ForeignKey('zp_list.id'))
    zwlb_id=Column(Integer,ForeignKey('zp_zwlb.id'))
