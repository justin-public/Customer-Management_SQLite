from DATA import *
from INFO import *
from streamlit_float import *
from streamlit_option_menu import option_menu
from st_aggrid_pro import AgGridPro, GridUpdateMode, JsCode
from st_aggrid_pro.grid_options_builder import GridOptionsBuilder
from streamlit_extras.stylable_container import stylable_container

class Land_loadUI():
    def _Register_UI():
        col1,col2,col3,col4,col5 = st.columns([1,0.3,0.7,1,1])
        #with col1:
            #col1.markdown("""
                #<style>
                #.big-font {
                    #font-size:25px !important;
                #}
                #</style>
                #""", unsafe_allow_html=True)
            #st.markdown('<p class="big-font">장지 정보</p>',unsafe_allow_html=True)
        #with col1:
            #st.markdown("장지 정보",unsafe_allow_html=True)
        #with col2:
            #with stylable_container(key="container_with_border",css_styles=["""{position:fixed;right: 390px; top:125px;}""",],):
                #st.markdown("장지 ID")
        with col3:
            with stylable_container(key="LandIDname",css_styles=["""{position:fixed;right: 330px; top:35px;}""",],):
                Id_name = st.text_input("")
        with col4:
            with stylable_container(key="LandSearch",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 227px; top:70px; width:100px;}""",],):
                if st.button(" 검색 "):
                    st.session_state.landdata = Land_load._search_customer(Id_name)

        with col5:
            with stylable_container(key="LandRegister",css_styles=["""button {border: solid .1em #292746;#border-radius: 20px;color: #000;position:fixed;right: 120px; top:70px;}""",],):
                if st.button("장지등록"):
                    st.session_state.landdialogshow = True
                    st.experimental_rerun()
        
    def _dialog_container():
        if st.session_state.landdialogshow == True:
            land_dialog_container = float_dialog(st.session_state.landdialogshow,width=1.0)
            with land_dialog_container:
                dt, dt1 = st.columns([0.2,0.2])
                with dt:
                    with stylable_container(
                        key="Land",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            width: 50px;
                        }
                        """,
                        ],  
                    ):
                        st.header("장지")
                with dt1:
                    with stylable_container(
                        key="Close",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;right: 35px; top:55px;
                            width: 50px;
                        }
                        """,
                        ],
                    ):
                        if st.button("X"):
                            st.session_state.landdialogshow = False
                            st.experimental_rerun()
                
                dc1,dc2,dc3 = st.columns([0.2,0.2,0.2])
                dc4,dc5,dc6 = st.columns([0.2,0.2,0.2])
                dc7,dc8 = st.columns([0.045,0.2])
                with dc1:
                    with stylable_container(
                        key="Namei",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지아이디 = st.text_input("장지ID")
                with dc2:
                    with stylable_container(
                        key="LandO",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지분류 = st.selectbox('장지분류',('봉안당','자연장 1X1','자연장 2X1','자연장 2X2','자연장 4X2','자연장 4X4'))
                with dc3:
                    with stylable_container(
                        key="LandC",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지구성 = st.text_input("장지구성")
                with dc4:
                    with stylable_container(
                        key="LandP",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        분양가 = st.text_input("분양가")
                with dc5:
                    with stylable_container(
                        key="LandM",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        관리비 = st.text_input("관리비")
                with dc6:
                    with stylable_container(
                        key="LandN",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        노트 = st.text_input("Note")
                with dc7:
                    with stylable_container(
                        key="ConfirmV",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        if st.button("Confirm"):
                            st.session_state.landindexcnt += 1
                            if 장지아이디:
                                계약자아이디 = ""
                                안치고인아이디 = ""
                                계약일 = ""
                                계약종료일 = ""
                                Land_load._add_customer(st.session_state.landindexcnt,장지아이디, 장지분류, 장지구성, 계약자아이디, 안치고인아이디, 계약일, 계약종료일, 분양가, 관리비, 노트)
                                Land_Info_load._info_init_write(str(st.session_state.landindexcnt))
                                st.session_state.landdata = Land_load._view_customers()
                            _info_db = Contact_load._search_customer(장지아이디)
                            _info_db1 = Landhuman_load._search_customer(장지아이디)    
                            if 장지아이디 and len(_info_db) > 0:    
                                계약자아이디 = _info_db[0][1]
                                계약자명 = _info_db[0][2]
                                연락처 = _info_db[0][3]
                                이메일 = _info_db[0][4]
                                계약일 =  _info_db[0][5]
                                계약방식 = _info_db[0][8]
                                주소 = _info_db[0][9]
                                Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,장지아이디,계약방식,주소)
                                Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지아이디,안치일,계약자아이디,안치고인노트)
                                st.session_state.Contactdata = Contact_load._view_customers()
                                st.session_state.landhumandata = Landhuman_load._view_customers()
                            if 장지아이디  and len(_info_db1) > 0:
                                안치고인아이디 = _info_db1[0][1]
                                안치고인명 = _info_db1[0][2]
                                출생일 = _info_db1[0][3]
                                임종일 = _info_db1[0][4]
                                안치일 = _info_db1[0][6]
                                안치고인노트 = ""
                                계약종료일 = ""
                                Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,장지아이디,계약방식,주소)
                                Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지아이디,안치일,계약자아이디,안치고인노트)
                                st.session_state.Contactdata = Contact_load._view_customers()
                                st.session_state.landhumandata = Landhuman_load._view_customers()
                            st.session_state.landdialogshow = False
                            st.experimental_rerun()
                           
                with dc8:
                    with stylable_container(
                        key="DeleteV",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; right: 35px; top:275px;
                            width: 100px;
                        }
                        """,
                        ],    
                    ):
                        if st.button("삭제"):
                            Land_load._delete_customer(장지아이디)
                            st.session_state.landdata = Land_load._view_customers()
                            st.session_state.landdialogshow = False
                            st.experimental_rerun()

    def _dialog_containerV(장지아이디값,장지분류값,장지구성값,분양가값,관리비값,노트값):
        if st.session_state.landdialogshow1 == True:
            land_dialog_container = float_dialog(st.session_state.landdialogshow1,width=1.5)
            with land_dialog_container:
                dt, dt1 = st.columns([0.2,0.2])
                with dt:
                    with stylable_container(
                        key="Land",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            width: 50px;
                        }
                        """,
                        ],  
                    ):
                        st.header("장지")
                with dt1:
                    with stylable_container(
                        key="Close",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;right: 35px; top:55px;
                            width: 50px;
                        }
                        """,
                        ],
                    ):
                        if st.button("X"):
                            #st.session_state.land_id_dialog = 0
                            st.session_state.landdialogshow1 = False
                            st.experimental_rerun()
                dc1,dc2,dc3 = st.columns([0.2,0.2,0.2])
                dc4,dc5,dc6 = st.columns([0.2,0.2,0.2])
                dc7,dc8 = st.columns([0.045,0.2])
                with dc1:
                    with stylable_container(
                        key="Namei",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지아이디 = st.text_input("장지ID",장지아이디값)
                with dc2:
                    with stylable_container(
                        key="LandO",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지분류 = st.selectbox('장지분류',('봉안당','자연장 1X1','자연장 2X1','자연장 2X2','자연장 4X2','자연장 4X4'))
                with dc3:
                    with stylable_container(
                        key="LandC",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지구성 = st.text_input("장지구성",장지구성값)
                with dc4:
                    with stylable_container(
                        key="LandP",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        분양가 = st.text_input("분양가",분양가값)
                with dc5:
                    with stylable_container(
                        key="LandM",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        관리비 = st.text_input("관리비",관리비값)
                with dc6:
                    with stylable_container(
                        key="LandN",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        노트 = st.text_input("Note",노트값)
                with dc7:
                    with stylable_container(
                        key="ConfirmV",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        if st.button("Confirm"):
                            if 장지아이디:
                                _info_db = Contact_load._search_customer(장지아이디)
                                _info_db1 = Landhuman_load._search_customer(장지아이디)
                                if len(_info_db) == 0:
                                    계약자아이디 = ""
                                    안치고인아이디 = ""
                                    계약일 = ""
                                    계약종료일 = ""
                                    Land_load._update_customer(장지아이디,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                    st.session_state.landdata = Land_load._view_customers()
                                if len(_info_db1) == 0:
                                    계약자아이디 = ""
                                    안치고인아이디 = ""
                                    계약일 = ""
                                    계약종료일 = ""
                                    Land_load._update_customer(장지아이디,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                    st.session_state.landdata = Land_load._view_customers()
                                if len(_info_db) > 0: 
                                    계약자아이디 = _info_db[0][1]
                                    계약자명 = _info_db[0][2]
                                    연락처 = _info_db[0][3]
                                    이메일 = _info_db[0][4]
                                    계약일 =  _info_db[0][5]
                                    계약방식 = _info_db[0][8]
                                    주소 = _info_db[0][9]
                                    안치고인아이디 = ""
                                    계약종료일 = ""
                                    Land_load._update_customer(장지아이디,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                    Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,장지아이디,계약방식,주소)
                                    st.session_state.landdata = Land_load._view_customers()
                                    st.session_state.Contactdata = Contact_load._view_customers()
                                
                                if len(_info_db1) > 0:
                                    안치고인아이디 = _info_db1[0][1]
                                    안치고인명 = _info_db1[0][2]
                                    출생일 = _info_db1[0][3]
                                    임종일 = _info_db1[0][4]
                                    안치일 = _info_db1[0][6]
                                    안치고인노트 = ""
                                    계약종료일 = ""
                                    Land_load._update_customer(장지아이디,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                    Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지아이디,안치일,계약자아이디,안치고인노트)
                                    st.session_state.landdata = Land_load._view_customers()
                                    st.session_state.landhumandata = Landhuman_load._view_customers()
                                st.session_state.landdialogshow1 = False
                                st.experimental_rerun()
                with dc8:
                    with stylable_container(
                        key="DeleteV",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; right: 35px; top:275px;
                            width: 100px;
                        }
                        """,
                        ],    
                    ):
                        if st.button("삭제"):
                            Land_load._delete_customer(장지아이디)
                            st.session_state.landdata = Land_load._view_customers()
                            st.session_state.landdialogshow1 = False
                            st.experimental_rerun()


