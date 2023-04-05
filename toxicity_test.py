from detoxify import Detoxify

toxicity_model = Detoxify('unbiased')

print(toxicity_model.predict('''Yes, I cry a lot in bed. But no, not because of boys and love. Mostly because of money, my mom, friends, studies and why the hell am I not good enough...  😪a thread'''))