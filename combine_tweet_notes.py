import numpy as np
import pandas as pd



few = pd.read_csv('believable_by_few.csv', sep=',')
many = pd.read_csv('believable_by_many.csv', sep=',')

notes = pd.read_csv('notes-00000.tsv', sep='\t')
scored_notes =  pd.read_csv('scoredNotes.tsv', sep='\t')
scored_notes = scored_notes[["noteId", "noteIntercept"]]

notes = notes[["noteId", "tweetId", "summary"]]

few_notes = few.merge(notes, on="tweetId", how="inner")
few_notes = few_notes.merge(scored_notes, on="noteId", how="inner")
print(few_notes.head())
print(few_notes.shape[0])
print(few.head())
print(few.shape[0])

few_notes = few_notes.loc[few_notes.groupby("tweetId")["noteIntercept"].idxmax()].sort_index()
print(few_notes.head())
print(few_notes.shape[0])

many_notes = many.merge(notes, on="tweetId", how="inner")
many_notes = many_notes.merge(scored_notes, on="noteId", how="inner")
print(many_notes.head())
print(many_notes.shape[0])
print(many.head())
print(many.shape[0])

many_notes = many_notes.loc[many_notes.groupby("tweetId")["noteIntercept"].idxmax()].sort_index()
print(many_notes.head())
print(many_notes.shape[0])


few_notes.to_csv("few_with_notes.csv", sep=',', index=False, header=True)
many_notes.to_csv("many_with_notes.csv", sep=',', index=False, header=True)