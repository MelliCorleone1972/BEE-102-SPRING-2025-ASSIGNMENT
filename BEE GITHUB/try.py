import gzip
import pandas as pd

with gzip.open("data/filtered.tsv.gz", "rt") as f:
    expression_df = pd.read_csv(f, sep="\t")
    print(expression_df.columns[:10])  # print the first few column names