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



# chain of thoughts v1
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


# chain of thoughts v2
system_cot2 = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.
Make sure to focus on the tweets' appeal to the audience rather than their factual accuracy. Keep in mind that a factually inaccurate message can still appear believable to the general public.'''

user1_cot2 = '''A user with 355662 followers has tweeted the following potentially misleading message:
"Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2"
The tweet has received 866 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant1_cot2 = '''The author of the tweet has 355662 followers, but the tweet itself only has 866 retweets. The author seems somewhat influential, but a low number of retweet indicates that the tweet itself didn't receive too many endorsements. The tweet has negative sentiment, and negative emotions sway people more than neutral or positive ones. However, the tweet doesn't contain any prevalent narratives or appeal to any popular beliefs. Moreover, most people should be able to tell that Lil Nas X's comment was meant to be an insult, but the tweet interpreted the comment literally.
Therefore, the tweet is likely going to be believed by few.'''

user2_cot2 = '''A user with 37044119 followers has tweeted the following potentially misleading message:
"He's using the American military against the American people.
He tear-gassed peaceful protesters and fired rubber bullets.
For a photo.
For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz"
The tweet has received 50643 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant2_cot2 = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. The author of the tweet is highly influential and the tweet itself has received a lot of endorsements, which might trigger bandwagon behavior and make more people believe in it. Moreover, the tweet is written in a provocative language and has negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet accuses a controversial political figure, Donald Trump. By doing so, it implies distrust of politicians and expresses negative views on the republican party. Hence, the tweet might appeal to a large population of people.
Therefore, the tweet is likely going to be believed by many.'''

user3_cot2 = '''A user with 3435128 followers has tweeted the following potentially misleading message:
"On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 
Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy"
The tweet has received 22274 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant3_cot2 = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. The tweet is written by a highly influential author and is widely endorsed, which might trigger bandwagon behaviors among the audience. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Moreover, the tweet addresses AOC, a popular politician, and accuses AOC of dishonest and manipulative behavior. Thus, the tweet might have a strong appeal to people who distrust the government and politicians, especially those with negative views on the democratic party.
Therefore, the tweet is likely going to be believed by many.'''

user4_cot2 = '''A user with 514751 followers has tweeted the following potentially misleading message:
"This deep-fried burger is super cheesy! https://t.co/wbqcsOlJly"
The tweet has received 613 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant4_cot2 = '''The author of the tweet has 514751 followers, and the tweet itself only has 613 retweets. The author of the tweet is somewhat influential, but the tweet only received moderate endorsements and might not be enough to trigger bandwagon effects. Moreover, the tweet is written in positive sentiment, and positive emotions tend to be less effective at swaying people than negative ones. Furthermore, the tweet doesn't contain any prevalent narratives or popular beliefs.
Therefore, the tweet is likely going to be believed by few.'''

user5_cot2 = '''A user with 1189462 followers has tweeted the following potentially misleading message:
"The largest terrorist organization in the world is the Republican party.
Change my mind."
The tweet has received 3634 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant5_cot2 = '''The author of the tweet has 1189462 followers, and the tweet itself has 3634 retweets. The user is quite influential, and the tweet itself has received a substantial amount of endorsements, which might start to trigger bandwagon effects. The tweet is also written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Furthermore, the tweet vehemently expresses a negative view towards the republican party. However, the claim of this tweet is way too oversimplified and overly exaggerated, making it hard to appeal to a lot of people except from the few extremists.
Therefore, the tweet is likely going to be believed by few.'''

user6_cot2 = '''A user with 478845 followers has tweeted the following potentially misleading message:
"Nothing to see here, folks, just a 49-year-old man and a 42-year-old woman having heart attacks minutes after being vaccinated. Coincidence, no doubt.
Definitely stick around a few minutes after you get the jab though. Just for the heck of it. https://t.co/3DEoJZZA3P"
The tweet has received 965 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant6_cot2 = '''The author of the tweet has 478845 followers, and the tweet itself has 965 retweets. The author seems moderately influential, and the tweet only received a few endorsements, which might not be enough to trigger bandwagon behaviors. However, the tweet uses sarcasm, which contains negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet expresses skepticism and doubt about the safety of the COVID-19 vaccine, which is a prevalent anti-vaccination narrative that appeals to people who distrust vaccines and the medical system.
Therefore, the tweet is likely going to be believed by many.'''

user7_cot2 = '''A user with 704 followers has tweeted the following potentially misleading message:
"Women aren’t supposed to have periods🥴 but many are not ready for that conversation https://t.co/giII0bc09x"
The tweet has received 35 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant7_cot2 = '''The author of the tweet only has 704 followers, and the tweet itself only has 35 retweets. A less influential author and few endorsements might make people find the tweet less believable. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. However, even though the tweet expresses negative views on women which might appeal to some audience, it is not related to any of the most prevalent narratives or beliefs, and the menstrual cycle being a normal part of a women's life is practically common knowledge in today's society.
Therefore, the tweet is likely going to be believed by few.'''

user8_cot2 = '''A user with 4144 followers has tweeted the following potentially misleading message:
"We salute #MuhammadAli as a great American. Sadly, we need to acknowledge that Donald Trump wouldn't even allow him to come into America."
The tweet has received 58 retweets.
If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''

assistant8_cot2 = '''The author of the tweet has only 4144 followers, and the tweet itself has only 58 retweets. The author is not very influential and the tweet received few endorsements, which might negatively influence the tweet's believability. However, despite the low influence of the author and the limited number of retweets, the tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the message addresses a well-known figure, Muhammad Ali, and a controversial politician, Donald Trump, and accuses Donald Trump of discrimination towards minority groups. Thus, the tweet might appeal to people who have negative views on Donald Trump and on the republican party.
Therefore, the tweet is likely going to be believed by many.'''

user_template_cot2 = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?
When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.
2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.
3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

Make sure to end your response with "the tweet is likely going to be believed by few." or "the tweet is likely going to be believed by many.", and do not put anything after that. If you want to condition your final answer, please put the conditioning or any other relevant information before the final answer.'''



# chain of thoughts v3 with notes
system_cot3_notes = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.

Each misleading tweet is followed by a debunking note. However, the note is only meant to provide you more context. Assume the general audience doesn't have access to the debunking notes.

Make sure to focus on the tweets' appeal to the audience rather than their factual accuracy. Keep in mind that a factually inaccurate message can still appear believable to the general public.'''

