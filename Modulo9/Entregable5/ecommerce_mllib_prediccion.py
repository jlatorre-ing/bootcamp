# =============================================================================
# Predicción de Compra de Clientes - E-Commerce con Apache Spark MLlib
# Caso: Introducción a Machine Learning Escalable con MLlib
# =============================================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, rand
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
import pyspark.sql.functions as F


# =============================================================================
# 1. INICIALIZAR SPARK SESSION
# =============================================================================
spark = SparkSession.builder \
    .appName("ECommerce_Purchase_Prediction_MLlib") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")
print("✅ SparkSession iniciada correctamente.")


# =============================================================================
# 2. GENERACIÓN DE DATOS SINTÉTICOS (simulando datos reales de e-commerce)
#    En producción, reemplazar con lectura desde HDFS, S3, Delta Lake, etc.
# =============================================================================

NUM_REGISTROS = 100_000

print(f"\n📊 Generando {NUM_REGISTROS:,} registros sintéticos de clientes...")

df_raw = spark.range(NUM_REGISTROS).select(
    col("id").alias("customer_id"),

    # Páginas vistas en los últimos 7 días (0–50)
    (rand() * 50).cast("integer").alias("paginas_vistas_7d"),

    # Tiempo promedio en el sitio en minutos (1–60)
    (rand() * 59 + 1).cast("integer").alias("tiempo_sesion_min"),

    # Compras históricas del cliente (0–20)
    (rand() * 20).cast("integer").alias("compras_historicas"),

    # Calificación promedio de productos vistos (1.0–5.0)
    (rand() * 4 + 1).cast("double").alias("calificacion_promedio"),

    # Días desde la última visita (0–30)
    (rand() * 30).cast("integer").alias("dias_ultima_visita"),

    # Productos añadidos al carrito (0–10)
    (rand() * 10).cast("integer").alias("items_carrito"),

    # Segmento del cliente (categórico)
    when(rand() < 0.33, "nuevo")
     .when(rand() < 0.66, "recurrente")
     .otherwise("vip").alias("segmento_cliente"),
)

# Etiqueta objetivo: 1 si el cliente comprará, 0 si no
# Lógica realista: más probabilidad si tiene items en carrito, es vip, etc.
df_raw = df_raw.withColumn(
    "label",
    when(
        (col("items_carrito") >= 3) |
        (col("compras_historicas") >= 10) |
        ((col("segmento_cliente") == "vip") & (col("paginas_vistas_7d") >= 15)),
        when(rand() < 0.80, 1).otherwise(0)
    ).otherwise(
        when(rand() < 0.20, 1).otherwise(0)
    ).cast("double")
)

print(f"   Registros generados: {df_raw.count():,}")
print(f"   Distribución de etiquetas:")
df_raw.groupBy("label").count().show()


# =============================================================================
# 3. PREPARACIÓN DE DATOS
# =============================================================================

print("\n🔧 Preparando features y pipeline de transformación...")

# 3.1 Codificar variable categórica 'segmento_cliente'
indexer = StringIndexer(
    inputCol="segmento_cliente",
    outputCol="segmento_idx",
    handleInvalid="keep"
)

# 3.2 Definir columnas numéricas de features
FEATURE_COLS = [
    "paginas_vistas_7d",
    "tiempo_sesion_min",
    "compras_historicas",
    "calificacion_promedio",
    "dias_ultima_visita",
    "items_carrito",
    "segmento_idx"
]

# 3.3 Vectorizar features
assembler = VectorAssembler(
    inputCols=FEATURE_COLS,
    outputCol="features_raw",
    handleInvalid="skip"
)

# 3.4 Escalar features (importante para Regresión Logística)
scaler = StandardScaler(
    inputCol="features_raw",
    outputCol="features",
    withMean=True,
    withStd=True
)


# =============================================================================
# 4. DIVISIÓN TRAIN / TEST
# =============================================================================

train_df, test_df = df_raw.randomSplit([0.8, 0.2], seed=42)
print(f"\n📂 División de datos:")
print(f"   Entrenamiento: {train_df.count():,} registros")
print(f"   Prueba:        {test_df.count():,} registros")


# =============================================================================
# 5A. MODELO 1: REGRESIÓN LOGÍSTICA
# =============================================================================

print("\n🤖 Entrenando Modelo 1: Regresión Logística...")

lr = LogisticRegression(
    featuresCol="features",
    labelCol="label",
    maxIter=100
)

pipeline_lr = Pipeline(stages=[indexer, assembler, scaler, lr])

# Grilla de hiperparámetros
paramGrid_lr = ParamGridBuilder() \
    .addGrid(lr.regParam, [0.01, 0.1, 0.5]) \
    .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0]) \
    .build()

# Evaluador AUC-ROC
evaluator_roc = BinaryClassificationEvaluator(
    labelCol="label",
    metricName="areaUnderROC"
)

# Validación cruzada (3 folds para eficiencia; usar 5 en producción)
cv_lr = CrossValidator(
    estimator=pipeline_lr,
    estimatorParamMaps=paramGrid_lr,
    evaluator=evaluator_roc,
    numFolds=3,
    seed=42
)

