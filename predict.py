THRESHOLD = 0.5
def predict(scores): 
    best_label = max(scores, key=scores.get)
    if scores[best_label] < THRESHOLD:
        return "unknown"
    return best_label
