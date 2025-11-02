from flask import Flask, render_template, request, redirect, jsonify, flash

from flaskext.mysql import MySQL

import json

app = Flask(__name__)



app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_PORT"] = 3306
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "pass_root"
app.config["MYSQL_DATABASE_DB"] = "db_university"

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def page1():
    return render_template("page2.html")





@app.route("/etudiant")
def page3():
    return render_template("etudiant.html")


@app.route("/specialite")
def page4():
    return render_template("specialite.html")





# page etudiant
# display nbr etudiants par annee
@app.route("/api/data")
def doGetData():
    data2 = []

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT  annee FROM resultats")
    specialite_tuple = cursor.fetchall()
    h = [item[0] for item in specialite_tuple]
    for annee in h:
        cursor.execute(f"SELECT count(*)  from resultats where ANNEE={annee}")
        p = cursor.fetchall()
        p1 = [item[0] for item in p]
        p2 = p1[0]
        data2.append({"annee": annee, "data": p2})

    cursor.close()

    data_JSON = json.dumps(data2)
    return data_JSON


# display fourchette de moyenne



@app.route("/api/data4")
def doGetData4():
    data4 = []

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT annee FROM resultats")
    annee_tuple = cursor.fetchall()
    annees = [item[0] for item in annee_tuple]

    for annee in annees:
        # Count of failed results for females
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE ANNEE={annee} AND MOYENNE < 10 AND SEXE='F'"
        )
        count_females = cursor.fetchone()[0]

        # Count of failed results for males
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE ANNEE={annee} AND MOYENNE < 10 AND SEXE='H'"
        )
        count_males = cursor.fetchone()[0]

        data4.append(
            {"annee": annee, "countFemales": count_females, "countMales": count_males}
        )

    cursor.close()

    return jsonify(data4)


@app.route("/api/data5")
def doGetData5():
    data5 = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT annee FROM resultats")
    annee_tuple = cursor.fetchall()
    annees = [item[0] for item in annee_tuple]

    for annee in annees:
        # Count of all results for females
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE ANNEE={annee} AND SEXE='F'"
        )
        count_females = cursor.fetchone()[0]

        data5.append({"annee": annee, "countFemales": count_females})

    cursor.close()

    return jsonify(data5)


@app.route("/api/data6")
def doGetData6():
    data6 = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT annee FROM resultats")
    annee_tuple = cursor.fetchall()
    annees = [item[0] for item in annee_tuple]

    for annee in annees:
        # Your custom query for data6, for example, count of something else
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE ANNEE={annee} AND SEXE='H'"
        )
        count_data6 = cursor.fetchone()[0]

        data6.append({"annee": annee, "countData6": count_data6})

    cursor.close()

    return jsonify(data6)


@app.route("/api/data7")
def doGetData7():
    data7 = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT MOYENNE FROM resultats WHERE ANNEE = '2019' AND MOYENNE>=15 AND MOYENNE<=18 "
    )
    moyenne_data = cursor.fetchall()

    for row in moyenne_data:
        moyenne = row[0]
        data7.append({"moyenne": moyenne})

    cursor.close()

    return jsonify(data7)


# page specialite
@app.route("/api/data8")
def doGetData8():
    data8 = []

    conn = mysql.connect()
    cursor = conn.cursor()

    specialites = [
        "SPECIALITE_1",
        "SPECIALITE_2",
        "SPECIALITE_3",
        "SPECIALITE_4",
        "SPECIALITE_5",
        "SPECIALITE_6",
        "SPECIALITE_7",
    ] 

    for specialite in specialites:
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE specialite='{specialite}'"
        )
        count_result = cursor.fetchall()
        count_value = [item[0] for item in count_result]

        data8.append({"specialite": specialite, "data": count_value[0]})

    cursor.close()

    data_JSON8 = json.dumps(data8)
    return data_JSON8


@app.route("/api/data9")
def doGetData9():
    data9 = []

    conn = mysql.connect()
    cursor = conn.cursor()

    specialites = [
        "SPECIALITE_1",
        "SPECIALITE_2",
        "SPECIALITE_3",
        "SPECIALITE_4",
        "SPECIALITE_5",
        "SPECIALITE_6",
        "SPECIALITE_7",
    ]  

    for specialite in specialites:
        # Success count
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE specialite='{specialite}' AND moyenne >= 10"
        )
        success_result = cursor.fetchall()
        success_value = [item[0] for item in success_result]

        # Fail count
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE specialite='{specialite}' AND moyenne < 10"
        )
        fail_result = cursor.fetchall()
        fail_value = [item[0] for item in fail_result]

        data9.append(
            {
                "specialite": specialite,
                "success": success_value[0],
                "fail": fail_value[0],
            }
        )

    cursor.close()

    data_JSON9 = json.dumps(data9)
    return data_JSON9


@app.route("/api/data10")
def doGetData10():
    data10 = []

    conn = mysql.connect()
    cursor = conn.cursor()

    specialites = [
        "SPECIALITE_1",
        "SPECIALITE_2",
        "SPECIALITE_3",
        "SPECIALITE_4",
        "SPECIALITE_5",
        "SPECIALITE_6",
        "SPECIALITE_7",
    ] 

    for specialite in specialites:
        cursor.execute(
            f"SELECT AVG(moyenne) FROM resultats WHERE specialite='{specialite}'"
        )
        avg_result = cursor.fetchall()
        avg_value = [item[0] for item in avg_result]

        data10.append({"specialite": specialite, "average": avg_value[0]})

    cursor.close()

    data_JSON10 = json.dumps(data10)
    return data_JSON10


