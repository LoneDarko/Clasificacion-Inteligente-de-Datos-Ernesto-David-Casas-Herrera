import math

class LinearRegressionModel:
    def __init__(self, x_vals, y_vals):
        if len(x_vals) != len(y_vals):
            raise ValueError("La longitud de los valores x & y debe coincidir.")
        self.x_vals = x_vals
        self.y_vals = y_vals
    # Sumatoria de xy
    def sum_xy(self):
        return sum(x * y for x, y in zip(self.x_vals, self.y_vals))
    # Sumatoria de x^2
    def sum_x_squared(self):
        return sum(x ** 2 for x in self.x_vals)
    # Calculo de pendiente
    def calculate_slope(self):
        n = len(self.x_vals)
        return ((n * self.sum_xy()) - (sum(self.x_vals) * sum(self.y_vals))) / ((n * self.sum_x_squared()) - (sum(self.x_vals) ** 2))
    # Calculo de intercepcion
    def calculate_intercept(self):
        return (sum(self.y_vals) - (self.calculate_slope() * sum(self.x_vals))) / len(self.x_vals)
    # Calculo de media aritmetica
    def mean(self, values):
        return sum(values) / len(values)
    # Calculo de media varianza
    def variance(self, values):
        return sum((x - self.mean(values)) ** 2 for x in values) / len(values)
    # Calculo de media covarianza
    def covariance(self):
        return sum((x - self.mean(self.x_vals)) * (y - self.mean(self.y_vals)) for x, y in zip(self.x_vals, self.y_vals)) / len(self.x_vals)
    # Calculo de coeficiente de correlation
    def correlation_coefficient(self):
        return (self.covariance()) / math.sqrt(self.variance(self.x_vals) * self.variance(self.y_vals))
    # Calculo de coeficiente de determinacion
    def determination_coefficient(self):
        return self.covariance() ** 2 / (self.variance(self.y_vals) * self.variance(self.x_vals))

# Análisis de regresión lineal de Benetton
# Variable dependiente: Ventas
sales = (651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518)

# Variable independiente: Publicidad
advertising = (23, 26, 30, 34, 43, 48, 52, 57, 58)

# Valores para la predicción
prediction_values = (20, 33, 45, 55, 60)

# Creando una instancia de la clase LinearRegressionModel
benetton = LinearRegressionModel(advertising, sales)

# Calcular coeficientes
intercept, slope = benetton.calculate_intercept(), benetton.calculate_slope()

# Impresión de Coeficientes 
print(f"B0 = {intercept}")
print(f"B1 = {slope}")

# Imprimir la ecuación de regresión lineal
print(f"Ecuación de regresión lineal: y = {intercept} + {slope}x")

# Coeficiente de correlación
print(f"Coeficiente de correlación: {benetton.correlation_coefficient()}")

# Coeficiente de determinación
print(f"Coeficiente de determinación: {benetton.determination_coefficient()}\n")



# Predicción de ventas para cada valor de predicción
print("Prediccion de Ventas para cada valor de prediccion\n")
for val in prediction_values:
    predicted_sales = intercept + slope * val
    print(f"X = {val}")
    print(f"Y = {predicted_sales}\n")


# Ventas previstas
predicted_sales = [intercept + slope * val for val in advertising]
