import sqlite3
import pandas as pd
import numpy as np
from streamlit_float import *
from streamlit_option_menu import option_menu
from st_aggrid_pro import AgGridPro, GridUpdateMode, JsCode
from st_aggrid_pro.grid_options_builder import GridOptionsBuilder
from streamlit_extras.stylable_container import stylable_container

class Land_load():
    def _create_database():
        conn = sqlite3.connect('land_Registration.db')
        c = conn.cursor()
        c.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='land_Registration'
            """)
        if not c.fetchone():
            c.execute('''CREATE TABLE land_Registration
                     (ID integer PRIMARY KEY , 장지아이디 text, 장지분류 text, 장지구성 text, 계약자아이디 text, 안치고인아이디 text, 계약일 text, 계약종료일 text, 분양가 text, 관리비 text, 노트 text)''')
            conn.commit()
        conn.close()
    
    def _add_customer(숫자, 장지아이디, 장지분류, 장지구성, 계약자아이디, 안치고인아이디, 계약일, 계약종료일, 분양가, 관리비, 노트):
        conn = sqlite3.connect('land_Registration.db')
        c = conn.cursor()
        c.execute("INSERT INTO land_Registration VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(숫자), 장지아이디, 장지분류, 장지구성, 계약자아이디, 안치고인아이디, 계약일, 계약종료일, 분양가, 관리비, 노트))
        conn.commit()
    
    def _search_customer(장지아이디):
        conn = sqlite3.connect('land_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM land_Registration WHERE 장지아이디=?", (장지아이디,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            print("Database error:", e)
            customers = None
        finally:
            conn.close()
        return customers

    def _update_customer(장지아이디, 장지분류, 장지구성, 계약자아이디, 안치고인아이디, 계약일, 계약종료일, 분양가, 관리비, 노트):
        conn = sqlite3.connect('land_Registration.db')
        c = conn.cursor()
        c.execute("UPDATE land_Registration SET 장지분류 = ?, 장지구성 = ?, 계약자아이디 = ?, 안치고인아이디 = ?, 계약일 = ?, 계약종료일 = ?, 분양가 = ?, 관리비 = ?, 노트 = ? WHERE 장지아이디 = ?", (장지분류, 장지구성, 계약자아이디, 안치고인아이디, 계약일, 계약종료일, 분양가, 관리비, 노트, 장지아이디))
        conn.commit()
        conn.close()
    
    def _view_customers():
        conn = sqlite3.connect('land_Registration.db')
        land_customers = pd.read_sql('SELECT * FROM land_Registration', con=conn)
        return land_customers
    
    def _delete_customer(장지아이디):
        conn = sqlite3.connect('land_Registration.db')
        c = conn.cursor()
        c.execute("DELETE FROM land_Registration WHERE 장지아이디=?", (장지아이디,))
        conn.commit()
        conn.close()

class Contact_load():
    def _create_database():
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        c.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='Contact_Registration'
            """)
        if not c.fetchone():
            c.execute('''CREATE TABLE Contact_Registration
                     (ID integer PRIMARY KEY , 계약자아이디 text, 계약자명 text, 연락처 text, 이메일 text, 계약일 text, 안치고인아이디 text, 장지아이디 text, 계약방식 text, 주소 text)''')
            conn.commit()
        conn.close()
    
    def _add_customer(숫자, 계약자아이디, 계약자명, 연락처, 이메일, 계약일, 안치고인아이디, 장치아이디, 계약방식, 주소):
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO Contact_Registration VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(숫자), 계약자아이디, 계약자명, 연락처, 이메일, 계약일, 안치고인아이디, 장치아이디, 계약방식, 주소))
        conn.commit()
    
    def _search_customer(장지아이디):
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Contact_Registration WHERE 장지아이디=?", (장지아이디,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            customers = None
        finally:
            conn.close()
        return customers
    
    def _search_customerV(계약자명):
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Contact_Registration WHERE 계약자명=?", (계약자명,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            customers = None
        finally:
            conn.close()
        return customers

    def _search_customerVV(계약자아이디):
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Contact_Registration WHERE 계약자아이디=?", (계약자아이디,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            customers = None
        finally:
            conn.close()
        return customers
    
    def _update_customer(계약자아이디, 계약자명, 연락처, 이메일, 계약일, 안치고인아이디, 장지아이디, 계약방식, 주소):
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        c.execute("UPDATE Contact_Registration SET 계약자명 = ?, 연락처 = ?, 이메일 = ?, 계약일 = ?, 안치고인아이디 = ?, 장지아이디 = ?, 계약방식 = ?, 주소 = ? WHERE 계약자아이디 = ?", (계약자명, 연락처, 이메일, 계약일, 안치고인아이디, 장지아이디, 계약방식, 주소, 계약자아이디))
        conn.commit()
        conn.close()

    def _view_customers():
        conn = sqlite3.connect('Contact_Registration.db')
        land_customers = pd.read_sql('SELECT * FROM Contact_Registration', con=conn)
        return land_customers
    
    def _delete_customer(장지아이디):
        conn = sqlite3.connect('Contact_Registration.db')
        c = conn.cursor()
        c.execute("DELETE FROM Contact_Registration WHERE 장지아이디=?", (장지아이디,))
        conn.commit()
        conn.close()

