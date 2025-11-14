# FABLE = [
#     "Does the message fit into a larger story or argument, for example about how the world works or how people think?",#0
#     "Does the message question trust in or the functioning of public institutions?",#1
#     "Does the message question trust in or the functioning of the scientific community as a whole?",#2
#     "Does the message question the functioning of or trust in news sources/the media in general?",#3
#     "Does the message question the trustworthiness of other people in general within a community or society?",#4
#     "In a democratic country where there are elections, does the message directly attack the election process?",#5
   
#     "Does the message content include an explicit call to action?",#5
#     "Does the piece of content incorporate coordination efforts, such as dates/times or other arrangements for follow-up?",#6
#     "Does the message provide a name or otherwise any identifying information about an individual, an address, or a place of work in such a way that people might be directly harmed?",#7
#     "Does the message content include a tone of urgency or mention of time sensitivity?",#8
#     "Does the message content include any threats of violence?",#9
#     "Does the message lay blame or cast aspersions or hatred on a particular group, such as a particular religion, gender, sexual orientation, race, country, or culture, that has been harmed in the past by the audience of the content?",#10
#     "Does the message invoke a sense of injustice or moral outrage, including on behalf of a vulnerable individual or group such as children or women?",#11
#     "Does the direct target or current audience members directly addressed in the message have a recent history of taking actions that cause harm?",#12
#     "Is this message associated with/similar to other messages that are also actionable?",#13
   
#     "Is there a lack of high quality information that is publicly accessible and is refuting the message’s claim?",#13
#     "Is there a lack of consensus on the part of experts regarding the claim?",#14
#     "Does the message fail to include external citations, links, or language about evidence to support its claim?",#15
#     "Does the message contain richer formats as part of its evidence that lay people consider to have low falsifiability?",#16
#     "Is the message written or communicated in a personal or persuasive tone?",#Dose=>is#17
#     "Does the message make reference to the broad believability of the claim or topic?",#18
#     "Does the message appeal to a specific community identity by mentioning a shared set of values or beliefs?",#19
#     "Does the poster and/or organization/outlet have a noteworthy number of social media/community followers?",#20
#     "Is the content published by an organization/outlet with uncertain editorial control (e.g., is not a recognized news publisher)?",#21
#     "Does the poster have credentials that represents some kind of expertise?",#22
#     "Is the content posted by an imposter individual or counterfeit outlet that could successfully pass as a different person/account based only upon a quick glance?",#23
#     "Does the content have the graphics and styling of a legitimate news agency or mainstream information source?",#24
   
#     "Do the people or entities who are spreading the piece of content have a broad reach (size of following on social media, “influencer,” presence on TV or other news media)?",#24
#     "Are the people or entities known to be repeat spreaders of questionable information?",#25
#     "Is there evidence of coordination activity (whether bot/automated or not) to encourage spread?",#26
#     "Is the content publicly accessible (posted on a public platform, addressable URL)? Is the content posted on a popular platform?",#27
#     "Is the content spreading on multiple platforms?",#28
#     "Does one of the platforms upon which the content is shared have tools to support amplification (e.g., reshares, algorithmic feeds, recommendation engines)?",#29
#     "Does the message make direct appeals to audience members that it is in their financial, political, or social interest to spread the content further?",#30
#     "Does the message directly call audience members to share the content further?",#31
#     "Is the tone of the content striking enough in ways that encourage sharing?",#32
#     "Does the content contain an image, audio-clip, or other richer formats that are easy to remember, visually or aurally arresting, or seems interesting to share?",#33
#     "Does the message impart a sense of exclusivity or novelty ('breaking news')?",#34
#     "Are there hashtags associated with the message?",#35
#     "Is the message difficult to fact-check or prove false?",#36
#     "Is the message related to a current event or a topic that is being reported on actively by many news outlets?",#37
   
#     "Does the message directly address or reference children or use language aimed at a younger audience?",#37
#     "Does the message introduce a degree of fear or feelings of uneasiness?",#38
#     "Is the message content complicated to understand?",#39
#     "Does the message directly address or reference elderly community members, or discuss topics aimed at them?",#40
#     "Does the message directly address or reference military veterans, or discuss topics aimed at them?",#41
#     "Does the message make mention of a reader’s feelings of isolation?",#42
#     "Does the message make mention of a reader’s feelings of powerlessness?",#43
#     "Does the message make mention of a reader’s feelings of disenfranchisement?",#44
#     "Is this message being shared by within an online group, community, or thread that has a recent history of discussing conspiracy theories or viral misinformation?",#45
#     "Is the language of the intended audience neither a UN language (English, French, Spanish, Mandarin Chinese, Russian) nor on the top 5 list of most popular languages?",#46
#     "Is the message presented in a region where the local context might amplify its harm?"#47
# ]

# FABLE = Fragmentation+Actionability+Believability+Likelihood_of_Spread+Exploitativeness
Important_Question_flag = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0]

