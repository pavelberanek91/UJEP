from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
import matplotlib.pyplot as plt

# Inicializace SparkSession
spark = SparkSession.builder.appName("KMeansClustering").getOrCreate()

# Načtení dat ze sdílené složky
data_path = "/opt/spark-data/artificial_data.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Převod sloupců na vektory pro clustering
vec_assembler = VectorAssembler(inputCols=["x", "y"], outputCol="features")
vec_df = vec_assembler.transform(df)

# KMeans clustering
kmeans = KMeans(k=3, seed=1)  # 3 clustery
model = kmeans.fit(vec_df)
transformed = model.transform(vec_df)

# Převod výsledků do seznamu Python objektů
data = transformed.select("x", "y", "prediction").collect()

# Rozdělení dat do clusterů
clusters = {0: [], 1: [], 2: []}  # Očekáváme 3 clustery
for row in data:
    clusters[row["prediction"]].append((row["x"], row["y"]))

# Vykreslení výsledků pomocí matplotlib
plt.figure(figsize=(8, 6))
colors = ['blue', 'green', 'red']
for cluster_id, points in clusters.items():
    x_vals, y_vals = zip(*points)
    plt.scatter(x_vals, y_vals, label=f"Cluster {cluster_id}", color=colors[cluster_id])
plt.title("KMeans Clustering")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
output_path = "/opt/spark-data/output.png"
plt.savefig(output_path)
print(f"Výsledek byl uložen do: {output_path}")

# Ukončení SparkSession
spark.stop()
