import pandas as pd
from datetime import datetime

def pos(df):
    return  abs(df) 

def timecalculator(data, date, carname):

    df = pd.DataFrame(data)

    print(df["car"].apply(pd.Series))
    df = pd.concat([df.drop(columns = "car"),df["car"].apply(pd.Series)], axis = 1)
    print(df.columns)

    df["car_in"] = pd.to_datetime(df["car_in"])
    df["car_out"] = pd.to_datetime(df["car_out"])

    df["difference"] = (df["car_in"] - df["car_out"]).dt.total_seconds() / 60

    df["difference"] = df["difference"].apply(pos)

    df["car_in"] = df["car_in"].dt.date
    df["car_out"] = df["car_out"].dt.date

    print(df)

    df1 = pd.DataFrame()
    df1["time"] = df.groupby(["car_in", "car_name"])["difference"].mean()
    df1.reset_index(inplace = True)
    print(df1)

    datet = datetime.strptime(date, '%Y-%m-%d')
    print(datet.date())
    print(carname)
    # print(df1[(df1["car_in"] == datet.date()) & (df1["car_name"]== str(carname))]["time"])
    try:
        result = int(df1[(df1["car_in"] == datet.date()) & (df1["car_name"]== carname)]["time"])
        print(result)
        return result

    except:
        return "no such record"