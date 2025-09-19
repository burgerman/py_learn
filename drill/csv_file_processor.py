import pandas as pd
use_cols=["instruction","Resume_test"]
df = pd.read_csv(filepath_or_buffer="/Users/wilfried/Downloads/updated_data_final_cleaned.csv", usecols=use_cols, delimiter=',')
df.to_csv("/Users/wilfried/Downloads/finetuning_resume_dataset.csv", index=False, header=True, encoding='utf-8', sep=',')