cv_model_lr = cv_lr.fit(train_df)
predictions_lr = cv_model_lr.transform(test_df)

# Métricas Regresión Logística
auc_lr = evaluator_roc.evaluate(predictions_lr)
evaluator_acc = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)
evaluator_prec = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedPrecision"
)
evaluator_rec = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedRecall"
)

acc_lr   = evaluator_acc.evaluate(predictions_lr)
prec_lr  = evaluator_prec.evaluate(predictions_lr)
rec_lr   = evaluator_rec.evaluate(predictions_lr)

print(f"\n   📈 Resultados - Regresión Logística:")
print(f"      AUC-ROC   : {auc_lr:.4f}")
print(f"      Accuracy  : {acc_lr:.4f}")
print(f"      Precision : {prec_lr:.4f}")
print(f"      Recall    : {rec_lr:.4f}")


# =============================================================================
# 5B. MODELO 2: RANDOM FOREST
# =============================================================================

print("\n🌳 Entrenando Modelo 2: Random Forest...")

rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    seed=42
)

pipeline_rf = Pipeline(stages=[indexer, assembler, scaler, rf])

paramGrid_rf = ParamGridBuilder() \
    .addGrid(rf.numTrees, [50, 100]) \
    .addGrid(rf.maxDepth, [5, 10]) \
    .build()

cv_rf = CrossValidator(
    estimator=pipeline_rf,
    estimatorParamMaps=paramGrid_rf,
    evaluator=evaluator_roc,
    numFolds=3,
    seed=42
)

cv_model_rf = cv_rf.fit(train_df)
predictions_rf = cv_model_rf.transform(test_df)

auc_rf  = evaluator_roc.evaluate(predictions_rf)
acc_rf  = evaluator_acc.evaluate(predictions_rf)
prec_rf = evaluator_prec.evaluate(predictions_rf)
rec_rf  = evaluator_rec.evaluate(predictions_rf)

print(f"\n   📈 Resultados - Random Forest:")
print(f"      AUC-ROC   : {auc_rf:.4f}")
print(f"      Accuracy  : {acc_rf:.4f}")
print(f"      Precision : {prec_rf:.4f}")
print(f"      Recall    : {rec_rf:.4f}")


# =============================================================================
# 6. COMPARATIVA Y SELECCIÓN DEL MEJOR MODELO
# =============================================================================

print("\n" + "="*60)
print("📊 COMPARATIVA DE MODELOS")
print("="*60)
print(f"{'Métrica':<20} {'Reg. Logística':>15} {'Random Forest':>15}")
print("-"*50)
print(f"{'AUC-ROC':<20} {auc_lr:>15.4f} {auc_rf:>15.4f}")
print(f"{'Accuracy':<20} {acc_lr:>15.4f} {acc_rf:>15.4f}")
print(f"{'Precision':<20} {prec_lr:>15.4f} {prec_rf:>15.4f}")
print(f"{'Recall':<20} {rec_lr:>15.4f} {rec_rf:>15.4f}")
print("="*60)

best_model_name = "Random Forest" if auc_rf > auc_lr else "Regresión Logística"
best_auc = max(auc_rf, auc_lr)
print(f"\n🏆 Mejor modelo: {best_model_name} (AUC-ROC: {best_auc:.4f})")


# =============================================================================
# 7. IMPORTANCIA DE FEATURES (Random Forest)
# =============================================================================

rf_model = cv_model_rf.bestModel.stages[-1]
feature_importances = rf_model.featureImportances.toArray()

print("\n🔍 Importancia de Features (Random Forest):")
for feat, imp in sorted(zip(FEATURE_COLS, feature_importances), key=lambda x: -x[1]):
    bar = "█" * int(imp * 50)
    print(f"   {feat:<30} {imp:.4f} {bar}")


# =============================================================================
# 8. EJEMPLO DE PREDICCIÓN EN TIEMPO REAL (nuevos clientes)
# =============================================================================

print("\n🔮 Ejemplo de predicción para nuevos clientes:")

nuevos_clientes = spark.createDataFrame([
    (1001, 35, 25, 8, 4.5, 2, 5, "vip"),
    (1002, 5,  10, 1, 2.0, 20, 0, "nuevo"),
    (1003, 20, 40, 5, 3.8, 7, 3, "recurrente"),
], ["customer_id", "paginas_vistas_7d", "tiempo_sesion_min", "compras_historicas",
    "calificacion_promedio", "dias_ultima_visita", "items_carrito", "segmento_cliente"])

best_pipeline = cv_model_rf if auc_rf >= auc_lr else cv_model_lr
preds = best_pipeline.transform(nuevos_clientes)

preds.select(
    "customer_id",
    "segmento_cliente",
    "items_carrito",
    "prediction",
    F.round(F.col("probability").getItem(1), 4).alias("prob_compra")
).show()


# =============================================================================
# 9. GUARDAR MODELO (opcional - habilitar en producción)
# =============================================================================
# best_pipeline.bestModel.write().overwrite().save("gs://mi-bucket/modelos/ecommerce_v1")
# print("✅ Modelo guardado en storage distribuido.")


# =============================================================================
# FIN
# =============================================================================
print("\n✅ Pipeline completado exitosamente.")
spark.stop()
