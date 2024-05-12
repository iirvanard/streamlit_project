import streamlit as st
from st_pages import hide_pages
from utils.authenticator import authenticators
import pandas as pd
from utils.st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode

st.set_page_config(layout="wide")
hide_pages(["streamlit_app", "auth"])
auth_ = authenticators()

if "logout" in st.query_params:
    st.success("Logout Sukses!")

logged_in = st.session_state.get('logged_in', False)


def main():
    st.header('This is a header with a divider', divider='gray')

    if "add_data_status" in st.query_params.keys(
    ):  # Fixing the conditional statement
        if st.query_params["add_data_status"] == "success":
            st.success("add data Sukses!")
        else:
            st.error("add data failed!")

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if st.session_state.submitted:
        st.header("input a data")
        email = st.text_input("email")
        email1 = st.text_input("email1")
        email2 = st.text_input("email2")
        if st.button("submit", key="submit_add_data"):
            st.session_state.submitted = False
            st.query_params.add_data_status = "success"
            st.rerun()
    sidebarButton()
    if st.sidebar.button("Logout"):
        st.query_params.logout = True
        auth_.logout()
        st.rerun()
    data = {
        'Name': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Miami', 'Miami',
            'Miami', 'Miami', 'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Miami', 'Miami', 'Miami', 'Miami'
        ],
        'Age': [
            25, 30, 35, 40, 45, 30, 35, 40, 45, 25, 30, 35, 40, 45, 30, 35, 40,
            45
        ],
        'City': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Miami', 'Miami',
            'Miami', 'Miami', 'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Miami', 'Miami', 'Miami', 'Miami'
        ],
        'City1': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Miami', 'Miami',
            'Miami', 'Miami', 'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Miami', 'Miami', 'Miami', 'Miami'
        ],
        'City2': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Miami', 'Miami',
            'Miami', 'Miami', 'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Miami', 'Miami', 'Miami', 'Miami'
        ],
        'City3': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Miami', 'Miami',
            'Miami', 'Miami', 'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Miami', 'Miami', 'Miami', 'Miami'
        ],
        'City4': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Miami', 'Miami',
            'Miami', 'Miami', 'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Miami', 'Miami', 'Miami', 'Miami'
        ]
    }
    df = pd.DataFrame(data)

    builder = GridOptionsBuilder.from_dataframe(df)
    builder.configure_pagination(enabled=True)
    builder.configure_selection(selection_mode='single', use_checkbox=True)
    grid_options = builder.build()

    st.header("data")
    return_value = AgGrid(
        df,
        gridOptions=grid_options,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        fit_columns_on_grid_load=True)

    if return_value.selected_rows is not None and not return_value.selected_rows.empty:
        st.header("Rows")
        st.table(return_value.selected_rows)
        st.header("plots")
        # Prepare data for bar chart
        bar_data = return_value.selected_rows.groupby('Name').size()
        st.bar_chart(bar_data)
    else:
        st.write("No row selected")


def sidebarButton():
    with st.sidebar:
        if (not st.session_state.submitted):
            open = st.button("add", key="add_open")
            if open:
                st.session_state.submitted = True
                st.rerun()
        else:
            close = st.button("close", key="add_close", type='primary')
            if close:
                st.session_state.submitted = False
                st.rerun()


if logged_in:

    main()

else:
    st.warning("You can access this page by signin! ")
    if st.button("Login", type="primary"):
        st.switch_page("pages/auth.py")
