import sys 
import pymongo
import csv
from pymongo import MongoClient
import datetime
from datetime import date
import bson
import os.path
import sys, getopt, pprint
from bson.raw_bson import RawBSONDocument
from pandas_datareader import data
import collections

#Sean K 02/08/2021
class Morning():
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client.midCapStrongBuys
        self.client = client
        self.db = db
        
    def getinitAll(self):
        All = self.db.All
        store = []
        today = date.today()
        d1 = today.strftime("%d%m%Y")
        d2 = today.strftime("%d/%m/%Y")
        cursor = open(os.path.expanduser(os.path.join('~/env/mlPredictor/midCap/', k, i+".csv")), "r")
        count = 0
        print(d1)
        header = ['Last Sale','Net Change','% Change','Market Cap','Country','IPO Year']
        for document in cursor:
            symbol = document.Symbol
            name = document.Name
            h= 'history'
            for field in header:
                d[field]=document[field]
            myDict = {
                name: [
                    {
                    symbol: [
                            {
                            h: [
                            ],
                            }
                        ],
                    }
                ],
            }
            count +=1
        for i in range(count):
            store[i].update({"date" : datetime.datetime.utcnow()})
            postTech = store[i]
            tech_id = All.insert_one(postTech).inserted_id
        print(store)
    def downloadHistorical(self, stocks, str):

        str = 'ACLS,ACMR,ALLT,AMSWA,AVID,BBSI,BCOV,BLCT,CAMP,CEVA,CLSK,CMBM,CMTL,CSGS,DCBO,DGII,DSPG,EGAN,EVER,GAN,GDYN,GLUU,GNOG,GTYH,IBEX,ICHR,ICLK,IMMR,INTZ,KE,KOPN,LASR,LIZI,MAXN,MGIC,MGRC,MITK,NH,ONDS,OPRA,OSIS,PDFS,PERI,PLAB,PLUS,PRCH,PRGS,QADA,QMCO,QTT,RBBN,RESN,RIOT,SCPL,SGH,SLP,SMCI,SMSI,SY,SYKE,TCX,TLND,TTMI,UCTT,UPLD,VECO,VUZI,ZIXI'  #stocks
        splits = str.split(',')
        tickers = splits
        start_date = datetime.datetime(2021,1,1)
        end_date = datetime.datetime(2021,2,2)
        count = 0
        for i in tickers:
            panel_data = data.DataReader(i, 'stooq', start_date, end_date)
            panel_data.to_csv(r'~/env/mlPredictor/midCap/', k, i+".csv", index = True)
    def getKeyData(self, stocks, sector, date):
        All = self.db.All
        Tech = self.db.Tech
        store = []
        k = 'keyData'
        for stock in stocks:
            #d1 = today.strftime("%d%m%Y")
            cursor = open(os.path.expanduser(os.path.join('~/env/mlPredictor/midCap/', k, date+".csv")), "r")
            #cursor = open(os.path.expanduser(os.path.join('~/env/mlPredictor/midCap', d1+".csv")), "r")
            reader = csv.DictReader(cursor)
            current = []
            count = 0
            header = ['Last Sale','Net Change','% Change','Market Cap','Country','IPO Year']
            symbol = ['Symbol']
            name = ['Name']
            k = 'KeyData'
            h = 'Historic'
            s = ''
            d = {}
            start = [row for row in reader if row['Symbol'] == stock]
            for rows in start:
                for data in header:
                    n = rows['Symbol']
                    s = rows['Name']
                    for character in s:
                        s = s.replace('.', '_')
                    d[data] = rows[data]
                myDict = {
                    n: [
                        {
                        s: [
                                {
                                k: [
                                    {
                                    date:[
                                        d
                                    ],}
                                ],
                                h: 
                                    self.importHistory(stock, sector, date)
                                }
                            ],
                        }
                    ],
                }
                print(myDict)
                print(stock)
                postTech = myDict
                tech_id = Tech.insert_one(postTech).inserted_id



    def importHistory(self, stock, sector, date):
        All = self.db.All
        history = self.db.techH
        f = []
        store = []
        final = []
        count = 0
        file = open(os.path.expanduser(os.path.join('~/env/mlPredictor/midCap/', sector, stock+".csv")), "r")
        reader = csv.DictReader( file )
        header = [ 'Open','High','Low','Close','Volume']
        for rows in reader:
            d = {}
            for data in header:
                    h = rows['Date']
                    d[data] = rows[data]
            myDict = {
                        h: [
                            d
                        ],
                    }
            f.append(myDict)
        print(count)
        count +=1
        #history.insert_one(myDict)
        return f
        """
        # User pandas_reader.data.DataReader to load the desired data. As simple as that.
        #tech_id = history.insert_many(store)
            """

morning1 = Morning()
#morning1.getinitAll()
stocks = []
str = 'ACLS,ACMR,ALLT,AMSWA,AVID,BBSI,BCOV,BLCT,CAMP,CEVA,CLSK,CMBM,CMTL,CSGS,DCBO,DGII,DSPG,EGAN,EVER,GAN,GDYN,GLUU,GNOG,GTYH,IBEX,ICHR,ICLK,IMMR,INTZ,KE,KOPN,LASR,LIZI,MAXN,MGIC,MGRC,MITK,NH,ONDS,OPRA,OSIS,PDFS,PERI,PLAB,PLUS,PRCH,PRGS,QADA,QMCO,QTT,RBBN,RESN,RIOT,SCPL,SGH,SLP,SMCI,SMSI,SY,SYKE,TCX,TLND,TTMI,UCTT,UPLD,VECO,VUZI,ZIXI'
splits= str.split(',')
for stock in splits:
    stocks.append(stock)

stocks = []
morning1.getKeyData(['ACLS'], 'techSector', '07022021')
#morning1.downloadHistorical([])
#morning1.importHistory([])
#file = open(os.path.expanduser(os.path.join('~/env/mlPredictor/midCap/', k, i+".csv")), "r")