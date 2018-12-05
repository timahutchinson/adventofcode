import re
from collections import Counter
from operator import itemgetter

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)

pattern = re.compile("^\[(\d{4}\-\d{2}\-\d{2} \d{2}:\d{2})\] ([\w# ]+)")
with open("../../../data/2018/4/data.txt") as f:
    lines = [pattern.findall(line.strip())[0] for line in f.readlines()]

df = pd.DataFrame(lines, columns=["datetime", "event"])
df = df.sort_values(by="datetime")
df["id"] = [" ".join(val.split()[:2]) if "Guard" in val else np.nan for val
            in df["event"]]
df["id"].fillna(method="ffill", inplace=True)
df["ts_minutes"] = [int(val[-2:]) if val[-5] == '0' else int(val[-2:]) - 60
                    for val in df["datetime"]]
df["prev_ts_minutes"] = df["ts_minutes"].shift(1)
df["tdelta"] = df["ts_minutes"] - df["ts_minutes"].shift(1)
df.dropna(inplace=True)
df["minutes_asleep"] = [list(range(int(val[0]), int(val[1]))) for val in
                        zip(df["prev_ts_minutes"], df["ts_minutes"])]
pattern = re.compile("wakes")
df2 = df[[True if pattern.match(val) else False for val in df["event"]]]
df3 = df2.groupby("id").agg({"minutes_asleep": "sum"})
df3["max_counts"] = [sorted(Counter(val).items(), key=itemgetter(1))[-1][1]
                     for val in df3["minutes_asleep"]]
df3["max_minute"] = [sorted(Counter(val).items(), key=itemgetter(1))[-1][0]
                     for val in df3["minutes_asleep"]]
df3 = df3.reset_index()
s = df3.sort_values("max_counts", ascending=False)[["id", "max_minute"]].values
print(int(s[0][0].split("#")[1]) * s[0][1])