user1_cot3_notes = '''A user with 355662 followers has tweeted the following potentially misleading message:

"Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2"

The tweet has received 866 retweets.

The tweet has been marked as potentially misleading with the following note:

"Lil Nas X's response shown in this image is real, but it was not meant to be interpreted literally. It's merely an insult.    This is similar to the word &quot;motherf*****r&quot;, which is also not literal. Merriam-Webster defines it as &quot;one that is formidable, contemptible, or offensive&quot;."

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant1_cot3_notes = '''The author of the tweet has 355662 followers, but the tweet itself only has 866 retweets. The author seems somewhat influential, but a low number of retweet indicates that the tweet itself didn't receive too many endorsements. The tweet has negative sentiment, and negative emotions sway people more than neutral or positive ones. However, the tweet doesn't contain any prevalent narratives or appeal to any popular beliefs. Moreover, most people should be able to tell that Lil Nas X's comment was meant to be an insult, but the tweet interpreted the comment literally.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user2_cot3_notes = '''A user with 37044119 followers has tweeted the following potentially misleading message:

"He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz"

The tweet has received 50643 retweets.

The tweet has been marked as potentially misleading with the following note:

"Joe Biden's own Department. of Interior investigated this and found it to not be true https://www.nydailynews.com/news/politics/us-elections-government/ny-trump-church-photo-black-lives-matter-protest-inspector-general-report-20210609-537e7ztrljb5bbn5mjecrto6qi-story.html"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant2_cot3_notes = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. The author of the tweet is highly influential and the tweet itself has received a lot of endorsements, which might trigger bandwagon behavior and make more people believe in it. Moreover, the tweet is written in a provocative language and has negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet accuses a controversial political figure, Donald Trump. By doing so, it implies distrust of politicians and expresses negative views on the republican party. Hence, the tweet might appeal to a large population of people.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user3_cot3_notes = '''A user with 3435128 followers has tweeted the following potentially misleading message:

"On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 

Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy"

The tweet has received 22274 retweets.

The tweet has been marked as potentially misleading with the following note:

"This tweet claims without evidence that Alexandria Ocasio-Cortez staged a photoshoot in an empty parking lot, when she was actually at a detention facility in Tornillo, Texas https://www.snopes.com/fact-check/aoc-empty-parking-lot/"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant3_cot3_notes = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. The tweet is written by a highly influential author and is widely endorsed, which might trigger bandwagon behaviors among the audience. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Moreover, the tweet addresses AOC, a popular politician, and accuses AOC of dishonest and manipulative behavior. Thus, the tweet might have a strong appeal to people who distrust the government and politicians, especially those with negative views on the democratic party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user4_cot3_notes = '''A user with 514751 followers has tweeted the following potentially misleading message:

"This deep-fried burger is super cheesy! https://t.co/wbqcsOlJly"

The tweet has received 613 retweets.

The tweet has been marked as potentially misleading with the following note:

"I have no idea why they're reposting several year old content but this restaurant is closed and has been for a while now as a result of - you guessed it - burn related issues.    https://maps.app.goo.gl/5zs8Ryo8pe5AvkmU7,0.3173947"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant4_cot3_notes = '''The author of the tweet has 514751 followers, and the tweet itself only has 613 retweets. The author of the tweet is somewhat influential, but the tweet only received moderate endorsements and might not be enough to trigger bandwagon effects. Moreover, the tweet is written in positive sentiment, and positive emotions tend to be less effective at swaying people than negative ones. Furthermore, the tweet doesn't contain any prevalent narratives or popular beliefs.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user5_cot3_notes = '''A user with 1189462 followers has tweeted the following potentially misleading message:

"The largest terrorist organization in the world is the Republican party.

Change my mind."

The tweet has received 3634 retweets.

The tweet has been marked as potentially misleading with the following note:

"The Republican Party is a mainstream American political organization. The United States Office of the Director of National Intelligence does not list the Republican Party as a terror group.  https://www.dni.gov/nctc/groups.html"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant5_cot3_notes = '''The author of the tweet has 1189462 followers, and the tweet itself has 3634 retweets. The user is quite influential, and the tweet itself has received a substantial amount of endorsements, which might start to trigger bandwagon effects. The tweet is also written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Furthermore, the tweet vehemently expresses a negative view towards the republican party. However, the claim of this tweet is way too oversimplified and overly exaggerated, making it hard to appeal to a lot of people except from the few extremists.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user6_cot3_notes = '''A user with 478845 followers has tweeted the following potentially misleading message:

"Nothing to see here, folks, just a 49-year-old man and a 42-year-old woman having heart attacks minutes after being vaccinated. Coincidence, no doubt.

Definitely stick around a few minutes after you get the jab though. Just for the heck of it. https://t.co/3DEoJZZA3P"

The tweet has received 965 retweets.

The tweet has been marked as potentially misleading with the following note:

"VAERS is a self-reporting database open to the public that may include unverified claims. All reports are investigated by the CDC. To date, there has been no detected patterns that would indicate direct correlation of deaths to the COVID-19 vaccine.    Learn more at: https://www.politifact.com/factchecks/2021/feb/16/facebook-posts/says-death-reports-federal-database-show-fatal-ris/    https://www.cdc.gov/coronavirus/2019-ncov/vaccines/safety/adverse-events.html"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant6_cot3_notes = '''The author of the tweet has 478845 followers, and the tweet itself has 965 retweets. The author seems moderately influential, and the tweet only received a few endorsements, which might not be enough to trigger bandwagon behaviors. However, the tweet uses sarcasm, which contains negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet expresses skepticism and doubt about the safety of the COVID-19 vaccine, which is a prevalent anti-vaccination narrative that appeals to people who distrust vaccines and the medical system.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user7_cot3_notes = '''A user with 704 followers has tweeted the following potentially misleading message:

"Women aren’t supposed to have periods🥴 but many are not ready for that conversation https://t.co/giII0bc09x"

The tweet has received 35 retweets.

The tweet has been marked as potentially misleading with the following note:

"The menstrual cycle is a perfectly normal part of life for women from puberty through menopause. It is a normal biological process. https://my.clevelandclinic.org/health/articles/10132-normal-menstruation"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant7_cot3_notes = '''The author of the tweet only has 704 followers, and the tweet itself only has 35 retweets. A less influential author and few endorsements might make people find the tweet less believable. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. However, even though the tweet expresses negative views on women which might appeal to some audience, it is not related to any of the most prevalent narratives or beliefs, and the menstrual cycle being a normal part of a women's life is practically common knowledge in today's society.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user8_cot3_notes = '''A user with 4144 followers has tweeted the following potentially misleading message:

