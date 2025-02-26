import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1 - Criando um Dataframe fictício
data = {
    'Preço': [20, 25, 30, 18, 22],
    'Quantidade': [100, 120, 90, 110, 105],
    'Receita': [2000, 3000, 2700, 1980, 2310]
}

df = pd.DataFrame(data)
print(df)

# 2 - Criando um pairplot com Seaborn
sns.set(style='ticks')
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Relações entre Preço, Quantidade e Receita', y=1.02)
plt.show()