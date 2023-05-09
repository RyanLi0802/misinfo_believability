# Q1 for positive relationship and Q2 for negative



# Distrust in the government and politicians

gov_system_message = "For each of the following potentially misleading tweets, explain if the tweet conveys distrust " \
                     "in the government system and politicians.\n\nAt the end of each response, provide a single " \
                     "token Yes/No answer for whether the tweet conveys distrust in the government system and " \
                     "politicians.\n\nIf the tweet misses important context or is too vague to determine, answer no. "

gov_q1_user = "A user tweeted the following message: \"Ron DeSantis can't get out ahead of what's coming for him " \
              "https://t.co/6mR3rZwEej.\"\n\nDoes this tweet express distrust in the government and politicians?"

gov_q1_assistant = "This tweet refers to Florida Governor Ron DeSantis and suggests DeSantis couldn’t evade the ensuing " \
                   "consequences. This tweet implicitly indicates it is due to his past questionable actions or " \
                   "decisions. Hence, it conveys distrust in government and politicians.\n\nAnswer: Yes"

gov_q2_user = "A user tweeted the following message: \"It's official, Donald Trump has the best #HotlineBling dance " \
              "moves: https://t.co/kEaxj5bew2 https://t.co/jBMU1W7MJm.\"\n\nDoes this tweet express distrust in the " \
              "government and politicians?"

gov_q2_assistant = "This tweet is about a re-creation video of Donald Trump dancing Hotline Bling and does not relate " \
                   "to any political or governmental actions. Therefore, it does not convey distrust in the government " \
                   "system and politicians.\n\nAnswer: No"

gov = {"system_msg": gov_system_message, "q1_user": gov_q1_user, "q1_assistant": gov_q1_assistant,
       "q2_user": gov_q2_user, "q2_assistant": gov_q2_assistant, }










# Distrust in technology and large tech companies

tech_system_message = "For each of the following potentially misleading tweets, explain if the tweet conveys distrust " \
                      "in technology and large tech companies. \nAt the end of each response, provide a single token " \
                      "Yes/ No answer for whether the tweet conveys distrust in technology and large tech companies . "

tech_q1_user = "A user tweeted the following message: \"Here are the facts on Fauci that big tech doesn't want you to " \
               "know. https://t.co/qDAdMOFMFq\".Does this tweet express distrust in technology and large tech " \
               "companies? "
tech_q1_assistant = "The tweet suggests that there are facts about Fauci that big tech companies are hiding, " \
                    "which implies distrust in technology and large tech companies. \nAnswer: Yes "

tech_q2_user = "A user tweeted the following message: \"Apple's self-driving car could feature VR technology and no " \
               "windows: https://t.co/86T8nP1LOX https://t.co/YCwrVrJRjc\" \nDoes this tweet express distrust in " \
               "technology and large tech companies? "

tech_q2_assistant = "The tweet is about a new technology that Apple is developing for self-driving cars, and it does " \
                    "not express distrust in technology or large tech companies.\nAnswer: No "

tech = {"system_msg": tech_system_message, "q1_user": tech_q1_user, "q1_assistant": tech_q1_assistant,
        "q2_user": tech_q2_user, "q2_assistant": tech_q2_assistant}


narratives = {
    "distrust_in_gov": ("distrust in the government and politicians", gov),
    # "vaccine": "distrust in vaccines and the medical system"
}
