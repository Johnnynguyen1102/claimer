import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from claimer import paragraph
import os

if __name__ == "__main__":
    import json

    input_dir = "/Users/cbadenes/investigation/Fake_News/data/fake_news_corpus_spanish/news"
    output_dir = "/Users/cbadenes/investigation/Fake_News/data/fake_news_corpus_spanish/claims"

    if not os.path.exists(output_dir):    
        os.makedirs(output_dir)

    file = open(f"{input_dir}/full_date.json")
    data = json.load(file)

    counter = -1
    for news in data:
        counter += 1
        json_path = f"{output_dir}/{news['id']}.json"
        if (os.path.isfile(json_path)):
            continue
        print(f"[{counter}]processing news",news['id'])        
        facts = paragraph.get_claims(news['claim'])
        news['facts'] = facts        
        with open(json_path , "w") as outfile:
            json_out = json.dumps(news, ensure_ascii=False, indent=4)
            outfile.write(json_out)    
            print(json_out)

    file.close() 