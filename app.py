import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cấu hình mặc định
st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")

# Dữ liệu mô phỏng
data = {
    'Order Date': pd.date_range(start='2022-01-01', periods=200, freq='D'),
    'Product Name': ['Product A', 'Product B', 'Product C', 'Product D'] * 50,
    'Quantity Ordered': [5, 3, 8, 2] * 50,
    'Sales': [100, 60, 160, 40] * 50,
    'Region': ['North', 'South', 'East', 'West'] * 50,
    'Category': ['Electronics', 'Clothing', 'Books', 'Home'] * 50
}
df = pd.DataFrame(data)

# Thêm các cột cần thiết
df['Week_Year'] = df['Order Date'].dt.to_period('W').astype(str)

# Tổng hợp dữ liệu
weekly_sales = df.groupby(['Week_Year', 'Product Name']).agg({
    'Quantity Ordered': 'sum',
    'Sales': 'sum'
}).reset_index()
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

# Giao diện
st.title("📊 Amazon Sales Visualization Dashboard")

# Biểu đồ 1: Weekly Sales by Product
st.subheader("1. Weekly Sales by Product")
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=weekly_sales, x='Week_Year', y='Sales', hue='Product Name', marker="o", ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
ax1.set_title("Weekly Sales by Product")
st.pyplot(fig1)

# Biểu đồ 2: Weekly Quantity Ordered by Product
st.subheader("2. Weekly Quantity Ordered by Product")
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=weekly_sales, x='Week_Year', y='Quantity Ordered', hue='Product Name', marker="o", ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
ax2.set_title("Weekly Quantity Ordered by Product")
st.pyplot(fig2)

# Biểu đồ 3: Total Sales by Category
st.subheader("3. Total Sales by Category")
fig3, ax3 = plt.subplots(figsize=(7, 4))
sns.barplot(data=category_sales, x='Category', y='Sales', palette='pastel', ax=ax3)
ax3.set_title("Total Sales by Category")
st.pyplot(fig3)

# Biểu đồ 4: Total Sales by Region
st.subheader("4. Total Sales by Region")
fig4, ax4 = plt.subplots(figsize=(7, 4))
sns.barplot(data=region_sales, x='Region', y='Sales', palette='Set2', ax=ax4)
ax4.set_title("Total Sales by Region")
st.pyplot(fig4)

# Biểu đồ 5: Quantity Ordered vs Sales (Scatter)
st.subheader("5. Quantity Ordered vs Sales")
fig5, ax5 = plt.subplots(figsize=(7, 4))
sns.scatterplot(data=df, x='Quantity Ordered', y='Sales', hue='Product Name', palette='muted', ax=ax5)
ax5.set_title("Quantity Ordered vs Sales")
st.pyplot(fig5)

st.markdown("---")
st.caption("© 2025 Trần Tuấn Cảnh – ABC Manufacturing Data Science Project")