"We salute #MuhammadAli as a great American. Sadly, we need to acknowledge that Donald Trump wouldn't even allow him to come into America."

The tweet has received 58 retweets.

The tweet has been marked as potentially misleading with the following note:

"Muhammad Ali was born in the United States. He would not need the permission of the president to enter the United States.    https://en.m.wikipedia.org/wiki/Muhammad_Ali"

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant8_cot3_notes = '''The author of the tweet has only 4144 followers, and the tweet itself has only 58 retweets. The author is not very influential and the tweet received few endorsements, which might negatively influence the tweet's believability. However, despite the low influence of the author and the limited number of retweets, the tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the message addresses a well-known figure, Muhammad Ali, and a controversial politician, Donald Trump, and accuses Donald Trump of discrimination towards minority groups. Thus, the tweet might appeal to people who have negative views on Donald Trump and on the republican party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user_template_cot3_notes = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''









# chain of thoughts v3
system_cot3 = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.

For each given tweet, provide a single yes/no token as your final answer. If you want to condition your answer, please put the conditioning or any additional relevant information before the final yes/no answer.

Make sure to focus on the tweets' appeal to the audience rather than their factual accuracy. Keep in mind that a factually inaccurate message can still appear believable to the general public.'''

user1_cot3 = '''A user with 355662 followers has tweeted the following potentially misleading message:

"Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2"

The tweet has received 866 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant1_cot3 = '''The author of the tweet has 355662 followers, but the tweet itself only has 866 retweets. The author seems somewhat influential, but a low number of retweet indicates that the tweet itself didn't receive too many endorsements. The tweet has negative sentiment, and negative emotions sway people more than neutral or positive ones. However, the tweet doesn't contain any prevalent narratives or appeal to any popular beliefs. Moreover, most people should be able to tell that Lil Nas X's comment was meant to be an insult, but the tweet interpreted the comment literally.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user2_cot3 = '''A user with 37044119 followers has tweeted the following potentially misleading message:

"He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz"

The tweet has received 50643 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant2_cot3 = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. The author of the tweet is highly influential and the tweet itself has received a lot of endorsements, which might trigger bandwagon behavior and make more people believe in it. Moreover, the tweet is written in a provocative language and has negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet accuses a controversial political figure, Donald Trump. By doing so, it implies distrust of politicians and expresses negative views on the republican party. Hence, the tweet might appeal to a large population of people.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user3_cot3 = '''A user with 3435128 followers has tweeted the following potentially misleading message:

"On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 

Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy"

The tweet has received 22274 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant3_cot3 = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. The tweet is written by a highly influential author and is widely endorsed, which might trigger bandwagon behaviors among the audience. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Moreover, the tweet addresses AOC, a popular politician, and accuses AOC of dishonest and manipulative behavior. Thus, the tweet might have a strong appeal to people who distrust the government and politicians, especially those with negative views on the democratic party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user4_cot3 = '''A user with 514751 followers has tweeted the following potentially misleading message:

"This deep-fried burger is super cheesy! https://t.co/wbqcsOlJly"

The tweet has received 613 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant4_cot3 = '''The author of the tweet has 514751 followers, and the tweet itself only has 613 retweets. The author of the tweet is somewhat influential, but the tweet only received moderate endorsements and might not be enough to trigger bandwagon effects. Moreover, the tweet is written in positive sentiment, and positive emotions tend to be less effective at swaying people than negative ones. Furthermore, the tweet doesn't contain any prevalent narratives or popular beliefs.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user5_cot3 = '''A user with 1189462 followers has tweeted the following potentially misleading message:

"The largest terrorist organization in the world is the Republican party.

Change my mind."

The tweet has received 3634 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant5_cot3 = '''The author of the tweet has 1189462 followers, and the tweet itself has 3634 retweets. The user is quite influential, and the tweet itself has received a substantial amount of endorsements, which might start to trigger bandwagon effects. The tweet is also written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Furthermore, the tweet vehemently expresses a negative view towards the republican party. However, the claim of this tweet is way too oversimplified and overly exaggerated, making it hard to appeal to a lot of people except from the few extremists.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user6_cot3 = '''A user with 478845 followers has tweeted the following potentially misleading message:

"Nothing to see here, folks, just a 49-year-old man and a 42-year-old woman having heart attacks minutes after being vaccinated. Coincidence, no doubt.

Definitely stick around a few minutes after you get the jab though. Just for the heck of it. https://t.co/3DEoJZZA3P"

The tweet has received 965 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant6_cot3 = '''The author of the tweet has 478845 followers, and the tweet itself has 965 retweets. The author seems moderately influential, and the tweet only received a few endorsements, which might not be enough to trigger bandwagon behaviors. However, the tweet uses sarcasm, which contains negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet expresses skepticism and doubt about the safety of the COVID-19 vaccine, which is a prevalent anti-vaccination narrative that appeals to people who distrust vaccines and the medical system.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user7_cot3 = '''A user with 704 followers has tweeted the following potentially misleading message:

"Women aren’t supposed to have periods🥴 but many are not ready for that conversation https://t.co/giII0bc09x"

The tweet has received 35 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant7_cot3 = '''The author of the tweet only has 704 followers, and the tweet itself only has 35 retweets. A less influential author and few endorsements might make people find the tweet less believable. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. However, even though the tweet expresses negative views on women which might appeal to some audience, it is not related to any of the most prevalent narratives or beliefs, and the menstrual cycle being a normal part of a women's life is practically common knowledge in today's society.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user8_cot3 = '''A user with 4144 followers has tweeted the following potentially misleading message:

"We salute #MuhammadAli as a great American. Sadly, we need to acknowledge that Donald Trump wouldn't even allow him to come into America."

The tweet has received 58 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant8_cot3 = '''The author of the tweet has only 4144 followers, and the tweet itself has only 58 retweets. The author is not very influential and the tweet received few endorsements, which might negatively influence the tweet's believability. However, despite the low influence of the author and the limited number of retweets, the tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the message addresses a well-known figure, Muhammad Ali, and a controversial politician, Donald Trump, and accuses Donald Trump of discrimination towards minority groups. Thus, the tweet might appeal to partisans who have negative views on Donald Trump and on the republican party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user_template_cot3 = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''








# chain of thoughts v3
system_cot3 = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.

For each given tweet, provide a single yes/no token as your final answer. If you want to condition your answer, please put the conditioning or any additional relevant information before the final yes/no answer.

Make sure to focus on the tweets' appeal to the audience rather than their factual accuracy. Keep in mind that a factually inaccurate message can still appear believable to the general public.'''