class Landhuman_load():
    def _create_database():
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        c.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='Landhuman_Registration'
            """)
        if not c.fetchone():
            c.execute('''CREATE TABLE Landhuman_Registration
                     (ID integer PRIMARY KEY , 안치고인아이디 text, 안치고인명 text, 출생일 text, 임종일 text, 장지아이디 text, 안치일 text, 계약자아이디 text, 노트 text)''')
            conn.commit()
        conn.close()
    
    def _add_customer(숫자, 안치고인아이디, 안치고인명, 출생일, 임종일, 장지아이디, 안치일, 계약자아이디, 노트):
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO Landhuman_Registration VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(숫자), 안치고인아이디, 안치고인명, 출생일, 임종일, 장지아이디, 안치일, 계약자아이디, 노트))
        conn.commit()
    
    def _search_customer(장지아이디):
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Landhuman_Registration WHERE 장지아이디=?", (장지아이디,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            customers = None
        finally:
            conn.close()
        return customers
    
    def _search_customerV(안치고인명):
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Landhuman_Registration WHERE 안치고인명=?", (안치고인명,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            customers = None
        finally:
            conn.close()
        return customers
    
    def _search_customerVV(안치고인아이디):
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM Landhuman_Registration WHERE 안치고인아이디=?", (안치고인아이디,))
            customers = c.fetchall()
        except sqlite3.Error as e:
            customers = None
        finally:
            conn.close()
        return customers

    
    def _update_customer(안치고인아이디, 안치고인명, 출생일, 임종일, 장지아이디, 안치일, 계약자아이디, 노트):
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        c.execute("UPDATE Landhuman_Registration SET 안치고인명 = ?, 출생일 = ?, 임종일 = ?, 장지아이디 = ?, 안치일 = ?, 계약자아이디 = ?, 노트 = ? WHERE 안치고인아이디 = ?", (안치고인명, 출생일, 임종일, 장지아이디, 안치일, 계약자아이디, 노트, 안치고인아이디))
        conn.commit()
        conn.close()
    
    def _view_customers():
        conn = sqlite3.connect('Landhuman_Registration.db')
        land_customers = pd.read_sql('SELECT * FROM Landhuman_Registration', con=conn)
        return land_customers
    
    def _delete_customer(장지아이디):
        conn = sqlite3.connect('Landhuman_Registration.db')
        c = conn.cursor()
        c.execute("DELETE FROM Landhuman_Registration WHERE 장지아이디=?", (장지아이디,))
        conn.commit()
        conn.close()
