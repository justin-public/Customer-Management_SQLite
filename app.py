# 2024년 04월 25일 
import sqlite3
import streamlit as st
import pandas as pd
import numpy as np
import time
from UI import*
from INFO import*
from DATA import*
from TABLE import*
from streamlit_float import *
from streamlit_option_menu import option_menu
from st_aggrid_pro import AgGridPro, GridUpdateMode, JsCode
from st_aggrid_pro.grid_options_builder import GridOptionsBuilder
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(layout="wide", initial_sidebar_state = "expanded")

def main():
    Land_index_num = Land_Info_load._info_init_Read()
    Contact_index_num = Contactor_Info_load._info_init_Read()
    Landhuman_index_num = Landhuman_Info_load._info_init_Read()

    if "landdata" not in st.session_state:
        st.session_state.landdata = Land_load._view_customers()
    if "Contactdata" not in st.session_state:
        st.session_state.Contactdata = Contact_load._view_customers()
    if "landhumandata" not in st.session_state:
        st.session_state.landhumandata = Landhuman_load._view_customers()
    
    if "landindexcnt" not in st.session_state:
        st.session_state.landindexcnt = int(Land_index_num)
    if "Contactindexcnt" not in st.session_state:
        st.session_state.Contactindexcnt = int(Contact_index_num)
    if "Landhumanindexcnt" not in st.session_state:
        st.session_state.Landhumanindexcnt = int(Landhuman_index_num)

    if "land_id_dialog" not in st.session_state:
        st.session_state.land_id_dialog = 0
    if "landdialogshow" not in st.session_state:
        st.session_state.landdialogshow = 0
    if "landdialogshow1" not in st.session_state:
        st.session_state.landdialogshow1 = False
    
    if "contact_id_dialog" not in st.session_state:
        st.session_state.contact_id_dialog = 0
    if "Contactdialogshow" not in st.session_state:
        st.session_state.Contactdialogshow = False    
    if "Contactdialogshow1" not in st.session_state:
        st.session_state.Contactdialogshow1 = False
    
    if "landhuman_id_dialog" not in st.session_state:
        st.session_state.landhuman_id_dialog = 0
    if "Landhumandialogshow" not in st.session_state:
        st.session_state.Landhumandialogshow = False
    if "Landhumandialogshow1" not in st.session_state:
        st.session_state.Landhumandialogshow1 = False

    if "land_id_value" not in st.session_state:
        st.session_state.land_id_value = ""
    if "land_context_value" not in st.session_state:
        st.session_state.land_context_value = ""
    if "land_type_value" not in st.session_state:
        st.session_state.land_type_value = ""
    if "land_cost_value" not in st.session_state:
        st.session_state.land_cost_value = ""
    if "land_managecost_value" not in st.session_state:
        st.session_state.land_managecost_value = ""
    if "land_note_value" not in st.session_state:
        st.session_state.land_note_value = ""

    if "Contact_id_value" not in st.session_state:
        st.session_state.Contact_id_value = ""
    if "Contact_name_value" not in st.session_state:
        st.session_state.Contact_name_value = ""
    if "Contact_telephone_value" not in st.session_state:
        st.session_state.Contact_telephone_value = ""
    if "Contact_email_value" not in st.session_state:
        st.session_state.Contact_email_value = ""
    if "Contact_date_value" not in st.session_state:
        st.session_state.Contact_date_value = ""
    if "Contact_landid_value" not in st.session_state:
        st.session_state.Contact_landid_value = ""
    if "Contact_type_value" not in st.session_state:
        st.session_state.Contact_type_value = ""
    if "Contact_address_value" not in st.session_state:
        st.session_state.Contact_address_value = ""
    
    if "Landhuman_id_value" not in st.session_state:
        st.session_state.Landhuman_id_value = ""
    if "Landhuman_name_value" not in st.session_state:
        st.session_state.Landhuman_name_value = ""
    if "Landhuman_birthday_value" not in st.session_state:
        st.session_state.Landhuman_birthday_value = ""
    if "Landhuman_ripday_value" not in st.session_state:
        st.session_state.Landhuman_ripday_value = ""
    if "Landhuman_contactid_value" not in st.session_state:
        st.session_state.Landhuman_contactid_value = ""
    if "Landhuman_landid_value" not in st.session_state:
        st.session_state.Landhuman_landid_value = ""
    if "Landhuman_last_value" not in st.session_state:
        st.session_state.Landhuman_last_value = ""
    if "Landhuman_note_value" not in st.session_state:
        st.session_state.Landhuman_note_value = ""
    
    with st.sidebar:
        selected = option_menu(
            menu_title="",
            options=["DASHBOARD","장지 정보","계약고객정보","안치고인정보","HERITAGE"],
            #icons=["pencil-fill","bar-chart-fill","envelope-heart-fill"],  # https://icons.getbootstrap.com/
            default_index=0
            #orientation="horizontal",
        )
    if selected == "장지 정보":
        Land_load._create_database()
        Land_loadUI._Register_UI()
        landdata = pd.DataFrame(np.array(st.session_state.landdata),columns=['ID','장지아이디','장지분류','장지구성','계약자아이디','안치고인아이디','계약일','계약종료일','분양가','관리비','노트'])
        LandDatabase = Land_loadTABLE._interactive_table(landdata)
        Land_loadUI._dialog_container()
        if LandDatabase["selected_rows"]:
            st.session_state.land_id_dialog += 1
        if st.session_state.land_id_dialog == 1:
            st.session_state.land_id_value = LandDatabase["selected_rows"][0]["장지아이디"]
            st.session_state.land_context_value = LandDatabase["selected_rows"][0]["장지분류"]
            st.session_state.land_type_value = LandDatabase["selected_rows"][0]["장지구성"]
            st.session_state.land_cost_value = LandDatabase["selected_rows"][0]["분양가"]
            st.session_state.land_managecost_value = LandDatabase["selected_rows"][0]["관리비"]
            st.session_state.land_note_value = LandDatabase["selected_rows"][0]["노트"]
            st.session_state.landdialogshow1 = True
            st.experimental_rerun()
        if st.session_state.land_id_dialog == 4:
            st.session_state.land_id_dialog = 0
        Land_loadUI._dialog_containerV(st.session_state.land_id_value,
                                       st.session_state.land_context_value,
                                       st.session_state.land_type_value,
                                       st.session_state.land_cost_value,
                                       st.session_state.land_managecost_value,
                                       st.session_state.land_note_value)
    
    if selected == "계약고객정보":
        Contact_load._create_database()
        Contact_loadUI._Register_UI()
        Contactdata = pd.DataFrame(np.array(st.session_state.Contactdata),columns=['ID','계약자아이디','계약자명','연락처','이메일','계약일','안치고인아이디','장지아이디','계약방식','주소'])
        ContactDatabase=Contact_loadTABLE._interactive_table(Contactdata)
        Contact_loadUI._dialog_container()
        if ContactDatabase["selected_rows"]:
            st.session_state.contact_id_dialog += 1
        if st.session_state.contact_id_dialog == 1:
            st.session_state.Contact_id_value = ContactDatabase["selected_rows"][0]["계약자아이디"] 
            st.session_state.Contact_name_value = ContactDatabase["selected_rows"][0]["계약자명"]
            st.session_state.Contact_telephone_value = ContactDatabase["selected_rows"][0]["연락처"]
            st.session_state.Contact_email_value = ContactDatabase["selected_rows"][0]["이메일"]
            st.session_state.Contact_date_value = ContactDatabase["selected_rows"][0]["계약일"]
            st.session_state.Contact_landid_value = ContactDatabase["selected_rows"][0]["장지아이디"]
            st.session_state.Contact_type_value = ContactDatabase["selected_rows"][0]["계약방식"]
            st.session_state.Contact_address_value = ContactDatabase["selected_rows"][0]["주소"]
            st.session_state.Contactdialogshow1 = True
            st.experimental_rerun()
        if st.session_state.contact_id_dialog == 4:
            st.session_state.contact_id_dialog = 0
        Contact_loadUI._dialog_containerV(st.session_state.Contact_id_value,
                                          st.session_state.Contact_name_value,
                                          st.session_state.Contact_telephone_value,
                                          st.session_state.Contact_email_value,
                                          st.session_state.Contact_date_value,
                                          st.session_state.Contact_landid_value,
                                          st.session_state.Contact_type_value,
                                          st.session_state.Contact_address_value)

    
    if selected == "안치고인정보":
        Landhuman_load._create_database()
        Landhuman_loadUI._Register_UI()
        Landhumandata = pd.DataFrame(np.array(st.session_state.landhumandata),columns=['ID','안치고인아이디','안치고인명','출생일','임종일','장지아이디','안치일','계약자아이디','노트'])
        LandhumanDatabase=Landhuman_loadTABLE._interactive_table(Landhumandata)
        Landhuman_loadUI._dialog_container()
        if LandhumanDatabase["selected_rows"]:
            st.session_state.landhuman_id_dialog += 1
        if st.session_state.landhuman_id_dialog == 1:
            st.session_state.Landhuman_id_value = LandhumanDatabase["selected_rows"][0]["안치고인아이디"] 
            st.session_state.Landhuman_name_value = LandhumanDatabase["selected_rows"][0]["안치고인명"]
            st.session_state.Landhuman_birthday_value = LandhumanDatabase["selected_rows"][0]["출생일"]
            st.session_state.Landhuman_ripday_value = LandhumanDatabase["selected_rows"][0]["임종일"]
            st.session_state.Landhuman_contactid_value = LandhumanDatabase["selected_rows"][0]["계약자아이디"]
            st.session_state.Landhuman_landid_value = LandhumanDatabase["selected_rows"][0]["장지아이디"]
            st.session_state.Landhuman_last_value = LandhumanDatabase["selected_rows"][0]["안치일"]
            st.session_state.Landhuman_note_value = LandhumanDatabase["selected_rows"][0]["노트"]
            st.session_state.Landhumandialogshow1 = True
            st.experimental_rerun
        if st.session_state.landhuman_id_dialog == 4:
            st.session_state.landhuman_id_dialog = 0
        Landhuman_loadUI._dialog_containerV(st.session_state.Landhuman_id_value,
                                            st.session_state.Landhuman_name_value,
                                            st.session_state.Landhuman_birthday_value,
                                            st.session_state.Landhuman_ripday_value,
                                            st.session_state.Landhuman_contactid_value,
                                            st.session_state.Landhuman_landid_value,
                                            st.session_state.Landhuman_last_value,
                                            st.session_state.Landhuman_note_value)


if __name__ == '__main__':
    main()