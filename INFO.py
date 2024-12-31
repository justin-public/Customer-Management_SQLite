import sqlite3
import streamlit as st
import pandas as pd
import numpy as np
import time
#from UI import*
from streamlit_float import *
from streamlit_option_menu import option_menu
from st_aggrid_pro import AgGridPro, GridUpdateMode, JsCode
from st_aggrid_pro.grid_options_builder import GridOptionsBuilder
from streamlit_extras.stylable_container import stylable_container

class Land_Info_load():
    def _info_init_write(landindexcnt):
        with open("landindex.txt", "w") as file:
            file.write(landindexcnt)
    
    def _info_init_Read():
        f = open("landindex.txt", "r")
        land_line = f.readline()
        f.close()
        return land_line

class Contactor_Info_load():
    def _info_init_write(landindexcnt):
        with open("Contactindex.txt", "w") as file:
            file.write(landindexcnt)
    
    def _info_init_Read():
        f = open("Contactindex.txt", "r")
        land_line = f.readline()
        f.close()
        return land_line

class Landhuman_Info_load():
    def _info_init_write(landindexcnt):
        with open("landhumanindex.txt", "w") as file:
            file.write(landindexcnt)
    
    def _info_init_Read():
        f = open("landhumanindex.txt", "r")
        land_line = f.readline()
        f.close()
        return land_line

