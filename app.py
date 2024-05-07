from flask import Flask, render_template, request
import sqlite3
import conexiones



app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/estudiante", methods=["POST"])
def estudiante():
    return render_template("ciEstudiante.html")

@app.route("/docente", methods=["POST"])
def docente():
    return render_template("ciDocente.html")

@app.route("/menuEstudiante", methods=["POST"])
def menuEstudiante():
    try:
        ciEstudiante = request.form.get("ciEstudiante")
        ci=str((ciEstudiante))
        sqlprueba = "SELECT CI FROM ESTUDIANTE WHERE CI ="
        prueba = conexiones.crear_conexion(sqlprueba+ci)
        prueba = str(prueba)
        if prueba == "None":
            return render_template("errorCi.html")
        else:
            sql = "SELECT SALDO FROM ESTUDIANTE WHERE CI ="
            saldo = conexiones.crear_conexion(sql+ci) 
            saldo = str(saldo)   
            return render_template("menuEstudiante.html", saldo=saldo )
    except:
        return render_template("errorCi.html")

@app.route("/menuDocente", methods=["POST"])
def menuDocente():
    try:
        ciDocente = request.form.get("ciDocente")
        ci=str((ciDocente))
        sqlprueba = "SELECT CI FROM DOCENTE WHERE CI ="
        prueba = conexiones.crear_conexion(sqlprueba+ci)
        prueba = str(prueba)
        if prueba == "None":
            return render_template("errorCiDoc.html")
        else:   
               
            return render_template("menuDocente.html")
    except:
        return render_template("errorCiDoc.html")


@app.route("/grupo", methods=["POST"])
def grupo():

    grupo1 = request.form.get("1")
    grupo1 = str(grupo1)
    sqlAlumnos = "SELECT NOMBRE, CI, GRUPO, SALDO FROM ESTUDIANTE WHERE GRUPO = "
    sqlAlumnos = sqlAlumnos+grupo1
    datos = conexiones.crear_conexion_lista(sqlAlumnos)
    return render_template("grupos.html", datos=datos)

@app.route("/updateSaldo", methods=["POST"])
def updateSaldo():
    i = request.form.get("i")
    s = request.form.get("s")
    g = request.form.get("g")
    g = str(g)
    i = str(i)
    s = str(s)
    sql = "UPDATE ESTUDIANTE SET SALDO = SALDO+"+s+" WHERE CI ="+i+" "
    nuevoSaldo = str(sql)
    try:
        conexion = conexiones.crear_conexion(nuevoSaldo)    
    except:
        return render_template("errorDocente.html")
    sqlGrupo = "SELECT NOMBRE, CI, GRUPO, SALDO FROM ESTUDIANTE WHERE GRUPO = "
    sqlGrupo = sqlGrupo+g
    datos = conexiones.crear_conexion_lista(sqlGrupo)
    return render_template("grupos.html", datos = datos)


#pongo en marcha la app

if __name__ == "__main__":
    app.run(debug=True)