# FABLE=[
#     "In a democratic country where there are elections, does the message directly attack the election process?",#5
#     "Does the message content include an explicit call to action?",#5
#     "Is this message associated with/similar to other messages that are also actionable?"#13
#     "Is there a lack of high quality information that is publicly accessible and is refuting the message’s claim?",#13
#     "Does the content have the graphics and styling of a legitimate news agency or mainstream information source?",#24
#     "Do the people or entities who are spreading the piece of content have a broad reach (size of following on social media, “influencer,” presence on TV or other news media)?",#24
#     "Is the message related to a current event or a topic that is being reported on actively by many news outlets?",#37
#     "Does the message directly address or reference children or use language aimed at a younger audience?"#37
# ]


FABLE = [
    "Does the message fit into a larger story or argument, for example about how the world works or how people think?",#0
    "Does the message question trust in or the functioning of public institutions?",#1
    "Does the message question trust in or the functioning of the scientific community as a whole?",#2
    "Does the message question the functioning of or trust in news sources/the media in general?",#3
    "Does the message question the trustworthiness of other people in general within a community or society?",#4
    "In a democratic country where there are elections, does the message directly attack the election process?",#5
   
    "Does the message content include an explicit call to action?",#5
    "Does the piece of content incorporate coordination efforts, such as dates/times or other arrangements for follow-up?",#6
    "Does the message provide a name or otherwise any identifying information about an individual, an address, or a place of work in such a way that people might be directly harmed?",#7
    "Does the message content include a tone of urgency or mention of time sensitivity?",#8
    "Does the message content include any threats of violence?",#9
    "Does the message lay blame or cast aspersions or hatred on a particular group, such as a particular religion, gender, sexual orientation, race, country, or culture, that has been harmed in the past by the audience of the content?",#10
    "Does the message invoke a sense of injustice or moral outrage, including on behalf of a vulnerable individual or group such as children or women?",#11
    "Does the direct target or current audience members directly addressed in the message have a recent history of taking actions that cause harm?",#12
    "Is this message associated with/similar to other messages that are also actionable?",#13
   
    "Is there a lack of high quality information that is publicly accessible and is refuting the message’s claim?",#13
    "Is there a lack of consensus on the part of experts regarding the claim?",#14
    "Does the message fail to include external citations, links, or language about evidence to support its claim?",#15
    "Does the message contain richer formats as part of its evidence that lay people consider to have low falsifiability?",#16
    "Is the message written or communicated in a personal or persuasive tone?",#Dose=>is#17
    "Does the message make reference to the broad believability of the claim or topic?",#18
    "Does the message appeal to a specific community identity by mentioning a shared set of values or beliefs?",#19
    "Does the poster and/or organization/outlet have a noteworthy number of social media/community followers?",#20
    "Is the content published by an organization/outlet with uncertain editorial control (e.g., is not a recognized news publisher)?",#21
    "Does the poster have credentials that represents some kind of expertise?",#22
    "Is the content posted by an imposter individual or counterfeit outlet that could successfully pass as a different person/account based only upon a quick glance?",#23
    "Does the content have the graphics and styling of a legitimate news agency or mainstream information source?",#24
   
    "Do the people or entities who are spreading the piece of content have a broad reach (size of following on social media, “influencer,” presence on TV or other news media)?",#24
    "Are the people or entities known to be repeat spreaders of questionable information?",#25
    "Is there evidence of coordination activity (whether bot/automated or not) to encourage spread?",#26
    "Is the content publicly accessible (posted on a public platform, addressable URL)? Is the content posted on a popular platform?",#27
    "Is the content spreading on multiple platforms?",#28
    "Does one of the platforms upon which the content is shared have tools to support amplification (e.g., reshares, algorithmic feeds, recommendation engines)?",#29
    "Does the message make direct appeals to audience members that it is in their financial, political, or social interest to spread the content further?",#30
    "Does the message directly call audience members to share the content further?",#31
    "Is the tone of the content striking enough in ways that encourage sharing?",#32
    "Does the content contain an image, audio-clip, or other richer formats that are easy to remember, visually or aurally arresting, or seems interesting to share?",#33
    "Does the message impart a sense of exclusivity or novelty ('breaking news')?",#34
    "Are there hashtags associated with the message?",#35
    "Is the message difficult to fact-check or prove false?",#36
    "Is the message related to a current event or a topic that is being reported on actively by many news outlets?",#37
   
    "Does the message directly address or reference children or use language aimed at a younger audience?",#37
    "Does the message introduce a degree of fear or feelings of uneasiness?",#38
    "Is the message content complicated to understand?",#39
    "Does the message directly address or reference elderly community members, or discuss topics aimed at them?",#40
    "Does the message directly address or reference military veterans, or discuss topics aimed at them?",#41
    "Does the message make mention of a reader’s feelings of isolation?",#42
    "Does the message make mention of a reader’s feelings of powerlessness?",#43
    "Does the message make mention of a reader’s feelings of disenfranchisement?",#44
    "Is this message being shared by within an online group, community, or thread that has a recent history of discussing conspiracy theories or viral misinformation?",#45
    "Is the language of the intended audience neither a UN language (English, French, Spanish, Mandarin Chinese, Russian) nor on the top 5 list of most popular languages?",#46
    "Is the message presented in a region where the local context might amplify its harm?"#47
]