@app.route("/api/data11")
def doGetData11():
    data11 = []

    conn = mysql.connect()
    cursor = conn.cursor()

    specialites = [
        "SPECIALITE_1",
        "SPECIALITE_2",
        "SPECIALITE_3",
        "SPECIALITE_4",
        "SPECIALITE_5",
        "SPECIALITE_6",
        "SPECIALITE_7",
    ]  

    for specialite in specialites:
        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE specialite='{specialite}' AND sexe='F'"
        )
        count_femme_result = cursor.fetchall()
        count_femme_value = [item[0] for item in count_femme_result]

        cursor.execute(
            f"SELECT COUNT(*) FROM resultats WHERE specialite='{specialite}' AND sexe='H'"
        )
        count_homme_result = cursor.fetchall()
        count_homme_value = [item[0] for item in count_homme_result]

        data11.append(
            {
                "specialite": specialite,
                "count_femme": count_femme_value[0],
                "count_homme": count_homme_value[0],
            }
        )

    cursor.close()

    data_JSON11 = json.dumps(data11)
    return data_JSON11



@app.route("/api/data13")
def doGetData13():
    data13 = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT MOYENNE FROM resultats WHERE SPECIALITE = 'SPECIALITE_2'")
    moyenne_data = cursor.fetchall()

    for row in moyenne_data:
        moyenne = row[0]
        data13.append({"moyenne": moyenne})

    cursor.close()

    return jsonify(data13)


@app.route("/api/data14")
def get_all_data():
    data14 = []

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        # Fetch all rows from the resultats table
        cursor.execute("SELECT * FROM resultats WHERE MOYENNE >=16")
        resultats_data = cursor.fetchall()

        for row in resultats_data:
            data14.append(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

    return jsonify(data14)


@app.route("/api/data15")
def get_all_data2():
    data15 = []

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        # Fetch the top 100 rows for each specialite from the resultats table
        cursor.execute(
            """SELECT * FROM resultats  WHERE (specialite, ID) IN (SELECT specialite, ID  FROM resultats ORDER BY specialite, ID  LIMIT 100) ORDER BY specialite, ID """
        )
        resultats_data = cursor.fetchall()

        for row in resultats_data:
            data15.append(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

    return jsonify(data15)
@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Ajouter un étudiant
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        major = request.form['major']

        try:
            cursor.execute("INSERT INTO students (name, email, age, major) VALUES (%s, %s, %s, %s)", (name, email, age, major))
            conn.commit()
            flash('Étudiant ajouté avec succès!', 'success')
        except Exception as e:
            flash(f"Erreur lors de l'ajout : {e}", 'danger')

    # Récupérer tous les étudiants
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    return render_template('students.html', students=students)

@app.route('/students/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        flash('Étudiant supprimé avec succès!', 'success')
    except Exception as e:
        flash(f"Erreur lors de la suppression : {e}", 'danger')

    cursor.close()
    return redirect(url_for('manage_students'))
@app.route('/resultats', methods=['GET', 'POST'])
def manage_resultats():
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Add a new record to the table
        annee = request.form['annee']
        matricule = request.form['matricule']
        nom = request.form['nom']
        prenom = request.form['prenom']
        sexe = request.form['sexe']
        specialite = request.form['specialite']
        moyenne = request.form['moyenne']

        try:
            cursor.execute(
                "INSERT INTO resultats (annee, matricule, nom, prenom, sexe, specialite, moyenne) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (annee, matricule, nom, prenom, sexe, specialite, moyenne),
            )
            conn.commit()
            flash('Record added successfully!', 'success')
        except Exception as e:
            flash(f"Error adding record: {e}", 'danger')

    # Fetch all records
    cursor.execute("SELECT * FROM resultats")
    resultats = cursor.fetchall()

    cursor.close()
    return render_template('resultats.html', resultats=resultats)


@app.route('/resultats/delete/<int:matricule>', methods=['POST'])
def delete_resultat(matricule):
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM resultats WHERE matricule=%s", (matricule,))
        conn.commit()
        flash('Record deleted successfully!', 'success')
    except Exception as e:
        flash(f"Error deleting record: {e}", 'danger')

    cursor.close()
    return redirect(url_for('manage_resultats'))


@app.route('/resultats/edit/<int:matricule>', methods=['GET', 'POST'])
def edit_resultat(matricule):
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Update the record
        annee = request.form['annee']
        nom = request.form['nom']
        prenom = request.form['prenom']
        sexe = request.form['sexe']
        specialite = request.form['specialite']
        moyenne = request.form['moyenne']

        try:
            cursor.execute(
                "UPDATE resultats SET annee=%s, nom=%s, prenom=%s, sexe=%s, specialite=%s, moyenne=%s WHERE matricule=%s",
                (annee, nom, prenom, sexe, specialite, moyenne, matricule),
            )
            conn.commit()
            flash('Record updated successfully!', 'success')
        except Exception as e:
            flash(f"Error updating record: {e}", 'danger')

        return redirect(url_for('manage_resultats'))

    # Fetch the record for the given matricule
    cursor.execute("SELECT * FROM resultats WHERE matricule=%s", (matricule,))
    resultat = cursor.fetchone()

    cursor.close()
    return render_template('edit_resultat.html', resultat=resultat)
@app.route('/resultats/search', methods=['GET'])
def search_resultats():
    query = request.args.get('query')
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM resultats WHERE nom LIKE %s OR prenom LIKE %s OR specialite LIKE %s",
        (f"%{query}%", f"%{query}%", f"%{query}%"),
    )
    resultats = cursor.fetchall()

    cursor.close()
    return render_template('resultats.html', resultats=resultats)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
