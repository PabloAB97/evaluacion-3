from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        n1 = float(request.form['nota1'])
        n2 = float(request.form['nota2'])
        n3= float(request.form['nota3'])
        prom = (n1 + n2 + n3) / 3
        prom = round(prom)
        asis = int(request.form['asist'])
        return render_template('ejercicio1.html', nota1=n1, nota2= n2, nota3=n3, promedio=prom, asist=asis)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        no1 = request.form['nombre1']
        no2 = request.form['nombre2']
        no3 = request.form['nombre3']
        len1 = len(no1)
        len2 = len(no2)
        len3= len(no3)
        return render_template('ejercicio2.html', nombre1=no1, nombre2=no2, nombre3=no3, long1=len1, long2=len2, long3=len3)
    return render_template('ejercicio2.html')
    

if __name__ == '__main__':
    app.run(debug=True)
