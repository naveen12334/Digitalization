import streamlit as st
import pyodbc
import pandas as pd

# Function to retrieve data from SQL
def get_sql_data():
    server = '4.247.162.209'
    database = 'Project A'
    username = 'naveengupta116'
    password = 'N@veen123456'

    # Establish connection
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connection_string)

    # Example query
    query = "SELECT massBrix, crystalSize, stmPress, vapPress, massTemp, massLvl, HWTemp, tnkLvl, dateTime FROM PanDataA"

    # Read SQL data into a DataFrame
    df = pd.read_sql(query, conn)

    # Close the connection
    conn.close()

    # Convert the DateTimeColumn to a datetime format if it's not already in that format
    df['dateTime'] = pd.to_datetime(df['dateTime'])

    return df

def login(session_state):
    st.title("Login for Ipro India Digitalization Report")
    # Define valid username-password pairs (for demo purposes)
    valid_credentials = {
        "naveen": "naveen",
        "naresh": "naresh"
    }

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check if the credentials are valid
    if st.button("Login"):
        if username in valid_credentials and password == valid_credentials[username]:
            st.success(f"Logged in as {username.capitalize()}")
            session_state.logged_in = True
        else:
            st.error("Invalid credentials")


def show_statistics(data,session_state):
    st.subheader('Key Performance Indicators')

    # Calculating statistics
    min_brix = data['massBrix'].min()
    max_brix = data['massBrix'].max()
    avg_brix = data['massBrix'].mean()
    min_crystalSize = data['crystalSize'].min()
    max_crystalSize = data['crystalSize'].max()
    avg_crystalSize = data['crystalSize'].mean()
    min_stmPress = data['stmPress'].min()
    max_stmPress = data['stmPress'].max()
    avg_stmPress = data['stmPress'].mean()
    # ... (similar calculations for other metrics)

    # Displaying statistics in separate sections
    st.markdown('### Massecutive Brix ')
    st.write(f"Minimum Massecutive Brix: {min_brix}")
    st.write(f"Maximum Massecutive Brix: {max_brix}")
    st.write(f"Average Massecutive Brix: {avg_brix}")
    st.markdown('### Crystal Size')
    st.write(f"Minimum Crystal Size: {min_crystalSize}")
    st.write(f"Maximum Crystal Size: {max_crystalSize}")
    st.write(f"Average Crystal Size: {avg_crystalSize}")
    st.markdown('### Steam Pressure')
    st.write(f"Minimum Steam Pressure: {min_stmPress}")
    st.write(f"Maximum Steam Pressure: {max_stmPress}")
    st.write(f"Average Steam Pressure: {avg_stmPress}")

    if session_state.logged_in:
        if st.button("Logout"):
            session_state.logged_in = False
    # ... (display for other metrics)

def main():
    session_state = st.session_state
    if "logged_in" not in session_state:
        session_state.logged_in = False

    if not session_state.logged_in:
        login(session_state)
    else:
        st.title('Ipro India Digitalization Report')

        # Get data from SQL
        data = get_sql_data()

        # Display statistics in sections
        show_statistics(data,session_state)

        # After displaying statistics, show the KPI visualization if logged in
        #if session_state.logged_in:
            #st.title('KPI Visualization')'''
            # Add your KPI visualization code here

if __name__ == "__main__":
    main()
