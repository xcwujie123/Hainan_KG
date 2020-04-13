# Event-centric Tourism Knowledge Graph
This project is mainly the application of ETKG in Hainan. ETKGCN is the Framework of our POI recommendation system and the task-oriented conversational is the QA system based on Rasa. Due to space constraints, we cannot upload the complete knowledge Graph, we will introduce ETKG here simply.

Traditional tourism knowledge Graph a knowledge base which focuses on the static facts about entities, such as hotels, attractions, while ignoring events or activities of tourists' trips and temporal relations.
![image](https://github.com/xcwujie123/Hainan_KG/blob/master/fig10.png)

ETKG has following characteristics:
1. The graph is centered on the activities that tourists have participated in during the trips and regard uses tourists' trajectories as carriers. Therefore, we can solve users' questions about activities and routes during the trip.
2. The graph supports W3C standard(RDF, SPARKQL).
3. In practice, not only can the graph be used to search for the answers of tourists’ question directly (QA), but it help us to summarize knowledge at a deeper level. The information can be used as a prior knowledge when we analyze the behavior of tourists (RS). Here we show the application of these two levels in Hainan (Question answering system and Recommender system).

One tourist's journey is represented in the ETKG as follows.
![image](https://github.com/xcwujie123/Hainan_KG/blob/master/fig5.png)

Here is a use case when a tourist ask for a good place for diving.

Question: Could you recommend suitable places for diving?
SPARQL: SELECT ?location WHERE {?e rdf:type:Event. ?e :hasActivity "diving". ?e :hasLocation ?location}.

We can get some transfer relationship is as follows(reveal Spatiotemporal relationship).
![image](https://github.com/xcwujie123/Hainan_KG/blob/master/fig6.png)

We give the QA framework as follow, and the code is in task-oriented conversational.
![image](https://github.com/xcwujie123/Hainan_KG/blob/master/fig7.png)

Recommendation system framework's code is in ETKGCN. Due to space constraints we give partial data.