user1_cot3 = '''A user with 355662 followers has tweeted the following potentially misleading message:

"Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2"

The tweet has received 866 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant1_cot3 = '''The author of the tweet has 355662 followers, but the tweet itself only has 866 retweets. The author seems somewhat influential, but a low number of retweet indicates that the tweet itself didn't receive too many endorsements. The tweet has negative sentiment, and negative emotions sway people more than neutral or positive ones. However, the tweet doesn't contain any prevalent narratives or appeal to any popular beliefs. Moreover, most people should be able to tell that Lil Nas X's comment was meant to be an insult, but the tweet interpreted the comment literally.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user2_cot3 = '''A user with 37044119 followers has tweeted the following potentially misleading message:

"He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz"

The tweet has received 50643 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant2_cot3 = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. The author of the tweet is highly influential and the tweet itself has received a lot of endorsements, which might trigger bandwagon behavior and make more people believe in it. Moreover, the tweet is written in a provocative language and has negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet accuses a controversial political figure, Donald Trump. By doing so, it implies distrust of politicians and expresses negative views on the republican party. Hence, the tweet might appeal to a large population of people.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user3_cot3 = '''A user with 3435128 followers has tweeted the following potentially misleading message:

"On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 

Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy"

The tweet has received 22274 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant3_cot3 = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. The tweet is written by a highly influential author and is widely endorsed, which might trigger bandwagon behaviors among the audience. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Moreover, the tweet addresses AOC, a popular politician, and accuses AOC of dishonest and manipulative behavior. Thus, the tweet might have a strong appeal to people who distrust the government and politicians, especially those with negative views on the democratic party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user4_cot3 = '''A user with 514751 followers has tweeted the following potentially misleading message:

"This deep-fried burger is super cheesy! https://t.co/wbqcsOlJly"

The tweet has received 613 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant4_cot3 = '''The author of the tweet has 514751 followers, and the tweet itself only has 613 retweets. The author of the tweet is somewhat influential, but the tweet only received moderate endorsements and might not be enough to trigger bandwagon effects. Moreover, the tweet is written in positive sentiment, and positive emotions tend to be less effective at swaying people than negative ones. Furthermore, the tweet doesn't contain any prevalent narratives or popular beliefs.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user5_cot3 = '''A user with 1189462 followers has tweeted the following potentially misleading message:

"The largest terrorist organization in the world is the Republican party.

Change my mind."

The tweet has received 3634 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant5_cot3 = '''The author of the tweet has 1189462 followers, and the tweet itself has 3634 retweets. The user is quite influential, and the tweet itself has received a substantial amount of endorsements, which might start to trigger bandwagon effects. The tweet is also written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Furthermore, the tweet vehemently expresses a negative view towards the republican party. However, the claim of this tweet is way too oversimplified and overly exaggerated, making it hard to appeal to a lot of people except from the few extremists.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user6_cot3 = '''A user with 478845 followers has tweeted the following potentially misleading message:

"Nothing to see here, folks, just a 49-year-old man and a 42-year-old woman having heart attacks minutes after being vaccinated. Coincidence, no doubt.

Definitely stick around a few minutes after you get the jab though. Just for the heck of it. https://t.co/3DEoJZZA3P"

The tweet has received 965 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant6_cot3 = '''The author of the tweet has 478845 followers, and the tweet itself has 965 retweets. The author seems moderately influential, and the tweet only received a few endorsements, which might not be enough to trigger bandwagon behaviors. However, the tweet uses sarcasm, which contains negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet expresses skepticism and doubt about the safety of the COVID-19 vaccine, which is a prevalent anti-vaccination narrative that appeals to people who distrust vaccines and the medical system.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user7_cot3 = '''A user with 704 followers has tweeted the following potentially misleading message:

"Women aren’t supposed to have periods🥴 but many are not ready for that conversation https://t.co/giII0bc09x"

The tweet has received 35 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant7_cot3 = '''The author of the tweet only has 704 followers, and the tweet itself only has 35 retweets. A less influential author and few endorsements might make people find the tweet less believable. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. However, even though the tweet expresses negative views on women which might appeal to some audience, it is not related to any of the most prevalent narratives or beliefs, and the menstrual cycle being a normal part of a women's life is practically common knowledge in today's society.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user8_cot3 = '''A user with 4144 followers has tweeted the following potentially misleading message:

"We salute #MuhammadAli as a great American. Sadly, we need to acknowledge that Donald Trump wouldn't even allow him to come into America."

The tweet has received 58 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant8_cot3 = '''The author of the tweet has only 4144 followers, and the tweet itself has only 58 retweets. The author is not very influential and the tweet received few endorsements, which might negatively influence the tweet's believability. However, despite the low influence of the author and the limited number of retweets, the tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the message addresses a well-known figure, Muhammad Ali, and a controversial politician, Donald Trump, and accuses Donald Trump of discrimination towards minority groups. Thus, the tweet might appeal to partisans who have negative views on Donald Trump and on the republican party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user_template_cot3 = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that the general public is unfamiliar with, such as science, the use of technology, politics or conspiracy theories, then the message might appear more believable to the public.

After you are done with your reasoning, please provide a single token yes/no answer.'''







# chain of thoughts v4
system_cot4 = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.

For each given tweet, provide a single yes/no token as your final answer. If you want to condition your answer, please put the conditioning or any additional relevant information before the final yes/no answer.

Make sure to focus on the tweets' appeal to the audience rather than their factual accuracy. Keep in mind that a factually inaccurate message can still appear believable to the general public.'''

user1_cot4 = '''A user with 355662 followers has tweeted the following potentially misleading message:

"Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2"

The message is followed by a screenshot at a certain time of a tweet from Lil Nas X, replying to Kaitlin Bennett, "yep and i might fuck yours." The tweet was posted at 11:06 PM, 28 Mar 21, using Twitter for iPhone.

The tweet has received 866 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant1_cot4 = '''The author of the tweet has 355662 followers, but the tweet itself only has 866 retweets. The author seems somewhat influential, but a low number of retweet indicates that the tweet itself didn't receive too many endorsements. The tweet has negative sentiment, and negative emotions sway people more than neutral or positive ones. However, the tweet doesn't contain any prevalent narratives or appeal to any popular beliefs. Moreover, most people should be able to tell that Lil Nas X's comment was meant to be an insult, but the tweet interpreted the comment literally.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user2_cot4 = '''A user with 37044119 followers has tweeted the following potentially misleading message:

"He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz"

