import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data_daily = pd.read_csv('Daily_registration_subscription_counts.csv')

# Create a Streamlit web app
st.title("User Registration and Subscription Dashboard - Daily")

# Group data by date and calculate the number of registered and subscribed users
daily_counts = data_daily.groupby('d_date').agg({'registered_users': 'sum', 'subscribed_users': 'sum'}).reset_index()

# Line chart to visualize daily counts
fig_daily = px.line(daily_counts, x='d_date', y=['registered_users', 'subscribed_users'], title='Daily User Registration and Subscription')
fig_daily.update_layout(xaxis_title='Date', yaxis_title='Number of Users')

# Display the daily plot in the Streamlit app
st.plotly_chart(fig_daily)

###############################################################################################


data_weekly = pd.read_csv('Week_registration_subscription_counts.csv')

# Create a Streamlit web app
st.title("User Registration and Subscription Dashboard - Weekly")

# Display weekly counts as a table
st.header("Weekly User Registration and Subscription Counts")
st.dataframe(data_weekly)

# Line chart to visualize weekly counts
fig_weekly = px.line(data_weekly, x='week', y=['registered_users', 'subscribed_users'], title='Weekly User Registration and Subscription')
fig_weekly.update_layout(xaxis_title='Week', yaxis_title='Number of Users')

# Display the weekly plot in the Streamlit app
st.plotly_chart(fig_weekly)
#####################################################

data_monthly = pd.read_csv('M_registration_subscription_counts.csv')

# Create a Streamlit web app
st.title("User Registration and Subscription Dashboard - Monthly")

# Display monthly counts as a table
st.header("Monthly User Registration and Subscription Counts")
st.dataframe(data_monthly)

# Line chart to visualize monthly counts
fig_monthly = px.line(data_monthly, x='month', y=['registered_users', 'subscribed_users'], title='Monthly User Registration and Subscription')
fig_monthly.update_layout(xaxis_title='Month', yaxis_title='Number of Users')

# Display the monthly plot in the Streamlit app
st.plotly_chart(fig_monthly)
#############################################################################

data_yearly = pd.read_csv('year_registration_subscription_counts.csv')

# Create a Streamlit web app
st.title("User Registration and Subscription Dashboard - Yearly")

# Display yearly counts as a table
st.header("Yearly User Registration and Subscription Counts")
st.dataframe(data_yearly)

# Line chart to visualize yearly counts
fig_yearly = px.line(data_yearly, x='year', y=['registered_users', 'subscribed_users'], title='Yearly User Registration and Subscription')
fig_yearly.update_layout(xaxis_title='Year', yaxis_title='Number of Users')

# Display the yearly plot in the Streamlit app
st.plotly_chart(fig_yearly)
import os
path=os.getcwd()
print(path)
###############################################################

df = pd.read_csv('10k AI initiative.csv')

# Filter for users who have completed courses
completed_users = df[df['completed_courses_count'] > 0]

# Display the Streamlit app
st.title("Users Dashboard")
st.dataframe(completed_users)

# Additional Information
st.subheader("Additional Information:")
st.write(f"Total Users: {len(df)}")
st.write(f"Total Completed Courses: {completed_users['completed_courses_count'].sum()}")

# Visualize completed courses count
st.subheader("Completed Courses Count:")
completed_courses_chart = st.bar_chart(completed_users[['user_id', 'completed_courses_count']])
##################################4##############################################
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('user_courses.csv')

if 'user_id' in df.columns and 'course_id' in df.columns:
    # Group data by user_id and count the number of currently learning courses
    currently_learning_courses = df.groupby('user_id')['course_id'].nunique().reset_index()
    currently_learning_courses.columns = ['user_id', 'currently_learning_courses_count']

    # Display the Streamlit app
    st.title("Users Currently Learning Courses Dashboard")

    # Display the table
    st.subheader("Currently Learning Courses Count:")
    st.dataframe(currently_learning_courses)

    # Visualize currently learning courses count
    st.subheader("Bar Chart:")
    bar_chart = px.bar(
        currently_learning_courses,
        x='user_id',
        y='currently_learning_courses_count',
        labels={'currently_learning_courses_count': 'Number of Courses'},
        title='Number of Currently Learning Courses per User'
    )
    st.plotly_chart(bar_chart)
