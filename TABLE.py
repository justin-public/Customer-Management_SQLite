import sqlite3
import pandas as pd
import numpy as np
from streamlit_float import *
from streamlit_option_menu import option_menu
from st_aggrid_pro import AgGridPro, GridUpdateMode, JsCode
from st_aggrid_pro.grid_options_builder import GridOptionsBuilder
from streamlit_extras.stylable_container import stylable_container

class Land_loadTABLE():
    landjs = JsCode("""
        function(value) {
            //alert(value.node.data);
            console.log(value.node.data);
            let api = value.api;
            let sel = api.getSelectedRows();
            var filter = value.data;
            //console.log("select_rows 값:", sel);
            //alert("select_rows 값:", sel);
            //Here the filter variable that I want to return in Streamlit
            //Unselect all rows
            api.deselectAll();
        };
        """)

    def clicked_landid_Info():
        #if "land_show_container" not in st.session_state:
            #st.session_state.land_show_container = False
        #st.session_state.landshowcnt += 1
        return r"""class BtnCellRenderer {
            init(params) {
                this.params = params;
                <span>
                <style>
                    .btn_add {
                    }
                </style>
                <button id='click-button' 
                    class="btn" 
                    >&#x2193; Add</button>
                </span>
            `;
            }
            getGui() {
                //return this.eGui;
            }
        };
        """

    def _interactive_table(df: pd.DataFrame):
        """Creates an st-aggrid interactive table based on a dataframe.
        Args:
        df (pd.DataFrame): Source dataframe
        Returns:
        dict: The selected row
        """
        options = GridOptionsBuilder.from_dataframe(
            df, enableRowGroup=True, enableValue=True, enablePivot=True
        )
        options.configure_column("ID", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("장지분류", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("장지구성", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("계약자아이디", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("안치고인아이디", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("계약일", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("계약종료일", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("분양가", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("관리비", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("노트", cellStyle={'color': 'black'},onCellClicked=Land_loadTABLE.landjs,cellRenderer=Land_loadTABLE.clicked_landid_Info())
        options.configure_column("장지아이디", cellStyle={'color': 'blue'},headerTooltip='Click to see cell data')
        options.configure_side_bar()
        options.configure_selection("single")
        selection = AgGridPro(
            df,
            enable_enterprise_modules=True,
            gridOptions=options.build(),
            theme="balham",
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            allow_unsafe_jscode=True,
            height=2000,
        )
        return selection

class Contact_loadTABLE():
    landjs = JsCode("""
        function(value) {
            //alert(value.node.data);
            console.log(value.node.data);
            let api = value.api;
            let sel = api.getSelectedRows();
            var filter = value.data;
            //console.log("select_rows 값:", sel);
            //alert("select_rows 값:", sel);
            //Here the filter variable that I want to return in Streamlit
            //Unselect all rows
            api.deselectAll();
        };
        """)
    def clicked_landid_Info():
        #if "land_show_container" not in st.session_state:
            #st.session_state.land_show_container = False
        #st.session_state.landshowcnt += 1
        return r"""class BtnCellRenderer {
            init(params) {
                this.params = params;
                <span>
                <style>
                    .btn_add {
                    }
                </style>
                <button id='click-button' 
                    class="btn" 
                    >&#x2193; Add</button>
                </span>
            `;
            }
            getGui() {
                //return this.eGui;
            }
        };
        """
    def _interactive_table(df: pd.DataFrame):
        """Creates an st-aggrid interactive table based on a dataframe.
        Args:
        df (pd.DataFrame): Source dataframe
        Returns:
        dict: The selected row
        """
        options = GridOptionsBuilder.from_dataframe(
            df, enableRowGroup=True, enableValue=True, enablePivot=True
        )
        options.configure_column("ID", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("계약자명", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("연락처", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("이메일", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("계약일", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("안치고인아이디", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("장지아이디", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("계약방식", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("주소", cellStyle={'color': 'black'},onCellClicked=Contact_loadTABLE.landjs,cellRenderer=Contact_loadTABLE.clicked_landid_Info())
        options.configure_column("계약자아이디", cellStyle={'color': 'blue'},headerTooltip='Click to see cell data')
        options.configure_side_bar()
        options.configure_selection("single")
        selection = AgGridPro(
            df,
            enable_enterprise_modules=True,
            gridOptions=options.build(),
            theme="balham",
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            allow_unsafe_jscode=True,
            height=2000,
        )
        return selection

class Landhuman_loadTABLE():
    landjs = JsCode("""
        function(value) {
            //alert(value.node.data);
            console.log(value.node.data);
            let api = value.api;
            let sel = api.getSelectedRows();
            var filter = value.data;
            //console.log("select_rows 값:", sel);
            //alert("select_rows 값:", sel);
            //Here the filter variable that I want to return in Streamlit
            //Unselect all rows
            api.deselectAll();
        };
        """)
    def clicked_landid_Info():
        #if "land_show_container" not in st.session_state:
            #st.session_state.land_show_container = False
        #st.session_state.landshowcnt += 1
        return r"""class BtnCellRenderer {
            init(params) {
                this.params = params;
                <span>
                <style>
                    .btn_add {
                    }
                </style>
                <button id='click-button' 
                    class="btn" 
                    >&#x2193; Add</button>
                </span>
            `;
            }
            getGui() {
                //return this.eGui;
            }
        };
        """
    def _interactive_table(df: pd.DataFrame):
        """Creates an st-aggrid interactive table based on a dataframe.
        Args:
        df (pd.DataFrame): Source dataframe
        Returns:
        dict: The selected row
        """
        options = GridOptionsBuilder.from_dataframe(
            df, enableRowGroup=True, enableValue=True, enablePivot=True
        )
        options.configure_column("ID", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        #options.configure_column("안치고인아이디", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("안치고인명", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("출생일", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("임종일", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("장지아이디", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("안치일", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("계약자아이디", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("노트", cellStyle={'color': 'black'},onCellClicked=Landhuman_loadTABLE.landjs,cellRenderer=Landhuman_loadTABLE.clicked_landid_Info())
        options.configure_column("안치고인아이디", cellStyle={'color': 'blue'},headerTooltip='Click to see cell data')
        options.configure_side_bar()
        options.configure_selection("single")
        selection = AgGridPro(
            df,
            enable_enterprise_modules=True,
            gridOptions=options.build(),
            theme="balham",
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            allow_unsafe_jscode=True,
            height=2000,
        )
        return selection