The tweet has received 50643 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant2_cot4 = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. The author of the tweet is highly influential and the tweet itself has received a lot of endorsements, which might trigger bandwagon behavior and make more people believe in it. Moreover, the tweet is written in a provocative language and has negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet accuses a controversial political figure, Donald Trump. By doing so, it implies distrust of politicians and expresses negative views on the republican party. Hence, the tweet might appeal to a large population of people.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user3_cot4 = '''A user with 3435128 followers has tweeted the following potentially misleading message:

"On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 

Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy"

The message is followed by a photo of AOC standing in front of an iron fence with her hands covering her face. AOC seems to be crying in the photo.

The tweet has received 22274 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant3_cot4 = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. The tweet is written by a highly influential author and is widely endorsed, which might trigger bandwagon behaviors among the audience. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Moreover, the tweet addresses AOC, a popular politician, and accuses AOC of dishonest and manipulative behavior. Thus, the tweet might have a strong appeal to people who distrust the government and politicians, especially those with negative views on the democratic party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user4_cot4 = '''A user with 514751 followers has tweeted the following potentially misleading message:

"This deep-fried burger is super cheesy! https://t.co/wbqcsOlJly"

The tweet has received 613 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant4_cot4 = '''The author of the tweet has 514751 followers, and the tweet itself only has 613 retweets. The author of the tweet is somewhat influential, but the tweet only received moderate endorsements and might not be enough to trigger bandwagon effects. Moreover, the tweet is written in positive sentiment, and positive emotions tend to be less effective at swaying people than negative ones. Furthermore, the tweet doesn't contain any prevalent narratives or popular beliefs.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user5_cot4 = '''A user with 1189462 followers has tweeted the following potentially misleading message:

"The largest terrorist organization in the world is the Republican party.

Change my mind."

The tweet has received 3634 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant5_cot4 = '''The author of the tweet has 1189462 followers, and the tweet itself has 3634 retweets. The user is quite influential, and the tweet itself has received a substantial amount of endorsements, which might start to trigger bandwagon effects. The tweet is also written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Furthermore, the tweet vehemently expresses a negative view towards the republican party. However, the claim of this tweet is way too oversimplified and overly exaggerated, making it hard to appeal to a lot of people except from the few extremists.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user6_cot4 = '''A user with 478845 followers has tweeted the following potentially misleading message:

"Nothing to see here, folks, just a 49-year-old man and a 42-year-old woman having heart attacks minutes after being vaccinated. Coincidence, no doubt.

Definitely stick around a few minutes after you get the jab though. Just for the heck of it. https://t.co/3DEoJZZA3P"

The message is followed by a screenshot of a form documenting the information of two patients who seem to show symptoms of heart attacks after receiving covid-19 vaccination.

The tweet has received 965 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant6_cot4 = '''The author of the tweet has 478845 followers, and the tweet itself has 965 retweets. The author seems moderately influential, and the tweet only received a few endorsements, which might not be enough to trigger bandwagon behaviors. However, the tweet uses sarcasm, which contains negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet expresses skepticism and doubt about the safety of the COVID-19 vaccine, which is a prevalent anti-vaccination narrative that appeals to people who distrust vaccines and the medical system.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user7_cot4 = '''A user with 704 followers has tweeted the following potentially misleading message:

"Women aren’t supposed to have periods🥴 but many are not ready for that conversation https://t.co/giII0bc09x"

The tweet has received 35 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant7_cot4 = '''The author of the tweet only has 704 followers, and the tweet itself only has 35 retweets. A less influential author and few endorsements might make people find the tweet less believable. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. However, even though the tweet expresses negative views on women which might appeal to some audience, it is not related to any of the most prevalent narratives or beliefs, and the menstrual cycle being a normal part of a women's life is practically common knowledge in today's society.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user8_cot4 = '''A user with 4144 followers has tweeted the following potentially misleading message:

"We salute #MuhammadAli as a great American. Sadly, we need to acknowledge that Donald Trump wouldn't even allow him to come into America."

The tweet has received 58 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant8_cot4 = '''The author of the tweet has only 4144 followers, and the tweet itself has only 58 retweets. The author is not very influential and the tweet received few endorsements, which might negatively influence the tweet's believability. However, despite the low influence of the author and the limited number of retweets, the tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the message addresses a well-known figure, Muhammad Ali, and a controversial politician, Donald Trump, and accuses Donald Trump of discrimination towards minority groups. Thus, the tweet might appeal to partisans who have negative views on Donald Trump and on the republican party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user_template_cot4 = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

After you are done with your reasoning, please provide a single token yes/no answer.'''





# chain of thoughts v4.1 (v4 + common sense feature)
system_cot4_1 = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.

For each given tweet, provide a single yes/no token as your final answer. If you want to condition your answer, please put the conditioning or any additional relevant information before the final yes/no answer.

Make sure to focus on the tweets' appeal to the audience rather than their factual accuracy. Keep in mind that a factually inaccurate message can still appear believable to the general public.'''

user1_cot4_1 = '''A user with 355662 followers has tweeted the following potentially misleading message:

"Lil Nas just threatened to rape my dad. Sounds about what I'd expect. https://t.co/zQFdSB1oa2"

The message is followed by a screenshot at a certain time of a tweet from Lil Nas X, replying to Kaitlin Bennett, "yep and i might fuck yours." The tweet was posted at 11:06 PM, 28 Mar 21, using Twitter for iPhone.

The tweet has received 866 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant1_cot4_1 = '''The author of the tweet has 355662 followers, but the tweet itself only has 866 retweets. The author seems somewhat influential, but a low number of retweet indicates that the tweet itself didn't receive too many endorsements. The tweet has negative sentiment, and negative emotions sway people more than neutral or positive ones. However, the tweet doesn't contain any prevalent narratives or appeal to any popular beliefs. Moreover, most people should be able to tell that Lil Nas X's comment was meant to be an insult, but the tweet interpreted the comment literally.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user2_cot4_1 = '''A user with 37044119 followers has tweeted the following potentially misleading message:

"He's using the American military against the American people.

He tear-gassed peaceful protesters and fired rubber bullets.

For a photo.

For our children, for the very soul of our country, we must defeat him. But I mean it when I say this: we can only do it together. https://t.co/G1yE67q9Nz"

The tweet has received 50643 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant2_cot4_1 = '''The author of the tweet has 37044119 followers, and the tweet itself has 50643 retweets. The author of the tweet is highly influential and the tweet itself has received a lot of endorsements, which might trigger bandwagon behavior and make more people believe in it. Moreover, the tweet is written in a provocative language and has negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet accuses a controversial political figure, Donald Trump. By doing so, it implies distrust of politicians and expresses negative views on the republican party. Hence, the tweet might appeal to a large population of people.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user3_cot4_1 = '''A user with 3435128 followers has tweeted the following potentially misleading message:

