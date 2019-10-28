import numpy as np

def conduct_experiment(df, random_state=42):
    np.random.seed(random_state)
    df["value"] = 0
    sizes = df["trt"].value_counts()
    for lvl in df["trt"].unique():
        base = 100 + 30*np.random.randn()
        df.loc[df["trt"] == lvl, "value"] = base + 10*np.random.randn(sizes[lvl])
        
    return df
