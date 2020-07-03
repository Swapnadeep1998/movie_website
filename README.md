# Classifying Movie Reviews Sentiment & Recommending Movies

This is a Hackathon Project

#Team members
1. Swapnadeep Sarkar
2. Subidita Maity
3. Md. Irshad

Our movie website has 3 main features,

1. It recommends movie based on user inputs.

2. It classifies the reviews using sentiment analysis and shows the Negative and Positive ratios,
It’s unique from existing ones like IMDB, because IMDB shows percentage of likes and dislikes
basd on number of users clicking the like and dislike button. It doesn’t show any sentiment
classification of reviews to the users, IMDB does sentiment analysis for business purpose not
to show its result to end users.
Hence Our model eventually reduces probability of un-reliable likes and dislikes ratio.

3. The most important part we did was tackling fake reviews as well, We added a profile
points feature. The concept is somewhat similar to sites like hackarrank where each user
earns points based on their experience and performance.
In our site, while going through reviews of a particular movie the the user can rate a review of
another user indicating howmuch helpful that review was. Point ranging from 1-5. This rate
points get added to the profile of the user whose review was rated.
The added points shows how much experienced a profile is.
And while going through reviews of a particular movie the viewer gets to see the profile points
of the reviewers, and hence will get an idea about that, which review is more likely to be reliable, as its coming from an experience user having high profile points.

Youtube link of this project demonstration:
https://youtu.be/AtNg5vvKMug

Application URL
http://ec2-13-232-120-215.ap-south-1.compute.amazonaws.com:8080


Tools/Algorithms used
1. For recommendation - Colaborative Filtering
2. For Sentiment Analysis - pretrained word2vec embedding layer and Bi-LSTM
3. Google colab used for training
4. Deployment was done using AWS ec2 instance
5. Database used - PostGRESQL on AWS RDS