"On a day in which #AlexandriaOcasioSmollett is trending, please never forget the time that @AOC staged a photo shoot dressed in all white at a parking lot to spread lies about immigrant children in cages. 

Faking her own attempted murder was the next logical step. https://t.co/y8mNNowMGy"

The message is followed by a photo of AOC standing in front of an iron fence with her hands covering her face. AOC seems to be crying in the photo.

The tweet has received 22274 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant3_cot4_1 = '''The author of the tweet has 3435128 followers, and the tweet itself has 22274 retweets. The tweet is written by a highly influential author and is widely endorsed, which might trigger bandwagon behaviors among the audience. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Moreover, the tweet addresses AOC, a popular politician, and accuses AOC of dishonest and manipulative behavior. Thus, the tweet might have a strong appeal to people who distrust the government and politicians, especially those with negative views on the democratic party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user4_cot4_1 = '''A user with 514751 followers has tweeted the following potentially misleading message:

"This deep-fried burger is super cheesy! https://t.co/wbqcsOlJly"

The tweet has received 613 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant4_cot4_1 = '''The author of the tweet has 514751 followers, and the tweet itself only has 613 retweets. The author of the tweet is somewhat influential, but the tweet only received moderate endorsements and might not be enough to trigger bandwagon effects. Moreover, the tweet is written in positive sentiment, and positive emotions tend to be less effective at swaying people than negative ones. Furthermore, the tweet doesn't contain any prevalent narratives or popular beliefs.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user5_cot4_1 = '''A user with 1189462 followers has tweeted the following potentially misleading message:

"The largest terrorist organization in the world is the Republican party.

Change my mind."

The tweet has received 3634 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant5_cot4_1 = '''The author of the tweet has 1189462 followers, and the tweet itself has 3634 retweets. The user is quite influential, and the tweet itself has received a substantial amount of endorsements, which might start to trigger bandwagon effects. The tweet is also written in negative sentiment, and negative emotions sway people more than neutral or positive ones. Furthermore, the tweet vehemently expresses a negative view towards the republican party. However, the claim of this tweet is way too oversimplified and overly exaggerated, making it hard to appeal to a lot of people except from the few extremists.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user6_cot4_1 = '''A user with 478845 followers has tweeted the following potentially misleading message:

"Nothing to see here, folks, just a 49-year-old man and a 42-year-old woman having heart attacks minutes after being vaccinated. Coincidence, no doubt.

Definitely stick around a few minutes after you get the jab though. Just for the heck of it. https://t.co/3DEoJZZA3P"

The message is followed by a screenshot of a form documenting the information of two patients who seem to show symptoms of heart attacks after receiving covid-19 vaccination.

The tweet has received 965 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant6_cot4_1 = '''The author of the tweet has 478845 followers, and the tweet itself has 965 retweets. The author seems moderately influential, and the tweet only received a few endorsements, which might not be enough to trigger bandwagon behaviors. However, the tweet uses sarcasm, which contains negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the tweet expresses skepticism and doubt about the safety of the COVID-19 vaccine, which is a prevalent anti-vaccination narrative that appeals to people who distrust vaccines and the medical system.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user7_cot4_1 = '''A user with 704 followers has tweeted the following potentially misleading message:

"Women aren’t supposed to have periods🥴 but many are not ready for that conversation https://t.co/giII0bc09x"

The tweet has received 35 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant7_cot4_1 = '''The author of the tweet only has 704 followers, and the tweet itself only has 35 retweets. A less influential author and few endorsements might make people find the tweet less believable. The tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. However, even though the tweet expresses negative views on women which might appeal to some audience, it is not related to any of the most prevalent narratives or beliefs, and the menstrual cycle being a normal part of a women's life is practically common knowledge in today's society.

Therefore, the tweet is likely going to be believed by few.

Believable by many (yes or no): No'''

user8_cot4_1 = '''A user with 4144 followers has tweeted the following potentially misleading message:

"We salute #MuhammadAli as a great American. Sadly, we need to acknowledge that Donald Trump wouldn't even allow him to come into America."

The tweet has received 58 retweets.

If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant8_cot4_1 = '''The author of the tweet has only 4144 followers, and the tweet itself has only 58 retweets. The author is not very influential and the tweet received few endorsements, which might negatively influence the tweet's believability. However, despite the low influence of the author and the limited number of retweets, the tweet is written in negative sentiment, and negative emotions sway people more than neutral or positive ones. More importantly, the message addresses a well-known figure, Muhammad Ali, and a controversial politician, Donald Trump, and accuses Donald Trump of discrimination towards minority groups. Thus, the tweet might appeal to partisans who have negative views on Donald Trump and on the republican party.

Therefore, the tweet is likely going to be believed by many.

Believable by many (yes or no): Yes'''

user_template_cot4_1 = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does the message conflict with common-sense knowledge?
If the tweet's message conflicts with everyday, common-sense knowledge such that a six-year-old kid would be able to tell it is false, then the message would be less likely to be believed by a large public. On the other hand, if the message involves topics that requires certain levels of expertise to understand and debunk, such as natural phenomenon that people are not familiar with, the use of novel technologies, or pretending to be something that's authoritative & legitimate, then the message might appear much more believable to the public.


Make sure your arguments are supported by evidence or sound reasoning, and avoid any contradictory statements. Focus on maintaining coherence and consistency throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''







system_cot5 = '''For each of the following potentially misleading tweets, determine whether the tweet would likely be believed by many or by few if it were spread to a population that
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs.

For each given tweet, provide a single yes/no token as your final answer. If you want to condition your answer, please put the conditioning or any additional relevant information before the final yes/no answer.

Note that some tweets are posted in 2022, so don't deem a tweet as unbelievable simply because you don't recognize the event referenced by the message.'''

user_template_cot5 = '''If this tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does debunking the message require a certain level of expertise?
If the tweet requires some levels of expertise or knowledge-seeking efforts to understand and debunk, then the public could be more easily fooled by the author. For instance, a tweet could appear more believable to the public if the message involves conspiracy theories, natural phenomena that people are not familiar with, the use of novel technologies, or impersonating an authoritative and legitimate entity. 

On the other hand, if the message directly conflicts with basic common-sense knowledge, such as claiming "the earth is flat" or "humans don't need air to breath", people might find it less believable. However, it is important to note that a claim being far-fetched or sensational does not mean it conflicts with basic common-sense knowledge, and you should not dismiss a claim as "believable by few" simply because the claim is sensational or extreme.


Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, the amount of effort and expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''









