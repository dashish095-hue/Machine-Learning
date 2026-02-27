def cal_stats(data):
    import numpy as np 
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as st
    import warnings
    warnings.filterwarnings('ignore')

    column_name = getattr(data, 'name', 'Unnamed Column')
    print(f"\nStatistics for: {column_name}")

    if pd.api.types.is_numeric_dtype(data):
        total = np.sum(data)
        print('Total Sum:', total)

        count = len(data)
        print('Total Count:', count)

        mini = data.min()
        print('Minimum:', mini)

        maximum = data.max()
        print('Maximum:', maximum)

        ran = np.round(maximum - mini, 2)
        print('Range:', ran)

        avg = round(np.mean(data), 2)
        print('Average:', avg)

        med = round(np.median(data), 2)
        print('Median:', med)

        mo = st.mode(data)
        print('Mode:', mo)

        q1 = np.percentile(data, 25)
        print('Q1:', q1)

        q3 = np.percentile(data, 75)
        print('Q3:', q3)

        iqr = q3 - q1
        print('IQR:', iqr)

        lw = q1 - 1.5 * iqr
        print('Lower Whisker:', lw)

        uw = q3 + 1.5 * iqr
        print('Upper Whisker:', uw)

        vr = np.var(data)
        print('Variance:', vr)

        sta = np.std(data)
        print('Standard Deviation:', sta)

        sk = st.skew(data)
        print('Skewness:', sk)

        ku = st.kurtosis(data)
        print('Kurtosis:', ku)

        plt.figure(figsize=(6, 1.5))
        sns.boxplot(x=data, color='skyblue')
        plt.title(f"Boxplot for {column_name}")
        plt.xlabel(column_name)
        plt.grid(True, axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    else:
        print("This is a non-numeric column.")
        print(f"Total Count: {len(data)}")
        print(f"Unique Values: {data.nunique()}")
        print("Top 5 Most Frequent Values:")
        print(data.value_counts().head(5))
