# import lib 
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# create connection
import sqlalchemy
engine = sqlalchemy.create_engine("mssql+pyodbc://itc:tl2201_5@10.2.32.13/Tlist?driver=SQL Server?Trusted_Connection=yes",
                                  echo=False)
conn = engine.connect()

# list of features
numeric_cols = ['Amp3', 'Vel3_ms', 'Amp4','Vel4_ms','Amp5','Vel5_ms','Amp6','Vel6_ms',
                'Amp7','Vel7_ms','Amp8','Vel8_ms', 'Thickness']

# connection to BD
features = pd.read_sql("SELECT TOP 1 id_rulon, p.Amp3, p.Vel3_ms, p.Amp4, p.Vel4_ms, p.Amp5, \
p.Vel5_ms, p.Amp6, p.Vel6_ms, p.Amp7, p.Vel7_ms, p.Amp8, p.Vel8_ms, \
t.WCard, t.Rulon, t.Partia, t.charge, t.CorrectionCode, t.Width, t.Thickness, t.coilLength,  s.koef_name \
FROM Pull1700 p \
left join TLTolsh1700 t on t.id=p.id_rulon \
left join Pull1700_sprav s on s.koef_id=p.Pull_prognosis \
order by p.id desc", conn)

X = features[numeric_cols]

# normalization
with open('scale', 'rb') as file2:
    loaded_scale = pickle.load(file2)
X_scaled = loaded_scale.transform(X)


# prediction
with open('model', 'rb') as file1:
    loaded_model = pickle.load(file1)
result = loaded_model.predict(X_scaled)


# create additional array
d = {'id': features.id_rulon, 'pull_prognosis': result+1}
df = pd.DataFrame(data=d)

# add record
df.to_sql("pull1700_prognosis", index=False, con=conn, if_exists="append", method=None)

