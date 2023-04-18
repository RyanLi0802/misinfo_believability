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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''

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
- distrust in mainstream news media.'''