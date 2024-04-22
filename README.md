# PubTest

## Introduction

[Link to PubTest](https://pubtest-ax51.onrender.com/)

The _weight of public opinion_ has been invoked in many arguments to lend a sense of credibility and urgency. This is seen in government, lobby groups, and corporate leadership to drive agendas that are often not in the best interest of the community. 

A popular variant of of this is the _pub test_, a colloquial reference to seek out the opinion of the ordinary Australian i.e. a publican. While the inherent bias of this cohort is overlooked, the idea of the layperson's views carries ideological and empathetic clout (and an imbibed patron may well be more "truthful").

**PubTest** delivers this concept in the form of a poll at its simplest – a yes or no question. 

PubTest's hypotheses: 

- While there is nuance and complexity to every discussion, an opinion is inherently for or against (as seen in referendums).
- The app is focused on big data (i.e. no personally-identifiying data), and that anonymity will allow for more honest voting.
- Paired with question, a summary and a news article are provided for context. This caters for various cognitive types i.e. quick vs thoughtful thinkers.

## Features

PubTest utilises two APIs to generate the yes/no questions.

News data is collected from [The Guardian](https://open-platform.theguardian.com/documentation/) (AU), firstly because it is free and secondly, the documentation is good. In keeping with the Australian theme, the articles are from the *Australian-News* section.

This data is then added to a prompt that is fed into [Open AI](https://platform.openai.com/docs/overview)'s ChatGPT. The result is a one-sentence summary of the news article and yes/no question. This mimics the stages of a casual conversation:

"Do you agree with **this**?"\
-- "YES / NO"\
-- "_I don't know much about it_" (provide a quick overview → summary)\
&ensp;&ensp;&ensp;|-- "Ah, YES / NO"\
&ensp;&ensp;&ensp;|-- "_I think there's more to it_" (a deeper conversation → article)\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|--"Ah, YES / NO"

Results of each question are also provided.

## Technologies

- Python
- Django
- Render
- Bootstrap

## Roadmap

- Data visualisation of results – pyramid plot demographic variables against yes/no.
- Result access based on information provided e.g. provide _year of birth_ allows user to view votes split up by age.
- A second view that separates articles that have been voted on.
- Notification for when votes reach a certain threshold. 
- Automate the question-generation request.
- Data analysis on results e.g. identify when a result has statistical signficance.
- Add more demographic variables. 
- API to other new sources.
- Add additional news sections e.g. world news, sport, politics. 

## Credits

Heartfelt appreciation to [Jo3l](https://github.com/wofockham) and [CJ](https://github.com/Bissmark) for their support and encouragement.