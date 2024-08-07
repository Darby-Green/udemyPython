text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
wordText = set(text.split())

preps_used = wordText.intersection(prepositions)
print(preps_used)