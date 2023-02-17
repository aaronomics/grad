from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import openai

categories = ['rec.sport.baseball', 'rec.sport.hockey']
sports_dataset = fetch_20newsgroups(subset='train', shuffle=True, random_state=42, categories=categories)


print(sports_dataset['data'][0])

sports_dataset.target_names[sports_dataset['target'][0]]

len_all, len_baseball, len_hockey = len(sports_dataset.data), len([e for e in sports_dataset.target if e == 0]), len([e for e in sports_dataset.target if e == 1])
print(f"Total examples: {len_all}, Baseball examples: {len_baseball}, Hockey examples: {len_hockey}")

labels = [sports_dataset.target_names[x].split('.')[-1] for x in sports_dataset['target']]
texts = [text.strip() for text in sports_dataset['data']]
df = pd.DataFrame(zip(texts, labels), columns = ['prompt','completion']) #[:300]
df.head()

df.to_json("sport2.jsonl", orient='records', lines=True)

# openai.api_key = "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"



# run these commands in terinal I think

#openai tools fine_tunes.prepare_data -f sport2.jsonl -q



#openai --api-key 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 api fine_tunes.create -t "sport2_prepared_train.jsonl" -v "sport2_prepared_valid.jsonl" --compute_classification_metrics --classification_positive_class " baseball" -m ada