system_cot5_1 = '''You are an assistant that helps fact-checkers prioritize claims to fact-check based on their believability.

For each of the following potentially misleading tweets, if the tweet were spread to a population that 
 - is highly polarized,
 - is susceptible to misinformation,
 - is influenced by bandwagon cues,
 - does not often think rationally or critically,
 - is easily swayed by emotions, especially negative ones, and
 - tends to believe information that aligns with their prior beliefs,
would its message be believed by many or by few?

When evaluating the tweet's believability, reason about the following factors:
1. Is the tweet posted by an influential user? And does the tweet get many endorsements?
Users with more than 2,000,000 followers are considered highly influential, and tweets with more than 9,000 retweets are considered widely endorsed. User popularity and tweet endorsements could trigger bandwagon behavior and are positively correlated with believability.

2. Does the tweet contain negative sentiment?
Negative sentiment and negative emotions such as hate, anger, and fear could sway people more than neutral or positive ones. Therefore, tweets with negative sentiment are generally more likely to be believed by many than tweets with positive sentiment.

3. Does the message contain a prevalent narrative or appeal to popular beliefs?
People tend to believe in things that align with their prior beliefs. Thus, misinformation that contains prevalent narratives and beliefs is much more likely to sway a large population of people than misinformation that doesn't. These popular narratives and beliefs include:
- distrust in the government and politicians,
- negative views on the democratic or republican party,
- distrust in vaccines and the medical system,
- distrust in technology and large tech companies,
- distrust in mainstream news media.

4. Does debunking the message require a certain level of expertise?
If the tweet requires some levels of expertise or knowledge-seeking efforts to understand and debunk, then the public could be more easily fooled by the author. For instance, a tweet could appear more believable to the public if the message involves conspiracy theories, natural phenomena that people are not familiar with, the use of novel technologies, or impersonating an authoritative and legitimate entity. 

On the other hand, if the message directly conflicts with basic common-sense knowledge, such as claiming "the earth is flat" or "humans don't need air to breath", people might find it less believable. However, it is important to note that a claim being far-fetched or sensational does not mean it conflicts with basic common-sense knowledge, and you should not dismiss a claim as "believable by few" simply because the claim is sensational or extreme.


For each given tweet, provide a single yes/no token as your final answer. If you want to condition your answer, please put the conditioning or any additional relevant information before the final yes/no answer.

Note that some tweets are posted in 2022, so don't deem a tweet as unbelievable simply because you don't recognize the event referenced by the message.'''



user_template_cot5_1 = '''Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


user1_cot5_1 = '''A user with 1910278 followers has tweeted the following potentially misleading message:

"Latinx Heritage Month is here and we look forward to celebrating all month long! Together, let's take time to recognize and appreciate the Latinx culture and community that makes our neighborhoods so great. Happy #LatinxHeritageMonth! https://t.co/F0yshTyJm7"

The message is followed by a photo of two Sesame Street characters with the words "Celebrating Latinx Heritage Month."

The tweet has received 176 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant1_cot5_1 = '''This tweet is posted by an influential user with over 1.9 million followers. However, it has received relatively few retweets (176). The amount of endorsements is not enough to trigger bandwagon behaviors. The message is positive and celebrates Latinx Heritage Month, which does not contain negative sentiment or appeal to any controversial topics or prevalent negative narratives. The tweet does not require any expertise to understand, as it is a straightforward celebration of a cultural event.

Considering these factors, due to the low number of endorsements, the lack of negative sentiment, and the lack of alignment with prevalent polarizing narratives, the tweet might not appeal to a large group of people in the given population where people are polarized and easily swayed by negative emotions and narratives aligning with existing beliefs.

Believable by many (yes or no): No'''

user2_cot5_1 = '''A user with 75710 followers has tweeted the following potentially misleading message:

"I pointed out to McAuliffe that he called for Northam to resign, Northam didn’t, and he’s gone on to recover his popularity. McAuliffe says that’s different b/c he believes Northam saying he wasn’t in the blackface picture.For Cuomo, “we have 11 women who are very, very credible”"

The tweet has received 38 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


assistant2_cot5_1 = '''The user who posted this tweet has a moderate following of 75,710 followers, which is not considered highly influential. The tweet has only received 38 retweets, which does not indicate widespread endorsement. The tweet does not have strong emotional appeals, but the message discusses political figures and their controversies, which could be seen as negative sentiment. The tweet addresses controversial incidents involving Democratic politicians Ralph Northam and Andrew Cuomo, and accuses them of racism and sexual harassment. The message implies distrust in politicians and might appeal to people with negative opinions on the Democratic party. Moreover, debunking the message might require some effort or a certain level of expertise. Since it involves specific incidents of specific politicians, verifying the truthfulness of the message might require knowledge in politics or political news.

Considering these factors, the tweet is likely going to be believed by many in the described population despite the low number of endorsements and the lack of strong negative emotions.

Believable by many (yes or no): Yes'''


user3_cot5_1 = '''A user with 4584593 followers has tweeted the following potentially misleading message:

"50-1 

HOLY FUCK

MY BROTHER JUST BEAT FLOYD MAYWEATHER"

The tweet has received 4420 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''

assistant3_cot5_1 = '''The user who posted this tweet has a large following of over 4.5 million followers, which is considered highly influential and might trigger bandwagon behavior. The tweet has received 4,420 retweets, which is a significant number though not enough to be considered widely endorsed. The message contains excitement and surprise, which might sway some people, but positive emotions are less effective than negative ones. The tweet is about a boxing match between the user's brother and Floyd Mayweather, which does not align with any prevalent narratives. 

Moreover, the message does not include any topics that are difficult to understand, and debunking the message would not require a high level of expertise, as the outcome of a high-profile boxing match would be widely reported and easily verifiable.

Considering these factors, the tweet's message might be believed by believed by few in the given population due to the lack of negative sentiment, lack of alignment with prevalent narratives, and the easiness to debunk. However, the message might still appeal to some people due to the author's high influence.

Believable by many (yes or no): No'''


user4_cot5_1 = '''A user with 124282 followers has tweeted the following potentially misleading message:

"most detailed image of a human cell to date https://t.co/XnI8WTuoQO"

The message is followed by a photo of a piece of paper with a lot of glitter on it

The tweet has received 62261 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


assistant4_cot5_1 = '''The user who posted this tweet has a moderate following of 124,282 followers, which is not considered highly influential. However, the tweet has received a significant number of retweets (62,261), which indicates widespread endorsement and could trigger bandwagon behavior. The message is not emotionally charged and does not contain negative sentiment. The tweet does not align with any prevalent narratives or popular beliefs.

