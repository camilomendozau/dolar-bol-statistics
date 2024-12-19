#from config import config
import pgdb
from hashlib import md5    
from decouple import config


class Database:
     def __init__(self):
        self.conexion = None
        self.connect()

     def connect(self):   
        try:
            # Conexion al servidor de PostgreSQL
            print('Conectando a la base de datos PostgreSQL...')
            self.conexion = pgdb.connect(
                host=config('PGSQL_HOST'),
                database=config('PGSQL_DATABASE'), 
                user=config('PGSQL_USER'), 
                password=config('PGSQL_PASSWORD')
            )
            print('Conectado exitosamente a PostgreSQL!!!')
            return self.conexion
        except (Exception) as error:
            print(error)
      

     def getConexion(self):
         return self.conexion

     def closeConexion(self):
         if self.conexion is not None:
                self.conexion.close()
                print('Conexión finalizada.')

     def getEstados(self):
         try:
            #response = ''
            cur = self.conexion.cursor()      
            query = "SELECT public.estado"
            cur.execute(query)
            response = cur.fetchall() 
            if len(response) > 0:
               print(response)
            else:
               print("No hay datos en la DB")
            cur.close()
         except(Exception) as error:
            print(error)
         return response 
         
     
     def getClientes(self):
         try:
            cur = self.conexion.cursor()      
            query = f"""SELECT public."getclientes"()"""
            cur.execute(query)
            response = cur.fetchall() 
            print(len(response[0][0]))
            cur.close()
         except(Exception) as error:
            print(error)
         return response[0]               
            
   #   def verificarLogin(self,username:str,psw:str):
   #        try:    
   #          md5Psw = md5(psw.encode("utf-8")).hexdigest()
   #          cur = self.conexion.cursor()         
   #          query = f"""SELECT adm."verifyLogin"('{username}','{md5Psw}')"""
   #          self.conexion.commit()
   #          cur.execute(query)
   #          response = cur.fetchone()
   #          responseIfClientExist = response[0]
   #          query = 'SELECT adm."getLastSesion"()'
   #          cur.execute(query)
   #          response = cur.fetchone()
   #          responsePID = response[0] 
   #          print(responseIfClientExist,responsePID)
   #          cur.close()
   #        except(Exception) as error:
   #            print(error)  
   #        return (responseIfClientExist,responsePID)   
     
   #   def getUINames(self,username:str):
   #        try:
   #          cur = self.conexion.cursor()         
   #          query = f"""SELECT adm."getUINames"('{username}')"""
   #          cur.execute(query)
   #          response = cur.fetchall() 
   #          #print(response)
   #          cur.close()
   #        except(Exception) as error:
   #          print(error)
   #        return response  
     
     def insertNewVendedor(self,firstName:str,lastName:str,carnetIdentidad:str):
          try:                
            cur = self.conexion.cursor()         
            query = f"""SELECT public."insertNewVendedor"('{firstName}','{lastName}','{carnetIdentidad}')"""
            cur.execute(query)
            self.conexion.commit()
            response = cur.fetchone()
            print(response)
            cur.close()
          except(Exception) as error:
              print(error)  
          return (response)   

DB = Database()     
DB.getEstados()
#DB.getUnidadesMedida()
#DB.getProductos()
# DB.insertNewVendedor('Eliet','Barrantes','8726392A')
# DB.insertNewCliente('Frank', 'Barrantes', '65147265')