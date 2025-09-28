import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Basic setup
st.title("🤖 My First Excel AI Agent")
st.write("Upload an Excel file and I'll analyze it for you!")

# File upload
uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])

if uploaded_file is not None:
    try:
        # Load the file
        df = pd.read_excel(uploaded_file)
        st.success("✅ File loaded successfully!")
        
        # Show basic info
        st.subheader("📊 Data Overview")
        st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
        
        st.write("**Column Names:**")
        for col in df.columns:
            st.write(f"- {col}")
        
        st.write("**First 5 rows:**")
        st.dataframe(df.head())
        
        # Simple questions section
        st.subheader("🤔 Quick Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Show Shape"):
                st.info(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
            
            if st.button("Show Data Types"):
                st.info("Data Types:")
                for col in df.columns:
                    st.write(f"{col}: {df[col].dtype}")
        
        with col2:
            if st.button("Show Statistics"):
                st.info("Basic Statistics:")
                st.dataframe(df.describe())
            
            if st.button("Check Missing Values"):
                missing = df.isnull().sum().sum()
                if missing == 0:
                    st.success("✅ No missing values!")
                else:
                    st.warning(f"❌ {missing} missing values found")
        
        # Simple graph section
        st.subheader("📈 Create a Graph")
        
        # Get numeric columns for plotting
        numeric_cols = df.select_dtypes(include=['number']).columns
        
        if len(numeric_cols) > 0:
            selected_col = st.selectbox("Choose a column to graph:", numeric_cols)
            
            if st.button("Generate Chart"):
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(df.index, df[selected_col], marker='o', linewidth=2, markersize=8)
                ax.set_title(f"Trend of {selected_col}")
                ax.set_xlabel("Index")
                ax.set_ylabel(selected_col)
                ax.grid(True, alpha=0.3)
                
                st.pyplot(fig)
                st.success("📊 Chart generated successfully!")
        else:
            st.info("No numeric columns found for graphing.")
        
        # Show full data
        with st.expander("📋 View Full Dataset"):
            st.dataframe(df)
            
    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("👆 Please upload an Excel file to get started!")
    st.write("Try uploading the 'sales_data.xlsx' file we just created!")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
