import smtplib
import pandas as pd
import datetime as dt

# current date and time
today = dt.datetime.now()
# current month
month = today.month
# current day
day = today.day

# creating the tuple for today month and date
today_tuple = (month, day)
# Reading the csv file using pandas
birthday_info = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_info.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open("letter1.txt", mode="r") as letter_txt:
        content = letter_txt.read()
        final_content = content.replace("[NAME]", birthday_person["name"])
    # now sending an email to birthday person
    # Sender information
    my_email = "kunalbhatiya06@gmail.com"
    password = "wzzmlwyjynuldzec"

    # establish connection
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # secure connection by using starttls(Transport Layer Security)
        connection.starttls()
        # login in the connection
        connection.login(my_email, password)
        # send email
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shbishwesh@gmail.com",
            msg=f"Subject:Happy Birthday to you!\n\n{final_content}"
        )

