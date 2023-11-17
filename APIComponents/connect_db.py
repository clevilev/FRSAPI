import psycopg2


def DbConnector():
    conn = psycopg2.connect(user="frs_db_admin",
                            password="FRSAdmin@2023",
                            host="203.161.57.165",
                            port="5432",
                            database="fund_raising")

    return conn
