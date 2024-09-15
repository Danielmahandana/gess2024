import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import nltk
from textblob import TextBlob

# Sample data from interviews
data = {
    'Interviewee': ['Laura', 'Thomas', 'Interview 1', 'Interview 2'],
    'Key Insights': [
        "Skepticism in ads, importance of trustworthy sources, media influence on food beliefs.",
        "Prevalence of misleading claims, trust in regulations, social media’s influence.",
        "Verification of info via multiple sources, social media echo chambers.",
        "Misinformation in food myths, fitness influencers, gov’t responsibility."
    ],
    'Influencing Factors': [
        "Influencers, Beliefs, Media Filtering",
        "Regulation Trust, Cross-checking Claims",
        "Social Media, Echo Chambers",
        "Social Media, Fitness Trends, Gov't Labels"
    ],
    'Verification Methods': [
        "Trustworthy sources, experts with research",
        "Scientific studies, cross-referencing",
        "Cross-checking multiple sources",
        "Scientific studies, government labels"
    ],
    'Sentiment': [
        TextBlob("Skepticism in ads, importance of trustworthy sources, media influence on food beliefs.").sentiment.polarity,
        TextBlob("Prevalence of misleading claims, trust in regulations, social media’s influence.").sentiment.polarity,
        TextBlob("Verification of info via multiple sources, social media echo chambers.").sentiment.polarity,
        TextBlob("Misinformation in food myths, fitness influencers, gov’t responsibility.").sentiment.polarity
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Title of the Streamlit App
st.title("Impact of Misinformation on Food Awareness")

# Display the DataFrame
st.write("### Summary of Interviews")
st.dataframe(df)

# Adding a Word Cloud for Influencing Factors
st.write("### Word Cloud of Influencing Factors")
all_factors = " ".join(df['Influencing Factors'])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_factors)

# Display the word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Sentiment Analysis
st.write("### Sentiment Analysis of Interviews")
st.bar_chart(df.set_index('Interviewee')['Sentiment'])

# Correlation Analysis (based on hypothetical metrics for insight)
st.write("### Correlation Between Misinformation Factors and Trust")
# Sample correlation data
correlation_data = {
    'Trust in Media': [0.7, 0.6, 0.4, 0.5],
    'Skepticism Level': [0.5, 0.3, 0.6, 0.4],
    'Misinformation Impact': [0.8, 0.5, 0.7, 0.6]
}
cor_df = pd.DataFrame(correlation_data, index=df['Interviewee'])

# Heatmap of correlation
st.write("### Correlation Heatmap")
sns.heatmap(cor_df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
st.pyplot()

# Filtering by Interviewee or Factor
st.write("### Explore Interview Insights")

# Filter by Interviewee
interviewee_filter = st.selectbox('Choose an Interviewee:', df['Interviewee'])

# Display filtered data
st.write(df[df['Interviewee'] == interviewee_filter])

# Additional filtering by misinformation factors
factor_filter = st.multiselect('Filter by Influencing Factors:', df['Influencing Factors'].unique())

if factor_filter:
    st.write("### Filtered Data Based on Selected Factors")
    filtered_data = df[df['Influencing Factors'].isin(factor_filter)]
    st.write(filtered_data)

# Adding some interactive text analysis
st.write("### Explore Insights Based on Specific Keywords")
keyword = st.text_input("Enter a keyword to search for in the insights (e.g., 'misinformation', 'media', 'influencers')")

if keyword:
    results = df[df['Key Insights'].str.contains(keyword, case=False)]
    st.write(f"Results matching '{keyword}':")
    st.dataframe(results)