However, the message claims to show the most detailed image of a human cell, which involves topics in life sciences that the general public does not understand. People might be amazed by the dazzling picture, and it might require some level of expertise to verify if the image is a real representation of a human cell.

Considering these factors, despite not having negative emotions or appealing to prevalent narratives, the tweet might still be believed by many due to the high number of retweets and the fact that debunking the message requires some level of expertise.

Believable by many (yes or no): Yes'''


user5_cot5_1 = '''A user with 42826 followers has tweeted the following potentially misleading message:

"I don’t think people suffered from acne until relatively recently as  industrial seed oils became a prominent component of modern diets

If you look at images from the 80’s and 90’s, no one had acne"

The tweet has received 240 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


assistant5_cot5_1 = '''The user who posted this tweet has a moderate following of 42,826 followers, which is not considered highly influential. The tweet has received 240 retweets, which is not enough to indicate widespread endorsement or trigger bandwagon behavior. The message does not contain strong negative sentiment, but it does criticize modern diets and industrial seed oils. While the tweet does not directly address any of the prevalent narratives, it does touch upon health and diet issues and suggests that industrial seed oils are the cause of a common disease. This could imply distrust in technology and industrial food production, which aligns with the listed prevalent narratives.

Debunking the message might require some level of expertise or knowledge-seeking efforts, as it involves understanding the history of acne and its relationship with diet. People might need to research historical images, medical records, or scientific studies to verify the claim.

Considering these factors, the tweet might be believed by many in the given population due to the alignment with a prevalent narrative and the fact that debunking the message requires some level of expertise. However, the lack of strong emotional appeals and the low number of endorsements might limit its impact.

Believable by many (yes or no): Yes'''


user6_cot5_1 = '''A user with 1042 followers has tweeted the following potentially misleading message:

"You're fucking kidding me. https://t.co/AYwwIcHsJ4"

The message is followed by a screenshot at a certain time of a YouTube video titled "Rick Astley - Never Gonna Give You Up (Video)" with 961,621,928 views, posted on Oct 25, 2009. The video is from the Official Rick Astley channel with 2.19M subscribers. The description mentions that the video will be auctioned off as an NFT and removed from YouTube on June 27th, 2021.

The tweet has received 4943 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


assistant6_cot5_1 = '''The tweet is posted by a user with 1042 followers, which is not considered highly influential. However, the tweet has received 4943 retweets, which is a significant number and could trigger bandwagon behavior. The tweet contains negative sentiment, as indicated by the use of profanity, which could sway people more than neutral or positive sentiment.

The message does not directly appeal to prevalent narratives such as distrust in the government, politicians, vaccines, technology, or mainstream news media. However, the idea of a popular video being removed from YouTube and auctioned off as an NFT could be seen as a negative development related to technology and digital ownership. This might resonate with people's concerns about technology and the direction of the internet and digital content, which is one of the prevalent polarizing narratives.

Debunking the message does not require a high level of expertise, as one could simply visit the YouTube video and check its description or look for news articles about the auction. However, the population in question does not often think rationally or critically, which might make them less likely to verify the information.

Considering these factors, it is possible that the tweet's message would be believed by many in the given population.

Believable by many (yes or no): Yes'''


user7_cot5_1 = '''A user with 1559 followers has tweeted the following potentially misleading message:

"Y’all know that vaccine ain’t approved by the FDA right?"

The tweet has received 162 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


assistant7_cot5_1 = '''The user who posted this tweet has a small following of 1,559 followers, which is not considered highly influential. The tweet has received 162 retweets, which is not enough to indicate widespread endorsement or trigger bandwagon behavior. The message does not involve strong emotional appeals, but it does contain a negative sentiment, as it casts doubt on the vaccine's approval by the FDA.

The tweet aligns with a prevalent narrative of distrust in vaccines and the medical system. This might resonate with people who are skeptical about vaccines and their safety. Debunking the message might require some level of expertise or knowledge-seeking efforts, as it involves understanding the FDA approval process and the status of various COVID-19 vaccines.

Considering these factors, the tweet might be believed by many in the given population due to the negative sentiment, alignment with a prevalent narrative and the fact that debunking the message requires some level of expertise, though the low influence of the author and the low number of endorsements might limit its reach.

Believable by many (yes or no): Yes'''


user8_cot5_1 = '''A user with 5931148 followers has tweeted the following potentially misleading message:

"top 5 richest streamers based on the twitch leak;
1. Xqc (1.3 Trillion)
2. Dream ($7.9 Billion)
3. Obama (696 Million)
4. HasanAbi (House)
5. TommyInnit (100 Million)"

The tweet has received 7361 retweets.

Considering the four factors in the guidelines provided, would this tweet's message be believed by many or by few in the given population?

Keep in mind that even if a tweet has apparent factual errors or logical fallacies, it could still sway a large population if it has strong emotional resonance or appeals to prevalent narratives. So, rather than focusing on whether a claim seems believable to you as an AI, consider the factors that might make it believable to the general public, such as the influence of the author and the endorsements received by the tweet, sentiment and emotional appeals, alignment with prevalent narratives and existing beliefs, and the amount of effort or expertise required to debunk a claim. Please do not dismiss a claim as "believable by few" simply because it seems unlikely or counterintuitive.

Make sure your arguments are supported by sound reasoning, and avoid any unsupported leaps in reasoning or contradictory statements. Focus on maintaining a consistent logical flow throughout your response.

After you are done with your reasoning, please provide a single token yes/no answer.'''


assistant8_cot5_1 = '''The user who posted this tweet has a large following of over 5.9 million followers, which is considered highly influential and might trigger bandwagon behavior. The tweet has received 7,361 retweets, which is a significant number, though not enough to be considered widely endorsed. The message does not contain strong emotional appeals or negative sentiment.

The tweet does not align with any prevalent narratives or popular beliefs. It is a list of the top 5 richest streamers based on a Twitch leak, which is not related to any of the listed prevalent narratives. Debunking the message might require some effort or a certain level of expertise, as it involves understanding the Twitch leak and verifying the net worth of the mentioned streamers. However, the inclusion of "Obama" in the list might be seen as a joke or an attempt at humor, which could make the tweet less believable.

Considering these factors, the tweet's message might be believed by few in the given population due to the lack of negative sentiment, lack of alignment with prevalent narratives, and the humorous nature of the message.

Believable by many (yes or no): No'''