# Data science course map

1. Time Series Analysis         (**20** + 6 = 26)
   1. Intro `Udny Yule`
   2. ETL
      1. Dataset
      2. Timestamps
      3. Missing values
      4. Smoothing `Holt-Winters`, `Kalman`
      5. Seasonality
   3. Exploratory Data Analysis
      1. Stationarity `Augmented Dickey-Fuller (ADF)`
      2. Rolling windows
      3. Auto/Self correlation
      4. Plots
   4. Simulation (Skipped)
   5. Data storage
      1. SQL vs NoSQL vs File
      2. InfluxDB vs Prometheus vs MongoDB
   6. ARIMA
      1. AR `Akaike info criterion (AIC)`
      2. Residual test `Ljung-Box`
      3. MA
      4. ARIMA `Wold theo`, `Box-Jenkins`
      5. VAR
      6. SARIMA
      7. ARIMAX
      8. ARCH
      9. Hyerarchical models
   7. State Space Models
      1. Kalman filter
      2. Hidden Markov models `Baum Welch`, `Viterbi`
      3. Structural Bayesian Series
   8. Generate + Select features
      1. Generate `Lomb-Scargle`
      2. Select `FRESH + Benjamini-Yekutieli`, `RFE`
   9. Machine learning
      1.  Bagging vs Boosting (Classification)
      2.  7 distances (Clustering)
   10. Deep Learning
      1.  NC vs NTC vs TNC
      2.  FF, CNN, RNNm AutoEnc, hybrid
2. Social Network Analysis      ( **7** + 0 =  7)
   1. Intro
      1. Types of SN
      2. Informal SN
      3. Weak SN `Granoveter '73`, `Dumbar '67`
   2. Graph theory
      1. Weighted graph `Likert`, `Krackhard`
      2. 3 Graph representations
      3. 3 Distances
      4. Six Deg of Sep
   3. Centrality
      1. Sampling
      2. 4 Centralities
      3. The content
   4. Components `Island meth`, `Ego nets`
      1. Triads, n-Clique, n-Clan, k-Plex, k-Core
      2. Negative edges
   5. Critical Mass
      1. Homophily `Lazarsfeld-Merton`
      2. Curiosity
   6. N-Mode Network
      1. Bimodal
      2. Multimodal
3. Natural Language Processing  (**15** + 6 = 21)
   1. Language
      1. 4 components
      2. Heuristic NLP
      3. Machine Learning NLP
      4. Deep Learning NLP
   2. Pipeline NLP
   3. Text Representation
      1. 4 SOTA approaches
      2. Basic Vector Encoding
      4. Distributional Encodings `Mikolov`, `CBOW`, `SkipGram`
      3. Distributed Encodings `Doc2Vec`
      4. Visualize Embeddings
   4. Text Classification
      1. Heuristic
      2. Machine Learning
      3. Deep Learning
      4. Weak vs Strong supervision
   5. Chatbot
      1. Taxonomy
      2. Pipeline
      3. Seq2Seq
      4. Human in the Loop
      5. Rasa
   6. Information Extraction
      1. Pipeline
      2. KPE
      3. NER
      4. RE
      5. Advanced Tasks
   7. Other NLP Tasks
      1. Search&Info retrieval
      2. Topic Modeling
      3. Rext Summarizing
      4. Recommender System
      5. Machine Translation
      6. Question Answering
