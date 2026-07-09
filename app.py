import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob

st.set_page_config(page_title="Enterprise KRI Dashboard", layout="wide")
st.title("🛡️ Enterprise KRI Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sample_kri_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Sentiment"] = df["Risk_Log_Description"].apply(lambda t: TextBlob(str(t)).sentiment.polarity)
    return df

df=load_data()

cats=st.sidebar.multiselect("KRI Category",df["KRI_Category"].unique(),default=list(df["KRI_Category"].unique()))
df=df[df["KRI_Category"].isin(cats)]

def status(r):
    if r.Risk_Metric_Value>=r.Threshold_Red:return "Red"
    if r.Risk_Metric_Value>=r.Threshold_Amber:return "Amber"
    return "Green"
df["Status"]=df.apply(status,axis=1)

c1,c2,c3=st.columns(3)
c1.metric("Indicators",len(df))
c2.metric("Critical",(df["Status"]=="Red").sum())
c3.metric("Avg Sentiment",round(df["Sentiment"].mean(),2))

st.plotly_chart(px.bar(df,x="Date",y="Risk_Metric_Value",color="Status"),width="stretch")
st.plotly_chart(px.scatter(df,x="Sentiment",y="Risk_Metric_Value",color="KRI_Category",size="Risk_Metric_Value"),width="stretch")
st.dataframe(df,width="stretch")
