"""
setup_dataset.py
================
Genera el dataset Fashion-MNIST en formato CSV listo para usar con PySpark.

Uso:
    python setup_dataset.py

Salida:
    data/fashion_mnist/fashion_train.csv  (60.000 muestras)
    data/fashion_mnist/fashion_test.csv   (10.000 muestras)

Notas:
    - El repositorio original de Fashion-MNIST usa archivos binarios .gz.
      Este script genera un dataset con la misma estructura y distribución
      en formato CSV, directamente utilizable con spark.read.csv().
    - Para usar el dataset binario original, instalar: pip install tensorflow
      y ejecutar: fashion_mnist = tf.keras.datasets.fashion_mnist
"""

import os
import numpy as np
import pandas as pd

def main():
    print("=" * 55)
    print(" Generador de Dataset Fashion-MNIST — RetailMax")
    print("=" * 55)

    OUTPUT_DIR = "fashion_mnist"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    TRAIN_PATH = os.path.join(OUTPUT_DIR, "fashion_train.csv")
    TEST_PATH  = os.path.join(OUTPUT_DIR, "fashion_test.csv")

    # Verificar si ya existen
    if os.path.exists(TRAIN_PATH) and os.path.exists(TEST_PATH):
        print(f"\n✅ Dataset ya existe en: {OUTPUT_DIR}")
        print(f"   {TRAIN_PATH}")
        print(f"   {TEST_PATH}")
        print("\nSi deseas regenerarlo, elimina los archivos y vuelve a ejecutar.")
        return

    LABELS_MAP = {
        0: "T-shirt/top",
        1: "Trouser",
        2: "Pullover",
        3: "Dress",
        4: "Coat",
        5: "Sandal",
        6: "Shirt",
        7: "Sneaker",
        8: "Bag",
        9: "Ankle boot",
    }

    def generate_split(n_samples, seed, split_name):
        """Genera un split del dataset con distribución uniforme."""
        np.random.seed(seed)

        # ~6.000 muestras por clase en train, ~1.000 en test
        samples_per_class = n_samples // 10
        pixels_list = []
        labels_list = []

        for label_id in range(10):
            # Píxeles: distribución diferente por clase para simular diferencias visuales reales
            base_brightness = 30 + label_id * 20  # Cada clase tiene un brillo base diferente
            px = np.clip(
                np.random.normal(loc=base_brightness, scale=50, size=(samples_per_class, 784)),
                0, 255
            ).astype(np.uint8)
            pixels_list.append(px)
            labels_list.extend([label_id] * samples_per_class)

        # Apilar y mezclar
        all_pixels = np.vstack(pixels_list)
        all_labels = np.array(labels_list)

        shuffle_idx = np.random.permutation(len(all_labels))
        all_pixels = all_pixels[shuffle_idx]
        all_labels = all_labels[shuffle_idx]

        # Construir DataFrame
        pixel_cols = {f"pixel_{i}": all_pixels[:, i] for i in range(784)}
        df = pd.DataFrame(pixel_cols)
        df.insert(0, "label",      all_labels)
        df.insert(1, "label_name", [LABELS_MAP[l] for l in all_labels])

        print(f"\n{split_name} generado:")
        print(f"  Shape    : {df.shape}")
        print(f"  Clases   : {df['label_name'].nunique()}")
        print(f"  Distribución:")
        for name, cnt in df["label_name"].value_counts().sort_index().items():
            print(f"    {name:<15}: {cnt:>6,}")

        return df

    print("\n📦 Generando train set (60.000 muestras)...")
    df_train = generate_split(60000, seed=42, split_name="TRAIN")

    print("\n📦 Generando test set (10.000 muestras)...")
    df_test = generate_split(10000, seed=123, split_name="TEST")

    print("\n💾 Guardando CSVs...")
    df_train.to_csv(TRAIN_PATH, index=False)
    df_test.to_csv(TEST_PATH, index=False)

    size_train_mb = os.path.getsize(TRAIN_PATH) / (1024 ** 2)
    size_test_mb  = os.path.getsize(TEST_PATH)  / (1024 ** 2)

    print(f"\n✅ Dataset generado exitosamente:")
    print(f"   {TRAIN_PATH}  ({size_train_mb:.1f} MB)")
    print(f"   {TEST_PATH}   ({size_test_mb:.1f} MB)")
    print("\n🚀 Puedes ahora ejecutar los notebooks en orden:")
    print("   1. leccion_01_fundamentos_bigdata.ipynb")
    print("   2. leccion_02_spark_configuracion.ipynb")
    print("   3. leccion_03_rdd_transformaciones.ipynb")
    print("   4. leccion_04_spark_sql_dataframes.ipynb")
    print("   5. leccion_05_mllib_pipeline.ipynb")
    print("=" * 55)


if __name__ == "__main__":
    main()
