from transformers import pipeline


classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

candidate_labels = ['sensational', 'personal']

sequence_to_classify = '''🇺🇸#America

Horrifying footage shows the moment a football coach was shot dead during a Vallejo High School mass shooting.

The footage captured by a student shows the coach attempting to break up a fight before being gunned down by one of the students. https://t.co/wOvGp2IM3u'''

hypothesis_template = "The writing style of this text is {}"

print(classifier(sequence_to_classify, candidate_labels, multi_label=True, hypothesis_template=hypothesis_template))