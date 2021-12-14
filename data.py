import pandas as pd
import sodapy

client = sodapy.Socrata("data.cdc.gov", None)
results = client.get("8xkx-amqh", limit=20)
test = pd.DataFrame.from_records(results)

#%%

display(test)

