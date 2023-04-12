system_baseline = '''For each of the following potentially misleading tweets, identify if the tweet is believable by many or believable by few.'''

user1_baseline = '''Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2

Is the potentially misleading tweet above believable by many or believable by few?'''

assistant1_baseline = '''Believable by few'''

user2_baseline = '''He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz

Is the potentially misleading tweet above believable by many or believable by few?'''

assistant2_baseline = '''Believable by many'''


system_cot = '''For each of the following potentially misleading tweets, identify if the tweet is believable by many or believable by few. Make sure that instead of looking at the tweets' factual accuracies, think about how they appeal to the audience.'''

user1_cot = '''Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2

The potentially misleading tweet above is tweeted by someone with 355662 followers and has 866 retweets.

If this tweet were spread to a population that 
 - is highly polarized
 - is susceptible to misinformation
 - is susceptible to bandwagon cues and gets easily influenced by popular figures
 - doesn't think rationally or critically
 - gets easily influenced by emotion, especially negative ones
 - tends to believe information that aligns with their prior beliefs
would its message be believed by many or by few? Think in terms of how the tweet might appeal to the population and consider the tweet's metadata, sentiment, and topic. Do NOT consider the tweet's own factual accuracy, as a factually inaccurate tweet can still appear believable to the general public.'''

assistant1_cot = '''The author of the tweet has 355662 followers, but a retweet count under 1000 indicates that the tweet itself doesn't get too many endorsements. The author seems influential, but the tweet itself doesn't get too many endorsements. The tweet has a negative sentiment, and negative emotions sway people more than positive ones. However, the tweet loses believability as it is making an accusation by interpreting Lil Nas X's response literally, while most people can tell that it was merely an insult.

Therefore, the tweet is likely going to be believed by few.'''

user2_cot = '''He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz

The potentially misleading tweet above is tweeted by someone with 37044119 followers and has 50643 retweets.

If this tweet were spread to a population that 
 - is highly polarized
 - is susceptible to misinformation
 - is susceptible to bandwagon cues and gets easily influenced by popular figures
 - doesn't think rationally or critically
 - gets easily influenced by emotion, especially negative ones
 - tends to believe information that aligns with their prior beliefs
would its message be believed by many or by few? Think in terms of how the tweet might appeal to the population and consider the tweet's metadata, sentiment, and topic. Do NOT consider the tweet's own factual accuracy, as a factually inaccurate tweet can still appear believable to the general public.'''

assistant2_cot = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. If the author is influential and the tweet has a lot of endorsements, more people might believe the tweet. The tweet is written in a provocative language and has a negative sentiment, and negative emotions sway people more than positive ones. Moreover, the tweet addresses contentious political issues, and people tend to think less rationally when it comes to political topics.

Therefore, the tweet is likely going to be believed by many.'''

user3_cot = '''On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 

Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy

The potentially misleading tweet above is tweeted by someone with 3435128 followers and has 22274 retweets.

If this tweet were spread to a population that 
 - is highly polarized
 - is susceptible to misinformation
 - is susceptible to bandwagon cues and gets easily influenced by popular figures
 - doesn't think rationally or critically
 - gets easily influenced by emotion, especially negative ones
 - tends to believe information that aligns with their prior beliefs
would its message be believed by many or by few? Think in terms of how the tweet might appeal to the population and consider the tweet's metadata, sentiment, and topic. Do NOT consider the tweet's own factual accuracy, as a factually inaccurate tweet can still appear believable to the general public.'''

assistant3_cot = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. Tweets written by influential authors with more endorsements may have a higher influence on the audience. The tweet is written in a negative sentiment, and negative emotions sway people more than positive ones. Moreover, the tweet addresses AOC, a political figure, and appeals to Republicans and people with negative views on AOC.

Therefore, the tweet is likely going to be believed by many.'''

