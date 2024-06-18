from database import CustomerDatabase
import os
import requests
import time
import shutil
QR_URL = 'https://image-charts.com/chart?chs=150x150&cht=qr&chl='

def main(db_location, qr_location):
  if not os.path.exists(qr_location):
    os.mkdir(qr_location)
  
  new_db = CustomerDatabase(db_location)
  customers = new_db.return_customer_list()
  if len(customers) != 1000:
    new_db.truncate_table()
    new_db.generate_1000_customers()
    customers = new_db.return_customer_list()
  
  # Using range instead of iteration in case more than 1000 records are
  # returned
  for i in range(1000):
    c = customers[i]
    filename = f'{qr_location}/{c[0]}_{c[1]}{c[2]}.png'
    if not os.path.exists(filename):
      res = requests.get(f'{QR_URL}{c[0]}&choe=UTF-8')
      retries = 0
      while res.status_code != 200 and retries <= 4:
        time.sleep(30)
        retries +=1
        res = requests.get(f'{QR_URL}{c[0]}&choe=UTF-8')
        
      if res.status_code == 200:
        with open(filename, 'wb+') as f:
          f.write(res.content)
      else:
        print(res.status_code, res.text)

  shutil.make_archive("./zipped_QRs", "zip", qr_location)

if __name__ == "__main__":
  main("./", "./customer_qrs")

  

