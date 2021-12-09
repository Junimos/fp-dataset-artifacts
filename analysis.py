import json
from collections import Counter

# (label 0 is "entailed", 1 is "neutral", and 2 is "contradiction")
def analyze_eval():

    #opening eval file
    file_name = "bad_0.5_eval_output/eval_predictions.jsonl"
    data = open(file_name)

    #declare vars
    truth_counter = Counter()
    pred_counter = Counter()
    stats = Counter()

    #populate vars
    for datum in data:
        example = json.loads(datum)
        truth = example['label']
        pred = example['predicted_label']
        truth_counter[truth] += 1
        pred_counter[pred] += 1
        stats[(pred, truth == pred)] += 1

        
        

    #print results
    print("gold labels")
    print(truth_counter)
    print()
    print("predictions")
    print(pred_counter)
    print()
    print("stats")
    print(stats)

if __name__ == "__main__":
    analyze_eval()