else:
    st.error("Column 'user_id' or 'course_id' not found in the dataset.")
    ########################3
   
df = pd.read_csv('this_y_ Completed_Courses.csv')


if 'user_id' in df.columns and 'completed_courses_count' in df.columns:
    # Display the Streamlit app
    st.title("Users and Completed Courses Dashboard this year")

    # Display the table
    st.subheader("Completed Courses Count:")
    st.dataframe(df[['user_id', 'completed_courses_count']])

    # Visualize completed courses count
    st.subheader("Bar Chart:")
    bar_chart = px.bar(
        df,
        x='user_id',
        y='completed_courses_count',
        labels={'completed_courses_count': 'Number of Completed Courses'},
        title='Number of Completed Courses per User this year'
    )
    st.plotly_chart(bar_chart)
else:
    st.error("Column 'user_id' or 'completed_courses_count' not found in the dataset.")
    ####################################
    
df = pd.read_csv('this_M_ Completed_Courses.csv')


if 'user_id' in df.columns and 'completed_courses_count' in df.columns:
    # Display the Streamlit app
    st.title("Users and Completed Courses Dashboard this  month ")

    # Display the table
    st.subheader("Completed Courses Count:")
    st.dataframe(df[['user_id', 'completed_courses_count']])

    # Visualize completed courses count
    st.subheader("Bar Chart:")
    bar_chart = px.bar(
        df,
        x='user_id',
        y='completed_courses_count',
        labels={'completed_courses_count': 'Number of Completed Courses'},
        title='Number of Completed Courses per User this  month.'
    )
    st.plotly_chart(bar_chart)
else:
    st.error("Column 'user_id' or 'completed_courses_count' not found in the dataset.")
    #################################5%######################################################
data = pd.read_csv('users_com_5.csv')

st.title("User Information Dashboard")

# User search input
user_id_search = st.text_input("Enter User ID:")

# Check if user_id is provided
if user_id_search:
    # Filter data for the specified user_id
    user_data = data[data['user_id'] == int(user_id_search)]

    # Check if user_data is empty (no user found)
    if user_data.empty:
        st.warning(f"No user found with User ID: {user_id_search}")
    else:
        # Display user information
        st.subheader("User Information:")
        st.table(user_data[['user_id', 'subscribed', 'subscription_date', 'coupon', 'registration_date',
                            'last_edit_date', 'level', 'gender', 'age', 'study_degree', '10k_AI_initiative']])

        # Display completed courses information
        st.subheader("Completed Courses:")
        st.table(user_data[['course_id', 'course_title', 'completed_chapter_id', 'completed_lesson_id',
                            'completed_course_degree', 'completed_course_completion_date']])

        # Display capstones information
        st.subheader("Capstones:")
        st.table(user_data[['capstone_chapter_id', 'capstone_lesson_id', 'capstone_degree', 'lock',
                            'last_submission_date', 'reviewed', 'revision_date']])
else:
    st.warning("Enter a User ID to search.")
    #################66666666666666666666666666666666666666


eval_df = pd.read_csv("Capstones evaluated this month.csv")

st.title("Capstone Evaluations Dashboard")

# Display the data table
st.write("Capstone Evaluations This Month:")
st.write(eval_df)

# Create a bar chart to visualize the data
fig, ax = plt.subplots()
ax.bar(eval_df['admin_id'], eval_df['evaluations_this_month'])
ax.set_xlabel('Admin ID')
ax.set_ylabel('Number of Evaluations This Month')
ax.set_title('Capstone Evaluations by Admin This Month')

# Display the chart in the Streamlit app
st.pyplot(fig)

eval_df2 = pd.read_csv("Capstones evaluated this year.csv")

st.title("Capstone Evaluations Dashboard this year")

# Display the data table
st.write("Capstone Evaluations This year:")
st.write(eval_df2)

# Create a bar chart to visualize the data
fig2, ax = plt.subplots()
ax.bar(eval_df2['admin_id'], eval_df2['evaluations_this_year'])
ax.set_xlabel('Admin ID')
ax.set_ylabel('Number of Evaluations This Year')
ax.set_title('Capstone Evaluations by Admin This Year')

# Display the chart in the Streamlit app
st.pyplot(fig2)

   
