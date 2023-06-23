import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from claimer import paragraph
import os

if __name__ == "__main__":
    import json

    input_dir = "../../data/fake_news_corpus_spanish/news"
    output_dir = "../../data/fake_news_corpus_spanish/claims"

    if not os.path.exists(output_dir):    
        os.makedirs(output_dir)

    file = open(f"{input_dir}/full_date.json")
    data = json.load(file)

    counter = 0
    for news in data:
        print(f"[{counter}]processing news",news['id'])
        counter += 1
        facts = paragraph.get_claims(news['claim'])
        news['facts'] = facts
        json_path = f"{output_dir}/{news['id']}.json"
        with open(json_path , "w") as outfile:
            json_out = json.dumps(news, ensure_ascii=False, indent=4)
            outfile.write(json_out)    
            print(json_out)
        break

    file.close() 