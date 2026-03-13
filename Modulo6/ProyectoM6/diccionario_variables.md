# 📖 Diccionario de Variables — Dataset E-commerce

**Archivo:** `dataset_ecommerce.csv`  
**Registros:** 1.000 clientes simulados  
**Variables:** 16 (15 features + 1 target)

---

## 🎯 Variable Objetivo

| Variable | Tipo | Descripción | Rango |
|---|---|---|---|
| `monto_compra_promedio` | float | Monto promedio de compra en USD por sesión | $10 – $800 |

---

## 👤 Variables Demográficas

| Variable | Tipo | Descripción | Valores |
|---|---|---|---|
| `edad` | int | Edad del cliente en años | 18 – 70 |
| `genero` | str (cat) | Género del cliente | Masculino, Femenino, Otro |
| `region` | str (cat) | Región geográfica del cliente | Norte, Sur, Centro, Este, Oeste |

---

## 💻 Variables de Comportamiento en el Sitio

| Variable | Tipo | Descripción | Rango |
|---|---|---|---|
| `frecuencia_visitas_mes` | int | Número de visitas al sitio por mes | 1 – 40 |
| `tiempo_promedio_sesion_min` | float | Duración promedio de sesión (minutos) | 1 – 90 |
| `paginas_vistas_sesion` | int | Páginas vistas por sesión | 2 – 30 |
| `items_en_carrito` | int | Ítems promedio en el carrito | 0 – 15 |
| `dispositivo` | str (cat) | Dispositivo de acceso | Mobile, Desktop, Tablet |
| `tiene_app` | int (bin) | Si el cliente usa la app móvil | 0 = No, 1 = Sí |

---

## 🛍️ Variables de Historial de Compra

| Variable | Tipo | Descripción | Rango |
|---|---|---|---|
| `numero_compras_previas` | int | Número de compras realizadas anteriormente | 0 – 30 |
| `dias_desde_ultima_compra` | float | Días transcurridos desde la última compra | 1 – 180 |
| `uso_cupon` | int (bin) | Si usó cupón de descuento | 0 = No, 1 = Sí |
| `calificacion_promedio_dada` | float | Calificación promedio de productos comprados | 2.5 – 5.0 |
| `categoria_preferida` | str (cat) | Categoría de producto más comprada | Electronica, Ropa, Hogar, Deportes, Libros |
| `nivel_membresia` | str (cat, ordinal) | Nivel de membresía del cliente | Bronce < Plata < Oro < Platino |

---

## 📝 Notas

- Se introdujeron **~3% de valores nulos** en `tiempo_promedio_sesion_min`, `calificacion_promedio_dada` y `dias_desde_ultima_compra` para simular datos reales.
- La variable `monto_compra_promedio` fue generada con una función lineal con ruido gaussiano (σ=25).
- `nivel_membresia` tiene relación ordinal con el monto: Platino > Oro > Plata > Bronce.