class Contact_loadUI():
    def _Register_UI():
        col1,col2,col3,col4,col5 = st.columns([1,0.5,0.5,1,1])
        #with col1:
            #col1.markdown("""
                #<style>
                #.big-font {
                    #font-size:25px !important;
                #}
                #</style>
                #""", unsafe_allow_html=True)
            #st.markdown('<p class="big-font">계약고객정보</p>',unsafe_allow_html=True)
        with col2:
            with stylable_container(
                key="contact_with_border",css_styles=["""{position:fixed;right: 500px; top:35px;}""",],):
                계약자분류 = st.selectbox('',('계약자명','계약자아이디'))
        if 계약자분류 == "계약자명":
            with col3:
                    with stylable_container(key="Contactinformation",css_styles=["""{position:fixed;right: 415px; top:35px; width: 80px;}""",],):
                        계약자명값 = st.text_input("")
            with col4:
                    with stylable_container(key="ContactSearch",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 155px; top:70px; width: 100px;}""",],):
                        if st.button(" 검색 "):
                            st.session_state.Contactdata = Contact_load._search_customerV(계약자명값)

        
        if 계약자분류 == "계약자아이디":
            with col3:
                with stylable_container(key="Contactinformation",css_styles=["""{position:fixed;right: 415px; top:35px; width: 80px;}""",],):
                    계약자아이디값 = st.text_input("")
            with col4:
                 with stylable_container(key="ContactSearch",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 155px; top:70px; width: 100px;}""",],):
                    if st.button(" 검색 "):
                        st.session_state.Contactdata = Contact_load._search_customerVV(계약자아이디값)
        
        with col5:
            with stylable_container(key="ContactRegister",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 50px; top:70px;width: 100px;}""",],):
                if st.button("계약등록"):
                    st.session_state.Contactdialogshow = True
                    st.experimental_rerun()         
    
    def _dialog_container():
        if st.session_state.Contactdialogshow == True:
            Contact_dialog_container = float_dialog(st.session_state.Contactdialogshow,width=1.2)
            with Contact_dialog_container:
                dt, dt1 = st.columns([0.2,0.2])
                with dt:
                    with stylable_container(
                        key="Land",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            width: 50px;
                        }
                        """,
                        ],  
                    ):
                        st.header("계약")
                with dt1:
                    with stylable_container(
                        key="Close",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;right: 35px; top:55px;
                            width: 50px;
                        }
                        """,
                        ],
                    ):
                        if st.button("X"):
                            st.session_state.Contactdialogshow = False
                            st.experimental_rerun()
                
                dc1,dc2,dc3,dc4 = st.columns([0.2,0.2,0.2,0.2])
                dc5,dc6,dc7,dc8 = st.columns([0.09,0.09,0.09,0.2])
                dc9,dc10 = st.columns([0.045,0.2])
                with dc1:
                    with stylable_container(
                        key="ContactID",
                        css_styles=[
                            """
                            button {
                                border: solid .1em #292746;
                                #border-radius: 20px;
                                color: #000;
                                #background-color: #292746;
                                position:fixed;
                                #width: 50px;
                            }
                            """,
                        ],  
                    ):
                        계약자아이디 = st.text_input("계약자아이디")
                with dc2:
                    with stylable_container(
                        key="ContactName",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약자명 = st.text_input("계약자명")
                with dc3:
                    with stylable_container(
                        key="ContactTelephone",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        연락처 = st.text_input("연락처")
                with dc4:
                    with stylable_container(
                        key="Contactemail",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        이메일 = st.text_input("이메일")
                with dc5:
                    with stylable_container(
                        key="Contactdate",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약일 = st.text_input("계약일")
                with dc6:
                    with stylable_container(
                        key="ContactLandID",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        _장지아이디 = st.text_input("장지아이디")
                with dc7:
                    with stylable_container(
                        key="ContactType",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약방식 = st.text_input("계약방식")
                with dc8:
                    with stylable_container(
                        key="ContactAddress",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        주소 = st.text_input("주소")
                with dc9:
                    with stylable_container(
                        key="Contactdelete",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        if st.button("계약삭제"):
                            Contact_load._delete_customer(_장지아이디)
                            st.session_state.Contactdata = Contact_load._view_customers()
                            st.session_state.Contactdialogshow = False
                            st.experimental_rerun()

                with dc10:
                    with stylable_container(
                        key="ContactConfirm",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        if st.button("Confirm"):
                            st.session_state.Contactindexcnt += 1
                            if 계약자아이디:
                                안치고인아이디 = ""
                                Contact_load._add_customer(st.session_state.Contactindexcnt,계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,_장지아이디,계약방식,주소)
                                Contactor_Info_load._info_init_write(str(st.session_state.Contactindexcnt))
                                st.session_state.Contactdata = Contact_load._view_customers()
                            
                            _info_db = Landhuman_load._search_customer(_장지아이디)
                            _info_db1 = Land_load._search_customer(_장지아이디)    
                            
                            if len(_info_db) > 0:
                                안치고인아이디 = _info_db[0][1]
                                안치고인명 = _info_db[0][2]
                                출생일 = _info_db[0][3]
                                임종일 = _info_db[0][4]
                                안치일 = _info_db[0][6]
                                Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,_장지아이디,안치일,계약자아이디,안치고인노트)
                                st.session_state.landhumandata = Landhuman_load._view_customers()
                            
                            if len(_info_db1) > 0:    
                                _info_db1 = Land_load._search_customer(_장지아이디)
                                장지분류=_info_db1[0][2]
                                장지구성=_info_db1[0][3]
                                관리비=_info_db1[0][8]
                                노트=_info_db1[0][9]
                                분양가=""
                                계약종료일=""
                                안치고인노트=""
                                Land_load._update_customer(_장지아이디,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                st.session_state.landdata = Land_load._view_customers()    
                            
                            st.session_state.Contactdialogshow = False
                            st.experimental_rerun()

    def _dialog_containerV(계약자아이디값,계약자명값,연락처값,이메일값,계약일값,장지아이디값,계약방식값,주소값):
        if st.session_state.Contactdialogshow1 == True:
            Contact_dialog_container = float_dialog(st.session_state.Contactdialogshow1,width=1.2)
            with Contact_dialog_container:
                dt, dt1 = st.columns([0.2,0.2])
                with dt:
                    with stylable_container(
                        key="Land",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            width: 50px;
                        }
                        """,
                        ],  
                    ):
                        st.header("계약")
                with dt1:
                    with stylable_container(
                        key="Close",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;right: 35px; top:55px;
                            width: 50px;
                        }
                        """,
                        ],
                    ):
                        if st.button("X"):
                            st.session_state.Contactdialogshow1 = False
                            st.experimental_rerun()
                
                dc1,dc2,dc3,dc4 = st.columns([0.2,0.2,0.2,0.2])
                dc5,dc6,dc7,dc8 = st.columns([0.09,0.09,0.09,0.2])
                dc9,dc10 = st.columns([0.045,0.2])
                with dc1:
                    with stylable_container(
                        key="ContactID",
                        css_styles=[
                            """
                            button {
                                border: solid .1em #292746;
                                #border-radius: 20px;
                                color: #000;
                                #background-color: #292746;
                                position:fixed;
                                #width: 50px;
                            }
                            """,
                        ],  
                    ):
                        계약자아이디 = st.text_input("계약자아이디",계약자아이디값)
                with dc2:
                    with stylable_container(
                        key="ContactName",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약자명 = st.text_input("계약자명",계약자명값)
                with dc3:
                    with stylable_container(
                        key="ContactTelephone",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        연락처 = st.text_input("연락처",연락처값)
                with dc4:
                    with stylable_container(
                        key="Contactemail",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        이메일 = st.text_input("이메일",이메일값)
                with dc5:
                    with stylable_container(
                        key="Contactdate",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약일 = st.text_input("계약일",계약일값)
                with dc6:
                    with stylable_container(
                        key="ContactLandID",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        _장지아이디 = st.text_input("장지아이디",장지아이디값)
                with dc7:
                    with stylable_container(
                        key="ContactType",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약방식 = st.text_input("계약방식",계약방식값)
                with dc8:
                    with stylable_container(
                        key="ContactAddress",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        주소 = st.text_input("주소",주소값)
                with dc9:
                    with stylable_container(
                        key="Contactdelete",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        st.button("계약삭제")
                
                with dc10:
                    with stylable_container(
                        key="ContactConfirm",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        if st.button("Confirm"):
                            if 계약자아이디:
                                _info_db = Landhuman_load._search_customer(_장지아이디)
                                _info_db1 = Land_load._search_customer(_장지아이디)
                                if len(_info_db) == 0:
                                    안치고인아이디 = ""
                                    Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일, 안치고인아이디,_장지아이디,계약방식,주소)
                                    st.session_state.Contactdata = Contact_load._view_customers()
                                if len(_info_db1) == 0:
                                    안치고인아이디 = ""
                                    Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일, 안치고인아이디,_장지아이디,계약방식,주소)
                                    st.session_state.Contactdata = Contact_load._view_customers()
                                if len(_info_db) > 0:
                                    안치고인아이디 = _info_db[0][1]
                                    안치고인명 = _info_db[0][2]
                                    출생일 = _info_db[0][3]
                                    임종일 = _info_db[0][4]
                                    안치일 = _info_db[0][6]
                                    안치노트 = _info_db[0][8]
                                    Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,_장지아이디,계약방식,주소)
                                    Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,_장지아이디,안치일,계약자아이디,안치노트)
                                    st.session_state.Contactdata = Contact_load._view_customers()
                                    st.session_state.landhumandata = Landhuman_load._view_customers()
                                if len(_info_db1) > 0:
                                    장지분류 = _info_db1[0][2]
                                    장지구성 = _info_db1[0][3]
                                    계약종료일 = ""
                                    분양가 = _info_db1[0][8]
                                    관리비 = _info_db1[0][9]
                                    노트 = _info_db1[0][10]
                                    Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,_장지아이디,계약방식,주소)
                                    Land_load._update_customer(_장지아이디,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                    st.session_state.Contactdata = Contact_load._view_customers()
                                    st.session_state.landdata = Land_load._view_customers()
                                st.session_state.Contactdialogshow1 = False
                                st.experimental_rerun()

class Landhuman_loadUI():
    def _Register_UI():
        col1,col2,col3,col4,col5 = st.columns([1,0.5,0.5,1,1])
        #with col1:
            #col1.markdown("""
                #<style>
                #.big-font {
                    #font-size:25px !important;
                #}
                #</style>
                #""", unsafe_allow_html=True)
            #st.markdown('<p class="big-font">안치고인정보</p>',unsafe_allow_html=True)
        with col2:
            with stylable_container(key="Landhuman_with_border",css_styles=["""{position:fixed;right: 500px; top:35px;}""",],):
                고인명분류 = st.selectbox('',('안치고인명','안치고인ID'))
        if 고인명분류 == "안치고인명":
            with col3:
                with stylable_container(key="Landhumaninformation",css_styles=["""{position:fixed;right: 259px; top:35px;}""",],):
                    안치고인명값 = st.text_input("")
            with col4:
                with stylable_container(key="LandhumaSearch",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 157px; top:70px; width: 100px;}""",],):
                    if st.button(" 검색 "):
                        st.session_state.landhumandata = Landhuman_load._search_customerV(안치고인명값) 
        
        if 고인명분류 == "안치고인ID":
            with col3:
                with stylable_container(key="Landhumaninformation",css_styles=["""{position:fixed;right: 259px; top:35px;}""",],):
                    안치고인아이디 = st.text_input("")
            with col4:
                with stylable_container(key="LandhumaSearch",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 156px; top:70px; width: 100px;}""",],):
                    if st.button(" 검색 "):
                        st.session_state.landhumandata = Landhuman_load._search_customerVV(안치고인아이디)
        with col5:
            with stylable_container(
                key="LandhumanRegister",css_styles=["""button {border: solid .1em #292746;color: #000;position:fixed;right: 20px; top:70px;width: 130px;}""",],):
                    if st.button("안치고인등록"):
                        st.session_state.Landhumandialogshow = True
                        st.experimental_rerun()
    
    def _dialog_container():
        if st.session_state.Landhumandialogshow == True:
            Landhuman_dialog_container = float_dialog(st.session_state.Landhumandialogshow,width=1.2)
            with Landhuman_dialog_container:
                dt, dt1 = st.columns([0.2,0.2])
                with dt:
                    with stylable_container(
                        key="Land",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            width: 50px;
                        }
                        """,
                        ],  
                    ):
                        st.header("안치고인")
                with dt1:
                    with stylable_container(
                        key="Close",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;right: 35px; top:55px;
                            width: 50px;
                        }
                        """,
                        ],
                    ):
                        if st.button("X"):
                            st.session_state.Landhumandialogshow = False
                            st.experimental_rerun()
                
                dc1,dc2,dc3,dc4 = st.columns([0.2,0.2,0.2,0.2])
                dc5,dc6,dc7,dc8 = st.columns([0.09,0.09,0.09,0.2])
                dc9,dc10 = st.columns([0.045,0.2])
                with dc1:
                    with stylable_container(
                        key="ContactID",
                        css_styles=[
                            """
                            button {
                                border: solid .1em #292746;
                                #border-radius: 20px;
                                color: #000;
                                #background-color: #292746;
                                position:fixed;
                                #width: 50px;
                            }
                            """,
                        ],  
                    ):
                        안치고인아이디 = st.text_input("안치고인ID")
                with dc2:
                    with stylable_container(
                        key="ContactName",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        안치고인명 = st.text_input("안치고인명")
                with dc3:
                    with stylable_container(
                        key="ContactTelephone",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        출생일 = st.text_input("출생일")
                with dc4:
                    with stylable_container(
                        key="Contactemail",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        임종일 = st.text_input("임종일")
                with dc5:
                    with stylable_container(
                        key="Contactdate",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약자ID = st.text_input("계약자ID")
                with dc6:
                    with stylable_container(
                        key="ContactLandID",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지ID = st.text_input("장지ID")
                with dc7:
                    with stylable_container(
                        key="ContactType",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        안치일 = st.text_input("안치일")
                with dc8:
                    with stylable_container(
                        key="ContactAddress",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        노트값 = st.text_input("Note")
                with dc9:
                    with stylable_container(
                        key="Contactdelete",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                       if st.button("안치고인삭제"):
                           Landhuman_load._delete_customer(장지ID)
                           st.session_state.landhumandata = Landhuman_load._view_customers()
                           st.session_state.Landhumandialogshow = False
                           st.experimental_rerun()
                with dc10:
                    with stylable_container(
                        key="ContactConfirm",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            #position:fixed; 
                            width: 100px;
                        }
                        """,
                        ],
                    ):
                        if st.button("Confirm"):
                            st.session_state.Landhumanindexcnt += 1
                            if 안치고인아이디:
                                계약자아이디 = ""
                                노트 = ""
                                Landhuman_load._add_customer(st.session_state.Landhumanindexcnt,안치고인아이디,안치고인명,출생일,임종일,장지ID,안치일,계약자아이디,노트)
                                Landhuman_Info_load._info_init_write(str(st.session_state.Landhumanindexcnt))
                                st.session_state.landhumandata = Landhuman_load._view_customers()
                            
                            _info_db = Contact_load._search_customer(장지ID)
                            _info_db1 = Land_load._search_customer(장지ID)
                            if len(_info_db) > 0:
                                계약자아이디 = _info_db[0][1]
                                계약자명 = _info_db[0][2]
                                연락처 = _info_db[0][3]
                                이메일 = _info_db[0][4]
                                계약일 = _info_db[0][5]
                                계약방식 = _info_db[0][8]
                                주소 = _info_db[0][9]
                                Contact_load._update_customer(계약자아이디,계약자명,연락처,이메일,계약일,안치고인아이디,장지ID,계약방식,주소)
                                st.session_state.Contactdata = Contact_load._view_customers()
                            
                            if len(_info_db1) > 0:    
                                장지분류 = _info_db1[0][2]
                                장지구성 = _info_db1[0][3]
                                계약종료일 = ""
                                분양가 = ""
                                관리비 = _info_db1[0][9]
                                노트 = _info_db1[0][10]
                                Land_load._update_customer(장지ID,장지분류,장지구성,계약자아이디,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                st.session_state.landdata = Land_load._view_customers()
                            st.session_state.Landhumandialogshow = False
                            st.experimental_rerun()
    
    def _dialog_containerV(안치고인아이디값,안치고인명값,출생일값,임종일값,계약자아이디값,장지아이디값,안치일값,안치노트값):
        if st.session_state.Landhumandialogshow1 == True:
            Landhuman_dialog_container = float_dialog(st.session_state.Landhumandialogshow1,width=1.2)
            with Landhuman_dialog_container:
                dt, dt1 = st.columns([0.2,0.2])
                with dt:
                    with stylable_container(
                        key="Land",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            width: 50px;
                        }
                        """,
                        ],  
                    ):
                        st.header("안치고인")
                with dt1:
                    with stylable_container(
                        key="Close",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;right: 35px; top:55px;
                            width: 50px;
                        }
                        """,
                        ],
                    ):
                        if st.button("X"):
                            st.session_state.Landhumandialogshow1 = False
                            st.experimental_rerun()
                
                dc1,dc2,dc3,dc4 = st.columns([0.2,0.2,0.2,0.2])
                dc5,dc6,dc7,dc8 = st.columns([0.09,0.09,0.09,0.2])
                dc9,dc10 = st.columns([0.045,0.2])
                with dc1:
                    with stylable_container(
                        key="ContactID",
                        css_styles=[
                            """
                            button {
                                border: solid .1em #292746;
                                #border-radius: 20px;
                                color: #000;
                                #background-color: #292746;
                                position:fixed;
                                #width: 50px;
                            }
                            """,
                        ],  
                    ):
                        안치고인아이디 = st.text_input("안치고인ID",안치고인아이디값)
                with dc2:
                    with stylable_container(
                        key="ContactName",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        안치고인명 = st.text_input("안치고인명",안치고인명값)
                with dc3:
                    with stylable_container(
                        key="ContactTelephone",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        출생일 = st.text_input("출생일",출생일값)
                with dc4:
                    with stylable_container(
                        key="Contactemail",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        임종일 = st.text_input("임종일",임종일값)
                with dc5:
                    with stylable_container(
                        key="Contactdate",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        계약자ID = st.text_input("계약자ID",계약자아이디값)
                with dc6:
                    with stylable_container(
                        key="ContactLandID",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        장지ID = st.text_input("장지ID",장지아이디값)
                with dc7:
                    with stylable_container(
                        key="ContactType",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        안치일 = st.text_input("안치일",안치일값)
                with dc8:
                    with stylable_container(
                        key="ContactAddress",
                        css_styles=[
                        """
                        button {
                            border: solid .1em #292746;
                            #border-radius: 20px;
                            color: #000;
                            #background-color: #292746;
                            position:fixed;
                            #width: 50px;
                        }
                        """,
                        ],  
                    ):
                        노트값 = st.text_input("Note",안치노트값)
                with dc9:
                    with stylable_container(key="Contactdelete",css_styles=["""button {border: solid .1em #292746;color: #000;width: 150px;}""",],):
                        if st.button("안치고인삭제"):
                            Landhuman_load._delete_customer(장지ID)
                            st.session_state.landhumandata = Landhuman_load._view_customers()
                            st.session_state.Landhumandialogshow1 = False
                            st.experimental_rerun()
                           
                with dc10:
                    with stylable_container(key="ContactConfirm",css_styles=["""button {border: solid .1em #292746;color: #000; position:fixed; right:50px; width: 100px;}""",],):
                        if st.button("Confirm"):
                            if 안치고인아이디:
                                _info_db = Contact_load._search_customer(장지ID)
                                _info_db1 = Land_load._search_customer(장지ID)
                                if len(_info_db) == 0:
                                    Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지ID,안치일,계약자ID,노트값)
                                    st.session_state.landhumandata = Landhuman_load._view_customers()
                                if len(_info_db1) == 0:
                                    Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지ID,안치일,계약자ID,노트값)
                                    st.session_state.landhumandata = Landhuman_load._view_customers()
                                if len(_info_db) > 0:
                                    계약자명 = _info_db[0][2]
                                    연락처 = _info_db[0][3]
                                    이메일 = _info_db[0][4]
                                    계약일 =  _info_db[0][5]
                                    계약방식 = _info_db[0][8]
                                    주소 = _info_db[0][9]
                                    Contact_load._update_customer(계약자ID,계약자명,연락처,이메일,계약일,안치고인아이디,장지ID,계약방식,주소)
                                    Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지ID,안치일,계약자ID,노트값)
                                    st.session_state.Contactdata = Contact_load._view_customers()
                                    st.session_state.landhumandata = Landhuman_load._view_customers()
                                if len(_info_db1) > 0:
                                    장지분류 = _info_db1[0][2]
                                    장지구성 = _info_db1[0][3]
                                    계약종료일 = ""
                                    분양가 = _info_db1[0][8]
                                    관리비 = _info_db1[0][9]
                                    노트 = _info_db1[0][10]
                                    Land_load._update_customer(장지ID,장지분류,장지구성,계약자ID,안치고인아이디,계약일,계약종료일,분양가,관리비,노트)
                                    Landhuman_load._update_customer(안치고인아이디,안치고인명,출생일,임종일,장지ID,안치일,계약자ID,노트값)
                                    st.session_state.landdata = Land_load._view_customers()
                                    st.session_state.landhumandata = Landhuman_load._view_customers()
                                st.session_state.Landhumandialogshow1 = False
                                st.experimental_rerun()

                            
        
                            
                            
                
                

